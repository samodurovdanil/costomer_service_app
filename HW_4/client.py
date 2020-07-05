from socket import *
import time, json, unittest


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
        return 'Сообщение от сервера: ', data['alert']
    elif command == 'y':
        return 'Подключение отменено!'


# print(connect_to_server(input("Подключиться к серверу? (y/n): ")))

class TestClient(unittest.TestCase):

    def test_connection_on(self):
        self.assertEqual(connect_to_server('y'), ('Сообщение от сервера: ', 'Connection settled'))

    def test_connection_off(self):
        self.assertEqual(connect_to_server('n'), 'Подключение отменено!')
