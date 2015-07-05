#!/usr/bin/env python
#import sys
import os
import logging
import yaml
import pygodaddy
from urllib2 import urlopen
 
# GLOBALS
CONFIG_FILE = 'config.yaml'

#
# Parses the config file
#
def read_config_file():
	with open (os.path.dirname(os.path.realpath(__file__)) + '/' + CONFIG_FILE) as myfile:
		config = yaml.safe_load(myfile)

	return config

def get_public_ip():
	return urlopen('http://ip.42.pl/raw').read()

def constrain_logfile(config):
	# Don't allow the log file to become greater than 10MB
	if os.path.exists(config['log_file']):
		statinfo = os.stat(config['log_file'])
		if statinfo.st_size >= 10485760:
			print "removing log file"
			os.remove(config['log_file'])
	return
 
def setup_logfile(config):
	constrain_logfile(config)
	logging.basicConfig(filename = config['log_file'], format = '%(asctime)s %(message)s', level = logging.INFO)
	return

#
# check locally if IP has changed
#
def check_ip_file(config, public_ip):
	if os.path.exists(config['ip_file']):
		with open(config['ip_file'], 'r') as fo:
			old_ip = fo.read(50)

		if old_ip == public_ip:
			print "ip is the same.. not doing anything"
			return 1
	# return if no file exists, or the IP is new
	return

def write_ip_file(config, public_ip):
	if not os.path.exists(config['ip_file']):
		fo = open(config['ip_file'], "w")
		fo.write(public_ip)
		fo.close()
	else:
		fo = open(config['ip_file'], "r+")
		fo.seek(0)
		fo.write(public_ip)
		fo.truncate()
		fo.close()
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
							write_ip_file(config)
						else:
							logging.info("Failed to update Host '{0}' IP to '{1}'".format(dns_record.hostname, public_ip))
				else:
						logging.info("Nothing was changed")
						write_ip_file(public_ip)
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
	check_ip_file(public_ip)

	if check_ip_file(config, public_ip) != 1:
		update_dns(config, public_ip)

#
# Run the script
#
main()
