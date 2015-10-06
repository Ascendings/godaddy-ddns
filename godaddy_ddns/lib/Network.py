# Dependencies
import os
import sys

from urllib.request import urlopen

class Network:

	config = {}
	logger = None

	def __init__(self, config, logger):
		self.config = config
		self.logger = logger

	def getPublicIP(self):
		ip = urlopen('http://ip.42.pl/raw').read()
		ip = ip.decode() # Decode to utf-8 string
		
		return ip
	
	def checkIpCache(self, public_ip):
		filename = os.path.realpath(self.config['ip_file'])
		filepath = os.path.dirname(filename)
		
		if not os.path.exists(filepath):
			self.logger.info('Creating {0} directory for ip file.'.format(filepath))
			try:
				os.mkdir(filepath)
			except IOError as e:
				self.logger.error('Failed to create {0}'.format(filepath))
				self.logger.error('Terminating')
				print(e)
				sys.exit()
			else:
				self.logger.info('{0} was successfully created'.format(filepath))
				print('Successfully created directory')
		else:
			self.logger.debug('{0} already exists, not creating'.format(filepath))
			print('{0} already exists'.format(filepath))
	
		if os.path.exists(filename):
			with open(filename, 'r') as fo:
				old_ip = fo.read(50)
	
			if old_ip == public_ip:
				print('ip is the same.. not doing anything')
				self.logger.info('IP has not changed, I am not doing anything now.')
				return 1
			else:
				print('IP has changed, going to try to update GoDaddy.')
				self.logger.info('IP has changed, I am going to attempt an update at GoDaddy.')
		
		# return if no file exists, or the IP is new
		return

	def writeIpFile(self, ip):
		if not os.path.exists(self.config['file']):
			with open(self.config['file'], 'w') as fo:
				fo.write(ip)
		else:
			with open(self.config['file'], 'r+') as fo:
				fo.seek(0)
				fo.write(ip)
				fo.truncate()
		return