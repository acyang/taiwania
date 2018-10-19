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
totp = pyotp.TOTP("YOUR_OTPPRIVATE_KEY")
current_otp=totp.now()
print("Current OTP:", totp.now())

address="140.110.148.11"
username=input('USERNAME: ')
password=getpass.getpass('PASSWORD: ')

commnd1='PATH\TO\WINSCP\WinSCP.exe'
arg1='sftp://'+username+':'+password+totp.now()+'@'+address+'/'

subprocess.call([commnd1, arg1 ], shell=True)

if( totp.verify(current_otp)==True): # => True
    print("Current OTP:", totp.now(), "is still work")
else:
    print("Current OTP:", totp.now(), "is not still work, wait for 30s")
    time.sleep(30)
    print("Renew OTP")
    print("Current OTP:", totp.now())

commnd2='PATH\TO\PUTTY\putty.exe'
arg2="-ssh"
arg3="-X"
arg4=username+"@"+address
arg5="-pw"
arg6=password+totp.now()

subprocess.call([commnd2, arg2, arg3, arg4, arg5, arg6 ], shell=True)
