import socket

server_socket = socket.socket()
server_socket.bind(('', 9090))
server_socket.listen(1)
conn, addr = server_socket.accept()

data = conn.recv(1024).decode('utf-8')
print(f"Получено сообщение от клиента: {data}")

response = "Hello, client"
conn.send(response.encode('utf-8'))
print(f"Отправлено сообщение клиенту: {response}")

conn.close()
server_socket.close()