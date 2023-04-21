import socket

# Set up listening socket
diode_addr = ('localhost', 7000)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(diode_addr)

# Connect to proxy-2
proxy2_addr = ('localhost', 8000)

# Receive UDP packets from sender and forward them to proxy-2
while True:
    data, addr = s.recvfrom(1024)
    if not data:
        break
    s.sendto(data, proxy2_addr)

# Close the connection
s.close()
