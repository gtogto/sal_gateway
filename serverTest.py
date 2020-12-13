import socket
import time
import requests, json

HOST = '192.168.0.72'
PORT = 8081        

num = 1

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()
client_socket, addr = server_socket.accept()

print('Connected by', addr)

#response=requests.post(url, headers=header, data=date)
data=client_socket.recv(1024)
print('received from', addr, data.decode())
while True:	
    time.sleep(2)
#data = client_socket.recv(1024)
		
#if not data:
#        break


#print('Received from', addr, data.decode())
    #data = {'name': 'gw', 'content': 'ok', 'num': num}
    #print("send: name: {0}, content: {1}".format(data['name'], data['content']))
    #client_socket.sendall(json.dumps(data).encode('UTF-8'))
    client_socket.sendall('instant Password Received okay!'.encode())
    #response=requests.post(url, headers=header, data=data)


client_socket.close()
server_socket.close()
