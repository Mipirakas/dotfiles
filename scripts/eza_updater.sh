#!/bin/bash

wget https://github.com/eza-community/eza/releases/latest/download/eza_x86_64-unknown-linux-gnu.tar.gz

sudo tar -xvzf eza_x86_64-unknown-linux-gnu.tar.gz -C /usr/local/bin
sudo rm -rf eza_x86_64-unknown-linux-gnu.tar.gz
