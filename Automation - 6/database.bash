#!/bin/bash
apt upgrade -y
apt install mariadb-server open-vm-tools -y
hostnamectl set-hostname maas-sql
cd /etc/mysql/mariadb.conf.d/
rm 50-server.cnf
wget https://raw.githubusercontent.com/rouwens/Fontys/S3/Automation%20-%206/50-server.cnf
systemctl restart mysql
mysql -u root -e "CREATE USER 'daan'@'%' IDENTIFIED BY 'daan0409';"
mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'daan'@'%' IDENTIFIED BY 'daan0409';"
mysql -u root -e "CREATE DATABASE nextcloud;"
mysql -u root -e "GRANT GRANT OPTION ON *.* TO 'daan'@'%';"
