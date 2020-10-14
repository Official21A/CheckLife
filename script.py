import requests
import sys

TIMEOUT = 1

def open_connection(url):
	try:
		response = requests.get(url, timeout=TIMEOUT, allow_redirects=False)
		print(f":> Result: URL={response.url} >> ", end="")
		print(f"{response.status_code} {response.reason}")
	except:
		print(":?Program failed, Something is wrong with your system.")	
		sys.exit(-1)