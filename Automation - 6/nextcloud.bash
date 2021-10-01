#!/bin/bash
apt upgrade -y
apt install apache2 libapache2-mod-php7.4 php7.4 php7.4-{bcmath,bz2,curl,gd,json,mbstring,mysql,xml,zip} zip open-vm-tools -y
hostnamectl set-hostname maas-nextcloud
cd /var/www/
rm -r html
wget https://download.nextcloud.com/server/releases/nextcloud-22.2.0.zip
unzip nextcloud-22.2.0.zip
mv nextcloud html
chmod -R 0777 /var/www/html/
cd /home/ubuntu
wget https://files.phpmyadmin.net/phpMyAdmin/5.1.1/phpMyAdmin-5.1.1-all-languages.zip
unzip phpMyAdmin-5.1.1-all-languages.zip
mv phpMyAdmin-5.1.1-all-languages phpmyadmin
mv phpmyadmin /var/www/html/
cd /var/www/html/phpmyadmin
wget https://raw.githubusercontent.com/rouwens/Fontys/S3/Automation%20-%206/config.inc.php
chmod 0644 config.inc.php
