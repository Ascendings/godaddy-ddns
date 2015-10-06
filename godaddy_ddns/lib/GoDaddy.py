import os
import sys
import pygodaddy

class GoDaddy:

	client = None
	config = None
	logger = None
	network = None

	def __init__(self, config, logger, network):
		self.client = pygodaddy.GoDaddyClient()
		self.config = config
		self.logger = logger
		self.network = network
		
		# Log into GoDaddy
		self.client.login(config['username'], config['password'])
	
	def updateDNS(self, public_ip):
		print("Updating DNS")
	 
		for domain in self.client.find_domains():
			for dns_record in self.client.find_dns_records(domain):
				logger.debug("Domain '{0}' DNS records: {1}".format(domain, self.client.find_dns_records(domain)))
				# only update the bluewolf subdomain
				if dns_record.hostname == self.config['hostname']:
					if public_ip != dns_record.value:
						if self.client.update_dns_record(dns_record.hostname + "." + domain, public_ip):
							logger.info("Host '{0}' public IP set to '{1}'".format(dns_record.hostname, public_ip))
							# update our local copy of IP
							network.writeIpFile(self.config, public_ip)
						else:
							logger.info("Failed to update Host '{0}' IP to '{1}'".format(dns_record.hostname, public_ip))
					else:
						logger.info("Nothing was changed")
						network.writeIpFile(self.config, public_ip)
				else:
					logger.info("Not {0}: '{1}', skipping".format(self.config['hostname'], dns_record.hostname))
		return