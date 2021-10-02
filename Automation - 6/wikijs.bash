#!/bin/bash
apt upgrade -y
apt install nodejs open-vm-tools npm -y
hostnamectl set-hostname maas-wikijs
cd /home/ubuntu
wget https://github.com/Requarks/wiki/releases/download/2.5.219/wiki-js.tar.gz
mkdir wiki
tar xzf wiki-js.tar.gz -C ./wiki
cd ./wiki
