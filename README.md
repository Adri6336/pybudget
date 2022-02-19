# Pybudget
This is a python script that will determine your budget for your current pay period.

![pybudget_](https://repository-images.githubusercontent.com/461317333/36a9c308-a924-450f-b711-b795621c86cc)

# Using Pybudget

Pybudget is currently incompatible with Windows and must be ran on a Linux distro. 

First you'll need to install by running the install script as a super user. In a Debian/Ubuntu 
based distro, you'll do this by opening the terminal where you downloaded the script and entering:
> sudo python3 install.py

If you don't want to run the script for this, you can install the requirements manually.
1. sudo apt install python3-pip
2. pip3 install termcolor

After installing the requirements, navigate to the directory where you downloaded the 
script to in the terminal and enter the following commands:

1. chmod +x pybudget
2. ./pybudget \<your paycheck or total income for the pay period without the dollar sign \>
3. The above command will prompt the script to make two files for you (config and expenses). Fill them as you're told by the bot.
4. Press the up arrow on your keyboard to get the command in the second step, press enter.
5. Enjoy a budget according to your specifications!
