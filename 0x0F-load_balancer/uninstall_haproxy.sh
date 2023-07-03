#!/usr/bin/env bash
# run: sudo ./uninstall_haproxy.sh

# stop the HAProxy service - your server has systemctl/else service
sudo systemctl stop haproxy

# cleanup the HAProxy package; and traces
sudo apt-get remove --purge haproxy -y
sudo rm -rf /etc/haproxy
sudo apt-get autoremove -y

# clear the package cache:
sudo apt-get clean

echo "HAProxy has been uninstalled successfully."
