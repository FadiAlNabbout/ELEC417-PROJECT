import socket
import hashlib

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8083))
server.listen(5)

challenge_phrase = "qwerty"
hashed_challenge = hashlib.sha256(challenge_phrase.encode()).hexdigest()

while True:
	client, addr = server.accept()
	request = client.recv(1024).decode()
	if request == hashed_challenge:
		client.send("Connection established".encode())
	else:
		client.send("Incorrect challenge response".encode())
client.close()
server.close()
