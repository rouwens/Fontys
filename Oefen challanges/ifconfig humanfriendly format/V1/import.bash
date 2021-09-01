rm info.txt
ifconfig $1 | grep inet | awk '$1 == "inet" { print $2 }' >> info.txt
ifconfig $1 | grep inet | awk '$1 == "inet" { print $4 }' >> info.txt
ip r | grep default | awk '$1 == "default" { print $3 }' >> info.txt
ifconfig $1 | grep ether | awk '$1 == "ether" { print $2 }' >> info.txt
