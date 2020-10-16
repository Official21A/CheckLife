import requests
import sys
import threading
import time

TIMEOUT = 1

results = {}


def open_connection(url):
	global results
	try:
		response = requests.get(url, timeout=TIMEOUT, allow_redirects=False)
		response.raise_for_status() 
		results[f"{url}"] = f"{response.status_code} {response.reason}//{response.elapsed}"	
	except requests.exceptions.RequestException as e:
		results[f"{url}"] = f"{e}"


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


def print_all():
	global results
	for key, value in results.items():
		print(f"URL={key} :: Result={value}")


def create():
	url_list = ["https://github.com","www.google.com","https://www.upgrad.com"]
	execute(url_list)
	while True:
		if len(results.keys()) == len(url_list):
			break;
	print_all()


if __name__ == "__main__":
	create()		