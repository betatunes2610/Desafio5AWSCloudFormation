# 🚀 Projeto de Simulação – Arquitetura SemParar  
Integração AWS (Localstack) + Oracle Service Bus (OSB) via Docker

---

## 📌 Visão Geral

Este projeto simula duas linhas de integração utilizadas em arquiteturas corporativas semelhantes às do ecossistema **SemParar**, combinando:

- **Serviços AWS simulados via Localstack**  
- **Orquestração completa com eventos (S3 → Lambda → SQS → Lambda → DynamoDB)**  
- **Integração com Oracle Service Bus (OSB) via Docker e JDeveloper 12C**  
- **Fluxo síncrono via API Gateway → Lambda → DynamoDB**  
- **Ambiente local totalmente reproduzível e sem dependência da AWS real**

O objetivo é demonstrar habilidades em **arquitetura distribuída**, **integrações híbridas**, **SOA**, **serverless**, **cloud computing**, e **orquestração de eventos**.

---

# 🧱 Arquitetura Geral

O projeto é dividido em **duas linhas principais**:

---

# 🟦 Linha 1 – Upload JSON → S3 → Lambda → SQS → Lambda → DynamoDB

### 🔹 Fluxo

1. Arquivo JSON é enviado ao **S3** (Localstack).  
2. O bucket dispara um evento que invoca um **Lambda**.  
3. O Lambda valida/processa o conteúdo e envia mensagem ao **SQS**.  
4. Um segundo Lambda consome o SQS.  
5. Os dados são persistidos no **DynamoDB** (tabela `DadosSemParar`).  
6. Não há autenticação na V1, mas o projeto está preparado para evoluir.

### 🔹 Tecnologias

- Localstack (S3, Lambda, SQS, DynamoDB)  
- AWS SDK  
- Modelagem NoSQL  
- Event-driven architecture  

---

# 🟩 Linha 2 – OSB (Oracle Service Bus) → API Gateway → Lambda → DynamoDB

### 🐳 Infraestrutura OSB via Docker

Foram utilizadas imagens oficiais Oracle disponíveis em:  
https://container-registry.oracle.com/

Componentes utilizados:

- **database** → Instância Oracle Database necessária ao domínio SOA  
- **soasuite** →  
  - Admin Server  
  - Service Manager  
  - OSB Server  

Todos os containers foram conectados via uma **Docker network** dedicada.

---

### 🧩 Desenvolvimento no JDeveloper 12C

Estrutura criada:

- **Aplicação:** `OSBConveniadosAPP`  
- **Projeto:** `OSBConveniadosProject`

### Serviços criados:

#### 🔹 Proxy Service  
- Nome: **ProxyServiceOSBConveniados**  
- Protocolo: **HTTP**  
- Path: `/conveniados`  

#### 🔹 Pipeline
- Nome: **pipelineOSBConveniados**  
- Contém:
  - Router
  - Regras de roteamento
  - Conexão com Business Service

#### 🔹 Business Service
##### URL configurada para consumir o API Gateway Localstack:

http://host.docker.internal:4566/restapis/d1pjgsef5h/dev/_user_request_/conveniados


#### 🔹 Deploy
- Foi criado um deployment name para todo o conjunto.  
- Deploy executado com sucesso no console OSB.

---

# 🟧 Fluxo OSB → API Gateway → Lambda → DynamoDB

1. OSB envia o JSON para o API Gateway.  
2. O Gateway aciona um Lambda.  
3. O Lambda verifica se o registro já existe na tabela Conveniados no DynamoDB.  
4. Caso exista → retorna **"Registro já consta na base de dados"**  
5. Caso não exista → grava → retorna **"Registro gravado com sucesso"**

---

# 🗂️ Estrutura do Repositório

```bash
📦 semparar-simulacao
├── 📁 infra
│   ├── docker
│   │   ├── docker-compose-osb.yml
│   │   ├── network-config.md
│   │   └── oracle-setup.md
│   ├── localstack
│   │   ├── docker-compose-localstack.yml
│   │   ├── api-gateway-config.json
│   │   ├── dynamodb-tables.json
│   │   └── s3-bucket.json
│   └── README.md
│
├── 📁 lambdas
│   ├── lambda-s3-to-sqs
│   │   ├── index.py
│   │   └── package.json
│   ├── lambda-sqs-to-dynamo
│   │   ├── index.py
│   │   └── package.json
│   └── lambda-osb-gateway
│       ├── index.py
│       └── package.json
│
├── 📁 osb
│   ├── OSBConveniadosAPP.jws
│   ├── ProxyServiceOSBConveniados.xml
│   ├── pipelineOSBConveniados.pipeline
│   ├── BusinessServiceOSBConveniados.xml
│   └── deploy-config.md
│
├── 📁 docs
│   ├── arquitetura.png
│   ├── fluxograma.png
│   ├── banner-linkedin.png
│   └── video-roteiro.md
│
├── 📁 samples
│   └── exemplo-payload.json
│
└── README.md
