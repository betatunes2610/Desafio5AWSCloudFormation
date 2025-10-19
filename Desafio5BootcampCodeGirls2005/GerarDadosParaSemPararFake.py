import json
from random import randint, uniform, choice
from datetime import datetime, timedelta
import random
import string

# Função para gerar uma data aleatória nos últimos 30 dias
def random_date():
	today = datetime.now()
	days_ago = randint(1, 30)
	random_date = today - timedelta(days=days_ago)
	return random_date.strftime("%Y-%m-%dT%H:%M:%S")

# Função para gerar ID tag(EPC) em hexadecimal
def generate_random_hex(length):
  """Gera string hexadecimal aleátoria, passando a quantidade desejada (24)"""
  hex_characters = '0123456789abcdef' 
  return ''.join(random.choices(hex_characters, k=length))

# Função para gerar placa de veículo aleatorio
def random_placa():
    placa_veiculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choices(placa_veiculo, k=7))

# Clientes fictícios
tipos_transacoes = ["pedagio", "estacionamento", "abastecimento", "drive-thru"]

# Gerar registros
registros = []
for i in range(1000):
	registro = {
     	"data_hora": random_date(),
		"tipo": choice(tipos_transacoes),
		"veiculo": random_placa(),
		"valor": round(uniform(10.0, 50.0), 2),
  		"id": generate_random_hex(24),
        "tid": generate_random_hex(24),
		"status": random.choice(['aprovado', 'reprovado'])
	}
	registros.append(registro)

# Salvar no arquivo JSON
with open("registrosSemPararFake.json", "w") as f:
	json.dump(registros, f, indent=4, ensure_ascii=False)

print("Arquivos 'registrosSemPararFake.json' gerado com sucesso!")


