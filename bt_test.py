# Using Hexiwear with Python
import pexpect
import time
import sys
import socket
import binascii
import pygatt 
from bluepy.btle import Peripheral

HOST = '192.168.0.3'
PORT = 8088

filename = "gto_log1.txt"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()
client_socket, addr = server_socket.accept()

print("logging Start")
orig_stdout = sys.stdout
sys.stdout = open(filename, 'w')
print('connected By.', addr)
data=client_socket.recv(1024)
print('received from', addr, data.decode())
recvData = data.decode('UTF-8')

#recvData = data.decode()
#getPassword = recvData[21:27]
print('instant origin password = ', recvData)
getPassword = recvData[2:8]
passwordCount = recvData[1:2]
print('instant get password = ', getPassword)
print('instant hex password = ', getPassword.encode("utf-8").hex())
print('Password Count = ', passwordCount)
#binascii.hexlify(b'getPassword')
#print(getPassword.encode("utf-8").hex())
#passwordCount = (getPassword.encode("utf-8").hex())[0:2]
#print('pw count = ', passwordCount)
#print(recvData.encode("utf-8").hex())
#DEVICE = "50:33:8B:F2:DB:10" #SAL_DOOR0
#DEVICE = "40:2E:71:72:68:4F"
#SAL_GW0
DEVICE = "50:33:8B:F1:28:57" #SAL_GW0
service_uuid = "0000ffe0-0000-1000-8000-00805f9b34fb"
read_uuid = "0000ffe1-0000-1000-8000-00805f9b34fb"
print("Hexiwear address:"),
print(DEVICE)
# Run gatttool interactively.
print("Run gatttool...")
child = pexpect.spawn("gatttool -I")

# Connect to the device.
print("Connecting to "),
print(DEVICE),
child.sendline("connect {0}".format(DEVICE))
child.expect("Connection successful", timeout=5)
#print(" Connected!") 
#child.sendline("char-write-req 0x0003 47544F")
print(" Connected!")
#value = DEVICE.char_read("0000ffe1-0000-1000-8000-00805f9b34fb")
# function to transform hex string like "0a cd" into signed integer
def hexStrToInt(hexstr):
	val = int(hexstr[0:2],16) + (int(hexstr[3:5],16)<<8)
	if ((val&0x8000)==0x8000): # treat signed 16bits
		val = -((val^0xffff)+1)
	return val
# data logging untile press 'Ctrl+C'
#print("logging start")
#orig_stdout = sys.stdout
#sys.stdout = open(filename, 'w')

if (passwordCount == '1'):
    command = "char-write-req 0x0003 5B3158" + getPassword.encode("utf-8").hex() + "5D"
    print(command)
    child.sendline(command)
    child.expect("written successfully", timeout=5)
    print("1st pw done~!")

elif (passwordCount == '2'):
    command = "char-write-req 0x0003 5B3258" + getPassword.encode("utf-8").hex() + "5D"
    print(command)
    child.sendline(command)
    child.expect("written successfully", timeout=5)
    print("2nd pw done~!")

else:
    print("warning password")

"""
while True:
	time.sleep(2)
	data = client_socket.recv(1023)

	print('recv from', addr, data.decode())
	client_socket.sendall(data)
"""
"""
# BLE Message
try:
	while True:
		command = "char-write-cmd 0x0003 5B31583132333435365D"
		print(command)
		child.sendline(command)
#sleep(2)
#child.expect("written successfully", timeout=10)
#child.sendline("char-read-hnd 0x0003")
#child.expect("\r\n", timeout=10)
#print(child.before)

except KeyboardInterrupt:
	pass
"""
#child.sendline("char-read-hnd 0x0003")
#child.expect("\r\n", timeout=10)
#print(child.before)

client_socket.close()
server_socket.close()

sys.stdout.close()
#sys.stdout = orig_stdouti

print(" ")
print("Logging end")
