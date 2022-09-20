import os
import configparser

vm_name = ""
vm_ram = ""
vm_cpu = ""

config = configparser.ConfigParser()
config.read('config.ini')

vmware_host = config['vmware']['host']
vmware_username = config['vmware']['username']
vmware_password = config['vmware']['password']

print ("Wat is de naam van VM waarvan je de specs wilt veranderen?")
vm_name = input()

print()
print ("Hoeveelheid RAM?")
vm_ram = input()

print ()
print ("Hoeveelheid CPU?")
vm_cpu = input ()

os.system("clear")
print ("VM naam: " + vm_name)
print ("RAM: " + vm_ram)
print ("CPU: " + vm_cpu)
print ()
print ("Kloppen deze gegevens? y/n")
answer = input()

if answer == "y":

    line_cred = "Connect-VIServer -Server " + vmware_host + " -Protocol https -User " + vmware_username + " -Password " + vmware_password + "\n"
    line_vm_stop = "Stop-VM -VM " + vm_name + " -confirm:$false" + "\n"
    line_vm_change = "Get-VM -Name " + vm_name + " | Set-VM -MemoryGB " + vm_ram + " -NumCpu " + vm_cpu + " -confirm:$false" + "\n"
    line_vm_start = "Start-VM -VM " + vm_name + " -confirm:$false" + "\n"

    a_file = open("powershell/vmware_vm_scaling.ps1", "r")
    list_of_lines = a_file.readlines()

    list_of_lines[1] = line_cred
    list_of_lines[2] = line_vm_stop
    list_of_lines[3] = line_vm_change
    list_of_lines[4] = line_vm_start

    a_file = open("powershell/vmware_vm_scaling.ps1", "w")
    a_file.writelines(list_of_lines)
    a_file.close()

    cmd = "pwsh ./powershell/vmware_vm_scaling.ps1"
    os.system(cmd)

    print ()
    print ("Wijzigingen zijn doorgevoerd")

elif answer == "n":
    print ()
    print ("Wijzigingen niet toegepast, afgebroken door de gebruiker")

else:
    print ()
    print ("Input niet herkend, er zijn geen wijzigingen doorgevoerd")