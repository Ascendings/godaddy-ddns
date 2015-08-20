#!/usr/bin/env python3

# Import dependencies
from lib import Config
from lib import Logger
from lib import Network

# Setup our stuff
config = Config.Config('config/config.yaml')
logger = Logger.Logger(config.get('log'))
network = Network.Network

# Start the logger
logger.run()

# Get the public IP
ip = network.getPublicIP()



#
# Main method
#
#def main():
#	# Load the configuration
#	config = read_config_file()
#
#	# Make sure the log file is all good
#	setup_logfile(config)
#
#	# Retrieve our public IP address
#	public_ip = get_public_ip()
#
#	if check_ip_file(config, public_ip) != 1:
#		update_dns(config, public_ip)
#
#
# Run the script
#
#main()