#from pyVim import connect

#my_cluster = connect.ConnectNoSSL("192.168.251.2", 443, "sa_gns3", "C9jZF3wEttlzrcqflxJZ")

#searcher = my_cluster.content.searchIndex

# Find a VM
#vm = searcher.FindByIp(ip="192.168.253.3", vmSearch=True)

#cspec = vm.ConfigSpec()
#cspec.numCPUs = 4 # if you want 4 cpus
#cspec.numCoresPerSocket = 2 # if you want dual-processor with dual-cores
#cspec.memoryMB = 6096 # 1GB of memory
#vm.Reconfigure(cspec)

import os

cmd1 = "Stop-VM -VM PROCNLVNRPY01 -confirm:$false" + "\n"
cmd2 = "Get-VM -Name PROCNLVNRPY01 | Set-VM -MemoryGB 2 -NumCpu 2 -confirm:$false" + "\n"
cmd3 = "Start-VM -VM PROCNLVNRPY01 -confirm:$false" + "\n"


a_file = open("../vmware-gns3.ps1", "r")
list_of_lines = a_file.readlines()

list_of_lines[2] = cmd1
list_of_lines[3] = cmd2
list_of_lines[4] = cmd3

a_file = open("../vmware-gns3.ps1", "w")
a_file.writelines(list_of_lines)
a_file.close()

print ("Wacht")
os.system("pwsh ../vmware-gns3.ps1")

#cmd ="Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false "
#completed = subprocess.run(["pwsh", "-Command", cmd], capture_output=True)

#cmd ="Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false "
#completed = subprocess.run(["pwsh", "-Command", cmd], capture_output=True)
#print (completed)