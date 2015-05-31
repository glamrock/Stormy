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
#   run script as root to install a jabber server
# =========================================================================== #

# CHECK IF ROOT

function root {
    if [[ `whoami` != root ]]; then
        echo "This install script should be run as root. (aka administrator)"
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

#NodeJS
    gpg --keyserver keys.mayfirst.org --recv-keys 136221EE520DDFAF0A905689B9316A7BC7917B12

# Tor build keys
    gpg --keyserver keys.mayfirst.org --recv-keys 74A941BA219EC810 A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89

# Other Tor development keys
    gpg --keyserver keys.mayfirst.org --recv-keys \
	  4A90646C0BAED9D456AB3111E5B81856D0220E4B \
	  35CD74C24A9B15A19E1A81A194373AA94B7C3223 \
	  8C4CD511095E982EB0EFBFA21E8BF34923291265 \
	  AD1AB35C674DF572FBCE8B0A6BC758CBC11F6276 \
	  0D24B36AA9A2A651787876451202821CBE2CD9C1 \
	  25FC1614B8F87B52FF2F99B962AF4031C82E0039 \
	  261C5FBE77285F88FB0C343266C8C2D7C5AA446D \
	  C963C21D63564E2B10BB335B29846B3C683686CC \
	  68278CC5DD2D1E85C4E45AD90445B7AB9ABBEEC6 \
	  0291ECCBE42B22068E685545627DEE286B4D6475 \
	  02959AA7190AB9E9027E07363B9D093F31B0974B \
	  C2E34CFC13C62BD92C7579B56B8AAEB1F1F5C9B5 \
	  8738A680B84B3031A630F2DB416F061063FEE659 \
	  B35BF85BF19489D04E28C33C21194EBB165733EA \
	  F65CE37F04BA5B360AE6EE17C218525819F78451 \
	  B1172656DFF983C3042BC699EB5A896A28988BF5 \
	  879BDA5BF6B27B6127450A2503CF4A0AB3C79A63

# Update
    apt-get update -y -qq

addsource 
}


#----- ADD SOFTWARE SOURCES -----#

function addsource {
# Adds sources for various dependencies
    echo 'Adding software sources'
	local sources_list_d='/etc/apt/sources.list.d'
	local sources_list_file='single.list'

# Detect if Ubuntu or Debian
    if [[ $dist == "Ubuntu" ]]||[[ $dist == "Debian" ]]; then
	  [ -d $sources_list_d ] || mkdir -p $sources_list_d
	  echo "deb  http://deb.torproject.org/torproject.org $version main"| tee -a $sources_list_d/$sources_list_file
# Detect Wat
    else
        echo 'Sorry, this script is just for Ubuntu or Debian systems!'
        echo 'Using another OS? Send a request to griffin@torproject.org'
        echo 'https://github.com/glamrock/stormy'
        exit
    fi

# Update after the new sources
        apt-get update -y -qq
        apt-get install deb.torproject.org-keyring -y -qq #better safe than sorry
        echo 'Done.'

    torque #head to jabber install function
}


#----- Tor Dependencies and creation -----#

#----- Because the jabber installation process requires the onionsite hostname, tor must be configured first

function torque { 

    echo 'Configuring your Tor Hidden Service'

# overwrite the existing torrc, but check if it contains an existing hs first

if ! grep -qw "#HiddenServiceDir /var/lib/tor/hidden_service" /etc/tor/torrc; then
    echo "You are about to replace an existing tor configuration file."
    echo 'Continue? (Y)es  /  (N)o' 
    read -p '' REPLY

  if [ "$REPLY" == "y" ]||[ "$REPLY" == "Y" ]; then
    cp /etc/tor/torrc /etc/tor/torrc.original
    >| /etc/tor/torrc #truncate the torrc

  cat << EOF > /etc/tor/torrc

#Log notice file /var/log/tor/notices.log
RunAsDaemon 1 # Will run tor in the background

HiddenServiceDir /var/lib/tor/jabber/
# HiddenServicePort 80 127.0.0.1:80 # uncomment if creating a clearnet website.
HiddenServicePort 2368 127.0.0.1:2368 #default ghost port

EOF


  else #no - cancels hs setup
      echo "Stormy will now cancel onion service setup."
            echo 'Continue? (Y)es  /  (N)o' 
            read -p '' SEANCE
          if [ "$SEANCE" == "y" ]||[ "$SEANCE" == "Y" ]; then
            apt-get purge ejabberd -y -qq
            apt-get autoclean -y -qq
            apt-get autoremove -y -qq
            apt-get update -y -qq
            apt-get -f install -y -qq
            clear && echo "Goodbye."
            exit
          else
            clear && echo "Goodbye."
            exit
        fi
  fi
else 
    >| /etc/tor/torrc #empty the current torrc

  cat << EOF > /etc/tor/torrc

#Log notice file /var/log/tor/notices.log
RunAsDaemon 1 # Will run tor in the background

HiddenServiceDir /var/lib/tor/jabber/
# HiddenServicePort 80 127.0.0.1:80 # uncomment if creating a clearnet website.
HiddenServicePort 2368 127.0.0.1:2368 #default ghost port

EOF

fi

    chown -hR debian-tor /var/lib/tor #set ownership for this folder and all subfolders to user debian-tor
    mkdir -p /var/lib/tor/jabber
    chmod 0700 /var/lib/tor/jabber 

    sed -i '/RUN_DAEMON=.*/c\RUN_DAEMON="yes"' /etc/default/tor #allow to start on boot, even if it was previously set to no
    update-rc.d tor defaults
    echo 'Your hidden service will start on boot.'

spooky #let's bring it all together now
}

