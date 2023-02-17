import socket 

target_ip = 
target_port = 

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b":3 ", (target_host, target_ip))

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()