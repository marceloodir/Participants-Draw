#!/usr/bin/python3

import cgi
import cgitb
import sorteio

print("Content-type: text/html\n\n")
print("<html>")
print('<head><meta charset="UTF-8" />')

cgitb.enable()
sorteio.limpar()

print('<meta http-equiv="refresh" content="3;url=http://localhost:8080" /> ')
print("</head>")
print("<body>Participantes Apagados, aguarde...</body></html>")
