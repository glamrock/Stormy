#!/bin/bash
# -*- Mode: sh; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
# 
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
        echo "This install script should be run as root. (aka administrator)"
#       echo "Please try again using the sudo command."
        exit;
    else
        keyfob
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
          apt-get purge popularity-contest #not a dependency for Debian
        elif [[ `lsb_release -is` == "Ubuntu" ]]
          sed -i '/PARTICIPATE/c\PARTICIPATE="no"' ./etc/popularity-contest.conf
          chmod -x /etc/cron.daily/popularity-contest #I need more info here
    fi
}


#----- ADD DEVELOPER KEYS -----#

function keyfob {
    apt-key adv --keyserver keys.mayfirst.org --recv-keys 136221EE520DDFAF0A905689B9316A7BC7917B12 #node
    
    apt-key adv --keyserver keys.mayfirst.org --recv-keys 4A90646C0BAED9D456AB3111E5B81856D0220E4B 35CD74C24A9B15A19E1A81A194373AA94B7C3223 8C4CD511095E982EB0EFBFA21E8BF34923291265 AD1AB35C674DF572FBCE8B0A6BC758CBC11F6276 0D24B36AA9A2A651787876451202821CBE2CD9C1 25FC1614B8F87B52FF2F99B962AF4031C82E0039 261C5FBE77285F88FB0C343266C8C2D7C5AA446D C963C21D63564E2B10BB335B29846B3C683686CC 68278CC5DD2D1E85C4E45AD90445B7AB9ABBEEC6 A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 0291ECCBE42B22068E685545627DEE286B4D6475 02959AA7190AB9E9027E07363B9D093F31B0974B C2E34CFC13C62BD92C7579B56B8AAEB1F1F5C9B5 8738A680B84B3031A630F2DB416F061063FEE659 B35BF85BF19489D04E28C33C21194EBB165733EA F65CE37F04BA5B360AE6EE17C218525819F78451 B1172656DFF983C3042BC699EB5A896A28988BF5 879BDA5BF6B27B6127450A2503CF4A0AB3C79A63 #tor build keys

    apt-key adv --keyserver keys.mayfirst.org --recv-keys 

addsource

}


#----- ADD SOFTWARE SOURCES -----#

function addsource {
# Adds sources for various dependencies
    echo 'Adding software sources'
    cp /etc/apt/sources.list /etc/apt/sources.list.original #backup original sources file


# Detect if Ubuntu
    if [[ `lsb_release -is` == "Ubuntu" ]]

# Detect if Debian

    elif [[ `lsb_release -is` == "Debian" ]]





# Detect Wat
    else
        echo 'Sorry, this script is just for Ubuntu or Debian systems!'
        echo 'Using another OS? Send a request to griffin@torproject.org'
        echo 'https://github.com/glamrock/stormy'
        exit
    fi

# Update after the new sources
        apt-get update -y -qq
        echo 'Done.'

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





#----- Logout Dialogue -----#

function logout {
    echo 'Please reboot if possible. Your hidden service will start automatically.'
    read -p "(O)kay! / (I) can't yet."

if [ '$REPLY' == 'o' ]; then
    sudo shutdown -r +1 "Rebooting!"

elif [ '$REPLY' == 'O' ]; then
    sudo shutdown -r +1 "Rebooting!"
else
    echo 'Please reboot your system when possible. Remember, your hidden services will start automatically whenever the system starts.'
    exit
fi
}


#----- Exit Dialogue -----#

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

