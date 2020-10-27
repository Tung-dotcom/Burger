import subprocess
from decouple import config

IP_DEVICE = config('IP_DEVICE')
proc = subprocess.Popen(["ping","-t", IP_DEVICE], stdout=subprocess.PIPE)
while True:
	line = proc.stdout.readline()
	if not line:
		break
	try:
		connected_ip = line.decode("utf-8").split()[2].replace(':', '')
		print(connected_ip)
		if connected_ip == IP_DEVICE:
			print("Tung is home")
			break
		else:
			print("Pinging...")
	except:
		pass