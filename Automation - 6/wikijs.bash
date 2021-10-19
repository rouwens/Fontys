#!/bin/bash
apt upgrade -y
apt install open-vm-tools docker.io -y
hostnamectl set-hostname maas-wikijs
docker run -d -p 80:3000 --name wiki --restart unless-stopped -e "DB_TYPE=mysql" -e "DB_HOST=192.168.13.3" -e "DB_PORT=3306" -e "DB_USER=daan" -e "DB_PASS=daan0409" -e "DB_NAME=wiki" requarks/wiki:2
