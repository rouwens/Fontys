import os
import linecache

#os.system("bash import.bash")
print ("Enter the name from the network interface")
interface = input()
cmd ="bash import.bash {0}".format(interface)
os.system(cmd)

ip = linecache.getline('info.txt', 1)
netmask = linecache.getline('info.txt', 2)
gateway = linecache.getline('info.txt', 3)
mac = linecache.getline('info.txt', 4)

print ("IP address: ", ip)
print ("Netmask: ", netmask)
print ("Gatway: ", gateway)
print ()
print ("MAC address: ", mac)
