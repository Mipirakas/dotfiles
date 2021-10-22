#!/bin/bash

# Update packages
sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo apt clean
dpkg  --get-selections | grep deinstall | awk '{print $1}' | xargs sudo apt purge -y
