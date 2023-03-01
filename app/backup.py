import json
import os

def backup_write(json_data):
    f = open('app/backup.txt','a+')
    f.write(json.dumps(json_data))
    f.write('\n')

def backup_check():
    if os.stat('app/backup.txt').st_size == 0:
        print('yeah boyyyy')

def buckup_send():
    print('jopa')




