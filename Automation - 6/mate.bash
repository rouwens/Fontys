#!/bin/bash
apt upgrade -y
hostnamectl set-hostname pc2
apt install tasksel open-vm-tools-desktop -y
tasksel install ubuntu-mate-desktop
reboot now
