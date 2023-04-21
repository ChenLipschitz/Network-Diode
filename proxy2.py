import socket

# Set up listening socket
proxy2_addr = ('localhost', 8000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(proxy2_addr)

# Receive file data and write it to a file
filename = 'received_file.txt'
with open(filename, 'wb') as f:
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        f.write(data)

# Close the connection
s.close()

# Connect to receiver
receiver_addr = ('localhost', 9000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(receiver_addr)

# Send file data to receiver
with open(filename, 'rb') as f:
    s.sendall(f.read())

# Close the connection
s.close()
