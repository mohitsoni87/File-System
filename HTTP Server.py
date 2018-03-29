import http.server
import socketserver, os
os.chdir('C:\\')

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    import os
    os.system('start http://192.168.137.102:8000/')
    httpd.serve_forever()
