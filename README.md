# CRM-IA-Broco
CRM utilizando: LangFlow, Whatsapp API e Render

## 📁 Repositório: `CRM-IA-Broco`

### 🧠 Propósito
Este repositório contém a API principal do CRM com Inteligência Artificial, desenvolvida com **FastAPI**. Ele atua como **webhook do WhatsApp**, recebendo mensagens, processando-as com o Langflow e respondendo automaticamente via API do WhatsApp.

---

### ⚙️ Variáveis de Ambiente Necessárias

Configure as seguintes variáveis no ambiente (ex: Render, `.env`, etc.):

| Variável              | Descrição                                                                 |
|-----------------------|---------------------------------------------------------------------------|
| `WHATSAPP_TOKEN`      | Token de acesso da API do WhatsApp (Meta). Expira em 24h no modo sandbox. |
| `WHATSAPP_PHONE_ID`   | ID do número de telefone conectado à API do WhatsApp.                     |
| `LANGFLOW_ENDPOINT`   | URL pública do Langflow (ex: `https://langflow-app-xxxx.onrender.com`).   |

> ⚠️ **Importante:** Se estiver usando o token temporário do WhatsApp, renove-o manualmente no Meta for Developers antes de cada deploy.

---

### 🚀 Como testar

#### 1. Verificação do Webhook (GET)
Use o Postman ou navegador:

```
GET /webhook?hub.mode=subscribe&hub.verify_token=visao_cria&hub.challenge=123456
```

**Resposta esperada:** `123456`

#### 2. Simular mensagem do WhatsApp (POST)

```http
POST /webhook
Content-Type: application/json
```

```json
{
  "entry": [
    {
      "changes": [
        {
          "value": {
            "messages": [
              {
                "from": "5511999999999",
                "text": {
                  "body": "Olá, tudo bem?"
                }
              }
            ]
          }
        }
      ]
    }
  ]
}
```

---

### 📦 Deploy

- Plataforma recomendada: **Render**
- Tipo de serviço: **Web Service**
- Porta: `$PORT`
- Comando de inicialização:  
  ```bash
  uvicorn main:app --host 0.0.0.0 --port $PORT
  ```

---
