import os
import random
import string
import time
import re

ssh_dns = "ssh 192.168.123.11 "
ssh_database = "ssh 192.168.123.13 "
ssh_webserver = "ssh 192.168.123.14 "
haakje = "'"
dubbelhaakje = '"'

os.system ("clear")

print ("Wat is domein naam dat je wilt gebruiken?")
domain = input()
cleandomain = re.sub(r'[^\w\s]', '', domain)
print()

tekens = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ''.join((random.choice(tekens) for i in range(5)))

print ("Downloading Wordpress")
cmd = "wget https://nl.wordpress.org/latest-nl_NL.zip"
os.system (cmd)
time.sleep (2)

print ("Unpacking Wordpress")
cmd = ("unzip latest-nl_NL.zip")
os.system (cmd)
time.sleep(3)

print ()
print ("Removing Wordpress archive")
cmd = ("rm latest-nl_NL.zip ")
os.system (cmd)
time.sleep(2)

print()
print ("Install database")

yml_database = "        name: " + cleandomain + "\n"
yml_username = "        name: " + cleandomain + "\n"
yml_password = "        password: " + password + "\n"
yml_priv     = "        priv: '" + cleandomain + ".*:ALL,GRANT'" + "\n"

a_file = open("wordpress.yml", "r")
list_of_lines = a_file.readlines()
list_of_lines[7] = yml_database
list_of_lines[12] = yml_username
list_of_lines[13] = yml_password
list_of_lines[14] = yml_priv

a_file = open("wordpress.yml", "w")
a_file.writelines(list_of_lines)
a_file.close()

cmd = "ansible-playbook wordpress.yml -k"
os.system (cmd)


print ("Configuring Wordpress")
cmd = "mv wordpress/wp-config-sample.php wordpress/wp-config.php"
os.system(cmd)
time.sleep(2)

wp_config_db = "define( 'DB_NAME', '" + cleandomain + "' );" + "\n"
wp_config_usr = "define( 'DB_USER', '" + cleandomain + "' );\n"
wp_config_pwd = "define( 'DB_PASSWORD', '" + password + "' );\n"
wp_config_host = "define( 'DB_HOST', '192.168.123.13' );\n"

# Write Wordpress DB config
a_file = open("wordpress/wp-config.php", "r")
list_of_lines = a_file.readlines()
list_of_lines[22] = wp_config_db
list_of_lines[25] = wp_config_usr
list_of_lines[28] = wp_config_pwd
list_of_lines[31] = wp_config_host

a_file = open("wordpress/wp-config.php", "w")
a_file.writelines(list_of_lines)
a_file.close()

print ()
print ("Installing Wordpress on the server")
time.sleep (2)
cmd = "ssh 192.168.123.14 'cd /home/localadmin && wget -r ftp://localadmin:daan0409@192.168.123.12/wordpress/*'"
os.system (cmd)

print ()
print("Configure Apache2")
time.sleep (2)
#Moving Wordpress files to the right place
cmd = "ssh 192.168.123.14 'echo daan0409 | sudo -S mv /home/localadmin/192.168.123.12/wordpress /var/www/html/" + cleandomain + "'"
os.system (cmd)

#Generate vhost file
serveradmin = "    ServerAdmin admin@" + domain + "\n"
servername = "    ServerName " + domain + "\n"
serveralias = "    ServerAlias www." + domain + "\n"
documentroot = "    DocumentRoot /var/www/html/" + cleandomain + "\n"

vhost = domain + ".conf"
cmd = "cp vhost.temp " + vhost
os.system (cmd)

a_file = open(vhost, "r")
list_of_lines = a_file.readlines()
list_of_lines[1] = serveradmin
list_of_lines[2] = servername
list_of_lines[3] = serveralias
list_of_lines[4] = documentroot

a_file = open(vhost, "w")
a_file.writelines(list_of_lines)
a_file.close()

#Installing vhost on the target server
cmd = "ssh 192.168.123.14 'cd /home/localadmin && wget -r ftp://localadmin:daan0409@192.168.123.12/" + vhost +"'"
os.system (cmd)

cmd = "ssh 192.168.123.14 'echo daan0409 | sudo -S mv /home/localadmin/192.168.123.12/" + vhost + " /etc/apache2/sites-available/'"
os.system (cmd)

cmd = "ssh 192.168.123.14 'echo daan0409 | sudo -S sudo a2ensite" + vhost "'"
os.system (cmd)

cmd = "ssh 192.168.123.14 'echo daan0409 | sudo systemctl restart apache2'"
os.system (cmd)

print()
print ("Cleaning up")
cmd = "rm -r wordpress"
os.system (cmd)

print ()
print ("Finisht")
print ("--------")
print ()
print ("Username = " + cleandomain)
print ("Passowrd = " + password)
time.sleep (2)
