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
    fi
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






function popcon {

# Long live the king
# Note: in Ubuntu, while it is a dep of ubuntu-standard, removing both won't
# destroy the system. It is also toggled off by default: PARTICIPATE="no"

    if [ $(sudo dpkg-query -l | grep gedit | wc -c) -ne 0 ];
    then 
      apt-get purge popularity-contest
    fi
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

## END OF TRANSMISSION ##

