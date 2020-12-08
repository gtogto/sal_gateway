# Using Hexiwear with Python
import pexpect
import time
import sys

filename = "gto_log1.txt"
 
DEVICE = "50:33:8B:F2:DB:10"
#DEVICE = "40:2E:71:72:68:4F"
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

command = "char-write-req 0x0003 47544F"
print(command)
child.sendline(command)
child.expect("written successfully", timeout=5)
print("done~!")

