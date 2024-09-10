import socket
import json

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

data = client_socket.recv(1024)
data_list = json.loads(data.decode())
print("Received list:", data_list)

client_socket.close()
