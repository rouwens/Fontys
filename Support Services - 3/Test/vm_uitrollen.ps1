Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Connect-VIServer -Server 192.168.1.254 -Protocol https -User root -Password daan0409
Get-VM Webserver| Get-HardDisk | Copy-HardDisk -DestinationPath "[Servers] webserver-aktdp/HDD" -DestinationStorageFormat Thin
New-VM -Name webserver-aktdp -Datastore Servers -NumCPU 1 -MemoryGB 2 -NetworkName "Host-only" -Floppy -CD  -GuestID debian10_64Guest -DiskPath "[Servers] webserver-aktdp/HDD.vmdk"
Start-VM -VM "webserver-aktdp"
