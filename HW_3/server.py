from socket import *
import time, json


def answer(msg_from_client):
    print(msg_from_client)
    if msg_from_client['action'] == 'presence':
        msg_to_client = {
            "response": '200',
            "alert": "Connection settled"
        }
        return msg_to_client


s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 7777))
s.listen()
while True:
    client, addr = s.accept()
    answer_to_client = answer(json.loads(client.recv(1000000)))
    client.send(json.dumps(answer_to_client, sort_keys=True, indent=4).encode('utf-8'))
