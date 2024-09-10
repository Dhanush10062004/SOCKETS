import socket
import os

# Define the buffer size
BUFFER_SIZE = 4096

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is listening on port 12345...")

# Accept a connection
conn, addr = server_socket.accept()
print(f"Connection from {addr}")

# Specify the file to send
filename = "hello.txt"
filesize = os.path.getsize(filename)

# Send filename and filesize to the client
conn.send(f"{filename},{filesize}".encode())

# Open the file and send it in chunks
with open(filename, "rb") as file:
    while True:
        # Read the file in chunks of BUFFER_SIZE
        bytes_read = file.read(BUFFER_SIZE)
        if not bytes_read:
            break
        conn.sendall(bytes_read)

print("File sent successfully!")
conn.close()
server_socket.close()
