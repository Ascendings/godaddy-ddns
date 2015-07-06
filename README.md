# GoDaddy Dynamic DNS

Current version: 0.1.0

###Credits

This script was inspired by http://blogs.umb.edu/michaelbazzinott001/2014/09/14/ddns-with-godaddy/

####Table of Contents

1. [Overview](#overview)
2. [Setup - The basics of setting up godaddy-ddns](#setup)
3. [Usage - Configuration options and additional functionality](#usage)
4. [Limitations - OS compatibility, etc.](#limitations)
5. [License - Licensing information](#license)
6. [Contact - How to contact me](#contact)

##Overview

Python script that performs DDNS checks against GoDaddy's DNS servers

##Setup

Simply just clone the repo, and then copy/move config.example.yaml to config.yaml

This program requires a couple Python modules to get running. The required modules (which can be installed through `pip install _____`) are:
`pyyaml`
`pygodaddy`

##Usage

To run this script, you simply need to do (from the script's directory):

`./DynDNS.py`

###Configuration

All of the configuration for this program is handled through the `config.yaml` file

####`godaddy_username`

Your GoDaddy account's username

####`godaddy_password`

Your GoDaddy account's password

####`log_file`

The location you would like for the script's log file

####`log_level`

The log level you would like. Currently supported levels are `INFO` and `DEBUG`

####`log_max_size`

The max size (in megabytes) you would like the log file to be

NOTE: this option does not currently work

####`ip_file`

Location where to store the public IP - this helps to avoid unnecessarily querying GoDaddy if nothing has changed

NOTE: this file does not need to exist before running; it will be created as necessary

####`record_hostname`

The hostname of the A record to check against

NOTE: This is the hostname you want to check against, NOT the fully-qualified domain name.

##Limitations

This module has been tested on Raspbian Wheezy, and as of now there are no issues to be aware of.

##License

This script/program is licensed under the Apache License 2.0

##Contact

brotherballantine@gmail.com