function spooky { 

    echo 'Generating .onion address'
    sudo -u debian-tor tor --runasdaemon 1 #run tor to generate a hostname

    hostname=$(cat /var/lib/tor/jabber/hostname)
    echo "Your onion address is":  "$hostname"

popcon #disable popularity contest
}


#----- DISABLE POPULARITY -----#

function popcon {

# Long live the king
# Note: in Ubuntu, while it is a dep of ubuntu metapackages, removing both might
# not destroy the system. It is also toggled off by default: PARTICIPATE="no"
# http://ubuntuforums.org/showthread.php?t=1654103 gives me pause.

    if [ $(dpkg-query -l | grep -c popularity-contest) -ne 0 ];
    then
        if [[ $dist == "Debian" ]]; then
          apt-get purge popularity-contest #not a dependency for Debian
        elif [[ $dist == "Ubuntu" ]]; then
            # delete the entire config string, then replace with a "no"
          sed -i '/PARTICIPATE/c\PARTICIPATE="no"' /etc/popularity-contest.conf
          chmod -x /etc/cron.daily/popularity-contest # Ensure popularity-contest cronjob does not run daily
    fi
   fi

jabber 
}


#----- Install Jabber and related XMPP dependencies -----#

function jabber {
    echo 'Installing dependencies...'

# Open to ideas on replacing OpenSSL
    apt-get install openssl -y -qq
    apt-get install ejabberd -y -qq

# Double-check for broken deps before finishing up
    echo 'Checking integrity...'
    apt-get check -y -qq

# Debian users are less nervous than Ubuntu users, but still.
    echo 'Dependencies installed!'

cert 
}

function cert {  # now it's time to generate a real certificate to use with jabber
    cd /etc/ejabberd/
    openssl req -nodes -newkey rsa:4096 -keyout private.key -out CSR.csr -subj "/C=NL/ST=State/L=City/O=Company Name/OU=Department/CN=$hostname"
    >| ejabberd.pem # empty the original snakeoil keyfile
    cat private.key >> ejabberd.pem
    cat certificate.pem >> ejabberd.pem

config
}


