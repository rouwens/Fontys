Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Connect-VIServer -Server 192.168.251.2 -Protocol https -User sa_gns3 -Password C9jZF3wEttlzrcqflxJZ
Stop-VM -VM PROCNLVNRG301 -confirm:$false
Get-VM -Name PROCNLVNRG301 | Set-VM -MemoryGB 2 -NumCpu 2 -CoresPerSocket 2 -confirm:$false
Start-VM -VM PROCNLVNRG301 -confirm:$false
Disconnect-VIServer -Confirm:$false
