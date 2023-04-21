import socket
import hashlib

# Set up listening socket
proxy1_addr = ('localhost', 6000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(proxy1_addr)
s.listen()

# Wait for connection from sender
print("Proxy-1 is listening...")
conn, addr = s.accept()
print(f"Connection established with {addr}.")

# Receive file data
filedata = b''
while True:
    data = conn.recv(1024)
    if not data:
        break
    filedata += data

# Calculate MD5 hash
filehash = hashlib.md5(filedata)
md5 = filehash.hexdigest()

# Send MD5 hash to sender
conn.sendall(md5.encode())

# Close the connection
conn.close()
s.close()

# Connect to network diode
diode_addr = ('localhost', 7000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send file to network diode
s.sendto(filedata, diode_addr)

# Close the connection
s.close()
