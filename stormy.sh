#!/bin/bash

# =========================================================================== #
# Stormy, the easy hidden service creator
# by Griffin Boyce <griffin@torproject.org>, with review from various dags
# 
# https://github.com/glamrock/Stormy
# 
# Usage: 
#   stormy (runs guided wizard)
#   stormy [options] [$nick]
#   stormy --purge [$nick]  (attempts to delete a hidden service and content)
# =========================================================================== #


# CHECK IF ROOT

function root {
    ROOT_UID="0"

    if [ "$UID" -ne "$ROOT_UID" ] ; then
        echo 'Requires administrator privileges. Please run with sudo.'
        exit;
    else
        addsource
    fi
}



version=$(lsb_release -cs)
dist=$(lsb_release -is)


#----- DISABLE POPULARITY -----#

function popcon {

# Long live the king
# Note: in Ubuntu, while it is a dep of ubuntu metapackages, removing both might
# not destroy the system. It is also toggled off by default: PARTICIPATE="no"
# http://ubuntuforums.org/showthread.php?t=1654103 gives me pause.

    if [ $(dpkg-query -l | grep popularity-contest | wc -c) -ne 0 ];
    then     
        if [[ `lsb_release -is` == "Debian" ]]
          apt-get purge popularity-contest
        elif [[ `lsb_release -is` == "Ubuntu" ]] #I need more info here
          sed -i '/PARTICIPATE/c\PARTICIPATE="no"' ./etc/popularity-contest.conf
          chmod -x /etc/cron.daily/popularity-contest
    fi
}



#----- ADD SOFTWARE SOURCES -----#

function addsource {
# Adds sources for various Ghost dependencies

# Detect if Ubuntu
    if [[ `lsb_release -is` == "Ubuntu" ]]
        echo 'Adding software sources'
        cp /etc/apt/sources.list /etc/apt/sources.list.original #backup original sources file
        


        sudo add-apt-repository ppa:chris-lea/node.js -y -qq #nodejs
        sudo apt-get update -y -qq

        

        echo 'Done.'

# Detect if Debian

    elif [[ `lsb_release -is` == "Debian" ]]
        echo 'Adding software sources'
        apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 136221EE520DDFAF0A905689B9316A7BC7917B12
        cp /etc/apt/sources.list /etc/apt/sources.list.original
        echo "deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu lucid main" | tee -a /etc/apt/sources.list
        echo "deb-src http://ppa.launchpad.net/chris-lea/node.js/ubuntu lucid main" | tee -a /etc/apt/sources.list 
        apt-get update -y -qq
        echo 'Done.'

# Detect Wat
    else
        echo 'Sorry, this script is just for Ubuntu or Debian systems!'
        exit
    fi

    wizard #fly off to the wizard function
}



# Halper function

function halp {
	printf "Usage: stormy [-g, --ghost]\n"\
	"       stormy  (without options will run the wizard)\n"\
    "Options:\n"\
    "-g       ghost     Create a Ghost blog installation, or modify an existing one \n"\
    "-w       website   Install a basic webserver and configure Tor\n"\
    "--cloud            Setup Cozy Cloud for you to privately manage your tasks & calendar\n"\
    "-t       tor       Configure Tor hidden service by itself (with no website or content)\n"\
    "--wiki   moinmoin  Create a wiki \n"\
    "--jabber           Create a private Jabber server\n"\
    "-v                 Adjust VirtualHost settings\n"\

    "Advanced Options:\n"\
    ""

	exit;
}








# Exit dialogue
function end {
    echo ''
    read -p 'Are you sure you want to quit? (Y)es/(n)o '
    if [ '$REPLY' == 'n' ]; then
        clear && wizard
    else
        clear && exit
    fi
}

root #start at the beginning

## END OF TRANSMISSION ##

