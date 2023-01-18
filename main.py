import streamlit as st 
import pandas as pd
import pycep_correios
import dao
import boto3
import folium_map
import aux_function

from pycep_correios import WebService
from streamlit_folium import folium_static
from st_aggrid import AgGrid, GridUpdateMode, AgGridTheme, DataReturnMode
from st_aggrid.grid_options_builder import GridOptionsBuilder


@st.cache
def conn_db():
    return dao.connect_db()

@st.cache(allow_output_mutation=True)
def load_data(conn):
    dt_colaboradores, dt_servicos, dt_equipe = aux_function.load_data(conn)
    return dt_colaboradores, dt_servicos, dt_equipe

@st.cache
def aws_client():
    client = aux_function.aws_client()
    return client

def search_by_zipcode(zipcode:str):
    if zipcode.isnumeric():
        info = pycep_correios.get_address_from_cep(zipcode, webservice=WebService.CORREIOS)
        return info
    else: return {'uf':'','cidade':'', 'bairro':'','logradouro':''}

conn = conn_db()

sidebar = st.sidebar.header('MENU')

header =  st.container()

servicos = st.container()

plot_map = st.container()

criar_servico = st.container()

with header:
    st.title('GERENCIADOR DE SERVIÇOS - ABC ENGENHARIA')

with servicos:

    dt_colaboradores, dt_servicos, dt_equipe = load_data(conn=conn)    
    
    # MERGE A ORDEM DE SERVIÇO COM A LISTA DO EXECUTORES
    merge_dt = pd.merge(left=dt_servicos,right=dt_equipe,how='inner',on='ordem_de_servico').reset_index()
    merge_dt = merge_dt[['ordem_de_servico','cliente','endereco','lat','long','encarregado','oficial','ajudante']]

    gd = GridOptionsBuilder.from_dataframe(merge_dt[merge_dt.columns[~merge_dt.columns.isin(['lat','long'])]].copy())
    gd.configure_pagination(enabled=True)
    gd.configure_default_column(groupable=True,)
    # gd.configure_selection(selection_mode='multiple',use_checkbox=False)
    gridoption = gd.build()
    grid_table =  AgGrid(merge_dt, gridOptions=gridoption,update_mode=GridUpdateMode.MANUAL,
    data_return_mode=DataReturnMode.FILTERED,theme=AgGridTheme.MATERIAL)

    try:
        sel_rows = pd.Series(grid_table['data']['ordem_de_servico'])
    except KeyError:
        st.warning('Não há dados para exibir, selecione todos ou filtre pelo menos 1 linha')

with plot_map:
    try:
        st.header('MAPA DE LOCALIZAÇÃO DOS SERVIÇOS')
        sel_rows = merge_dt[merge_dt['ordem_de_servico'].isin(sel_rows.to_list())]
        sel_rows.reset_index(inplace=True,drop=True)

        map = folium_map.plot_map(sel_rows)
        folium_static(map)
    except Exception or KeyError or NameError :
        pass

with criar_servico:
    st.header('NOVO SERVIÇO')
    with st.expander('EXPANDIR'):
        with st.form('Crie um Serviço', clear_on_submit=False):

            os = st.text_input('Ordem de Serviço')
            cliente = st.text_input(label='Cliente')
            servico = st.text_area(label='Serviço')

            col1,col2 = st.columns([1,1])
            cep = col1.text_input('CEP',max_chars=8)

            b1 = st.form_submit_button('BUSCAR',type='secondary') 
            
            if b1:
                info = search_by_zipcode(cep)
            else: info = search_by_zipcode(cep)

            uf = st.text_input(label='Estado',max_chars=15,value= info['uf'])
            cidade = st.text_input(label='Cidade',max_chars=15, value= info['cidade'])
            bairro = st.text_input(label='Bairro',max_chars=30, value= info['bairro'])
            logradouro = st.text_input(label='Lougradouro',max_chars=100, value= info['logradouro'])
            complemento = st.text_input(label='Complemento',max_chars=20)

            st.subheader('EXECUÇÃO')
            encarregado = st.selectbox('Encarregado',dt_colaboradores['nome'][dt_colaboradores['funcao'] == 'ENCARREGADO'])
            oficial = st.selectbox('Oficial',dt_colaboradores['nome'][dt_colaboradores['funcao'] == 'OFICIAL'])
            ajudante =  st.selectbox('Ajudante',dt_colaboradores['nome'][dt_colaboradores['funcao'] == 'AJUDANTE'])

            b2 = st.form_submit_button('Salvar')

        if b2:
            endereco = f"{logradouro}, {complemento} - {bairro}, {cidade} - {uf}, {cep}"

            client = aws_client()

            result = client.search_place_index_for_text(IndexName='geolocalizacao-2', Text=endereco)

            lat = result.get('Results')[0]['Place']['Geometry']['Point'][1]
            lon = result.get('Results')[0]['Place']['Geometry']['Point'][0]

            dt_dict = {'ordem_de_servico':int(os),'cliente':cliente,'endereco':endereco,'lat':lat,'long':lon}
            dao.insert_data('servicos',dt_dict,conn)

            equipe = {'ordem_de_servico':int(os),'encarregado':encarregado,'oficial':oficial,'ajudante':ajudante}
            dao.insert_data('equipe', equipe, conn)

            st.success('serviço cadastrado!')
                



        
