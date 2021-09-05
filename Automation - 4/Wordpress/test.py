import re 

domain = "rouwens.com"
haakje = "'"
ssh = "ssh 192.168.123.13 "
cmd = "echo daan0409 |sudo -S mysql -u root -e "
sql = "'create database "
database = domain + ";'"

print (ssh + haakje + cmd + sql + database + haakje)
test = re.sub(r'[^\w\s]', '', cmd)
print (test)
