Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Connect-VIServer -Server 192.168.254.34 -Protocol https -User root -Password Daan0409.
Start-VM -VM "webserver-scaling-backup"
Start-Sleep -s 60
Stop-VM -VM Web -Confirm:$false
Get-VM -Name Web | Set-VM -MemoryGB 4 -Confirm:$false
Get-VM -name web | Set-VM -NumCpu 4 -Confirm:$false
Start-VM -VM "Web"
Start-Sleep -s 60
Stop-VM -VM webserver-scaling-backup -Confirm:$false
