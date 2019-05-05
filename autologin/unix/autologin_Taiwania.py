#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:36:25 2018

@author: acyang
"""
import sys, os
import pyotp
import getpass

servers = {
    'a': ("Taiwania","clogin1","140.110.148.11"),
    'b': ("Taiwania","clogin2","140.110.148.12"),
    'c': ("Taiwania","glogin1","140.110.148.15"),
    'd': ("Taiwania","glogin2","140.110.148.16"),
    'e': ("Taiwania2","login1","203.145.219.98"),
    'f': ("Taiwania2","login2","203.145.219.100")
}
print("Select which server you want to login:")
for id in sorted(servers):
    print(id, "):", servers[id][0],servers[id][1],servers[id][2])

choice=input('Input your choice: ')

address=servers[choice][2]
#print(address)

username=input("Input your username: ")

password=getpass.getpass("Input your password: ")

secretkey=input("Input your secretkey: ")
totp = pyotp.TOTP(secretkey)
current_otp=totp.now()
print("Current OTP:", current_otp)

os.putenv("SSHPASS", password+totp.now())

os.system("echo $SSHPASS")

cmd="sshpass -e ssh -X " + username + "@" + address
print(cmd)

os.system(cmd)

os.unsetenv("SSHPASS")