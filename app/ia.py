import requests
import os

def ask_ia(message):
    api_key = os.getenv("OPENROUTER_API_KEY")
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "Você é um assistente de um consultório de psicologia. Responda apenas sobre agendamentos, documentos, lembretes e informações administrativas."},
            {"role": "user", "content": message}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]
