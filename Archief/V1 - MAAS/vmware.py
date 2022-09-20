import os
import configparser
from time import sleep


start = 1
counter = 0
vm_present = ""
#max_gns3_nodes = 6

config = configparser.ConfigParser()
config.read('config.ini')

vmware_host = config['vmware']['host']
vmware_username = config['vmware']['username']
vmware_password = config['vmware']['password']
str_max_gns3_nodes = config['vmware']['max_vm']

int_max_gns3_nodes = int(str_max_gns3_nodes)

while start == 1:
    if counter != int_max_gns3_nodes:
        counter += 1
        str_counter = str(counter)
        vm_name = "PROCNLVNRG30" + str_counter
        
        line_cred = "Connect-VIServer -Server " + vmware_host + " -Protocol https -User " + vmware_username + " -Password " + vmware_password + "\n"
        line_vm = "$Exists = get-vm -name " + vm_name +" -ErrorAction SilentlyContinue" + "\n"
        
        a_file = open("powershell/vmware_vm_check.ps1", "r")
        list_of_lines = a_file.readlines()

        list_of_lines[1] = line_cred
        list_of_lines[2] = line_vm

        a_file = open("powershell/vmware_vm_check.ps1", "w")
        a_file.writelines(list_of_lines)
        a_file.close()

        cmd = "pwsh ./powershell/vmware_vm_check.ps1"
        os.system(cmd)

        vm_present = os.path.isfile("./vm")

        if vm_present == False:
            print ("VM does exist")
                    
        else:
            print ("VM doesn't exists")
            os.remove ("./vm")
            line_vm_name = "$vmName = " + "'" + vm_name + "'" + "\n"

            b_file = open("powershell/vmware_vm_create.ps1", "r")
            list_of_lines = b_file.readlines()

            list_of_lines[0] = line_vm_name
            list_of_lines[2] = line_cred
            

            b_file = open("powershell/vmware_vm_check.ps1", "w")
            b_file.writelines(list_of_lines)
            b_file.close()

        
        