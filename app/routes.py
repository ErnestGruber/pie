from app import app
from flask import request
import requests
import json
from app.backup import backup_write


@app.route('/indata', methods=['POST'])
def indata():
    json = request.get_json()
    dictToSend = json
    dictFromServer = 'Error'
    code = 999
    try:
        res = requests.post('https://pconapi.ru/signin/', json=dictToSend)
        dictFromServer = res.json()
    except Exception:
        backup_write(dictToSend)
    return dictFromServer

