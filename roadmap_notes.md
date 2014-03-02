###Ghost
* init.d script to ensure forever runs on boot
* script updating procedures for Ghost? Or is this covered by PPA?
* install theme script?

###Misc/All scripts
* installing unattended-updates for security
* move wat-dection to `domino` function

###Set up tor:
* Create user `tor`
* Assign all tasks to user `tor`
* init.d script to launch HS on boot
* Output relevant details to file in `/home/tor`
* Backup keys to `/home/tor`

###Backup Ghost sqlite database
* cron monthly to `/home/tor/month-year`

###Create separate script for just installing the Tor Hidden Service (non-ghost)
* (all as above, plus)
* Select directory for hidden service, else `/var/www`
* Select port (or automatically pick one)
* Existing key? [y/N]
  * Key select
* Setup all cron tasks

###Jekyll
* Jekyll install + Tor install
* Making a downloadable backup / git repo backup
* Separate rake script `publi.sh` to run after making a blog post with vim
* Restoring a backup from a git repo
* Change theme?

###Unrelated / Semi-related / Maybe related but only if you're me?
* Detect OS and install sudo/su? This would streamline code a bit since I wouldn't need to detect at various intervals, buuut would make it much less portable to BSD and other heretical platforms.
* At some point, make a BSD vm to get a shallot (maybe future feature for BSD?)
* Is it possible to save users from themselves?
* Detect apache/php, and if so, exit script? This would piss a lot of people off, but would reduce the number of (successful) mass attacks against tor hidden services.
* Harden their platform for them?

###Other platforms to consider
* APAF is a thing that exists. #peerpressure
* Bloxsom? (I really hate their design though. This would end with me designing a new theme for the platform =/ )
* Jekyll -- too advanced for most users of this script, but maybe.
  * ACTUALLY. This could work fairly well for some more advanced users. Because I'm scripting up the process, setup is both consistent and auditable.
* moinmoin or other flatfile wiki
* OONI co-installation to run periodic tests and send the data back to me via hidden service? This would be 10x amaze
