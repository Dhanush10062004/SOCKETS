import socket
import struct


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))


data = client_socket.recv(4)
integer = struct.unpack('!I', data)[0]
print("Received integer:", integer)

client_socket.close()
