import os

stat = os.system("ssh 192.168.178.254 -l root 'systemctl status apache2'")
print (stat)

if stat == 0:
    print ("Apache2 running")

else:
    print ("Apache2 stopped")