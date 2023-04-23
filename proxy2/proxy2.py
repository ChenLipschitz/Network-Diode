import socket

# Set up listening socket
proxy2_addr = ('10.9.0.5', 8000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(proxy2_addr)
s.listen()

# Wait for connection from network-diode
print("proxy2 is listening...")
conn, addr = s.accept()
print(f"Connection established with {addr}.")

# Receive file data
filedata = b''
while True:
    data = conn.recv(1024)
    print(data)
    print("recived data in proxy2")
    if not data:
        break
    filedata += data


# Connect to user
user_addr = ('10.9.0.6', 9000)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(user_addr)
    s.sendall(filedata)

# Close the connection
s.close()


