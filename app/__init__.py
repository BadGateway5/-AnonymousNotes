from flask import Flask
from .user import user
from apscheduler.schedulers.background import BackgroundScheduler
from .user.utils import delete_notes

app = Flask(__name__)
app.secret_key = "12345"
app.register_blueprint(user)

def print_hello():
    return "hello world"

scheduler = BackgroundScheduler()
scheduler.add_job(delete_notes, 'interval', seconds=5)  # Запуск каждую минуту
scheduler.start()