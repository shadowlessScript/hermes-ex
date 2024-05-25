# importing the socket library
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time
from client import Client

HOST = "127.0.0.1"
GATE = 9090
BUFSIZ = 1024 # MAX SIZE OF MESSAGES
ADDR = (HOST, GATE)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

messages = []
def receive_messages():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            messages.append(msg)
            print(msg)
        except Exception as e:
            print(f"Error: {e}")
            break


def send_message(msg):
    client_socket.send(bytes(msg, "utf-8"))
    if msg == "!leave":
        client_socket.close()



receive_thread = Thread(target=receive_messages)
receive_thread.start()

send_message("Ben")
time.sleep(5)
send_message("hello")
time.sleep(5)
send_message("!leave")



