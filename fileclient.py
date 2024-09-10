import socket

BUFFER_SIZE = 4096

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

file_info = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = file_info.split(',')
filename = "received_" + filename 
filesize = int(filesize)

# Open the file to write the received data
with open(filename, "wb") as file:
    bytes_received = 0
    while bytes_received < filesize:
        # Receive data in chunks
        data = client_socket.recv(BUFFER_SIZE)
        if not data:
            break
        file.write(data)
        bytes_received += len(data)

print(f"File {filename} received successfully!")
client_socket.close()
