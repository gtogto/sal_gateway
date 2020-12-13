import socket

HOST = '192.168.0.72'  
PORT = 8081       

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

client_socket.sendall('Hello GW'.encode())

data = client_socket.recv(1024)
print('Received', repr(data.decode()))

client_socket.close()
