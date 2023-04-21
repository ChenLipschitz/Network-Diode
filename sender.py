import socket
import hashlib

# Connect to proxy-1
proxy1_addr = ('localhost', 6000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(proxy1_addr)

# Select file
filename = 'file.txt'

# Send file to proxy-1
with open(filename, 'rb') as f:
    file_data = f.read()
    s.sendall(file_data)

# Calculate MD5 hash of file
file_hash = hashlib.md5(file_data)
md5_hash = file_hash.hexdigest()

# Send file data and MD5 hash to Proxy-1
message = file_data + b' ' + md5_hash.encode()
s.sendall(message)

# Receive MD5 hash from proxy-1
md5_from_proxy1 = s.recv(1024).decode()

# Compare hashes
if md5_from_proxy1 == md5_hash:
    print("File sent successfully.")
else:
    print("Error: Hashes do not match.")

# Close the connection
s.close()
