import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server listening on port 12345...")


conn, addr = server_socket.accept()


message = "Hello from server!"
conn.send(message.encode())

conn.close()
