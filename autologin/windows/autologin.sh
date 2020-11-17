#!/bin/bash

### wt.exe wsl.exe ~/bin/autologin.sh !U !@ !#
### Synchronize Time with NTP to make sure TOTP works.
### sudo zypper in ntp to get ntpdate
#sudo ntpdate -s time.stdtime.gov.tw

case $2 in
  "140.110.148.21")
    address="140.110.148.11"
    ;;
  "140.110.148.22")
    address="140.110.148.12"
    ;;
  "203.145.219.101")
    address="203.145.219.98"
    ;;
  "203.145.219.102")
    address="203.145.219.100"
    ;;
  *)
    address="140.110.148.11"
    echo "Cannot mapping target server, the default selection is Taiwania  clogin1  140.110.148.11"
    ;;
esac

echo "You are connecting to ${address}"

#read -p "Input your username: " username
username=$1
read -s -p "Input your password: " password

read -p "Input your secretkey: " secretkey

### Make sure you have oathtool installed in your system.
### The following cmd is for oathtool 2.4.1
### sudo zypper in oath-toolkit
totp=`oathtool --totp --base32 ${secretkey}`
echo ${totp}

### Make sure you have sshpass installed in your system.
### sudo zypper in sshpass
export SSHPASS=${password}${totp}
#echo $SSHPASS

### Use -o "StrictHostKeyChecking no" to avoid prompte
### Make sure your openssh version is higer than 7.6
echo "sshpass -e ssh -X -o 'StrictHostKeyChecking no' ${username}"@"${address}"
sshpass -e ssh -X -o "StrictHostKeyChecking no" ${username}"@"${address}
unset SSHPASS
