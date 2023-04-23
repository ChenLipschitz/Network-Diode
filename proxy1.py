import socket
import hashlib

# Set up listening socket
proxy1_addr = ('10.9.0.3', 6000)
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
    print(data)
    print("recived data in proxy1")
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



# Send to neteork 
network_diode_address = ('10.9.0.4', 7000)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(network_diode_address)
    s.sendall(filedata)

