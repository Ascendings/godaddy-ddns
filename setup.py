#!/usr/bin/env python3

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'GoDaddy Dynamic DNS script,
	'author': 'Ascendings',
	'url': 'https://github.com/Ascendings/godaddy-ddns',
	'download_url': 'https://github.com/Ascendings/godaddy-ddns/archive/master.zip',
	'author_email': 'brotherballantine@gmail.com',
	'version': '0.3.0',
	'install_requires': ['nose', 'pygodaddy'],
	'packages': ['godaddy-ddns', 'python3', 'python3-yaml'],
	'scripts': [],
	'name': 'godaddy_ddns'
}

setup(**config)