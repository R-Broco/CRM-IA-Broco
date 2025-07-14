def handle_whatsapp_message(data):
    # Aqui você pode extrair a mensagem e número do cliente
    message = data.get("Body", "").lower()
    sender = data.get("From", "")

    # Exemplo de resposta simples
    if "agendar" in message:
        return {"message": "Claro! Qual dia e horário você prefere?"}
    elif "documento" in message:
        return {"message": "Você pode enviar o documento por aqui mesmo."}
    else:
        return {"message": "Olá! Sou o assistente do consultório. Como posso ajudar?"}
