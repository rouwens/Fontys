import os

counter = 0
max_gns3_nodes = 6
vm_name = ""

if counter != max_gns3_nodes:
    counter += 1
    str_counter = str(counter)
    vm_name = "PROCNLVNRG30" + str_counter
    
    line1 = "$Exists = get-vm -name " + vm_name +" -ErrorAction SilentlyContinue" + "\n"
    a_file = open("./vmware.ps1", "r")
    list_of_lines = a_file.readlines()

    list_of_lines[2] = line1

    a_file = open("./vmware.ps1", "w")
    a_file.writelines(list_of_lines)
    a_file.close()

    cmd = "pwsh ./vmware.ps1"
    os.system(cmd)