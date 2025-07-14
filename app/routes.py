from flask import Blueprint, request, jsonify
from .whatsapp import handle_whatsapp_message
from .scheduler import schedule_reminder

main = Blueprint('main', __name__)

@main.route("/", methods=["GET"])
def index():
    return "CRM-IA está rodando!"

@main.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    response = handle_whatsapp_message(data)
    return jsonify(response)

@main.route("/schedule", methods=["POST"])
def schedule():
    data = request.json
    result = schedule_reminder(data)
    return jsonify(result)
