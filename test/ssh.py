import os.path
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.253.2", username="ub_localadmin",
key_filename=os.path.join(os.path.expanduser('~'), ".ssh", "id_rsa"))
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ls /mnt")
print(ssh_stdout.read().decode())