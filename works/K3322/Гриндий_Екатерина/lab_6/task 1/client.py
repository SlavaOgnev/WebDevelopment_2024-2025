import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 9090))

message = "Hello, server"
client_socket.send(message.encode('utf-8'))
print(f"Отправлено сообщение на сервер: {message}")

response = client_socket.recv(1024).decode('utf-8')
print(f"Получено сообщение от сервера: {response}")

client_socket.close()