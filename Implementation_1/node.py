# Echo server program
import socket

node_list = []
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

#with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as u:
#    #u.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
#    u.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#    u.sendto(b'192.168.0.109', ('<broadcast>', 60000))
#    #u.bind(("", 60000))
#    data, addr = u.recvfrom(1024)
#    node_list = node_list + data
#    print(node_list)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Server: connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            EXIT = '192.168.0.46'    # The remote host
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as t:
                t.connect((EXIT, PORT))
                t.sendall(data+data)
                data = t.recv(1024)
                if not data: break
                conn.sendall(data)

# Echo client program
#import socket

#HOST = '192.168.0.108'    # The remote host
#PORT = 50007              # The same port as used by the server
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    s.sendall(b'Hello, world')
#    data = s.recv(1024)
#print('Client: received', repr(data))
