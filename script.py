import requests
import sys

TIMEOUT = 1

def open_connection(url):
	try:
		response = requests.get(url, timeout=TIMEOUT, allow_redirects=False)
	except:
		print("::> Program failed, Something is wrong with your system.")	
		sys.exit(-1)