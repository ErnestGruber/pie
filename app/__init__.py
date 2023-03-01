from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from app.backup import backup_check


app = Flask(__name__)

from app import routes

def check_upload():
    backup_check()

scheduler = BackgroundScheduler()
job = scheduler.add_job(check_upload, 'interval', minutes=5)
scheduler.start()