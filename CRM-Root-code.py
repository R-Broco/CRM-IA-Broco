from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
WHATSAPP_PHONE_ID = os.getenv("WHATSAPP_PHONE_ID")
LANGFLOW_ENDPOINT = os.getenv("LANGFLOW_ENDPOINT")

@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    try:
        message = data['entry'][0]['changes'][0]['value']['messages'][0]
        sender = message['from']
        text = message['text']['body']

        # Envia para LangFlow
        response = requests.post(LANGFLOW_ENDPOINT, json={"input": text})
        reply = response.json().get("output", "Desculpe, não entendi.")

        # Envia resposta via WhatsApp
        send_whatsapp_message(sender, reply)
    except Exception as e:
        print("Erro:", e)
    return {"status": "ok"}

def send_whatsapp_message(to, message):
    url = f"https://graph.facebook.com/v18.0/{WHATSAPP_PHONE_ID}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    requests.post(url, headers=headers, json=payload)
