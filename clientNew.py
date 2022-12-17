import socket
import hashlib
# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 4041
# connection to hostname on the port.
client_socket.connect((host, port))
# send the username and hashed password to the server
username = "user1"
password = "password1"
hashed_password = hashlib.sha256(password.encode()).hexdigest()
client_socket.send((username + ":" + hashed_password).encode())
# receive the authentication response from the server
data = client_socket.recv(1024).decode()
if data == "Authentication successful":
# send a request to the server
	client_socket.send("Hello, can you process this request?".encode())
# receive the response from the server
	data = client_socket.recv(1024).decode()
	print("Received: %s" % data)
else:
	print("Authentication failed")
client_socket.close()
