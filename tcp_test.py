import socket

HOST = '192.168.0.68'  
PORT = 8088

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

print('connect gto')

client_socket.sendall('Hello GW'.encode())

data = client_socket.recv(1024)
print('Received', repr(data.decode()))

client_socket.close()
