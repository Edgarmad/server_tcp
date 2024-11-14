import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))
    print("Conexión establecida en localhost:5000")
    print("Ingrese un mensaje (o 'DESCONEXION' para salir)")
    while True:
        message = input("> ")
        
        client.send(message.encode())
        
        if message == "DESCONEXION":
            print("Cerrando conexión...")
            client.close()
            break
        
        response = client.recv(1024).decode()
        print(f"Matrix: {response}")

if __name__ == "__main__":
    start_client()
