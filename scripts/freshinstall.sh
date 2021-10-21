#!/bin/bash

# Edit .bashrc to include ~/.bash_personal
sed -i 's/.bash_aliases/.bash_personal/g' ~/.bashrc
source ~/.bashrc

# Update packages and install personal packages
sudo apt update
sudo apt install -y python-is-python3 neofetch exa
pkgupdate
pkgpurge

printf "\n\n\n\n########## Don't forget to copy your ssh keys to ~/.ssh/ ##########\n"
