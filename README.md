# GoDaddy Dynamic DNS

Current version: 0.1.0

###Credits

This script was inspired by http://blogs.umb.edu/michaelbazzinott001/2014/09/14/ddns-with-godaddy/

####Table of Contents

1. [Overview](#overview)
2. [Setup - The basics of setting up godaddy-ddns](#setup)
3. [Usage - Configuration options and additional functionality](#usage)
4. [Limitations - OS compatibility, etc.](#limitations)

##Overview

Python script that performs DDNS checks against GoDaddy's DNS servers

##Setup

Simply just clone the repo, and then copy/move config.example.yaml to config.yaml

This program requires a couple Python modules to get running. The required modules (which can be installed through `pip`) are:
`pyyaml`
`pygodaddy`

##Usage

To run this script, you simply need to do (from the script's directory):

`./DynDNS.py`

##Limitations

This module has been tested on Raspbian Wheezy, and as of now there are no issues to be aware of.

##License

This script/program is licensed under the Apache License 2.0

##Contact

brotherballantine@gmail.com
