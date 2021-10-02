#!/bin/bash
apt upgrade -y
apt install nodejs open-vm-tools npm -y
hostnamectl set-hostname maas-wikijs
cd /home/ubuntu
wget https://github.com/Requarks/wiki/releases/download/2.5.219/wiki-js.tar.gz
mkdir wiki
tar xzf wiki-js.tar.gz -C ./wiki
cd ./wiki
wget https://raw.githubusercontent.com/rouwens/Fontys/S3/Automation%20-%206/config.yml
cd /home/ubuntu
mv wiki /var/wiki
rm wiki-js.tar.gz
cd /etc/systemd/system
wget https://raw.githubusercontent.com/rouwens/Fontys/S3/Automation%20-%206/wiki.service
systemctl daemon-reload
systemctl start wiki
systemctl enable wiki
