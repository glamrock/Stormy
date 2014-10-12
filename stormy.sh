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
    if [[ `whoami` != root ]]; then
        echo "This install script should be run as root. (aka administrator)"
#       echo "Please try again using the sudo command."
        exit;
    else
        keyfob
    fi
}


#----- VARIOUS ITEMS -----#
version=$(lsb_release -cs)
dist=$(lsb_release -is)


#----- ADD DEVELOPER KEYS -----#

function keyfob {
    gpg --keyserver keys.mayfirst.org --recv-keys 136221EE520DDFAF0A905689B9316A7BC7917B12 #node

# Tor build keys
    gpg --keyserver keys.mayfirst.org --recv-keys 4A90646C0BAED9D456AB3111E5B81856D0220E4B 35CD74C24A9B15A19E1A81A194373AA94B7C3223 8C4CD511095E982EB0EFBFA21E8BF34923291265 AD1AB35C674DF572FBCE8B0A6BC758CBC11F6276 0D24B36AA9A2A651787876451202821CBE2CD9C1 25FC1614B8F87B52FF2F99B962AF4031C82E0039 261C5FBE77285F88FB0C343266C8C2D7C5AA446D C963C21D63564E2B10BB335B29846B3C683686CC 68278CC5DD2D1E85C4E45AD90445B7AB9ABBEEC6 A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 0291ECCBE42B22068E685545627DEE286B4D6475 02959AA7190AB9E9027E07363B9D093F31B0974B C2E34CFC13C62BD92C7579B56B8AAEB1F1F5C9B5 8738A680B84B3031A630F2DB416F061063FEE659 B35BF85BF19489D04E28C33C21194EBB165733EA F65CE37F04BA5B360AE6EE17C218525819F78451 B1172656DFF983C3042BC699EB5A896A28988BF5 879BDA5BF6B27B6127450A2503CF4A0AB3C79A63

addsource
}


#----- ADD SOFTWARE SOURCES -----#

function addsource {
# Adds sources for various dependencies
    echo 'Adding software sources'
    cp /etc/apt/sources.list /etc/apt/sources.list.original #backup original sources file


# Detect if Ubuntu
    if [[ `lsb_release -is` == "Ubuntu" ]]

    echo "deb  http://deb.torproject.org/torproject.org $version main"| tee -a /etc/apt/sources.list

# Detect if Debian

    elif [[ `lsb_release -is` == "Debian" ]]

    echo "deb  http://deb.torproject.org/torproject.org $version main"| tee -a /etc/apt/sources.list
# Detect Wat
    else
        echo 'Sorry, this script is just for Ubuntu or Debian systems!'
        echo 'Using another OS? Send a request to griffin@torproject.org'
        echo 'https://github.com/glamrock/stormy'
        exit
    fi

# Update after the new sources
        apt-get update -y -qq
        apt-get install deb.torproject.org-keyring #better safe than sorry
        echo 'Done.'

    wizard #fly off to the wizard function
}

#----- Install Ghost and related dependencies -----#
elif [ "$INPUT" -eq 2 ]; then
    ghost

