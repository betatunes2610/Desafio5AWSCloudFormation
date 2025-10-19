# Desafio5AWSCloudFormation
Repositório do Bootcamp AWS da DIO parceria Santander - Nesse foi implementado um caso de uso imitando dados semparar e foi adicionado ao desafio a parte da implementação dos conveniados
README.md — Laboratório: AWS CloudFormation
Sumário
Visão geral

Objetivos do laboratório

Arquitetura

Descrição do template CloudFormation

Passo a passo — deploy

Como validar que deu certo

Limpeza e custos

1. Visão geral
Este laboratório mostra a implementação do caso de uso do projeto SEM PARAR criado com AWS, claro que não será a cópia fiel do projeto, mas algumas funcionalidades referente ao mesmo.

Cenário prático: Na parte de dados do SEMPARAR foi gerado um bucket e ao inserir dados, dados fake criado em um programa feito em python para a geração de registros Fake, nesse bucket o mesmo irá fazer o invoke de um lambda function que irá passar os registros ao SQS para consumir as mensagens e enviar para o outro lambda function e esse lambda fará a inserção dos registro no DynamoDB.

2. Objetivos do laboratório
Ao final teremos a seguinte capacidade:

Entender a estrutura de de um projeto, desde a crição de buckets e lambdas até o consumo de um SQS e gravação de registros no banco de dados NO SQL. E como um desafio a mais, será criado a comunicação de um ORACLE
Business Service (OSB), fazendo o invoke de uma api gateway Localstack que chama um lambda e o mesmo insere registros na tabela Conveniados no banco DynamoDB.

Criar Bucket, Lambdas Functions, SQS, DynamoDB via Console
Utilização do Docker Desktop para criacao de containers de Weblogic com o oracle suite para a criacao de um dominio soaosb e com isso a criação de mais 4 containers onde crio um administrador de servicos, gerenciados de serviços e um oracle business service, uma banco de dados oracle e a criacao de Projeto OSB no JDeveloper 12c


3. Arquitetura
Descrição sequencial: 

Será criado um Bucket S3, dois Lambdas Function, SQS e tabela no DynamoDB. O Bucket será carregado com resgistros de clientes O Lambda será invocado e irá consumir um SQS que irá invocar um outro Lambda para gravar na tabela do banco do DynamoDB.


Diagramas (simplificado):
[Cliente --> [S3 Bucket] --> (CustomLambdaInvoker) -->[SQS] --> (CustomLambdaInvoker)  --> {grava registro DynamoDB}
[Cliente] --> [OSB] --> [API GATEWAY] --> (CustomLambdaInvoker) --> {grava registro DynamoDB} tabela Conveniados


4. Descrição:
seções tipicamente usadas:

Parameters — variáveis passadas no deploy (ex.: Nome do stack, ambiente, prefixo de nomes).
Mappings — mapeamentos
Resources — definição dos recursos (S3 Bucket, Lambda Function, DynamoDB Table, IAM Roles/Policies, Event Notification, CloudWatch Log Group, SQS).
Outputs — informações úteis (ex.: ARN do bucket, nome da tabela DynamoDB, URL do console).
Recursos (exemplo mínimo)
LambdaExecutionRole: Role com políticas mínimas — s3:GetObject, dynamodb:PutItem, logs:CreateLogStream, logs:PutLogEvents.
ProcessorLambda: Função Lambda (Python 3.13).
Containers Docker Desktop
Realização de pull de imagens da oracle via https://container-registry.oracle.com/
Instalação e utilização do JDeveloper 12c

5. Passo a passo:
— Para nao ocorrer cobrança utlizamos o localstack e o mesmo foi criado no container do docker desktop 
via power shell criacao de recursos (Depois crie os Lambdas Functions, Criar o SQS, Crie as tabelas DynamoDB etc) da AWS → com awslocal.


6. Como validar que deu certo

Verifique o bucket S3 criado (nome no output):
Verifique se o arquivo json esta no Bucket S3
Verifique a criação dos Lambdas Functions
Verifique a criação do SQS
Verifique a criação da API GATEWAY
Verifique a criação das tabelas no DynamoDB
Verificar se o banco oracle (soadb) esta no ar
Verificar se ADM no Docker esta running
Verificar se MS no Docker esta running
Verificar se OSB no Docker esta running

Faça o pull de imagens no site da oracle https://container-registry.oracle.com/ eu escolhi o Middlaware (opção suite pois essa imagem possui todos os recurso necessário para poder rodar o OSB) e Database. Assisti algumas aulas de docker. Li as instruções no proprio site da oracle (https://container-registry.oracle.com/), pois lá mostra o passo-a-passo.
lembre-se de criar um network no docker para que o ADM, o Manager Service e o OSB fiquem ligados a mesma rede
Lembrando que o dominio ideial para a utilização do OSB é o soaosb, pois será criado um banco de dados (soadb), ADM, Manager Service e um oracle Business Service, Todos precisam estar runinng.

Criar um projeto OSB no JDeveloper 12c
Realizar o deploy para que o console do Service Bus reconheça esse projeto
Lembrando que o URI no projeto OSB deve ser com o mesmo api id criado no localstack (api gateway)

Nesse Projeto OSB será criado:
um BS com a uri http://host.docker.internal:4566/restapis/<api id>/dev/_user_request_/conveniados
Proxy Service e nesse proxy service será criado um pipeline pois nesse pipeline sera setado a rota e nessa rota iremos associar com o BS criado
Pelo proxy service vai ser enviado um registro dos dados (json) do cliente que irá pegar a rota setada no pipeline, a uri cadastrada no BS e irá fazer o invoke da api gateway localstack, essa api ira
invocar o lambda que irá gravar o registro na tabela Conveniados DynamoDB
Na pasta imagens consta o registro da aplicaçao do projeto.
 


