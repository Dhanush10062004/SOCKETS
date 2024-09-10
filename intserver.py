import socket
import struct


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server listening on port 12345...")


conn, addr = server_socket.accept()


integer = 12345
conn.send(struct.pack('!I', integer))

conn.close()
