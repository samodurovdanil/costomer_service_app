from socket import *
import time, json
import logging
from LOG import client_log_config

APP_LOG = logging.getLogger('client')


def connect_to_server(command):
    if command == 'y':
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect(('localhost', 7777))
        except Exception as error:
            APP_LOG.error("Произошла ошибка: %s", error)
            return
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
        APP_LOG.info('Сообщение для отправки серверу: %s', presence_msg)
        s.send(json.dumps(presence_msg, sort_keys=True, indent=4).encode('utf-8'))
        data = json.loads(s.recv(1000000))
        APP_LOG.info('Собщение получнное от сервера: %s', data)
        return 'Сообщение от сервера: ', data['alert']
    elif command == 'n':
        APP_LOG.warning('Подключение отменено!')
        return 'Подключение отменено!'
    else:
        APP_LOG.warning('Подключение не установленно. Повторный запрос')
        connect_to_server(input("Начать взаимодействие с сервером? (y/n)?: "))


print(connect_to_server(input('Начать взаимодействие с сервером? (y/n)?: ')))
