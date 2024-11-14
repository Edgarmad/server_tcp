import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen(5)
    print("Servidor iniciado y esperando conexiones...")

    while True:
        client_socket, client_address = server.accept()
        print(f"Conexión establecida con {client_address}")
        print("Hola Sr. Anderson")

        while True:
            message = client_socket.recv(1024).decode()
            
            if message == "DESCONEXION":
                print("Servidor cierra la conexión con el cliente")
                client_socket.close()
                break
            elif "matrix" in message.lower():
                client_socket.send("un easter egg".encode())
                print(f"Cliente envía: {message}, Servidor responde: easter egg")
            else:
                response = message.upper()
                client_socket.send(response.encode())
                print(f"Cliente envía: {message}, Servidor responde: {response}")

if __name__ == "__main__":
    start_server()
