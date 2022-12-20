import stem
import stem.connection
import stem.socket
import socketserver

# Connect to the TOR control port
control_port = stem.socket.ControlPort(port = 9051)
stem.connection.authenticate(control_port)

# Set up a new TOR circuit
def new_circuit():
    control_port.send("SIGNAL NEWNYM\n")



class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Set up a new TOR circuit
        new_circuit()

        # Receive data from the client
        self.data = self.request.recv(1024).strip()

        # Send a response back to the client
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    # Create the server
    server = socketserver.TCPServer(("localhost", 8000), MyTCPHandler)

    # Start the server
    server.serve_forever()

