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
Disconnect-VIServer -Server * -Force