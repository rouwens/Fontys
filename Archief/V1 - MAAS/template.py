#Modules importeren
import cmd
import os
import configparser
import requests
import paramiko
import json
import time
import sys

#config bestand inladen en algemene variabelen toewijzen
config = configparser.ConfigParser()
config.read('config.ini')
download_url = config['default']['download_server'] 
location_qemu_images = config['default']['location_qemu_images']
location_iou_images = config['default']['location_iou_images'] 

#SSH client
ssh = paramiko.SSHClient()
ssh_username = config['default']['ssh_username'] 
ssh_location_private_key = config['default']['ssh_location_private_key']

#Platform bepalen
system = sys.platform

#Commando bepalen om het scherm leeg te halen per platform
if system == "win32":
    clear = os.system('cls')

if system == "linux":
    clear = os.system("clear")

#Namen van de beschikbare templates
template_names = ["1 - Fortigate", "2 - Cisco Switch"]

print ("Wat is het IP adres van de GNS3 server waarop je de template wilt installeren?", end="\n")
gns3_ip = input()
print (end="\n")

print ("Templates")
print (end="\n")
print(*template_names, sep="\n")
print (end="\n")

print ("Welke template wil je uitrollen? Kies hierbij het nummer", end="\n")
use_template = input()

if use_template == "1":
    template = "template_fortigate"
    template_type = "qemu"

elif use_template == "2":
    template = "template_cisco_switch"
    template_type = "iou"

else:
    print ("Input niet herkend. Probeer het opnieuw.")


# Waardes vanuit de desbetreffende config met de juiste type aan de variabelen hangen. (alleen QEMU gebaseerde VM) 
if template_type == "qemu":
    adapter_type = config[template]['adapter_type']
    adapters = int (config[template]['adapters'])
    boot_priority = config[template]['boot_priority']
    builtin = bool (config[template]['builtin'])
    category = config[template]['category']
    compute_id = config[template]['compute_id']
    console_auto_start = bool (config[template]['console_auto_start'])
    console_type = config[template]['console_type']
    cpu_throttling = int (config[template]['cpu_throttling'])
    cpus = int (config[template]['cpus'])
    create_config_disk = bool (config[template]['create_config_disk'])
    default_name_format = config[template]['default_name_format']
    hda_disk_image = config[template]['hda_disk_image']
    hda_disk_interface = config[template]['hda_disk_interface']
    hdb_disk_image = config[template]['hdb_disk_image']
    hdb_disk_interface = config[template]['hdb_disk_interface']
    legacy_networking = bool (config[template]['legacy_networking'])
    linked_clone = bool (config[template]['linked_clone'])
    name = config[template]['name']
    on_close = config[template]['on_close']
    platform = config[template]['platform']
    port_name_format = config[template]['port_name_format']
    port_segment_size = int (config[template]['port_segment_size'])
    process_priority = config[template]['process_priority']
    qemu_path = config[template]['qemu_path']
    ram = int (config[template]['ram'])
    replicate_network_connection_state = bool (config[template]['replicate_network_connection_state'])
    symbol = config[template]['symbol']
    template_type = config[template]['template_type']
    usage = config[template]['usage']

    #Download URLs genereren
    download_image1 = "curl http://" + download_url + location_qemu_images + hda_disk_image + " -o /home/sa_gns3/GNS3/images/QEMU/" + hda_disk_image
    download_image1_md5sum = " curl http://" + download_url + location_qemu_images + hda_disk_image + " -o /home/sa_gns3/GNS3/images/QEMU/" + hda_disk_image + ".md5sum"
    download_image2 = " curl http://" + download_url + location_qemu_images + hdb_disk_image + " -o /home/sa_gns3/GNS3/images/QEMU/" + hdb_disk_image
    download_image2_md5sum = " curl http://" + download_url + location_qemu_images + hdb_disk_image + " -o /home/sa_gns3/GNS3/images/QEMU/" + hdb_disk_image + ".md5sum"

    #SSH commando genereren
    cmd = download_image1 + "; " + download_image1_md5sum + "; " + download_image2 + "; " + download_image2_md5sum
    
    #De variabelen in JSON formaat zetten
    payload = {
        "adapter_type": adapter_type,
        "adapters": adapters,
        "boot_priority": boot_priority,
        "builtin": builtin,
        "category": category,
        "compute_id": compute_id,
        "console_auto_start": console_auto_start,
        "console_type": console_type,
        "cpu_throttling": cpu_throttling,
        "cpus": cpus,
        "create_config_disk": create_config_disk,
        "default_name_format": default_name_format,
        "hda_disk_image": hda_disk_image,
        "hda_disk_interface": hda_disk_interface,
        "hdb_disk_image": hdb_disk_image,
        "hdb_disk_interface": hdb_disk_interface,
        "legacy_networking": legacy_networking,
        "linked_clone": linked_clone,
        "name": name,
        "on_close": on_close,
        "platform": platform,
        "port_name_format": port_name_format,
        "port_segment_size": port_segment_size,
        "process_priority": process_priority,
        "qemu_path": qemu_path,
        "ram": ram,
        "replicate_network_connection_state":replicate_network_connection_state,
        "symbol": symbol,
        "template_type": template_type,
        "usage": usage
    }
