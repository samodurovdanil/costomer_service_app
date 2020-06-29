from socket import *
import time, json


def connect_to_server(command):
    if command == 'y':
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 7777))
        account_name = input('Имя пользователя: ')
        msg = input('Сообщение серверу: ')
        presence_msg = {
            "action": "presence",
            "time": int(time.time()),
            "type": "status",
            "user": {
                "account_name": account_name,
                "status": msg
            }
        }
        s.send(json.dumps(presence_msg, sort_keys=True, indent=4).encode('utf-8'))
        data = json.loads(s.recv(1000000))
        print('Сообщение от сервера: ', data['alert'])
    else:
        print('Подключение отменено!')


print(connect_to_server(input('Начать взаимодействие с сервером? (y/n)?: ')))
