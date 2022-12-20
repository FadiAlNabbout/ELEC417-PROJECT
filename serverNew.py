import socket
import hashlib
# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9991
# bind the socket to a public host, and a port
server_socket.bind((host, port))
# become a server socket
server_socket.listen(5)
# create a dictionary to store valid usernames and passwords
credentials = {
"user1": "password1",
"user2": "password2"
}
while True:
# establish a connection
	client_socket, address = server_socket.accept()
	print("Got a connection from %s" % str(address))
# receive the username and password from the client
	data = client_socket.recv(1024).decode()
	username, password = data.split(":")
# hash the password to compare to the stored hash
	hashed_password = hashlib.sha256(password.encode()).hexdigest()
# check if the username and password are valid
	if username in credentials and credentials[username] == hashed_password:
		client_socket.send("Authentication successful".encode())
# process requests from the client
	while True:
		data = client_socket.recv(1024).decode()
	if not data:
		break
		print("Received: %s" % data)
		client_socket.send(("ACK: " + data).encode())
	else:
		client_socket.send("Authentication failed".encode())
	client_socket.close()
	server_socket.close()
