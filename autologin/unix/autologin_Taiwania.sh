#!/bin/bash

### Synchronize Time with NTP to make sure TOTP works.
#ntpdate -s time.stdtime.gov.tw

echo "Select which server you want to login:"
echo "a): Taiwania  clogin1  140.110.148.11"
echo "b): Taiwania  clogin2  140.110.148.12"
echo "c): Taiwania  glogin1  140.110.148.15"
echo "d): Taiwania  glogin2  140.110.148.16"
echo "e): Taiwania2  login1  203.145.219.98"
echo "f): Taiwania2  login2 203.145.219.100"
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
    address="140.110.148.15"
    echo "Your selection is Taiwania  glogin1  140.110.148.15"
    ;;
  "d")
    address="140.110.148.16"
    echo "Your selection is Taiwania  glogin2  140.110.148.16"
    ;;
  "e")
    address="203.145.219.98"
    echo "Your selection is Taiwania2  login1  203.145.219.98"
    ;;
  "f")
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
totp=`oathtool --totp --base32 ${secretkey}`
echo ${totp}

export SSHPASS=${password}${totp}
#echo $SSHPASS

echo "sshpass -e ssh -X ${username}"@"${address}"
sshpass -e ssh -X ${username}"@"${address}
unset SSHPASS
