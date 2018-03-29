import socket, sys, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = str(sys.argv[1])
port = int(sys.argv[2])
s.connect((IP, port))
filename = input()
s.send(str.encode(filename))
path = input()
s.send(str.encode(path))
URL = conn.recv(2048)
print("Please go to the following Link to get your result: " + URL)
s.close()
quit()

