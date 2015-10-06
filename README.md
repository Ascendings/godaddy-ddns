# GoDaddy Dynamic DNS

Current version: 0.5.0

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

Simply just clone the repo, and then copy/move config.example.yaml to config.yaml

This program requires a couple Python modules to get running. The required modules (which can be installed through `pip install _____`) are:
`pyyaml`
`pygodaddy`

##Usage

To run this script, you simply need to do (from the script's directory):

`./DynDNS.py`

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

##Limitations

This program has been tested on Debian/Raspbian Wheezy and Jessie and on Ubuntu 15.04, and as of now there are no issues to be aware of.

As stated above, the script is not fully functional yet.

##License

This script/program is licensed under the Apache License 2.0

##Contact

brotherballantine@gmail.com