function config {


ADMIN_NAME=admin
SRV_NAME=$(cat /var/lib/tor/jabber/hostname)
PASS_LEN=10 # Length of the generated admin password
# '!"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'\'
PASS_CHARS=0123456789!#$%&*+/0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz

# make_pass len allowed_chars
make_pass()
{
  local i
  for i in `seq $1`; do printf "%s" "${2:$(($RANDOM%${#2})):1}"; done
}

# Find ed editor
which ed 2>&- >/dev/null && ED=ed
#which ex 2>&- >/dev/null && ED=ex

sudo apt-get -y install ejabberd

cat > /etc/ejabberd/ejabberd.cfg <<EOF
%% Admin user
{acl, admin, {user, "$ADMIN_NAME", "$SRV_NAME"}}.

%% Hostname
{hosts, ["$SRV_NAME"]}.

%% Logging
{loglevel, 0}.

%%% ===============
%%% LISTENING PORTS

{listen, [
    {5222, ejabberd_c2s, [
        {access, c2s},
        {shaper, c2s_shaper},
        {max_stanza_size, infinite},
        starttls_required,
        {certfile, "/etc/ejabberd/ejabberd.pem"},
        {ciphers, "HIGH:!SSLv2:!SSLv3:!TLSv1:!TLSv1.1:!aNULL"}
    ]},
    {5280, ejabberd_http, [
        http_bind, http_poll
    ]}
 ]}.

%%
%% s2s_certfile: Specify a certificate file.
%%
{s2s_certfile, "/etc/ejabberd/ejabberd.pem"}.

%%% ==============
%%% AUTHENTICATION

{auth_method, [internal, anonymous]}.
{auth_password_format, scram}.

%%% ===============
%%% TRAFFIC SHAPERS

{shaper, normal, {maxrate, 500000000}}.
{shaper, fast, {maxrate, 500000000}}.

%%% ====================
%%% ACCESS CONTROL LISTS

{acl, local, {user_regexp, ""}}.

%%% ============
%%% ACCESS RULES

{access, max_user_sessions, [{10, all}]}.
{access, max_user_offline_messages, [{5000, admin}, {100, all}]}.
{access, c2s, [{deny, blocked}, {allow, all}]}.
{access, c2s_shaper, [{none, admin}, {normal, all}]}.
{access, s2s_shaper, [{fast, all}]}.
{access, announce, [{allow, admin}]}.
{access, configure, [{allow, admin}]}.
{access, muc_admin, [{allow, admin}]}.
{access, muc, [{allow, all}]}.
{access, register, [{allow, all}]}.
{registration_timeout, infinity}.

{language, "en"}.

%%% =======
%%% MODULES

{modules, [
    {mod_ping, []},
    {mod_http_bind, []},
    {mod_muc, [
        {host, "conference.@HOST@"},
        {access, muc},
        {history_size, 0},
        {access_create, muc},
        {access_persistent, muc_admin},
        {access_admin, muc_admin},
        {max_users, 9999},
        {default_room_options, [
            {allow_change_subj, false},
            {allow_private_messages, true},
            {allow_query_users, true},
            {allow_user_invites, false},
            {anonymous, true},
            {logging, false},
            {members_by_default, false},
            {members_only, false},
            {moderated, false},
            {password_protected, false},
            {persistent, false},
            {public, false},
            {public_list, false}
        ]}
    ]},
    {mod_register, [
        {welcome_message, {"Welcome!"}},
        {access, register}
    ]}
 ]}.
EOF

if false; then
$ED -s ejabberd.cfg <<EOF
/^{acl, admin, {user/d
i
{acl, admin, {user, "$ADMIN_NAME", "$SRV_NAME"}}.
.
/^{hosts, \["/d
i
{hosts, ["$SRV_NAME"]}.
.
w
q
EOF
cp ejabberd.cfg /etc/ejabberd
fi

sudo /etc/init.d/ejabberd restart
sleep 1 # Give it time to start

pass=$(make_pass $PASS_LEN "$PASS_CHARS")

#sudo ejabberdctl unregister $ADMIN_NAME $SRV_NAME
sudo ejabberdctl register $ADMIN_NAME $SRV_NAME "$pass" || { echo "Failed to register admin" >&2; exit 1; }

sudo apt-get install unattended-upgrades
cat > /etc/apt/apt.conf.d/20auto-upgrades <<EOF
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
EOF

cat > /etc/apt/apt.conf.d/50unattended-upgrades <<EOF
Unattended-Upgrade::Allowed-Origins {
        "\${distro_id}:\${distro_codename}-security";
};
EOF


backup 
}


function backup {

  mkdir /var/lib/tor/backups

  cat <<EOF > /etc/cron.monthly/ejabberd
#!/bin/sh

sudo -u ejabberd ejabberdctl --node ejabberd backup /var/lib/tor/backups/"\${file}-jabber-\`date +%Y-%m\`.dmp"
done

EOF

#check for updates, and if they exist, execute them

cat <<EOF > /etc/cron.daily/ejabberd
#!bin/sh
done

EOF

# ensure cron scripts have execution permissions
chmod 0755 /etc/cron.monthly/ejabberd /etc/cron.daily/ejabberd

# time to finish up
    cleanup
}


#----- Cleanup -----#

function cleanup {
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
    echo 'Done!'
    sleep 5
    clear

    echo "Please take a moment to write down your hidden service address and passwords."
    echo ""
    echo "Your onion address is":  "$hostname"
    echo ""
    echo "Your hidden service's private key is located in /var/lib/tor/jabber"
    echo "Admin user "$ADMIN_NAME" on server $SRV_NAME has been created with "$pass" for a password."


    sleep 10


log #kick to start services function
}

#----- Start services -----#

function log {
  echo '>>> Starting Tor service'
  invoke-rc.d tor stop &>/dev/null
  invoke-rc.d tor start

  echo '>>> Starting Forever service'
  invoke-rc.d ejabberd stop &>/dev/null
  invoke-rc.d ejabberd start
}

root #start at the beginning

## END OF TRANSMISSION ##

