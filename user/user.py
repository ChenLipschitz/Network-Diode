import socket
import hashlib

# Set up listening socket
user_addr = ('10.9.0.6', 9000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(user_addr)
s.listen()

# Wait for connection from sender
print("User is listening...")
conn, addr = s.accept()
print(f"Connection established with {addr}.")

# Receive file data
filedata = b''
while True:
    data = conn.recv(1024)
    print(data)
    print("recived data in user")
    if not data:
        break
    filedata += data

with open("file_received.txt", "wb") as f:
    f.write(filedata)
    
# Close the connection
s.close()
