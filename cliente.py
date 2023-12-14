import socket

# Configurações do cliente
host = 'localhost'
port = 8080

# Criação do socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Conecta-se ao servidor
    client_socket.connect((host, port))

    while True:
        # Obtém a mensagem do usuário
        message = input("Digite uma mensagem para enviar ao servidor (ou 'exit' para sair): ")

        # Envia a mensagem para o servidor
        client_socket.sendall(message.encode('utf-8'))

        # Verifica se o cliente quer sair
        if message.lower() == 'exit':
            break
