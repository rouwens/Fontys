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

sudoPassword = 'daan0409'
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

print ("Configuring Wordpress")
#cmd = "mv " +domain+"/wp-config-sample.php " +domain+ "/wp-config.php"
cmd = "mv wordpress/wp-config-sample.php wordpress/wp-config.php"
os.system(cmd)
time.sleep(2)

# Write database name
a_file = open("wordpress/wp-config.php", "r")
list_of_lines = a_file.readlines()
list_of_lines[22] = "define( 'DB_NAME', 'wordpress' );\n"

a_file = open("wordpress/wp-config.php", "w")
a_file.writelines(list_of_lines)
a_file.close()

# Write database username
a_file = open("wordpress/wp-config.php", "r")
list_of_lines = a_file.readlines()
list_of_lines[25] = "define( 'DB_USER', 'daan' );\n"

a_file = open("wordpress/wp-config.php", "w")
a_file.writelines(list_of_lines)
a_file.close()

# Write database password
a_file = open("wordpress/wp-config.php", "r")
list_of_lines = a_file.readlines()
list_of_lines[28] = "define( 'DB_PASSWORD', 'daan0409' );\n"

a_file = open("wordpress/wp-config.php", "w")
a_file.writelines(list_of_lines)
a_file.close()

# Write database location
a_file = open("wordpress/wp-config.php", "r")
list_of_lines = a_file.readlines()
list_of_lines[31] = "define( 'DB_HOST', '192.168.123.13' );\n"

a_file = open("wordpress/wp-config.php", "w")
a_file.writelines(list_of_lines)
a_file.close()

print ()
print ("Installing Wordpress on the server")
cmd = "ssh 192.168.123.14 'cd /home/localadmin && wget -r ftp://localadmin:daan0409@192.168.123.12/wordpress/*'"
os.system (cmd)

print ()
print ("Finisht")
print ("--------")
print ()
print ("Username = " + cleandomain)
print ("Passowrd = " + password)
time.sleep (2)