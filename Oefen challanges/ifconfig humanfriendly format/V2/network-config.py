import subprocess
import os

print ("Vul hier de naam van je netwerkkaart")
kaart = input()

# Hiermee word de output van ifconfig opgeslagen in een string.
x = subprocess.check_output (['ifconfig', kaart])
text = str(x)

#Hiermee word de route tabel van het systeem uitgelezen
y = subprocess.check_output(['ip', 'r'])
text_gateway = str(y)

# Hiermee word een nslookup gedaan. In het test resultaat staat de gebruikte DNS server die ik later eruit filter.
z = subprocess.check_output(['nslookup', 'google.com'])
text_dns = str(z)

# Hier word het IP adres uit de volledige tekst geknipt.
inet_pos = text.index("inet") + 5
netmask_pos = text.index("netmask")
ip = text[inet_pos:netmask_pos]

# Hier word het subnetmasker uit de volledige tekst geknipt.
mask_voor = text.index("netmask") + len  ("netmask") + 1
mask_achter = text.index("broadcast")
mask = text[mask_voor:mask_achter]

#Hier word de defeaul gateway uit de volledige tekst geknipt.
gateway_voor = text_gateway.index("via") + 4
gateway_achter = text_gateway.index("dev")
gateway = text_gateway[gateway_voor:gateway_achter]

# Hier word de gebruikte DNS server uit de tekst geknipt.
dns_voor = text_dns.index("Server:") + 11
dns_achter = text_dns.index("Address") -2
dns = text_dns[dns_voor:dns_achter]

# Hier word het MAC adres uit het subnetmasker geknipt.
mac_voor = text.index("ether") + 5
mac_achter = text.index("txqueuelen")
mac = text[mac_voor:mac_achter]

print ()
print ("IP adres:  ",ip)
print ("Netmasker: ",mask)
print ("Gateway:   ", gateway)
print ("DNS server:", dns)
print ()
print ("Mac adres:", mac)