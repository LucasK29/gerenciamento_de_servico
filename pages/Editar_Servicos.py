import streamlit as st
import dao
import pandas as pd
import aux_function as af

def connect_db():
    conn = dao.connect_db()
    return conn

@st.experimental_memo
def load_data():
    conn = connect_db()
    return af.load_data(conn=conn)

af.aws_client()

dt_colaboradores, dt_servicos, dt_equipe = load_data()

st.title('EDITAR SERVIÇOS')

edit_line =  st.container()

edit_colaborador = st.container()

with edit_line:
    # MERGE A ORDEM DE SERVIÇO COM A LISTA DO EXECUTORES
    merge_dt = pd.merge(left=dt_servicos,right=dt_equipe,how='inner',on='ordem_de_servico').reset_index()
    merge_dt = merge_dt[['ordem_de_servico','cliente','endereco','lat','long','encarregado','oficial','ajudante']]
    st._legacy_dataframe(merge_dt)
    
    with st.expander('ALTERAR'):
        os = st.text_input(label='Insira a número da OS')
        col_1 = st.selectbox('Escolha o atributo', options=merge_dt.columns[:],key='atributo_selectbox')

        match col_1:
            case 'ordem_de_servico':
                val_1 = st.text_input('Digite o número da OS')
            case 'cliente':
                val_1 = st.text_input('Digite o cliente')

            case 'endereco':

                col1,col2 = st.columns([1,1])
                cep = col1.text_input('CEP',max_chars=8)

                b1 = st.button('BUSCAR') 
                
                if b1:
                    info = af.search_by_zipcode(cep)
                else: info = af.search_by_zipcode(cep)

                uf = st.text_input(label='Estado',max_chars=15,value= info['uf'])
                cidade = st.text_input(label='Cidade',max_chars=15, value= info['cidade'])
                bairro = st.text_input(label='Bairro',max_chars=30, value= info['bairro'])
                logradouro = st.text_input(label='Lougradouro',max_chars=100, value= info['logradouro'])
                complemento = st.text_input(label='Complemento',max_chars=20)

                val_1 = f"{logradouro}, {complemento} - {bairro}, {cidade} - {uf}, {cep}"

            case 'encarregado' | 'oficial' | 'ajudante':
                val_1 = st.selectbox(f'{col_1}',dt_colaboradores['nome'].loc[dt_colaboradores['funcao']==col_1.upper()])
                              
        
        if st.button(label='Atualizar'):

            if col_1 in ['encarregado','oficial','ajudante']:
                dao.update_row('equipe',col=f'{col_1}', val1=f'{val_1}', key='ordem_de_servico',val2=int(os),conn=connect_db())
                st.success('Atualizado com Sucesso!')
                af.clear_rerun()    
            elif col_1 in ['ordem_de_servico','cliente']:
                dao.update_row('servicos',col=f'{col_1}', val1=f'{val_1}', key='ordem_de_servico',val2=int(os),conn=connect_db())
                st.success('Atualizado com Sucesso!')
                af.clear_rerun() 
            elif col_1 == 'endereco':
                client = af.aws_clientaws_client()
                result = client.search_place_index_for_text(IndexName='geolocalizacao-2', Text=val_1)

                lat = result.get('Results')[0]['Place']['Geometry']['Point'][1]
                lon = result.get('Results')[0]['Place']['Geometry']['Point'][0]

                dao.update_row('servicos',col=f'{col_1}', val1=f'{val_1}', key='ordem_de_servico',val2=int(os),conn=connect_db())
                dao.update_row('servicos',col='lat', val1=lat, key='ordem_de_servico',val2=int(os),conn=connect_db())
                dao.update_row('servicos',col='long', val1=lon, key='ordem_de_servico',val2=int(os),conn=connect_db())
                st.success('Atualizado com Sucesso!')
                af.clear_rerun()
    
    with st.expander('DELETAR'):
        os_del = st.text_input(label='Insira a Ordem de Serviço', key='os_del')
        if st.button(label='Deletar',key='os_del_b'):
            dao.delete_data('servicos',key='ordem_de_servico',val=int(os_del),conn=connect_db())
            dao.delete_data('equipe',key='ordem_de_servico',val=int(os_del),conn=connect_db())
            st.experimental_memo.clear()
            st.success('Colaborador Deletado!!')
            af.clear_rerun()

with edit_colaborador:
    st.header('COLABORADORES')

    st._arrow_table(dt_colaboradores)

    with st.expander('NOVO'):
        nome = st.text_input(label='Insira o nome')
        funcao = st.selectbox(label='Insira o cargo',options=dt_colaboradores['funcao'].unique())
        if st.button(label='Gravar'):
            novo_dict = {'nome':nome,'funcao':funcao}    
            dao.insert_data('colaboradores',novo_dict,connect_db())
            st.success('Colaborador gravado com sucesso!!')
            af.clear_rerun()

    with st.expander('ALTERAR'):
        id_alt = st.text_input(label='Insira o ID do colaborador', key='id_alt')
        col = st.selectbox('Escolha o atributo', options=dt_colaboradores.columns[1:])
        
        if col == 'funcao':
            val1 = st.selectbox(label='Insira o cargo_',options=dt_colaboradores['funcao'].unique())
        else: val1 = st.text_input('Digite')
        
        if st.button(label='Alterar'):
            dao.update_row('colaboradores',col=f'{col}', val1=f'{val1}', key='id',val2=int(id_alt),conn=connect_db())
            st.success('Colaborador Deletado!!')
            af.clear_rerun()

    with st.expander('DELETAR'):
        id_del = st.text_input(label='Insira o ID do colaborador', key='id_del')
        if st.button(label='Deletar', key='id_del_b'):
            dao.delete_data('colaboradores',key='id',val=int(id_del),conn=connect_db())
            st.success('Colaborador Deletado!!')
            af.clear_rerun()

    



