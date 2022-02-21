# Pybudget
This is a python script that will determine your budget for your current pay period.

![pybudget_](https://repository-images.githubusercontent.com/461317333/36a9c308-a924-450f-b711-b795621c86cc)

# Using Pybudget

Pybudget is compatible with both Windows and Linux systems. 

## Windows

To get pybudget to run on your Windows PC, do the following:

1. Install the lastest version of [Python](https://www.python.org/).
2. Download the pybudget script.
3. Hold Win+R, then enter "powershell" into the box. Press enter.
4. Use the command cd to change folders, ls to see what's in your current folder, and pwd to see your current folder's path.
5. Use the above commands to navigate to the folder that you downloaded the script to.
6. The the command "pip install rich"
7. Enter the command "python pybudget \<put your paycheck value without the dollar sign here\>"
8. Follow the directions on the screen, then re-enter the previous command.


## Linux Distros (Debian/Ubuntu Based)
You can install the requirements manually by entering the following commands:
1. sudo apt install python3-pip
2. pip3 install termcolor

After installing the requirements, navigate to the directory where you downloaded the 
script to in the terminal and enter the following commands:

1. chmod +x pybudget
2. ./pybudget \<your paycheck or total income for the pay period without the dollar sign \>
3. The above command will prompt the script to make two files for you (config and expenses). Fill them as you're told by the bot.
4. Press the up arrow on your keyboard to get the command in the second step, press enter.
5. Enjoy a budget according to your specifications!
