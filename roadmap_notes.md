![Ignore Me!](http://i.imgur.com/1xV099o.jpg)

Ghost
    init.d script to ensure forever runs on boot
    move wat-dection to domino

Set up tor:
    Create user `tor`
    Assign all tasks to user `tor`
    init.d script to launch HS on boot
    Output relevant details to file in /home/tor
    Backup keys to /home/tor

Backup Ghost sqlite database
    cron monthly to /home/tor/month-year

Create separate script for just installing the Tor Hidden Service (non-ghost)
    (all as above, plus)
    Select directory for hidden service, else /var/www
    Select port (or automatically pick one)
    Existing key? [y/N]
        Key select
    Output 

Unrelated / Semi-related / Maybe related but only if you're me?

At some point, make a BSD vm to get a shallot
Is it possible to save users from themselves?
Detect apache/php, and if so, exit script?
Harden their platform for them?

