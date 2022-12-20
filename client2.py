import socket
import hashlib
import random
import struct

def generate_masked_ip():
	return ".".join([str(random.randint(0, 255)) for i in range(4)])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((generate_masked_ip(), 0))
client.connect(("localhost", 8083))

challenge_phrase = "qwerty"
hashed_challenge = hashlib.sha256(challenge_phrase.encode()).hexdigest()
client.send(hashed_challenge.encode())

response = client.recv(1024).decode()
if response == "Connection established":
	print("Connected to server successfully")
else:
	print("Failed to connect to server")

client.close()
