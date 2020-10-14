import requests
import sys
import threading

TIMEOUT = 1

def open_connection(url):
	try:
		response = requests.get(url, timeout=TIMEOUT, allow_redirects=False)
		print(f":> Result: URL={response.url} >> ", end="")
		print(f"{response.status_code} {response.reason}")
		if not response.OK:
			print(response.raise_for_status())
	except:
		print(":?Program failed, Something is wrong with your system.")	
		sys.exit(-1)


def start_a_check(id, url):
	print(f":>> Number{id} started == {url}")
	open_connection(url)
	print(f":>> Number{id} is out.")


def execute(url_list):
	id = 127
	for url in url_list:
		t = threading.Thread(open_connection, (id, url))
		t.start()
		id += 12


if __name__ == "__main__":
	create()		