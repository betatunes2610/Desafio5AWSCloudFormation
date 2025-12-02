# 🚀 Projeto SemParar — Arquitetura Serverless + OSB + LocalStack

Simulação completa do fluxo de processamento do **SemParar**, integrando **AWS Serverless**, **LocalStack** e **Oracle Service Bus (OSB)**.  
Este repositório demonstra experiência prática em **arquitetura cloud**, **processos assíncronos**, **integrações corporativas** e construção de ambientes replicáveis para portfólio profissional.

---

## ⭐ Visão Geral do Projeto

Este projeto simula dois fluxos reais utilizados no ecossistema SemParar:

### 🔹 1. Processamento de Passagens (Serverless AWS)
Pipeline assíncrono baseado em:
- Upload de JSON → **Amazon S3**
- Evento do S3 aciona → **AWS Lambda**
- Lambda publica mensagem → **Amazon SQS**
- Lambda consumidor processa fila
- Persistência dos dados no → **DynamoDB**

👉 Simula o registro de passagens (pedágio, estacionamento, drive-thru etc.)

### 🔹 2. Cadastro de Conveniados (OSB + API Gateway)
Integração corporativa envolvendo:
- **Oracle Service Bus (Proxy + Pipeline + Business Service)**
- Chamada ao **API Gateway (LocalStack)**
- Lambda valida CNPJ no **DynamoDB**
- Respostas de negócio:
  - ✔ Conveniado já existe  
  - ✔ Conveniado cadastrado com sucesso

👉 Simula integrações reais com parceiros da malha SemParar.

---

## 🏗️ Arquitetura da Solução

### Fluxo SemParar
Cliente → S3 → Lambda → SQS → Lambda Consumer → DynamoDB


### Fluxo Conveniados


OSB → API Gateway → Lambda → DynamoDB


---

## 🧰 Tecnologias Utilizadas

### ☁️ AWS / Cloud
- Amazon S3  
- AWS Lambda  
- Amazon SQS  
- Amazon DynamoDB  
- API Gateway  
- LocalStack (emulação local de serviços AWS)

### 🧩 Integração
- Oracle Service Bus (OSB)  
- JDeveloper 12c

### 🧑‍💻 Desenvolvimento
- Python 3  
- Docker & Docker Compose  
- Postman / cURL  
- Arquitetura modular por serviços

---

## 📂 Estrutura do Repositório



/semparar_repo
├── lambdas/
│ ├── uploader_handler/
│ ├── sqs_consumer/
│ └── conveniados_handler/
├── osb/
│ ├── proxy/
│ ├── pipeline/
│ └── business/
├── infra/
├── samples/
│ └── sample.json
└── README.md


---

## ▶️ Como Executar

### 1. Subir o ambiente local
```bash
docker-compose up -d

2. Enviar JSON para o fluxo SemParar
awslocal s3 cp samples/sample.json s3://semparar-bucket/

3. Testar o cadastro de conveniado
curl -X POST http://localhost:4566/restapis/<api-id>/local/_user_request_/conveniados \
  -d '{"cnpj":"12345678901234"}'

## 🎯 Diferenciais do Projeto

✔ Arquitetura corporativa real e replicável

✔ Integração entre cloud moderna e sistema legado

✔ Demonstração clara de domínio em AWS, OSB e processos assíncronos

✔ Repositório organizado, limpo e preparado para recrutadores

✔ Excelente conteúdo para portfólio profissional

✔ Inclui fluxo completo ponta a ponta

## 📌 Autor

Criado com foco em boas práticas, documentação clara e apresentação profissional no GitHub.
Perfeito para demonstrar conhecimento em Cloud, Serverless, Integrações e Infraestrutura Moderna.
