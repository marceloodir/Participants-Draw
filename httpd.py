#!/usr/bin/python3 

from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8080
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Iniciando o simple_httpd na porta: ',str(httpd.server_port))
httpd.serve_forever()
