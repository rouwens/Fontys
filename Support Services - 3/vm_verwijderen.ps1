Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Connect-VIServer -Server 192.168.1.254 -Protocol https -User root -Password daan0409
Stop-VM -VM scaling-webserver-1 -Confirm:$false
Remove-VM -VM scaling-webserver-1 -Confirm:$false
