#!/bin/bash
apt upgrade -y
apt install apache2 libapache2-mod-php7.4 php7.4 php7.4-{bcmath,bz2,curl,gd,json,mbstring,mysql,xml,zip} zip open-vm-tools -y
hostnamectl set-hostname maas-web
cd /var/www/
rm -r html
wget https://download.nextcloud.com/server/releases/nextcloud-22.2.0.zip
unzip nextcloud-22.2.0.zip
mv nextcloud html
chmod -R 0777 /var/www/html/
reboot now
