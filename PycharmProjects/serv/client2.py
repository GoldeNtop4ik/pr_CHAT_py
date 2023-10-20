
import socket
from _thread import *

client = socket.socket() # создаем сокет клиента
hostname = socket.gethostname() # получаем хост локальной машины
port = 1234  # устанавливаем порт сервера
client.connect((hostname, port)) # подключаемся к серверу

name = input("imya:")
client.send(name.encode())

def Send():
    while True:
        message = input("Input a text: ")  # вводим сообщение
        client.send(message.encode())  # отправляем сообщение серверу
def Take():
    while True:
        data = client.recv(1024)
        print(data.decode())

start_new_thread(Send, ())
start_new_thread(Take, ())

while True:
    a = 1