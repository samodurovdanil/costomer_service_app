from socket import *
import time, json
import LOG.server_log_config
import logging

APP_LOG = logging.getLogger('server')

def answer(msg_from_client):
    APP_LOG.info(f'Получено сообщение от клиента: {msg_from_client}')
    if msg_from_client['action'] == 'presence':
        msg_to_client = {
            "response": '200',
            "alert": "Connection settled"
        }
        APP_LOG.info('Сообщение для отправки клиенту: %s', msg_to_client)
        return msg_to_client


s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 7777))
s.listen()
while True:
    try:
        client, addr = s.accept()
        answer_to_client = answer(json.loads(client.recv(1000000)))
        client.send(json.dumps(answer_to_client, sort_keys=True, indent=4).encode('utf-8'))
    except Exception as error:
        APP_LOG.error("Произошла ошибка: %s", error)
        break