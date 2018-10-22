#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:36:25 2018

@author: acyang
"""
import pyotp
import subprocess
import getpass
import time
totp = pyotp.TOTP("YOUR_OTP_PRIVATE_KEY")
current_otp=totp.now()
print("Current OTP:", totp.now())

address="140.110.148.11"
username=input('USERNAME: ')
password=getpass.getpass('PASSWORD: ')

commnd2='PATH\TO\putty.exe'
arg2="-ssh"
arg3="-X"
arg4=username+"@"+address
arg5="-pw"
arg6=password+totp.now()

#subprocess.call([commnd2, arg2, arg3, arg4, arg5, arg6 ], shell=True)
subprocess.Popen([commnd2, arg2, arg3, arg4, arg5, arg6 ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#subprocess.Popen(['mspaint.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

count = 0
while count < 30:
    time.sleep(1)
    count += 1
    if totp.verify(current_otp)!=True:
        print("renew OTP done.")
        break
    print("Wait for new OTP "+str(count)+"/30")

commnd1='PATH\TO\WinSCP.exe'
arg1='sftp://'+username+':'+password+totp.now()+'@'+address+'/'

#subprocess.call([commnd1, arg1 ], shell=True)
subprocess.Popen([commnd1, arg1], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#subprocess.Popen(['notepad.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
