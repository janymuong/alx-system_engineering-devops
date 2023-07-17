#!/usr/bin/env bash
# install UFW if not already installed

sudo apt-get update -y
sudo apt-get install -y ufw

# configure ufw to allow necessary tcp ports
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp

echo "yes" | sudo ufw enable

# enable port forwarding rules in ufw config file:
sudo bash -c 'cat <<EOT >> /etc/ufw/before.rules
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
EOT'

# restart ufw to apply changes
sudo ufw disable
sudo ufw enable
sudo ufw status
