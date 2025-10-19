from datetime import datetime
import json
import boto3
import os
import logging
from decimal import Decimal
from urllib.parse import unquote_plus

# Configurar o logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)



def validar_registro(registro):
    campos_obrigatorios = {"data_hora", "tipo", "veiculo", "valor", "id", "tid", "status"}
    tipos_transacoes = ["pedagio", "estacionamento", "abastecimento", "drive-thru"]

    if not isinstance(registro, dict):
        return False, "Registro não é um objeto JSON válido."
    
    if not campos_obrigatorios.issubset(registro.keys()):
        return False, f"Campos obrigatórios faltando. Esperados: {campos_obrigatorios}"

    if not isinstance(registro['data_hora'], str):
        return False,  "O campo data_emissao deve ser uma string no formato de data."
    if not isinstance(registro['tipo'], str) and registro['tipo'] not in tipos_transacoes:
        return False, "Erro: O campo cliente deve ser uma string ou o Tipo informado é inválido!!!"
    if not isinstance(registro['veiculo'], str) and len(registro['veiculo'] == 7):
        return False, "Erro: O campo veículo deve ser uma string e deve conter 7 caracteres."
    if not isinstance(registro['valor'], (int, float, Decimal)):
        return False, "O campo valor deve ser numérico."
    if not isinstance(registro['id'], str) and len(registro['id'] == 24):
        return False, "O campo epc inválido."
    if not isinstance(registro['tid'], str) and len(registro['tid'] == 24):
        return False, "O campo tid inválido."
    if not isinstance(registro['status'], str) and registro['status'] not in ("aprovaod", "reprovado"):
        return False, "O campo status deve ser uma string com um dos valores que são: aprovado ou reprovado."
    
    return True, "Registro válido."


    

    
    
def inserir_registros_no_sqs(event):
    logger.info(f"event: {event}")
    s3 = boto3.client('s3')
    sqs = boto3.client('sqs')
    fila = sqs.get_queue_url(QueueName='SemPararQueue')
    queue_url = fila['QueueUrl']
    logger.info(f"URL: {queue_url}")
    for record in event['Records']:
        s3_bucket = record['s3']['bucket']['name']
        s3_key = record['s3']['object']['key']
      
      

        
    logger.info(f'Processando arquivo: s3//{s3_bucket}/{s3_key}')
    response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
    file_content = response['Body'].read().decode("utf-8", errors="ignore")
     
            
    # Tenta converter em lista de registros
    try:
        dados = json.loads(file_content)
    except json.JSONDecodeError as e:
        logger.error("Erro ao decodificar JSON:", e)
        exit()

    logger.info(f"{len(dados)} registros carregados do arquivo.")

    # Enviar cada registro para o SQS
    for i, registro in enumerate(dados, start=1):
        try:
            mensagem = json.dumps(registro)
            logger.info(f"Mensagem: {mensagem}")
            response = sqs.send_message(QueueUrl=queue_url, MessageBody=mensagem)
            logger.info(f"Registro {i} enviado com sucesso.")
        except Exception as e:
            logger.info(f"Falha ao enviar registro {i}: {e}")
          
       
           

    return {
        'statuscode': 200,
        'body': json.dumps('Processamento concluido com sucesso!')
    }

    

def lambda_handler(event, context):
    """Função principal que direciona o processamento baseado no evento da API"""
    inserir_registros_no_sqs(event)
   
