import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    hermes_server_ip = "127.0.0.1"
    gate = 9090

    client.connect((hermes_server_ip, gate))

    try:
        while True:
            msg = input("Enter your message: ")
            client.send(msg.encode("utf-8")[:1024])

            response = client.recv(1024)
            response = response.decode("utf-8")

            if response.lower() == "closed":
                break

            print(f"Received: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        print(f"Connection to hermes lost")

run_client()