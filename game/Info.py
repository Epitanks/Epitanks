import socket


def getinfoserver():
	# get IP address of the server
	informations = {
		'IP_ADDRESS': None,
		'PORT': 9009
	}
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('google.com', 0))
	informations['IP_ADDRESS'] = s.getsockname()[0]
	return informations
