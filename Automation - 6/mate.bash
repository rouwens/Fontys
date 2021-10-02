#!/bin/bash
apt upgrade -y
apt install tasksel open-vm-tools-desktop -y
tasksel install ubuntu-mate-desktop
reboot now