ghost() {
    echo 'Installing dependencies...'
    apt-get build-dep python-defaults -y -qq
    apt-get update -y -qq
    apt-get install iptables python python-dev python-software-properties -y -qq
    apt-get install tor

# NODE
    apt-get install g++ make nodejs -y -qq
    apt-get update -y -qq
    apt-get install npm -y -qq
    npm install forever -g
    npm install ghost -g

# Double-check for broken deps before finishing up
    echo 'Checking integrity...'
    apt-get check -y -qq

# Debian users are less nervous than Ubuntu users, but still.
    echo 'Dependencies installed!'

# Get and install Ghost

    cd /var/www
    wget -O ghost.zip https://ghost.org/zip/ghost-latest.zip
    unzip -d ghost ghost.zip
    rm ghost.zip
    cd ghost
    npm install --production #this installs Ghost

# Meddling with uncaught nodejs exceptions

# Do I want to tack this on to index.js?  In the cause of uncaught exceptions,
# it would force-crash Ghost and forever would bring it back up within 3 seconds

# process.on('uncaughtException', function (err) {
#  console.error((new Date).toUTCString() + ' uncaughtException:', err.message)
#  console.error(err.stack)
#  process.exit(1)
#})


# Start Ghost and set Forever
    cd /var/www/ghost
    NODE_ENV=production forever --minUptime=100ms --spinSleepTime=3000ms start index.js -e error.log

 if [[ `lsb_release -is` == "Ubuntu" ]]
    touch /etc/init/ghost.conf
    bash -c 'cat << EOF > /etc/init/ghost.conf
start on startup
stop on shutdown

exec forever start /var/www/ghost/ghost.js
    EOF'

 else #For Debian and non-Debian derivatives, manual labor is required

# Init.d file to auto-start forever+ghost
  bash -c 'cat << EOF > /etc/init.d/forever
    #!/bin/sh

    export PATH=$PATH:/usr/local/bin
    export NODE_PATH=$NODE_PATH:/usr/local/lib/node_modules
    export SERVER_PORT=80
    export SERVER_IFACE=127.0.0.1

    case "$1" in
      start)
      exec forever --sourceDir=/var/www/ghost -p ~/.forever --minUptime=100ms --spinSleepTime=3000ms start index.js -e error.log
      ;;

      stop)
      exec forever stop --sourceDir=/var/www/ghost index.js
      ;;
    esac

    exit 0
EOF'

    chmod +x /etc/init.d/forever
    ln -s /etc/init.d/forever /etc/rc.d/
    update-rc.d forever defaults #forever+ghost will now rise on boot

# kick over to popcon
    popcon
}



#----- Tor Dependencies and creation -----#

torque() { # should this be initiated before the wizard?



}



#----- RSS Reader -----#

rss() {

}


#----- XMPP Server -----#

jabber() {


    echo "Use the default Jabber configuration file? [Y/n]"
    
}


#----- IRC chat -----#

irc() {

    echo "Would you like to install a web-based chat client for your IRC service?"

}

#----- Mopidy Radio Streaming  -----#
#   Mopidy is undergoing heavy development
#   So it would need to be built from github source
#   
#radio() {
#}



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

cleanup
}


#----- Cleanup -----#
# elif [ "$INPUT" -eq 4 ]; then

    clear
    echo ''
    echo 'Finishing up!'
    echo ''

    # Check for broken packages
    echo 'Checking software integrity'
    apt-get -f install -y -qq

    # Remove leftover files
    echo 'Removing leftover packages...'
    apt-get autoremove -y -qq
    echo 'Cleaning up temporary cache...'
    apt-get clean -y -qq
    echo 'Done.'
    sleep 5

    clear

log #go to the logout function, just make sure it appears above this entry


#----- Logout Dialogue -----#

function log {
    echo 'Please reboot if possible. Your hidden service will start automatically.'
    read -p "(O)kay! / (I) can't yet.    " REPLY 

if [ "$REPLY" == "o" ]||[ "$REPLY" == "O" ]; then
    shutdown -r +1 "Rebooting!"

else
    echo 'Please reboot your system when possible.'
    echo 'Remember, your hidden services will start automatically whenever the system starts.'
    exit
fi
}

#----- Man Page -----#

elif [ "$INPUT" -eq 8 ]; then
    echo 'You have exited the wizard.'
    man stormy

#----- Exit Dialogue -----#

function end {
    echo ''
    read -p "Are you sure you want to quit? (Y)es/(n)o     " REPLY
    if [ "$REPLY" = "n" ]; then
        clear && wizard
    else
        clear && exit
    fi

}

# Return
# elif [ $INPUT -eq 9 ]; then
#    clear && wizard

elif [ "$INPUT" -eq 9 ]; then
    clear && end
fi
}

root #start at the beginning

## END OF TRANSMISSION ##

