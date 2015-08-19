import os
import sys
import yaml

class Config:
	
	config = {}

	def __init__(self, filename):
		filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '/' + filename
		
		self.config = self.readYaml(filepath)
	
	def readYaml(self, filepath):
		if not os.path.exists(filepath):
			print(filepath + ' does not exist. Try copying config.example.yaml to fix this.')
			sys.exit()
	
		with open(filepath) as myfile:
			return yaml.safe_load(myfile)
	
	def get(self, path):
		conf = self.config
		path = path.split('.')
		
		for bit in path:
			if bit in conf:
				conf = conf[bit]
		
		return conf