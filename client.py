class Client:
    def __init__(self, addr, client_socket):
        self.addr = addr
        self.client_socket = client_socket
        self.name = None
        self.password = None

    def set_name(self, name):
        self.name = name
    def __repr__(self):
        return f"Client({self.name}, {self.addr})"


class user:
    """Responsible for peer to peer communication"""

    def __init__(self, name):
        self.name = name

    