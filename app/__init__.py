from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from app.backup import backup_check
#from app.TCPServer import TCPServer


app = Flask(__name__)


from app import routes

def check_upload():
    backup_check()

#server = TCPServer()
#server.start()

scheduler = BackgroundScheduler()
job = scheduler.add_job(check_upload, 'interval', minutes=5)
scheduler.start()
if __name__ == "__main__":
    app.run()
