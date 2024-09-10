import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server listening on port 12345...")


conn, addr = server_socket.accept()

data_list = [1, 2, 3, 4, 5]
conn.send(json.dumps(data_list).encode())

conn.close()
