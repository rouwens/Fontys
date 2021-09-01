import os
import ipaddress

host = '192.168.178.254'
ip = ipaddress.ip_address(host)

cmd = "ssh {0} -l root 'date'".format(ip)
exec = os.popen(cmd).read()
print (exec)
print (cmd)