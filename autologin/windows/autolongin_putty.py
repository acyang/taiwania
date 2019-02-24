#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:36:25 2018
Setting custom command in winscp
-------
C:\Python35\python.exe D:\PortablePrograms\Winscp\autolongin_putty.py !U !@
-------
!U expands as usename
!@ expands as ipaddress
And this script mapping xdata node to normal login node.
@author: acyang
"""
import sys
import pyotp
import subprocess
import getpass
import time
totp = pyotp.TOTP("CBUPKACCSXQS7GLI5AH72QCG4VJYJRGKUDMW5TL4YGW7X5XEE7BQ====")
current_otp=totp.now()
print("Current OTP:", totp.now())

def host_mapping (input_ip):
    destination={
        "140.110.148.11" : "140.110.148.11",
        "140.110.148.12" : "140.110.148.12",
        "140.110.148.15" : "140.110.148.15",
        "140.110.148.16" : "140.110.148.16",
        "140.110.148.21" : "140.110.148.12",
        "140.110.148.22" : "140.110.148.16",
        "203.145.219.98" : "203.145.219.98",
        "203.145.219.100" : "203.145.219.100",
        "203.145.219.101" : "203.145.219.98",
        "203.145.219.102" : "203.145.219.100"
    }
    return destination.get(input_ip, None)

username=sys.argv[1]
#print(username)

address=host_mapping(sys.argv[2])
#print(address)


password=getpass.getpass('PASSWORD: ')

commnd1='D:\PortablePrograms\Winscp\putty.exe'

arg2="-ssh"
arg3="-X"
arg4=username+"@"+address
arg5="-pw"
arg6=password+totp.now()

subprocess.Popen([commnd1, arg2, arg3, arg4, arg5, arg6 ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
