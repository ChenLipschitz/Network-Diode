import socket

filename = 'file.txt'
host = '10.9.0.3'
port = 12345

with open(filename, 'rb') as f:
    data = f.read()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(data)
