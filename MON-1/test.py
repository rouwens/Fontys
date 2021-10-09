import subprocess

def test(input):
    input = input
    proc = subprocess.Popen(["ssh 192.168.178.254 -l root 'uname -r'"], stdout=subprocess.PIPE, shell=True)
    (ssh_kernel_version_rpi, err) = proc.communicate()
    str_ssh_kernel_version_rpi = str(ssh_kernel_version_rpi)

    clean_ssh_kernel_version_rpi = (str_ssh_kernel_version_rpi[2:-3])
    input = clean_ssh_kernel_version_rpi

    return (input)

input = ""

test(input)
print (input)