# Waardes vanuit de desbetreffende config met de juiste type aan de variabelen hangen. (alleen IOU gebaseerde VM) 
elif template_type == "iou":
    builtin = bool (config[template]['builtin'])
    category = config[template]['category']
    compute_id = config[template]['compute_id']
    console_auto_start = bool(config[template]['console_auto_start'])
    console_type = config[template]['console_type']
    default_name_format = config[template]['default_name_format']
    ethernet_adapters = int (config[template]['ethernet_adapters'])
    l1_keepalives = bool (config[template]['l1_keepalives'])
    name = config[template]['name']
    nvram = int (config[template]['nvram'])
    path = config[template]['path']
    ram = int (config[template]['ram'])
    serial_adapters = int(config[template]['serial_adapters'])
    startup_config = config[template]['startup_config']
    symbol = config[template]['symbol']
    template_type = config[template]['template_type']
    use_default_iou_values = bool(config[template]['use_default_iou_values'])

    #Download URLs genereren
    download_image1 = "curl http://" + download_url + location_iou_images + path + " -o /home/sa_gns3/GNS3/images/IOU/" + path
    download_image1_md5sum = " curl http://" + download_url + location_iou_images + path + " -o /home/sa_gns3/GNS3/images/IOU/" + path + ".md5sum"
    
    #SSH commando genereren
    cmd = download_image1 + "; " + download_image1_md5sum

    #De variabelen in JSON formaat zetten
    payload = {
        "builtin": builtin,
        "category": category,
        "compute_id": compute_id,
        "console_auto_start": console_auto_start,
        "console_type": console_type,
        "default_name_format": default_name_format,
        "ethernet_adapters": ethernet_adapters,
        "l1_keepalives": l1_keepalives,
        "name": name,
        "nvram": nvram,
        "path": path,
        "ram": ram,
        "serial_adapters": serial_adapters,
        "startup_config": startup_config,
        "symbol": symbol,
        "template_type": template_type,
        "use_default_iou_values": use_default_iou_values
    }

clear
print ("Overzicht")
print ()
print ("Host: " + gns3_ip)
print ("Template gegevens:")
print(json.dumps(payload, sort_keys=False, indent=4))
print ()
print ("Wil je de template uitrollen met de volgende gegevens? (y/n)" )
answer = input()
clear

if answer == "y":

    #API request om de template aan te maken uitvoeren.
    headers = {'content-type': 'application/json'}
    url = "http://" + gns3_ip + ":3080/v2/templates"
    r = requests.post(url, json=payload, headers=headers)

    # De overige images van de webserver downloaden
    
    if system == 'win32':
        k = paramiko.RSAKey.from_private_key_file(ssh_location_private_key)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=gns3_ip, username=ssh_username, pkey=k)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
        print(ssh_stdout.read().decode())

    elif system == 'linux':
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(gns3_ip, username=ssh_username,
            key_filename=os.path.join(os.path.expanduser('~'), ".ssh", "id_rsa"))
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
        print(ssh_stdout.read().decode())
    

    print ("De template is geimporteerd")
    time.sleep (2)

elif answer == "n":
    print ("Taak afgebroken door de gebruiker. Er zijn geen wijzigingen doorgevoerd")
else:
    print ("Input niet herkend. Er zijn geen wijzigingen doorgevoerd")