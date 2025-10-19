from decimal import Decimal
import json
import boto3
import traceback
from botocore.exceptions import ClientError
import logging

# Inicializa cliente DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabela = dynamodb.Table('DadosClientesSemParar')

# Configurar o logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def decimal_para_float(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError


def lambda_handler(event, context):
    try:
        logger.info(f"Evento recebido: {event}")
		
        # Supondo que o JSON tenha {"id": "123"}
        body = event['body']
        body_json = json.loads(body, parse_float=Decimal)
        registro_id = body_json.get("id")
        if not registro_id:
            return {"statusCode": 400, "body": json.dumps({"erro": "id não fornecido"})}

        # Consulta no DynamoDB
        response = tabela.get_item(Key={"id": registro_id})

        if "Item" not in response:
            return {"statusCode": 404, "body": json.dumps({"erro": "registro não encontrado"})}

        return {"statusCode": 200, "body": json.dumps(response["Item"], default=decimal_para_float)}

    except ClientError as e:
        print("Erro AWS:", e.response['Error']['Message'])
        return {"statusCode": 500, "body": json.dumps({"erro": e.response['Error']['Message']})}
    except Exception as e:
        print("Erro detectado:", str(e))
        traceback.print_exc()
        return {"statusCode": 500, "body": json.dumps({"erro": str(e)})}