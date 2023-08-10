#!/bin/bash

wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
unzip -o platform-tools-latest-linux.zip
sudo cp platform-tools/adb /usr/local/bin/adb
sudo cp platform-tools/fastboot /usr/local/bin/fastboot
sudo rm -rf platform-tools-latest-linux.zip platform-tools
