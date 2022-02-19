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

# END
terminate(0)
