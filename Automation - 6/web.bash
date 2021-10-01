#!/bin/bash
apt upgrade -y
apt install apache2 php7.4 php7.4-mysql php7.4-curl php7.4-json php7.4-cgi php7.4-xsl php7.4-zip zip -y
hostnamectl set-hostname maas-web
cd /var/www/html/
rm *
wget https://nl.wordpress.org/latest-nl_NL.zip
unzip latest-nl_NL.zip
cd wordpress
mv * /var/www/html/
chmod -R 0777 /var/www/html/
systemctl restart apache2