import boto3
import pycep_correios
import pandas as pd
import json

from pycep_correios import WebService

def aws_client():

    with open('access_key.json','r') as json_file:
        key = json.load(json_file)
        print(key)

    client = boto3.client('location',region_name='sa-east-1',
    aws_access_key_id=key['aws_access_key_id'],
    aws_secret_access_key=key['aws_secret_access_key'])
    return client

def search_by_zipcode(zipcode:str):
    if zipcode.isnumeric():
        info = pycep_correios.get_address_from_cep(zipcode, webservice=WebService.CORREIOS)
        return info
    else: return {'uf':'','cidade':'', 'bairro':'','logradouro':''}

def load_data(conn):
    dt_colaboradores = pd.read_sql_query("SELECT * FROM colaboradores", conn)
    dt_servicos = pd.read_sql_query("SELECT * FROM servicos", conn)
    dt_equipe = pd.read_sql_query("SELECT * FROM equipe", conn)
    return dt_colaboradores, dt_servicos, dt_equipe
