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
table = dynamodb.Table('DadosClientesSemParar')



def validar_registro(registro):
    campos_obrigatorios = {"data_hora", "tipo", "veiculo", "valor", "id", "tid", "status"}
    tipos_transacoes = ["pedagio", "estacionamento", "abastecimento", "drive-thru"]
    registro_json = json.loads(registro)
    if not isinstance(registro_json, dict):
        return False, "Registro não é um objeto JSON válido."
    
    if not campos_obrigatorios.issubset(registro_json.keys()):
        return False, f"Campos obrigatórios faltando. Esperados: {campos_obrigatorios}"

    if not isinstance(registro_json['data_hora'], str):
        return False,  "O campo data_emissao deve ser uma string no formato de data."
    if not isinstance(registro_json['tipo'], str) and registro_json['tipo'] not in tipos_transacoes:
        return False, "Erro: O campo cliente deve ser uma string ou o Tipo informado é inválido!!!"
    if not isinstance(registro_json['veiculo'], str) and len(registro_json['veiculo'] == 7):
        return False, "Erro: O campo veículo deve ser uma string e deve conter 7 caracteres."
    if not isinstance(registro_json['valor'], (int, float, Decimal)):
        return False, "O campo valor deve ser numérico."
    if not isinstance(registro_json['id'], str) and len(registro_json['id'] == 24):
        return False, "O campo id inválido."
    if not isinstance(registro_json['tid'], str) and len(registro_json['tid'] == 24):
        return False, "O campo tid inválido."
    if not isinstance(registro_json['status'], str) and registro_json['status'] not in ("aprovaod", "reprovado"):
        return False, "O campo status deve ser uma string com um dos valores que são: aprovado ou reprovado."
    
    return True, "Registro válido."

def lambda_handler(event, context):
    """
    Função Lambda que consome mensagens do SQS.
    Cada mensagem da fila gera um registro em 'event["Records"]'.
    """
    logger.info(f"event: {event}")
    for record in event['Records']:
        
        # Corpo da mensagem
        body = record['body']
        
        
           
        valido, mensagem = validar_registro(body)
       
        if not valido:
            logger.warning(f'Registro inválido: {mensagem}')
            continue
            
        
        try:
            body_json = json.loads(body, parse_float=Decimal)
            logger.info(f'Inserindo registro no DynamoDB: {body_json}')
            table.put_item(Item=body_json)
            logger.info(f"Registro: {body_json} inserido com sucesso!")
        except Exception as e:
            logger.error(f'Erro ao inserir registro no DynamoDB: {str(e)}')
            

    return {
        'statusCode': 200,
        'body': json.dumps('Mensagens processadas com sucesso!')
    }