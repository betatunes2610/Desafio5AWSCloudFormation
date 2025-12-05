import json
from random import randint, uniform, choice
import random
import string



# Função para gerar ID tag(EPC) em hexadecimal
def generate_id(length):
  """Gera id aleátorio, passando a quantidade desejada (24)"""
  id = '0123456789abcdef' 
  return ''.join(random.choices(id, k=length))

# Função para gerar placa de veículo aleatorio
def generate_cnpj(length):
    cnpj = "0123456789"
    return ''.join(random.choices(cnpj, k=length))

# Tipo
tipos_transacoes = ["pedagio", "estacionamento", "abastecimento", "drive-thru"]

# Nome Fantasia Ficticio
nomes_fantasia = [
    "AlphaTech Solutions",
    "Bella Vita Cafe",
    "Solare Energia Renovavel",
    "NuvemSoft Sistemas",
    "Doce Encanto Confeitaria",
    "EcoVerde Jardinagem",
    "Prime Motors",
    "BlueWave Consultoria",
    "VivaMais Saude",
    "Casa & Estilo Decoracoes",
    "Aurora Cosmeticos",
    "MundoPet Center",
    "Elite Contabil",
    "SmartBuild Engenharia",
    "Sabor de Casa Restaurante",
    "InnovaWeb Agencia Digital",
    "TopLine Distribuidora",
    "Golden Fitness Academia",
    "ValeTec Informatica",
    "Floratta Boutique"
]

# Gerar registros
registros = []
for i in range(25):
	registro = {
     	"id": generate_id(24),
		"nome_fantasia": choice(nomes_fantasia),
		"tipo": choice(tipos_transacoes),
		"cnpj": generate_cnpj(14),
		"status": random.choice(['ativo','inativo','suspenso'])
	}
	registros.append(registro)

# Salvar no arquivo JSON
with open("registrosConveniados.json", "w") as f:
	json.dump(registros, f, indent=4, ensure_ascii=False)

print("Arquivos 'registrosConveniados.json' gerado com sucesso!")

