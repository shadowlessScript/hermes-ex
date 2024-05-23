# importing the socket library
import socket
import threading


def handle_client(client_socket, client_addr):
    try:
        while True:
            request = client_socket.recv(1024)
            request = request.decode("utf-8")

            if request.lower() == "close":
                client_socket.send("closed".encode("utf-8"))
                break

            print(f"received: {request}")

            response = "accepted".encode("utf-8")
            client_socket.send(response)

    except Exception as e:
        print(f"Error when handling client: {e}")
    finally:
        client_socket.close()
        print(f"Connection to client ({client_addr[0]}:{client_addr[1]}) closed")

def deploy_hermes():
    """
    this will start the tcp server, by calling the socket object
    :return:
    """

     # giving the server an ip and port
    hermes_server_ip = "127.0.0.1"
    gate = 9090
    try:
        # create a socket object
        hermes_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.AF_INET -> SHOWS THE TYPE OF IP ADDRESS IN THIS CASE IT'S IPV4,
        # socket.SOCK_STREAM -> tells hermes to use tcp.

        # makes hermes listen through this ip and gate, using the bind method
        hermes_server.bind((hermes_server_ip, gate))

        # now make hermes listen for clients
        hermes_server.listen() # the argument in the listen method signifies the number of clients it should accept, in this case only one.
        print(f"Hermes is waiting for clients at {hermes_server_ip}:{gate}....")

        while True:
            # accepting incoming connections
            client_socket, client_addr = hermes_server.accept()
            print(f"Hermes accepted connection between, {client_addr[0]}:{client_addr[1]}")
            thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
            thread.start()
            client_socket.send(f"{client_addr[1]} has joined the chat :)".encode("utf-8"))


    except Exception as e:
        print(f"error: {e}")
    finally:
        hermes_server.close()

deploy_hermes()
