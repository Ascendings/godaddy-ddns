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
			print('{0} is not a supported log level. You can view https://docs.python.org/3/library/logging.html#logging-levels for supported logging levels.'.format(self.config['level']))
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
			'critical': logging.CRITICAL,
			'error': logging.ERROR,
			'warning': logging.WARNING,
			'notset': logging.NOTSET,
		}.get(log_level.lower(), False)
		
	def debug(self, msg, *args, **kwargs):
		logging.debug(msg, *args, **kwargs)
	
	def info(self, msg, *args, **kwargs):
		logging.info(msg, *args, **kwargs)
	
	def warning(self, msg, *args, **kwargs):
		logging.warning(msg, *args, **kwargs)
	
	def critical(self, msg, *args, **kwargs):
		logging.critical(msg, *args, **kwargs)
		
	def error(self, msg, *args, **kwargs):
		logging.error(msg, *args, **kwargs)
	
	def log(self, lvl, msg, *args, **kwargs):
		logging.log(lvl, msg, *args, **kwargs)
	
	def exception(self, msg, *args, **kwargs):
		logging.exception(msg, *args, **kwargs)