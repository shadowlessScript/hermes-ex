# importing the socket library
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time
from client import Client

HOST = "127.0.0.1"
GATE = 9090
BUFSIZ = 1024 # MAX SIZE OF MESSAGES
ADDR = (HOST, GATE)

HERMES_SERVER = socket(AF_INET, SOCK_STREAM)
try:
    HERMES_SERVER.bind(ADDR)
except Exception as e:
    HERMES_SERVER.close()


clients = []


def broadcast(msg, name=""):
    for client in clients:
        client = client.client_socket
        client.send(bytes(name, "utf8") + msg)


def client_communication(hermes_client):
    client = hermes_client.client_socket
    name = client.recv(BUFSIZ).decode("utf-8")
    hermes_client.set_name(name)
    msg = f"{name} has joined the chat!"
    broadcast(bytes(msg, "utf8"))
    while True:
        try:
            msg = client.recv(BUFSIZ)

            print(f"{name}: ", msg.decode("utf8"))
            if msg == bytes("!leave", "utf8"):
                broadcast(f"{name} has left the chat....".encode("utf8"), "")
                client.close()
                clients.remove(hermes_client)

                break
            else:
                broadcast(msg, name+":")
        except Exception as e:
            print(f"Error: {e}")
            break


def wait_for_connection():
    run = True

    while run:
        try:
            client_socket, client_addr = HERMES_SERVER.accept()
            hermes_client = Client(
                client_addr, client_socket)
            clients.append(hermes_client)
            print(f"Hermes accepted request from {client_addr} at {time.time()}")

            Thread(target=client_communication, args=(hermes_client,)).start()

        except Exception as e:
            print(f"error: {e}")
            HERMES_SERVER.close()

    HERMES_SERVER.close()


if __name__ == "__main__":
    HERMES_SERVER.listen(10)
    print("Hermes waiting for requests...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    HERMES_SERVER.close()
