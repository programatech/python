import socket

# Configurações do servidor
host = 'localhost'
port = 8080

# Criação do socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Liga o socket ao endereço e porta especificados
    server_socket.bind((host, port))

    # Habilita o servidor para aceitar conexões
    server_socket.listen()

    print(f"Servidor ouvindo em {host}:{port}")

    # Aceita a conexão do cliente
    client_socket, client_address = server_socket.accept()
    with client_socket:
        print(f"Conexão estabelecida com {client_address}")

        while True:
            # Recebe a mensagem do cliente
            data = client_socket.recv(1024)
            if not data:
                break

            # Exibe a mensagem no console do servidor
            print(f"Mensagem recebida do cliente: {data.decode('utf-8')}")

            # Você pode adicionar lógica aqui para processar a mensagem conforme necessário
