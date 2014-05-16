#!/bin/bash
# -*- Mode: sh; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
#
# Authors:
#   Griffin Boyce
#
# Description:
#   An installation script for Ghost, for Debian-based systems.
#
# Legal Stuff:
#   GPL v3, a supervillain-friendly license.

echo '8""""8'
echo '8    " e   e eeeee eeeee eeeee'
echo '8e     8   8 8  88 8   "   8'
echo '88  ee 8eee8 8   8 8eeee   8e'
echo '88   8 88  8 8   8    88   88'
echo '88eee8 88  8 8eee8 8ee88   88'
sleep 1

#----- FUNCTIONS -----#

#run initial function
domino

# CLEAN ENVIRONMENT FIRST
function domino {

# rewrite this area

# Empty various cache files
    echo 'Preparing workspace'

# CHECK IF ROOT
    ROOT_UID="0"

    if [ "$UID" -ne "$ROOT_UID" ] ; then
        echo 'Requires administrator privileges:'

        if [[ `lsb_release -is` == "Ubuntu" ]]
            sudo apt-get autoclean
        elif [[ `lsb_release -is` == "Debian" ]]
            su -
            apt-get autoclean
        fi
    fi

# Now move to "erpdert" function
erpdert
}

#----- RUN UPDATES -----#

function erpdert {
    echo 'Running updates'
    sudo apt-get update -y -qq
    sudo apt-get upgrade -y -qq

addsource
}

#----- ADD SOFTWARE SOURCES -----#
function addsource {
# Adds sources for various Ghost dependencies

# Detect if Ubuntu
    if [[ `lsb_release -is` == "Ubuntu" ]]
        echo 'Adding software sources'
        sudo add-apt-repository ppa:chris-lea/node.js -y -qq
        sudo apt-get update -y -qq
        echo 'Done.'

# Detect if Debian

    elif [[ `lsb_release -is` == "Debian" ]]
        echo 'Adding software sources'
        apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 136221EE520DDFAF0A905689B9316A7BC7917B12
        cp /etc/apt/sources.list /etc/apt/sources.list.original
        echo "deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu lucid main" | tee -a /etc/apt/sources.list
        echo "deb-src http://ppa.launchpad.net/chris-lea/node.js/ubuntu lucid main" | sudo tee -a /etc/apt/sources.list
        apt-get update -y -qq
        echo 'Done.'

# Detect Wat
    else
        echo 'Sorry, this script is just for Ubuntu or Debian systems!'
        echo 'Using another OS? Send a request to griffin@torproject.org'
        echo 'https://github.com/glamrock/stormy'
        exit
    fi

installmenu
}

#----- INSTALL SELECTION / MENU -----#
function installmenu {
INPUT=0
echo ''
echo 'MAIN MENU'
echo 'What would you like to do? (Enter the number of your choice)'
echo ''
#while [ true ]
#do
    echo '1. Install dependencies Ubuntu 12.04 and above'
    echo '2. Install dependencies for Debian'
    echo '3. Install Ghost'
    echo '4. Finish and Exit'
    echo '5. View instructions'
#    echo '6. Install Tor (if not using Tails)'
    echo '9. Exit without installing anything'

    read INPUT

#----- Install dependencies for Ubuntu 12.04, Mint, or Backtrack/Kali ----#
if [ $INPUT -eq 1 ]; then
    echo 'Installing dependencies...'

# PYTHON
    sudo apt-get build-dep python-defaults -y -qq
    sudo apt-get update -y -qq
    sudo apt-get install python python-dev python-software-properties -y -qq

# NODE
    sudo apt-get install g++ make nodejs -y -qq
    sudo apt-get update -y -qq
    sudo apt-get install npm -y -qq
    sudo npm install forever -g

# Double-check for broken deps before finishing up
    sudo apt-get check -y -qq

# Comfort for nervous users
    echo 'Dependencies installed!'

#kick back to menu
    installmenu

#----- Install Dependencies for Debian -----#
elif [ $INPUT -eq 2 ]; then
    echo 'Installing dependencies...'
    su -
    apt-get build-dep python-defaults -y -qq
    apt-get update -y -qq
    apt-get install python python-dev python-software-properties -y -qq

# NODE
    apt-get install g++ make nodejs -y -qq
    apt-get update -y -qq
    apt-get install npm -y -qq
    npm install forever -g
    
# Double-check for broken deps before finishing up
    echo 'Checking integrity...'
    apt-get check -y -qq

# Debian users are less nervous than Ubuntu users, but still.
    echo 'Dependencies installed!'

#kick back to menu
    installmenu

#----- Install Ghost -----#
elif [ $INPUT -eq 3]; then
    cd /var/www
    wget -O ghost.zip https://ghost.org/zip/ghost-latest.zip
    unzip -d ghost ghost.zip
    cd ghost
    npm install --production #this installs Ghost

    # Start Ghost
    NODE_ENV=production forever --minUptime=100ms --spinSleepTime=3000ms start index.js -e error.log

#----- Cleanup and Exit -----#
elif [ $INPUT -eq 4 ]; then

clear
echo ''
echo 'Finishing up!'
echo ''

# Check for broken packages
echo 'Checking software integrity'
sudo apt-get -f install -y -qq

# Remove leftover files
echo 'Removing leftover packages...'
sudo apt-get autoremove -y -qq
echo 'Cleaning up temporary cache...'
sudo apt-get clean -y -qq
echo 'Done.'
sleep 5

clear

# echo 'Please restart your session to complete installation.'

# Send back to command prompt
# exit

logout


# Return
# elif [ $INPUT -eq 9 ]; then
#    clear && main

elif [ $INPUT -eq 9 ]; then
    clear && end
fi
}


#----- Logout Dialogue -----#

function logout {
    echo 'Please reboot if possible. Ghost will start automatically.'
    read -p "(O)kay! / (I) can't yet."

if [ '$REPLY' == 'o' ]; then
    sudo shutdown -r +1 "Rebooting!"

elif [ '$REPLY' == 'O' ]; then
    sudo shutdown -r +1 "Rebooting!"
else
    echo 'Please reboot your system when possible. Remember, Ghost will start automatically whenever the system starts.'
    exit
fi
}

# Exit dialogue
function end {
    echo ''
    read -p 'Are you sure you want to quit? (Y)es/(n)o '
    if [ '$REPLY' == 'n' ]; then
        clear && installmenu
    else
        clear && exit
    fi
}

## END OF TRANSMISSION ##
