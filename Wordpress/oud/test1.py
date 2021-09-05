haakje = "'"
dubbelhaakje = '"'
host = "%"
at = "@"
wachtwoord = "blabla"
einde = ";'"
cleandomain = "rouwensorg"
ssh_database = "ssh 192.168.123.13 "
cmd = "echo daan0409 |sudo -S mysql -u root -e "
sql_database_cmd = "'create database "
sql_gebruiker_part1 = "CREATE USER " 'test'@'%'
sql_gebruiker_part2 = "IDENTIFIED BY "
database = cleandomain + ";'"
temp ="\n"

sql_database = ssh_database + dubbelhaakje + cmd + sql_database_cmd + database + dubbelhaakje + temp
sql_user = ssh_database + dubbelhaakje + cmd + sql_gebruiker_part1 + haakje + cleandomain + haakje + at + haakje + host + haakje + sql_gebruiker_part2 + haakje + wachtwoord + haakje + einde
a_file = open("shell.bash", "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = sql_database
list_of_lines[1] = sql_user

a_file = open("shell.bash", "w")
a_file.writelines(list_of_lines)
a_file.close()
