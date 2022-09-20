import requests
import paramiko
ssh = paramiko.SSHClient()
import json

payload = {
  "compute_id": "local",
  "hda_disk_image": "fortios.qcow2",
  "hda_disk_interface": "virtio",
  "hdb_disk_image": "empty30G.qcow2",
  "hda_disk_interface": "virtio",
  "name": "FortiGate_7.0.6_TEST",
  "platform": "i386",
  "ram": "1024",
  "usage": "Default_username_is_admin_no_password _is_set",
  "template_type": "qemu"
}

test = str(payload)
headers = {'content-type': 'application/json'}
myurl = "http://192.168.219.225:3080/v2/templates"
#r = requests.post(myurl, json=payload, headers=headers)

#k = paramiko.RSAKey.from_private_key_file(".\id_rsa")
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(hostname="192.168.219.225", username="ubuntu", pkey=k)
#ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("whoami")
#print(ssh_stdout.read().decode())

print(json.dumps(payload, sort_keys=False, indent=4))