import time
from datetime import datetime as dt


host_path = r"C:\Windows\System32\drivers\etc"
redirect = 127.0.0.1
blocked_websites = ["www.facebook.com", "facebook.com"]

while true:
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
		print("This is working hours...")
		time.sleep(100)
	else:
		print("Fun hours!")
	time.sleep(200)
