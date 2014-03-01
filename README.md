Stormy
=========

*Stormy* is a wizard to help people create Tor Hidden Services with just a couple of clicks. Currently, it's setup to install Ghost (a swanky nodejs-based blog platform). Another great option is to create an application using [APAF](https://apaf.readthedocs.org/en/latest/), but if you know how to code twisted-based applications in freaking python, then you're probably not even reading this :P

**To test:**
* ssh into your server
* Enter this command: `git clone https://github.com/glamrock/Stormy.git && cd Stormy && ./ghost-install.sh`
* Follow the instructions to either install or exit the script.
* Your instance will reboot automatically after install.

Once your hidden service is set up, go to your onion address. `xxxx.onion/ghost/` should ask you to set up a name and password for your blog. Do so now. Periodic backups of the sqlite backups will get sent to `/home/tor`.

**Reminder:** Always create hidden services on *their own machine*. ***Always***.

This is a work in progress, having begun at Tor's Winter Dev Meeting 2014. Treat all code as if I'm insane.

All code is licensed under MIT, a supervillain-friendly license. I'm still working on the [evil laugh](http://www.youtube.com/watch?v=IGqwqxRF598).

![Ignore Me!](http://i.imgur.com/1xV099o.jpg)
