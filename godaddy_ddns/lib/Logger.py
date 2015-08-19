import logging
import os
import sys

class Logger:
	
	config = {}
	
	def __init__(self, config):
		self.config = config
	
	def run(self):
		# Constrain log file
		self.constrainLogfile()
		
		# Setup log file
		self.setupLogfile()
	
	def setupLogfile(self):
		level = self.getLogLevel()
		if not level:
			print('{0} is not a supported log level. Supported levels are INFO and DEBUG.'.format(self.config['level']))
			sys.exit()
	
		logging.basicConfig(filename = self.config['file'], format = '%(asctime)s %(message)s', level = level)
		return

	def constrainLogfile(self):	
		# Don't allow the log file too large
		if os.path.exists(self.config['file']):
			statinfo = os.stat(self.config['file'])
			if statinfo.st_size >= 10485760:
				print("removing log file")
				os.remove(self.config['file'])
		return
	
	def getLogLevel(self, log_level = False):
		if not log_level:
			log_level = self.config['level']
		
		return {
			'info': logging.INFO,
			'debug': logging.DEBUG,
		}.get(log_level, False)