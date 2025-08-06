import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print("Сервер запущен и ожидает подключений...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключен клиент: {client_address}")

        data = client_socket.recv(1024).decode()
        print('Получено сообщение:', data)

        response = f'Ответ от сервера: {data}'
        client_socket.send(response.encode())

        client_socket.close()

if __name__ == "__main__":
    server()