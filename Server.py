import socket, select, sys, os, threading
from threading import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if(len(sys.argv) != 3):
      print("Format is \n Filename IP PORT")
      exit()

Server_IP, port = str(sys.argv[1]), int(sys.argv[2])
s.bind((Server_IP, port))
s.listen(10)
print('Server is Live!')

def ClientThread(conn, addr):
      conn.send(str.encode('Welcome to File Sharing! ' + str((addr[0])) + '\n'))
      conn.send(str.encode('Filename? '))
      filename = conn.recv(2048).decode('utf-8')
      filename = filename[:len(filename) - 2]
      conn.send(str.encode("Path? "))
      path = conn.recv(2048).decode('utf-8')
      path = path[:len(path) - 2]
      if(path == ''):
            dest = filename
      else:
            dest = path + '/' + filename
      URL = "Please go to the following Link to get your result: http://192.168.137.102:8000/" + dest
      conn.send(str.encode(URL))
      quit()
clients = []
while(1):
      conn, addr = s.accept()
      print('Connected with ' + addr[0])
      clients.append(conn)
      threading.Thread(target=ClientThread, args=(conn, addr)).start()
conn.close()
s.close()
