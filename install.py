#!/bin/python3
from os import system as sys
from os import geteuid as usertype
from sys import exit as terminate 

# 0. Root is needed
if not usertype() == 0:
    print('[X] Must run script as root')
    terminate(1)

# 1. Ensure that you've got pip
sys('sudo apt install python3-pip')

# 2. Install termcolor
sys('pip3 install termcolor')

# 3. Grab script
sys('wget https://raw.githubusercontent.com/Adri6336/pybudget/main/pybudget > /dev/null 2>&1')  # Downloads the script

# 4. Make script executable
sys('chmod +x pybudget')  # Makes the script executable

# 5. Give info
print('[i] Pybudget is now ready to use!')
print('[i] Start by entering command, "./pybudget <paycheck value>".')

# END
terminate(0)
