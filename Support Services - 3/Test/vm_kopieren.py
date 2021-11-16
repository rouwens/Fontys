import random
import string
import os

lengte = 5
letters = string.ascii_lowercase
willekeurige_string = ''.join(random.choice(letters) for i in range(lengte))
vm_naam = "webserver-" + willekeurige_string

cmd1 = 'Get-VM Webserver| Get-HardDisk | Copy-HardDisk -DestinationPath "[Servers] ' + vm_naam + '/HDD" -DestinationStorageFormat Thin' + "\n"
cmd2 = 'New-VM -Name Webserver-test -Datastore Servers -NumCPU 1 -MemoryGB 2 -NetworkName "Host-only" -Floppy -CD  -GuestID debian10_64Guest -DiskPath "[Servers] ' + vm_naam + '/HDD.vmdk"' + "\n"
cmd3 = 'Start-VM -VM "'+ vm_naam + '"' + "\n"

a_file = open("vm_kopieren.ps1", "r")
list_of_lines = a_file.readlines()

list_of_lines[2] = cmd1
list_of_lines[3] = cmd2
list_of_lines[4] = cmd3

a_file = open("vm_kopieren.ps1", "w")
a_file.writelines(list_of_lines)
a_file.close()

cmd = "scp vm_kopieren.ps1 daan@100.105.92.26:/home/daan"
os.system (cmd)