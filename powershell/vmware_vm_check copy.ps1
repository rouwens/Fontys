Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Connect-VIServer -Server 192.168.251.2 -Protocol https -User sa_gns3 -Password C9jZF3wEttlzrcqflxJZ
$Exists = get-vm -name PROCNLVNRG303 -ErrorAction SilentlyContinue
If ($Exists){
	Write-Output "VM is there"
    
}
Else {
	Write "VM not there"
	New-Item ./vm
}





line_vm_name = "$vmName = " + "'" + vm_name + "'" + "\n"

            b_file = open("powershell/vmware_vm_create.ps1", "r")
            list_of_lines = b_file.readlines()

            list_of_lines[0] = line_vm_name
            list_of_lines[2] = line_cred
            

            b_file = open("powershell/vmware_vm_check.ps1", "w")
            b_file.writelines(list_of_lines)
            b_file.close()
