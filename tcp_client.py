import socket 

target_host = # CHANGE THIS
target_port = # CHANGE THIS

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

client.send(b":3\r\n")

response = client.recv(4096)
print(response.decode())

client.close()
