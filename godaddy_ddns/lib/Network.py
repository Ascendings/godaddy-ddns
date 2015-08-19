from urllib.request import urlopen

class Network:

	def getPublicIP():
		ip = urlopen('http://ip.42.pl/raw').read()
		ip = ip.decode() # Decode to utf-8 string
		
		return ip