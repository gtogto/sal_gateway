import pexpect
import socket 
import time
import sys
import binascii
import pygatt
from _thread import *
from bluepy.btle import Peripheral

DEVICE = "50:33:8B:F1:28:57" #SAL_GW0
service_uuid = "0000ffe0-0000-1000-8000-00805f9b34fb"
read_uuid = "0000ffe1-0000-1000-8000-00805f9b34fb"
#passwordCount = '0'

print('gateWay server Start')
 
print("Hexiwear address:"),
print(DEVICE)
 
# Run gatttool interctively.
print("Run gatttool...")
child = pexpect.spawn("gatttool -I")
 
# Connect to the device.
print("connecting to "),
print(DEVICE),
child.sendline("connect {0}".format(DEVICE))
#child.expect("Connection successfful", timeout=5)
print(" Connected! ")


def threaded(client_socket, addr):
    print('connect by : ' + addr[0], ':', addr[1])
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print('disconnected by ' + addr[0], ':', addr[1])
                break
            print('recv from' + addr[0], ':', addr[1], data.decode())
            recvData = data.decode('UTF-8')
            getPassword = recvData[2:8]
            #global passwordCount
            passwordCount = recvData[1:2]
            print('instant get password = ', recvData)
            print('substring getPassword = ' , getPassword)
            print('password Count = ' + passwordCount)
            if (passwordCount == '1'):
                command = "char-write-req 0x0003 5B3158" + getPassword.encode("utf-8").hex() + "5D"
                print(command)
                child.sendline(command)
                child.expect("written successfully", timeout=5)
                print("1st pw done~!")

            if (passwordCount == '2'):
                command = "char-write-req 0x0003 5B3258" + getPassword.encode("utf-8").hex() + "5D"
                print(command)
                child.sendline(command)
                child.expect("written successfully", timeout=5)
                print("2nd pw done~!")
            else:
                print("warning password")
            break
            #client_socket.send('gateway')

        except ConnectionResetError as e:
            print ('disconnected by' + addr[0], ':', addr[1])
            break

    client_socket.close()
    #server_socket.close()

HOST = '192.168.0.3'
PORT = 8088

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

while True:
    print('wait')

    client_socket, addr = server_socket.accept()
    start_new_thread(threaded, (client_socket, addr))

#    if (passwordCount == '1'):
#        print("1st password received!")
#    if (passwordCount == '2'):
#        print("2nd password received!")
#    elif (passwordCount == '0'):
#        print('global value not changed!')
server_socket.close()

