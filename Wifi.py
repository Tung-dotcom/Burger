import subprocess
from decouple import config
import time

IP_DEVICE = config('IP_DEVICE')

proc = subprocess.Popen(["ping","-t", IP_DEVICE], stdout=subprocess.PIPE)
for i in range(1,10):
	line = proc.stdout.readline()
	if not line:
		break
	try:
		connected_ip = line.decode("utf-8").split()[2].replace(':', '')
		if connected_ip == IP_DEVICE:
			print("My phone is in the house")
			break
		else:
			time.sleep(2)
			print("Pinging...")
	except:
		pass