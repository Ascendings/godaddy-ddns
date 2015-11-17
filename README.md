# GoDaddy Dynamic DNS

Current version: 0.7.0

##Note

The current version does not fully work! Please take note of this.

I started to build this program over the summer, and then I got hit with a few projects that took priority, and then school started to take over as well. This will be completed ASAP, I promise that. A full version will come along with an updated README and everything, just be patient.

As of version 0.5.0 - from what I can test it works, however, it appears the pygodaddy library is broken (right now it's 10/6/2015 and I may be just doing something wrong) and I am unable to test past authenticating with GoDaddy.

###Credits

This script was inspired by http://blogs.umb.edu/michaelbazzinott001/2014/09/14/ddns-with-godaddy/

####Table of Contents

1. [Overview](#overview)
2. [Setup - The basics of setting up godaddy-ddns](#setup)
3. [Usage - How to use this thing](#usage)
4. [Configuration - Configuration options and additional functionality](#configuration)
5. [Limitations - OS compatibility, etc.](#limitations)
6. [License - Licensing information](#license)
7. [Contact - How to contact me](#contact)

##Overview

Python application that performs DDNS checks against GoDaddy's DNS servers.

This script checks the local device's public IP address using DNS (or a cached version of the address if DNS is unavailable), and
then checks to make sure GoDaddy's record is up-to-date with the device's current IP address.

I designed this program to be flexible, and rock-solid enough to perform Dynamic DNS with GoDaddy's DNS service.

##Setup

Do note that this program requires Python 3 (was tested with Python3.4). I'm sure it's possible to make this script run under Python 2, but I won't be doing that :). That means you will need to use the appropriate python and pip commands (or install the proper packges) that will go along with Python 3.x.

So to get started, simply just clone the repo, and then rename config.example.yaml to config.yaml - you may want to make a copy of this file first for a reference.

This program requires a couple Python modules to get running. The required modules (which can be installed through `pip3 install _____`) are:
`pyyaml`
`pygodaddy`


##Usage

To run this script, you simply need to do (from the script's directory):

`python3 godaddy-ddns/main.py`

Or you just run it from wherever you want:

`python3 path/to/godaddy-ddns/main.py`

###Repition for DynDNS effect

To truly have DynDNS, you will need to make a cron job (or something similar) that will run this script however often you please. I could make this program daemon and have it be a standalone program if people demand it.


##Configuration

All of the configuration for this program is handled through the `config.yaml` file (in the godaddy_ddns/config directory). The configuration is broken
up into related segments for easy readability

###godaddy:

####`username`

Your GoDaddy account's username

####`password`

Your GoDaddy account's password

####`hostname`

The hostname/record to check/change the IP

###log:

####`file`

The location you would like for the script's log file

####`level`

The log level you would like. Currently supported levels are `INFO` and `DEBUG`

####`max_size`

The max size (in megabytes) you would like the log file to be

NOTE: this option does not currently work

###ip:

####`file`

Location where to store the public IP - this helps to avoid unnecessarily querying GoDaddy if nothing has changed

NOTE: this file does not need to exist before running; it will be created as necessary


##Limitations/Issues

This program has been tested on Debian/Raspbian Wheezy and Jessie and on Ubuntu 15.04, and as of now there is only one small issue to be aware of.

After you run the script, be sure to check the log (by default this is in /var/log/godaddy-ddns.log) for any errors, as the script (as of now) does not report an error because of the new website. It looks like the pip package version of pygodaddy is not yet functional with the new GoDaddy website. To fix this, you will need to apply this fix, courtesy of claneys on GitHub.com, to your pygodaddy installation: https://github.com/claneys/pygodaddy/commit/9bfd1ffc082872947442c97471934f90053bb123

As stated above, the script is not guaranteed to be fully functional yet, although I have been making some serious progress with this project.


##License

This script/program is licensed under the Apache License 2.0


##Contact

Email me at: brotherballantine@gmail.com

Or hit me up on Google+ (https://plus.google.com/+GregoryBallantine1) or something
