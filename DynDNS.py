#!/usr/bin/env python
import sys
import os
import logging
import yaml
import pygodaddy
from urllib.request import urlopen
 
# GLOBALS
CONFIG_FILE = 'config.yaml'

#
# Parses the config file
#
def read_config_file():
	if not os.path.exists(CONFIG_FILE):
		print('config.yaml does not exist. Try copying config.example.yaml to fix this.')
		sys.exit()

	with open (os.path.dirname(os.path.realpath(__file__)) + '/' + CONFIG_FILE) as myfile:
		config = yaml.safe_load(myfile)

	return config

def get_public_ip():
	return urlopen('http://ip.42.pl/raw').read()

def constrain_logfile(config):	
	# Don't allow the log file too large
	if os.path.exists(config['log_file']):
		statinfo = os.stat(config['log_file'])
		if statinfo.st_size >= 10485760:
			print("removing log file")
			os.remove(config['log_file'])
	return
 
def setup_logfile(config):
	constrain_logfile(config)

	log_level = get_log_level(config['log_level'])
	if not log_level:
		print('{0} is not a supported log level. Supported levels are INFO and DEBUG.'.format(config['log_level']))
		sys.exit()

	logging.basicConfig(filename = config['log_file'], format = '%(asctime)s %(message)s', level = log_level)
	return

def get_log_level(level):
	return {
		'info': logging.INFO,
		'debug': logging.DEBUG,
	}.get(level, False)

#
# check locally if IP has changed
#
def check_ip_file(config, public_ip):
	if not os.path.exists(os.path.dirname(os.path.realpath(config['ip_file']))):
		logging.info('Creating {0} directory for ip file.'.format(os.path.dirname(os.path.realpath(config['ip_file']))))
		try:
			os.mkdir(os.path.dirname(os.path.realpath(config['ip_file'])))
		except IOError as e:
			print(e)
		else:
			print("Successful")

	if os.path.exists(config['ip_file']):
		with open(config['ip_file'], 'r') as fo:
			old_ip = fo.read(50)

		if old_ip == public_ip:
			print("ip is the same.. not doing anything")
			logging.info('IP has not changed, I am not doing anything now.')
			return 1
	# return if no file exists, or the IP is new
	return

def write_ip_file(config, public_ip):
	if not os.path.exists(config['ip_file']):
		with open(config['ip_file'], 'w') as fo:
			fo.write(public_ip)
	else:
		with open(config['ip_file'], 'r+') as fo:
			fo.seek(0)
			fo.write(public_ip)
			fo.truncate()
	return
 
def update_dns(config, public_ip):
	client = pygodaddy.GoDaddyClient()
	client.login(config['godaddy_username'], config['godaddy_password'])
 
	for domain in client.find_domains():
		for dns_record in client.find_dns_records(domain):
			logging.debug("Domain '{0}' DNS records: {1}".format(domain, client.find_dns_records(domain)))
			# only update the bluewolf subdomain
			if dns_record.hostname == config['record_hostname']:
				if public_ip != dns_record.value:
					if client.update_dns_record(dns_record.hostname + "." + domain, public_ip):
						logging.info("Host '{0}' public IP set to '{1}'".format(dns_record.hostname, public_ip))
						# update our local copy of IP
						write_ip_file(config, public_ip)
					else:
						logging.info("Failed to update Host '{0}' IP to '{1}'".format(dns_record.hostname, public_ip))
				else:
					logging.info("Nothing was changed")
					write_ip_file(config, public_ip)
			else:
				logging.info("Not {0}: '{1}', skipping".format(config['record_hostname'], dns_record.hostname))
	return

#
# Main method
#
def main():
	# Load the configuration
	config = read_config_file()

	# Make sure the log file is all good
	setup_logfile(config)

	# Retrieve our public IP address
	public_ip = get_public_ip()

	if check_ip_file(config, public_ip) != 1:
		update_dns(config, public_ip)

#
# Run the script
#
main()
