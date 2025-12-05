import boto3
import json
import os
import logging
from decimal import Decimal



# Configurar o logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Configurar o endpoint dinamicamente
dynamodb_endpoint = os.getenv('DYNAMODB_ENPOINT', None)
dynamodb = boto3.resource('dynamodb',endpoint_url=dynamodb_endpoint)

# Conectar à tabela DynamoDB
table = dynamodb.Table('Conveniados')

def buscar_registro_bd(body)->bool:
    
    id = body.get("id")
    logger.info(f'id = {id}') 
    resp = table.get_item(Key={"id" : id})
         
   
    return "Item" in resp
           

def validar_registro(registro):
    campos_obrigatorios = {"id", "nome_fantasia", "tipo", "cnpj", "status"}
    tipos_transacoes = ["pedagio", "estacionamento", "abastecimento", "drive-thru"]
    registro_json = json.loads(registro)
    
    if not isinstance(registro_json, dict):
        return False, "Registro não é um objeto JSON válido."
    
    if not campos_obrigatorios.issubset(registro_json.keys()):
        return False, f"Campos obrigatórios faltando. Esperados: {campos_obrigatorios}"

    if not isinstance(registro_json['id'], str) and len(registro_json['id'] == 24):
        return False, "O campo id inválido."
    if not isinstance(registro_json['nome_fantasia'], str):
        return False,  "O campo nome_fantasia deve ser uma string."
    if not isinstance(registro_json['tipo'], str) and registro_json['tipo'] not in tipos_transacoes:
        return False, "Erro: O campo tipo deve ser uma string ou o Tipo informado é inválido!!!"
    if not isinstance(registro_json['cnpj'], str) and len(registro_json['cnpj'] == 14):
        return False, "O campo cnpj inválido."
    if not isinstance(registro_json['status'], str) and registro_json['status'] not in ("ativo","inativo","suspenso"):
        return False, "O campo status deve ser uma string com um dos valores que são: ativo, inativo ou suspenso."
    
    return True, "Registro válido."

def lambda_handler(event, context):
    """
    Função Lambda que consome API Gatewat.
    Cada mensagem da fila gera um registro em 'event["Records"]'.
    """
       
     # Corpo da mensagem
    body = event['body']  
    logger.info(f"Body: {body}") 
        
           
    valido, mensagem = validar_registro(body)
       
    if not valido:
        logger.warning(f'Registro inválido: {mensagem}')
        
    body_json = json.loads(body, parse_float=Decimal)
    
    if buscar_registro_bd(body_json):
        return {
            'body': json.dumps('Registro ja consta cadastrado na base de dado!')
        }        
    else:    
        try:
           
            logger.info(f'Inserindo registro no DynamoDB: {body_json}')
            table.put_item(Item=body_json)
            logger.info(f"Registro: {body_json} inserido com sucesso!")
        except Exception as e:
            logger.error(f'Erro ao inserir registro no DynamoDB: {str(e)}')
                

        return {
            'statusCode': 200,
            'body': json.dumps('Mensagens processadas com sucesso!')
        }