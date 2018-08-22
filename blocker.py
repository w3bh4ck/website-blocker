import time
from datetime import datetime as dt


host_path = r"C:\Windows\System32\drivers\etc"
host_temp = "hosts"
redirect = "127.0.0.1"
blocked_websites = ["www.facebook.com", "facebook.com"]

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) > dt.now() > dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print("This is working hours...")
		with open(host_temp, 'r+') as file:
			content = file.read()
			for website in blocked_websites:
				if website in content:
					pass
				else:
					file.write(redirect+" "+website+"\n")

	else:
		print("Fun hours!")
	time.sleep(20)
