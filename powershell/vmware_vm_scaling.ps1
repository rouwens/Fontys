Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Connect-VIServer -Server 192.168.251.2 -Protocol https -User sa_gns3 -Password C9jZF3wEttlzrcqflxJZ
Stop-VM -VM PROCNLVNRG300 -confirm:$false
Get-VM -Name PROCNLVNRG300 | Set-VM -MemoryGB 6 -NumCpu 4 -confirm:$false
Start-VM -VM PROCNLVNRG300 -confirm:$false
