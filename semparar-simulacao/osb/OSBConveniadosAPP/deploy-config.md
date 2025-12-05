# 📦 Deploy de Projeto OSB no JDeveloper 12c

Este README descreve **exclusivamente o processo de deploy** de um projeto OSB (Oracle Service Bus) criado no **JDeveloper 12c**, contendo **Proxy Services**, **Pipeline**, e **Business Services**.

---

## 🚀 Pré-requisitos

* JDeveloper 12c instalado

* Oracle Service Bus configurado

* Projeto OSB já criado no JDeveloper

---

## 🔧 Passo a Passo do Deploy

### 1️⃣ Abra o JDeveloper

Inicie o **JDeveloper 12c** e abra o **projeto OSB** já criado.

---

### 2️⃣ Verifique a Configuração do Service Bus

No menu lateral **Service Bus**:

* Confirme que os **Proxy Services**, **Business Services** e **Pipelines** estão visíveis
* Verifique se não há erros de validação

---

### 4️⃣ Deploy Direto pelo JDeveloper

O método mais comum.

#### ▶ Passos:

1. Clique com o botão direito no projeto OSB
2. Selecione **Project Properties**
3. Procure por **Compiler**
4. Clica em Deployment
5. Em **Deployment Profiles** escolha **New Profile ** e informe qualquer nome
6. Clique em **OK**
7. Clique com o botão direito no projeto OSB
8. Selecione **Deploy > [Nome do Profile criado]**
9. Escolha o destino do deploy:

   * **Service Bus Local**
   * **Oracle Service Bus Standalone Server**
   * **IntegratedWebLogicServer**

O JDeveloper irá iniciar o processo de deploy e exibirá logs em tempo real.

---

### 5️⃣ Validar o Deploy

Após o deploy, você pode validar através do:

* **Service Bus Console**
* **Enterprise Manager (EM)**

Verifique:

* Proxy Services ativos
* Pipelines corretamente associados
* Business Services acessíveis

---

## 🧪 Testando o Serviço

Depois do deploy, utilize:

* Service Bus Console Test
* SoapUI / Postman

---

## ✔ Conclusão

Este README cobre somente o **deploy de um projeto OSB no JDeveloper 12c**. Caso deseje complementar com estrutura de projeto, arquitetura, diagramas ou exemplos de serviços, posso adicionar também.
