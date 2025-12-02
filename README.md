## 🚀 Simulação do Projeto SemParar

Localstack + AWS Services + Oracle Service Bus + Docker

Este repositório apresenta uma simulação completa do fluxo SemParar, integrando arquitetura serverless, mensageria, APIs e middleware corporativo (OSB).
A solução foi dividida em duas linhas: Serverless e OSB + Localstack.

## 🏗️ Arquitetura Geral

A solução é composta por duas estruturas independentes que se integram a sistemas distintos:

## 1️⃣ Linha Serverless (Localstack)

Fluxo completo:

Upload de arquivo JSON no S3

O S3 invoca um Lambda

O Lambda envia o payload para o SQS

Outro Lambda consome o SQS

O registro é validado e gravado no DynamoDB (DadosSemParar)

Mensagens de retorno indicam se o registro já existia ou foi gravado com sucesso

⚠️ Autenticação do DynamoDB ainda não implementada — será adicionada futuramente.

## 2️⃣ Linha OSB + Localstack

Fluxo de integração corporativa com Oracle Service Bus:

Ambiente criado com Docker utilizando imagens oficiais do Oracle Registry

Containers criados:

Oracle Database

SOA Suite (Admin Server, Service Manager, OSB Server)

Projeto criado no JDeveloper 12c:

Aplicação: OSBConveniadosAPP

Projeto: OSBConveniadosProject

Elementos criados no OSB:

Proxy Service: HTTP /conveniados

Pipeline: com router e rotas configuradas

Business Service: apontando para o API Gateway Localstack

Fluxo final:
OSB Console → API Gateway → Lambda → DynamoDB

## 🔧 Tecnologias Utilizadas
AWS (Localstack)

S3

Lambda

SQS

API Gateway

DynamoDB

Oracle

Oracle Service Bus (OSB)

Oracle Database

SOA Suite

JDeveloper 12c

Outros

Docker & Docker Networks

Arquitetura orientada a eventos

Mensageria assíncrona

## 📁 Estrutura do Repositório
semparar-simulation/
├── serverless-line/
├── osb-line/
├── docs/
└── assets/

## ▶️ Como Executar
1. Subir Localstack
localstack start

2. Subir containers Oracle (via docker-compose)
docker-compose up -d

3. Enviar arquivo JSON para o S3
aws s3 cp sample-upload.json s3://semparar-bucket/

4. Consumir pelo OSB

Enviar o JSON via console OSB para o proxy /conveniados.

## 📝 Autor

Portfólio desenvolvido por **Roberta Tunes Rocha**, com foco em arquitetura serverless, integrações corporativas e soluções cloud simuladas localmente.

## 🎥 Vídeo Explicativo

O roteiro completo está em:
docs/roteiro-video.md
