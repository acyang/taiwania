#!/bin/bash

### Synchronize Time with NTP to make sure TOTP works.
### sudo zypper in ntp to get ntpdate
#sudo ntpdate -s time.stdtime.gov.tw

echo "Select which server you want to login:"
echo "a): Taiwania  clogin1  140.110.148.11"
echo "b): Taiwania  clogin2  140.110.148.12"
echo "c): Taiwania2  login1  203.145.219.98"
echo "d): Taiwania2  login2 203.145.219.100"
read -p "Input your choice: " choice
case ${choice} in
  "a")
    address="140.110.148.11"
    echo "Your selection is Taiwania  clogin1  140.110.148.11"
    ;;
  "b")
    address="140.110.148.12"
    echo "Your selection is Taiwania  clogin2  140.110.148.12"
    ;;
  "c")
    address="203.145.219.98"
    echo "Your selection is Taiwania2  login1  203.145.219.98"
    ;;
  "d")
    address="203.145.219.100"
    echo "Your selection is Taiwania2  login2 203.145.219.100"
    ;;
  *)
    address="140.110.148.11"
    echo "You didn't select any server."
    echo "The default selection is Taiwania  clogin1  140.110.148.11"
    ;;
esac

#echo ${address}

read -p "Input your username: " username

read -s -p "Input your password: " password
echo
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
echo "sshpass -e ssh -X -o "StrictHostKeyChecking no" ${username}"@"${address}"
sshpass -e ssh -X -o "StrictHostKeyChecking no" ${username}"@"${address}
unset SSHPASS
