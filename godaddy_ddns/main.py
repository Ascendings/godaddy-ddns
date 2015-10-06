#!/usr/bin/env python3

#######################
# Import dependencies #
#######################
from lib import Config
from lib import Logger
from lib import Network
from lib import GoDaddy


###############
# Main method #
###############
def main():
	# Config class
	config = Config.Config('config/config.yaml')
	
	# Logger class
	logger = Logger.Logger(config.get('log'))
	# Start the logger
	logger.run()
	
	# Network class
	network = Network.Network({
		'ip_file': config.get('ip.file')
	}, logger)
	
	# GoDaddy class
	godaddy = GoDaddy.GoDaddy({
		'username': config.get('godaddy.username'),
		'password': config.get('godaddy.password'),
		'hostname': config.get('godaddy.hostname'),
		'type': config.get('godaddy.type'),
	}, logger, network)
	
	# Get the public IP
	ip = network.getPublicIP()
	
	if network.checkIpCache(ip) != 1:
		godaddy.updateDNS(ip)
	else:
		print("Everything is all good, mate")


# Run the program when the script is called
if __name__ == '__main__':
	main()