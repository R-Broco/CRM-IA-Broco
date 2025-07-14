from apscheduler.schedulers.background import BackgroundScheduler
import datetime

scheduler = BackgroundScheduler()
scheduler.start()

def schedule_reminder(data):
    name = data.get("name")
    time = data.get("time")  # formato: "2025-07-14 15:00:00"

    def send_reminder():
        print(f"Lembrete: Enviar mensagem para {name}")

    run_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    scheduler.add_job(send_reminder, 'date', run_date=run_time)

    return {"status": "Lembrete agendado com sucesso!"}
