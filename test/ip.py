from IPy import IP

print ("Vul IP adres in")
ip = input()

import socket
try:
    socket.inet_aton(ip)

except socket.error:
    print ("fout")