import requests
import sys
import threading

TIMEOUT = 1

def open_connection(url):
	try:
		response = requests.get(url, timeout=TIMEOUT, allow_redirects=False)
		response.raise_for_status() 
		print(f":> Result: URL={response.url} >> ", end="")
		print(f"{response.status_code} {response.reason}//{response.elapsed}")	
	except requests.exceptions.RequestException as e:
		print(f":?Program failed {url}. {e}")


def start_a_check(id, url):
	print(f":>> Number{id} started == {url}")
	open_connection(url)
	print(f":>> Number{id} is out.")


def execute(url_list):
	id = 127
	for url in url_list:
		t = threading.Thread(target=start_a_check, args=(id, url))
		t.start()
		id += 12


def create():
	url_list = ["https://github.com","www.google.com","https://www.upgrad.com"]
	execute(url_list)


if __name__ == "__main__":
	create()		