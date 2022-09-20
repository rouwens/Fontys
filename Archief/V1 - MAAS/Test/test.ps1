Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Connect-VIServer -Server 192.168.251.2 -Protocol https -User sa_gns3 -Password C9jZF3wEttlzrcqflxJZ

Get-VM "Daan" | Get-NetworkAdapter | Select-Object -ExpandProperty MacAddress 
Disconnect-VIServer -Server * -Force -Confirm $false



