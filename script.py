import requests
import sys
import threading
import time

PATH = "DATA"
TIMEOUT = 1

results = {}
url_list = []


def save(value):
	try:
		with open(PATH, "a+") as file:
			file.write(f"{value}\n")
			file.close()
	except (e,):
		print(e)	


def load():
	global url_list
	try:
		with open(PATH, "r") as file:
			url_list = file.readlines()
	except (e,):
		print(e)						


def update(value):
	global url_list
	try:
		with open(PATH, "w") as file:
			for line in url_list:
				if line.strip() != value:
					file.write(f"{line}")						
	except (e,):
		print(e)


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
		t = threading.Thread(target=start_a_check, args=(id, url.strip()))
		t.start()
		id += 12


def print_all():
	global results
	for key, value in results.items():
		print(f"URL={key} :: Result={value}")


def create():
	global url_list
	load()
	execute(url_list)
	while True:
		if len(results.keys()) == len(url_list):
			break;
	print_all()


def show():
	global url_list
	print(url_list)


def add(value):
	url_list.append(value)	
	print(f">{value} : Added.")
	save(value)


def remove(value):
	load()
	update(value)
	print(f">{value} : Removed")


def run(arvg):
	try:
		if len(arvg) == 1:
			create()
		elif arvg[1] == "-add":
			add(arvg[2])	
		elif arvg[1] == "-rmv":
			remove(arvg[2])
		elif arvg[1] == "-viw":
			show()
		else:
			print(">? Error")
	except (e,):
		print(e)						


if __name__ == "__main__":
	run(sys.argv)		