import discord
import os
import configparser
import subprocess

client = discord.Client()

config = configparser.ConfigParser()
config.read('../../discordtoken.ini')
token = config['discord']['token']


@client.event
async def on_ready():
    print('Bot online')

@client.event
async def on_message(message):
   
    if message.author == client.user:
        return

    if message.content.startswith('kernel_version_freeipa'):
        proc = subprocess.Popen(["ssh 192.168.123.10 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_freeipa, err) = proc.communicate()
        str_ssh_kernel_version_freeipa = str(ssh_kernel_version_freeipa)
        clean_ssh_kernel_version_freeipa = (str_ssh_kernel_version_freeipa[2:-3])
        
        await message.channel.send("Kernel version FreeIPA server")
        await message.channel.send(clean_ssh_kernel_version_freeipa)
    
    elif message.content.startswith('kernel_version_dns'):
        proc = subprocess.Popen(["ssh 192.168.123.11 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_dns, err) = proc.communicate()
        str_ssh_kernel_version_dns = str(ssh_kernel_version_dns)
        clean_ssh_kernel_version_dns = (str_ssh_kernel_version_dns[2:-3])
        
        await message.channel.send("Kernel version DNS server")
        await message.channel.send(clean_ssh_kernel_version_dns)
    
    elif message.content.startswith('kernel_version_ansible'):
        proc = subprocess.Popen(["ssh 192.168.123.12 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_ansible, err) = proc.communicate()
        str_ssh_kernel_version_ansible = str(ssh_kernel_version_ansible)
        clean_ssh_kernel_version_ansible = (str_ssh_kernel_version_ansible[2:-3])
        
        await message.channel.send("Kernel version Ansible server")
        await message.channel.send(clean_ssh_kernel_version_ansible)
    
    elif message.content.startswith('kernel_version_database'):
        proc = subprocess.Popen(["ssh 192.168.123.13 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_database, err) = proc.communicate()
        str_ssh_kernel_version_database = str(ssh_kernel_version_database)
        clean_ssh_kernel_version_database = (str_ssh_kernel_version_database[2:-3])
        
        await message.channel.send("Kernel version Datbase server")
        await message.channel.send(clean_ssh_kernel_version_database)
    
    elif message.content.startswith('kernel_version_web'):
        proc = subprocess.Popen(["ssh 192.168.123.14 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_web, err) = proc.communicate()
        str_ssh_kernel_version_web = str(ssh_kernel_version_web)
        clean_ssh_kernel_version_web = (str_ssh_kernel_version_web[2:-3])
        
        await message.channel.send("Kernel version Web server")
        await message.channel.send(clean_ssh_kernel_version_web)
    
    elif message.content.startswith('kernel_version_elk'):
        proc = subprocess.Popen(["ssh 192.168.123.15 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_elk, err) = proc.communicate()
        str_ssh_kernel_version_elk = str(ssh_kernel_version_elk)
        clean_ssh_kernel_version_elk = (str_ssh_kernel_version_elk[2:-3])
        
        await message.channel.send("Kernel version ELK server")
        await message.channel.send(clean_ssh_kernel_version_elk)
    
    elif message.content.startswith('kernel_version_ids'):
        proc = subprocess.Popen(["ssh 192.168.123.16 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_ids, err) = proc.communicate()
        str_ssh_kernel_version_ids = str(ssh_kernel_version_ids)
        clean_ssh_kernel_version_ids = (str_ssh_kernel_version_ids[2:-3])
        
        await message.channel.send("Kernel version IDS server")
        await message.channel.send(clean_ssh_kernel_version_ids)
    
    elif message.content.startswith('kernel_version_vpn'):
        proc = subprocess.Popen(["ssh 192.168.123.17 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_vpn, err) = proc.communicate()
        str_ssh_kernel_version_vpn = str(ssh_kernel_version_vpn)
        clean_ssh_kernel_version_vpn = (str_ssh_kernel_version_vpn[2:-3])
        
        await message.channel.send("Kernel version VPN server")
        await message.channel.send(clean_ssh_kernel_version_vpn)
    
    elif message.content.startswith('kernel_version_maas'):
        proc = subprocess.Popen(["ssh 192.168.123.18 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_maas, err) = proc.communicate()
        str_ssh_kernel_version_maas = str(ssh_kernel_version_maas)
        clean_ssh_kernel_version_maas = (str_ssh_kernel_version_maas[2:-3])
        
        await message.channel.send("Kernel version MAAS server")
        await message.channel.send(clean_ssh_kernel_version_maas)
    
    elif message.content.startswith('kernel_version_mail'):
        proc = subprocess.Popen(["ssh 192.168.123.19 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_mail, err) = proc.communicate()
        str_ssh_kernel_version_mail = str(ssh_kernel_version_mail)
        clean_ssh_kernel_version_mail = (str_ssh_kernel_version_mail[2:-3])
        
        await message.channel.send("Kernel version Mail server")
        await message.channel.send(clean_ssh_kernel_version_mail)
    
    elif message.content.startswith('kernel_version_jenkins'):
        proc = subprocess.Popen(["ssh 192.168.123.20 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_jenkins, err) = proc.communicate()
        str_ssh_kernel_version_jenkins = str(ssh_kernel_version_jenkins)
        clean_ssh_kernel_version_jenkins = (str_ssh_kernel_version_jenkins[2:-3])
        
        await message.channel.send("Kernel version Jenkins server")
        await message.channel.send(clean_ssh_kernel_version_jenkins)
    
    elif message.content.startswith('kernel_version_all'):
        proc = subprocess.Popen(["ssh 192.168.123.10 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_freeipa, err) = proc.communicate()
        str_ssh_kernel_version_freeipa = str(ssh_kernel_version_freeipa)
        clean_ssh_kernel_version_freeipa = (str_ssh_kernel_version_freeipa[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.11 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_dns, err) = proc.communicate()
        str_ssh_kernel_version_dns = str(ssh_kernel_version_dns)
        clean_ssh_kernel_version_dns = (str_ssh_kernel_version_dns[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.12 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_ansible, err) = proc.communicate()
        str_ssh_kernel_version_ansible = str(ssh_kernel_version_ansible)
        clean_ssh_kernel_version_ansible = (str_ssh_kernel_version_ansible[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.13 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_database, err) = proc.communicate()
        str_ssh_kernel_version_database = str(ssh_kernel_version_database)
        clean_ssh_kernel_version_database = (str_ssh_kernel_version_database[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.14 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_web, err) = proc.communicate()
        str_ssh_kernel_version_web = str(ssh_kernel_version_web)
        clean_ssh_kernel_version_web = (str_ssh_kernel_version_web[2:-3])        
    
        proc = subprocess.Popen(["ssh 192.168.123.15 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_elk, err) = proc.communicate()
        str_ssh_kernel_version_elk = str(ssh_kernel_version_elk)
        clean_ssh_kernel_version_elk = (str_ssh_kernel_version_elk[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.16 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_ids, err) = proc.communicate()
        str_ssh_kernel_version_ids = str(ssh_kernel_version_ids)
        clean_ssh_kernel_version_ids = (str_ssh_kernel_version_ids[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.17 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_vpn, err) = proc.communicate()
        str_ssh_kernel_version_vpn = str(ssh_kernel_version_vpn)
        clean_ssh_kernel_version_vpn = (str_ssh_kernel_version_vpn[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.18 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_maas, err) = proc.communicate()
        str_ssh_kernel_version_maas = str(ssh_kernel_version_maas)
        clean_ssh_kernel_version_maas = (str_ssh_kernel_version_maas[2:-3])

        proc = subprocess.Popen(["ssh 192.168.123.19 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_mail, err) = proc.communicate()
        str_ssh_kernel_version_mail = str(ssh_kernel_version_mail)
        clean_ssh_kernel_version_mail = (str_ssh_kernel_version_mail[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.20 'uname -r'"], stdout=subprocess.PIPE, shell=True)
        (ssh_kernel_version_jenkins, err) = proc.communicate()
        str_ssh_kernel_version_jenkins = str(ssh_kernel_version_jenkins)
        clean_ssh_kernel_version_jenkins = (str_ssh_kernel_version_jenkins[2:-3])
        
        await message.channel.send("Kernel version FreeIPA server")
        await message.channel.send(clean_ssh_kernel_version_freeipa)
        await message.channel.send("-------------------------------")
        await message.channel.send("Kernel version DNS server")
        await message.channel.send(clean_ssh_kernel_version_dns)
        await message.channel.send("-------------------------------")
        await message.channel.send("Kernel version Ansible server")
        await message.channel.send(clean_ssh_kernel_version_ansible)
        await message.channel.send("-------------------------------")
        await message.channel.send("Kernel version Datbase server")
        await message.channel.send(clean_ssh_kernel_version_database)
        await message.channel.send("-------------------------------")
        await message.channel.send("Kernel version Web server")
        await message.channel.send(clean_ssh_kernel_version_web)
        await message.channel.send("-------------------------------")        
        await message.channel.send("Kernel version ELK server")
        await message.channel.send(clean_ssh_kernel_version_elk)
        await message.channel.send("-------------------------------")
        await message.channel.send("Kernel version IDS server")
        await message.channel.send(clean_ssh_kernel_version_ids)
        await message.channel.send("-------------------------------")
        await message.channel.send("Kernel version VPN server")
        await message.channel.send(clean_ssh_kernel_version_vpn)
        await message.channel.send("-------------------------------")
        await message.channel.send("Kernel version MAAS server")
        await message.channel.send(clean_ssh_kernel_version_maas)
        await message.channel.send("-------------------------------")
        await message.channel.send("Kernel version Mail server")
        await message.channel.send(clean_ssh_kernel_version_mail)
        await message.channel.send("-------------------------------")
        await message.channel.send("Kernel version Jenkins server")
        await message.channel.send(clean_ssh_kernel_version_jenkins)
    
    if message.content.startswith('uptime_freeipa'):
        proc = subprocess.Popen(["ssh 192.168.123.10 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_freeipa, err) = proc.communicate()
        str_ssh_uptime_freeipa = str(ssh_uptime_freeipa)
        clean_ssh_uptime_freeipa = (str_ssh_uptime_freeipa[2:-3])
        
        await message.channel.send("Uptime FreeIPA server")
        await message.channel.send(clean_ssh_uptime_freeipa)
    
    elif message.content.startswith('uptime_dns'):
        proc = subprocess.Popen(["ssh 192.168.123.11 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_dns, err) = proc.communicate()
        str_ssh_uptime_dns = str(ssh_uptime_dns)
        clean_ssh_uptime_dns = (str_ssh_uptime_dns[2:-3])
        
        await message.channel.send("Uptime DNS server")
        await message.channel.send(clean_ssh_uptime_dns)
    
    elif message.content.startswith('uptime_ansible'):
        proc = subprocess.Popen(["ssh 192.168.123.12 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_ansible, err) = proc.communicate()
        str_ssh_uptime_ansible = str(ssh_uptime_ansible)
        clean_ssh_uptime_ansible = (str_ssh_uptime_ansible[2:-3])
        
        await message.channel.send("Uptime Ansible server")
        await message.channel.send(clean_ssh_uptime_ansible)
    
    elif message.content.startswith('uptime_database'):
        proc = subprocess.Popen(["ssh 192.168.123.13 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_database, err) = proc.communicate()
        str_ssh_uptime_database = str(ssh_uptime_database)
        clean_ssh_uptime_database = (str_ssh_uptime_database[2:-3])
        
        await message.channel.send("Uptime Datbase server")
        await message.channel.send(clean_ssh_uptime_database)
    
    elif message.content.startswith('uptime_web'):
        proc = subprocess.Popen(["ssh 192.168.123.14 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_web, err) = proc.communicate()
        str_ssh_uptime_web = str(ssh_uptime_web)
        clean_ssh_uptime_web = (str_ssh_uptime_web[2:-3])
        
        await message.channel.send("Uptime Web server")
        await message.channel.send(clean_ssh_uptime_web)
    
    elif message.content.startswith('uptime_elk'):
        proc = subprocess.Popen(["ssh 192.168.123.15 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_elk, err) = proc.communicate()
        str_ssh_uptime_elk = str(ssh_uptime_elk)
        clean_ssh_uptime_elk = (str_ssh_uptime_elk[2:-3])
        
        await message.channel.send("Uptime ELK server")
        await message.channel.send(clean_ssh_uptime_elk)
    
    elif message.content.startswith('uptime_ids'):
        proc = subprocess.Popen(["ssh 192.168.123.16 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_ids, err) = proc.communicate()
        str_ssh_uptime_ids = str(ssh_uptime_ids)
        clean_ssh_uptime_ids = (str_ssh_uptime_ids[2:-3])
        
        await message.channel.send("Uptime IDS server")
        await message.channel.send(clean_ssh_uptime_ids)
    
    elif message.content.startswith('uptime_vpn'):
        proc = subprocess.Popen(["ssh 192.168.123.17 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_vpn, err) = proc.communicate()
        str_ssh_uptime_vpn = str(ssh_uptime_vpn)
        clean_ssh_uptime_vpn = (str_ssh_uptime_vpn[2:-3])
        
        await message.channel.send("Uptime VPN server")
        await message.channel.send(clean_ssh_uptime_vpn)
    
    elif message.content.startswith('uptime_maas'):
        proc = subprocess.Popen(["ssh 192.168.123.18 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_maas, err) = proc.communicate()
        str_ssh_uptime_maas = str(ssh_uptime_maas)
        clean_ssh_uptime_maas = (str_ssh_uptime_maas[2:-3])
        
        await message.channel.send("Uptime MAAS server")
        await message.channel.send(clean_ssh_uptime_maas)
    
    elif message.content.startswith('uptime_mail'):
        proc = subprocess.Popen(["ssh 192.168.123.19 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_mail, err) = proc.communicate()
        str_ssh_uptime_mail = str(ssh_uptime_mail)
        clean_ssh_uptime_mail = (str_ssh_uptime_mail[2:-3])
        
        await message.channel.send("Uptime Mail server")
        await message.channel.send(clean_ssh_uptime_mail)
    
    elif message.content.startswith('uptime_jenkins'):
        proc = subprocess.Popen(["ssh 192.168.123.20 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_jenkins, err) = proc.communicate()
        str_ssh_uptime_jenkins = str(ssh_uptime_jenkins)
        clean_ssh_uptime_jenkins = (str_ssh_uptime_jenkins[2:-3])
        
        await message.channel.send("Uptime Jenkins server")
        await message.channel.send(clean_ssh_uptime_jenkins)
    
    elif message.content.startswith('uptime_all'):
        proc = subprocess.Popen(["ssh 192.168.123.10 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_freeipa, err) = proc.communicate()
        str_ssh_uptime_freeipa = str(ssh_uptime_freeipa)
        clean_ssh_uptime_freeipa = (str_ssh_uptime_freeipa[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.11 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_dns, err) = proc.communicate()
        str_ssh_uptime_dns = str(ssh_uptime_dns)
        clean_ssh_uptime_dns = (str_ssh_uptime_dns[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.12 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_ansible, err) = proc.communicate()
        str_ssh_uptime_ansible = str(ssh_uptime_ansible)
        clean_ssh_uptime_ansible = (str_ssh_uptime_ansible[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.13 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_database, err) = proc.communicate()
        str_ssh_uptime_database = str(ssh_uptime_database)
        clean_ssh_uptime_database = (str_ssh_uptime_database[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.14 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_web, err) = proc.communicate()
        str_ssh_uptime_web = str(ssh_uptime_web)
        clean_ssh_uptime_web = (str_ssh_uptime_web[2:-3])        
    
        proc = subprocess.Popen(["ssh 192.168.123.15 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_elk, err) = proc.communicate()
        str_ssh_uptime_elk = str(ssh_uptime_elk)
        clean_ssh_uptime_elk = (str_ssh_uptime_elk[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.16 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_ids, err) = proc.communicate()
        str_ssh_uptime_ids = str(ssh_uptime_ids)
        clean_ssh_uptime_ids = (str_ssh_uptime_ids[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.17 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_vpn, err) = proc.communicate()
        str_ssh_uptime_vpn = str(ssh_uptime_vpn)
        clean_ssh_uptime_vpn = (str_ssh_uptime_vpn[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.18 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_maas, err) = proc.communicate()
        str_ssh_uptime_maas = str(ssh_uptime_maas)
        clean_ssh_uptime_maas = (str_ssh_uptime_maas[2:-3])

        proc = subprocess.Popen(["ssh 192.168.123.19 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_mail, err) = proc.communicate()
        str_ssh_uptime_mail = str(ssh_uptime_mail)
        clean_ssh_uptime_mail = (str_ssh_uptime_mail[2:-3])
    
        proc = subprocess.Popen(["ssh 192.168.123.20 'uptime'"], stdout=subprocess.PIPE, shell=True)
        (ssh_uptime_jenkins, err) = proc.communicate()
        str_ssh_uptime_jenkins = str(ssh_uptime_jenkins)
        clean_ssh_uptime_jenkins = (str_ssh_uptime_jenkins[2:-3])
        
        await message.channel.send("Uptime FreeIPA server")
        await message.channel.send(clean_ssh_uptime_freeipa)
        await message.channel.send("-------------------------------")
        await message.channel.send("Uptime DNS server")
        await message.channel.send(clean_ssh_uptime_dns)
        await message.channel.send("-------------------------------")
        await message.channel.send("Uptime Ansible server")
        await message.channel.send(clean_ssh_uptime_ansible)
        await message.channel.send("-------------------------------")
        await message.channel.send("Uptime Datbase server")
        await message.channel.send(clean_ssh_uptime_database)
        await message.channel.send("-------------------------------")
        await message.channel.send("Uptime Web server")
        await message.channel.send(clean_ssh_uptime_web)
        await message.channel.send("-------------------------------")        
        await message.channel.send("Uptime ELK server")
        await message.channel.send(clean_ssh_uptime_elk)
        await message.channel.send("-------------------------------")
        await message.channel.send("Uptime IDS server")
        await message.channel.send(clean_ssh_uptime_ids)
        await message.channel.send("-------------------------------")
        await message.channel.send("Uptime VPN server")
        await message.channel.send(clean_ssh_uptime_vpn)
        await message.channel.send("-------------------------------")
        await message.channel.send("Uptime MAAS server")
        await message.channel.send(clean_ssh_uptime_maas)
        await message.channel.send("-------------------------------")
        await message.channel.send("Uptime Mail server")
        await message.channel.send(clean_ssh_uptime_mail)
        await message.channel.send("-------------------------------")
        await message.channel.send("Uptime Jenkins server")
        await message.channel.send(clean_ssh_uptime_jenkins)
    
    elif message.content.startswith('ram_rpi'):
        proc = subprocess.Popen(["ssh 192.168.178.254 -l root 'free -m'"], stdout=subprocess.PIPE, shell=True)
        (ssh_ram_rpi, err) = proc.communicate()
        str_ssh_ram_rpi = str(ssh_ram_rpi)
        clean_ram_rpi = (str_ssh_ram_rpi[2:-3])
        
        await message.channel.send("RAM usage RPI")
        await message.channel.send(clean_ram_rpi)

    elif message.content.startswith('system_rpi'):
        proc = subprocess.Popen(["ssh 192.168.178.254 -l root '/root/test.bash'"], stdout=subprocess.PIPE, shell=True)
        (ssh_system_rpi, err) = proc.communicate()
        str_ssh_system_rpi = str(ssh_system_rpi)
        clean_system_rpi = (str_ssh_system_rpi[2:-3])
        
        await message.channel.send("System usage RPI")
        await message.channel.send(clean_system_rpi)


client.run(token)