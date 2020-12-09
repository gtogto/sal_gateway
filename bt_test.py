# Using Hexiwear with Python
import pexpect
import time
import sys

filename = "gto_log1.txt"
 
#DEVICE = "50:33:8B:F2:DB:10"
#DEVICE = "40:2E:71:72:68:4F"
#SAL_GW0
DEVICE = "50:33:8B:F1:28:57"
#"40:2E:71:72:68:4F"
 
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

# function to transform hex string like "0a cd" into signed integer
def hexStrToInt(hexstr):
	val = int(hexstr[0:2],16) + (int(hexstr[3:5],16)<<8)
	if ((val&0x8000)==0x8000): # treat signed 16bits
		val = -((val^0xffff)+1)
	return val

# data logging untile press 'Ctrl+C'
print("logging start")
orig_stdout = sys.stdout
sys.stdout = open(filename, 'w')

command = "char-write-req 0x0003 5B31583132333435365D"
print(command)
child.sendline(command)
child.expect("written successfully", timeout=5)
print("done~!")

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

#child.sendline("char-read-hnd 0x0003")
#child.expect("\r\n", timeout=10)
#print(child.before)

sys.stdout.close()
sys.stdout = orig_stdout
print(" ")
print("Logging end")
