import json
import os
import requests

def backup_write(json_data):
    f = open('app/backup.txt','a+')
    f.write(json.dumps(json_data))
    f.write('\n')

def backup_check():
    if os.stat('app/backup.txt').st_size != 0:
        backup_send()

def backup_send():
    with open("file") as lines:
        for line in lines:
            dictToSend = line
            try:
                res = requests.post('https://pconapi.ru/signin/', json=dictToSend)
            except Exception:
                break





