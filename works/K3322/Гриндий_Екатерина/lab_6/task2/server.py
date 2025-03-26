import socket
import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Корни уравнения: x1 = {x1}, x2 = {x2}"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Уравнение имеет один корень: x = {x}"
    else:
        return "Уравнение не имеет действительных корней"

server_socket = socket.socket()
server_socket.bind(('localhost', 9090))
server_socket.listen(1)

while True:
    client_socket, addr = server_socket.accept()

    data = client_socket.recv(1024).decode()
    a, b, c = map(float, data.split(','))
    result = solve_quadratic_equation(a, b, c)

    client_socket.send(result.encode())
    client_socket.close()