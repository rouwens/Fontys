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
apt install mariadb-server open-vm-tools -y
hostnamectl set-hostname maas-sql
cd /etc/mysql/mariadb.conf.d/
rm 50-server.cnf
wget https://raw.githubusercontent.com/rouwens/Fontys/S3/Automation%20-%206/50-server.cnf
systemctl restart mysql
mysql -u root -e "CREATE USER 'daan'@'%' IDENTIFIED BY 'daan0409';"
mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'daan'@'%' IDENTIFIED BY 'daan0409';"
mysql -u root -e "CREATE DATABASE nextcloud;"
mysql -u root -e "GRANT GRANT OPTION ON *.* TO 'daan'@'%';';
