#!/bin/bash

# install git 
sudo apt install git -y

# clone from repo in xui-assistant directory
git clone https://github.com/sina0101/asiss-xui.git/root/assis-xui/



# مسیر فعلی را به دست می‌آورد
current_dir=$(dirname "$0")

# اجرای فایل پایتون
python3 "$current_dir/src.py"
