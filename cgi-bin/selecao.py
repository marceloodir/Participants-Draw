#!/usr/bin/python3

import cgi
import cgitb

print("Content-type: text/html\n\n")
print("<html>")
print('<head><meta charset="UTF-8" />')

cgitb.enable()
formulario = cgi.FieldStorage()
opcao = formulario['op'].value

if opcao == 'Adicionar': 
	print('<meta http-equiv="refresh" content="0;url=http://localhost:8080/adicionar.html" /> ')
elif opcao == 'Listar':
	print('<meta http-equiv="refresh" content="0;url=http://localhost:8080/cgi-bin/listar.py" /> ')
elif opcao == 'Sortear':
	print('<meta http-equiv="refresh" content="0;url=http://localhost:8080/cgi-bin/sortear.py" /> ')
elif opcao == 'Limpar':
	print('<meta http-equiv="refresh" content="0;url=http://localhost:8080/cgi-bin/limpar.py" /> ')
elif opcao == 'LimparP':
	print('<meta http-equiv="refresh" content="0;url=http://localhost:8080/remover.html" /> ')

print("</head>")
print("<body>Redirecionando...</body></html>")
