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
# 

echo "  :::::::::::::::::::  :::::::::"
echo "     :+:   :+:    :+: :+:    :+: "
echo "    +:+   +:+    +:+ +:+    +:+  "
echo "   +#+   +#+    +:+ +#++:++#:    "
echo "  +#+   +#+    +#+ +#+    +#+    "
echo " #+#   #+#    #+# #+#    #+#     "
echo "###    ########  ###    ###      "

#----- FUNCTIONS -----#

#run initial function
domino

# CLEAN ENVIRONMENT FIRST
function domino {
# Empty various cache files
    echo 'Preparing workspace'

# CHECK IF ROOT
    ROOT_UID="0"

    if [ "$UID" -ne "$ROOT_UID" ] ; then
        echo 'Requires administrator privileges:'
    fi

    sudo apt-get autoclean

# Now move to "erpdert" function
erpdert
}

#----- RUN UPDATES -----#

function erpdert {
    sudo apt-get update -y -qq

addsource
}

#----- ADD SOFTWARE SOURCES -----#
function addsource {
# Adds sources for various Ghost dependencies
    echo 'Adding software sources'
    sudo add-apt-repository ppa:chris-lea/node.js -y
    echo 'Done.'
ghostinstall
}

#----- INSTALL SELECTION / MENU -----#
function ghostinstall {
INPUT=0
echo ''
echo 'MAIN MENU'
echo 'What would you like to do? (Enter the number of your choice)'
echo ''
#while [ true ]
#do
echo '1. Install dependencies Ubuntu 12.04 and above'
echo '2. Install dependencies for Debian'
echo '3. Install APAF'
echo '4. Set up Tor'
echo '5. View instructions'
echo '9. Exit without installing anything'
read INPUT

#----- Install dependencies for Ubuntu 12.04, Mint, or Backtrack/Kali-----#
if [ $INPUT -eq 1 ]; then
    echo 'Installing dependencies...'
# PYTHON
    sudo apt-get build-dep python-defaults -y -qq
    sudo apt-get install python python-dev python-software-properties -y -qq
# NODE
    sudo apt-get install g++ make 
    
# Double-check for broken deps before finishing up
    sudo apt-get check -y -qq

    echo 'Installed!'

#kick over to lastclean
    lastclean

#----- Install Dependencies for Debian -----#
elif [ $INPUT -eq 2 ]; then
    echo 'Installing dependencies...'
# PYTHON
    sudo apt-get build-dep python python-dev -y -qq
    sudo apt-get install python python-dev -y -qq
# NODE
    sudo apt-get install gnome gnome-shell-extensions-common pyjavaproperties python-networkmanager -y -qq
    sudo apt-get build-dep olsrd -y -qq
    sudo apt-get install olsrd -y -qq
    sudo apt-get build-dep nm-dispatcher-olsrd -y -qq
    sudo apt-get install nm-dispatcher-olsrd -y -qq
    sudo apt-get build-dep ahcpd -y -qq
    sudo apt-get install ahcpd -y -qq
# Double-check for broken deps before finishing up
    sudo apt-get check -y -qq
    sudo apt-get build-dep commotion-mesh-applet -y -qq
    sudo apt-get install commotion-mesh-applet -y -qq
    echo 'Installed!'

#kick over to lastclean
    lastclean

# Return
# elif [ $INPUT -eq 9 ]; then
#    clear && main

elif [ $INPUT -eq 9 ]; then
    clear && end
fi
}


#----- Install Ghost -----#
elif [ $INPUT -eq 3]; then
    
    wget -O ghost.zip https://ghost.org/zip/ghost-latest.zip
    unzip -d ghost ghost.zip
    cd ghost

}

# CLEANUP SYSTEM
function lastclean {
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
sleep 3

clear

# echo 'Please restart your session to complete installation.'

# Send back to command prompt
# exit

logout
}

#logout dialogue

function logout {
echo ''
read -p "(O)kay! / (N)o, I'll log off later."

if [ '$REPLY' == 'o' ]; then
    sudo gnome-session-save --logout
else
    echo 'Please log out to complete Commotion configuration.'
    exit
fi
}

# Exit dialogue
function end {
echo ''
read -p 'Are you sure you want to quit? (Y)es/(n)o '
if [ '$REPLY' == 'n' ]; then
    clear && appinstall
else
    clear && exit
fi
}

## END OF TRANSMISSION ##
