import socket
import hashlib
from tqdm import tqdm

# Connect to proxy-2
proxy2_addr = ('localhost', 7000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(proxy2_addr)

# Receive file data
filedata = b''
filesize = 0
with tqdm(total=filesize, unit='B', unit_scale=True, desc='Downloading', leave=False) as pbar:
    while True:
        data = s.recv(1024)
        if not data:
            break
        filedata += data
        filesize += len(data)
        pbar.update(len(data))
file_data, md5_hash = data.split(b' ')


# Close the connection
s.close()

# Write received file data to a file
filename = 'received_file.txt'
with open(filename, 'wb') as f:
    f.write(filedata)

# Calculate MD5 hash
with open(filename, 'rb') as f:
    filehash = hashlib.md5()
    while chunk := f.read(4096):
        filehash.update(chunk)

# Compare hashes
if filehash.hexdigest() == md5_hash.decode():
    print("File downloaded successfully.")
else:
    print("Error: Hashes do not match.")
