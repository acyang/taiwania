#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:36:25 2018

@author: acyang
"""
import pyotp
import subprocess
import getpass
totp = pyotp.TOTP("your_OTP_KEY")
print("Current OTP:", totp.now())

address="140.110.148.11"
username=input('USERNAME: ')
password=getpass.getpass('PASSWORD: ')
arg='sftp://'+username+':'+password+totp.now()+'@'+address+'/'
subprocess.call(['PATH\TO\WinSCP.exe', arg ], shell=True)
