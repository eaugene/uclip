#!/usr/bin/env bash
echo "enter the password"
read pass
LIST_OF_APPS="xclip python2.7"

echo $pass | sudo -S apt-get update
echo $pass | sudo -S apt install -y $LIST_OF_APPS
echo $pass | sudo -S mkdir ~/uclip
echo $pass | sudo -S mv uclip /usr/local/bin
echo $pass | sudo -s cp * ~/uclip

echo "Installed Successfully"
