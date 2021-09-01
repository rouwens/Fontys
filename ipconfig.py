# open cmd and convert the text into strings.
# https://superuser.com/questions/19992/is-it-possible-for-ipconfig-on-vista-to-display-the-status-of-one-adapter-only

import subprocess

print ("What's the name of the interface?")
interfaceinput = input()
interface = '"' + interfaceinput + '"'
cmd = "netsh interface ip show addresses " + interface

process = subprocess.check_output(cmd ).decode('utf-8')
text = str(process)

# here you substract the ipv4 address from the text.
device_ip = text.index("IP Address") +36 
subnet_mask = text.index("Subnet Prefix")
ip_address = text[device_ip:subnet_mask]
print("Your device's IPv4 address:", ip_address)

# here you substract the subnet mask from the text.
subnet_mask = text.index("mask") +5
default_gate = text.index(")") 
subnet = text[subnet_mask:default_gate]
print("Your internet's Subnet Mask:", subnet)
