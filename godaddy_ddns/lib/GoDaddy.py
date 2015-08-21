import os
import sys
import pygodaddy

class GoDaddy:

	client = None
	logger = None

	def __init__(self, config, logger):
		self.client = pygodaddy.GoDaddyClient()
		self.config = config
		self.logger = logger
		
		# Log into GoDaddy
		self.client.login(config['godaddy_username'], config['godaddy_password'])
	
	def updateDNS(self, public_ip):
		print("Updating DNS")