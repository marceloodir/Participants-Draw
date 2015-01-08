#!/usr/bin/python3

import cgi
import cgitb
import sorteio

print("Content-type: text/html\n\n")
print("<html>")
print('<head><meta charset="UTF-8" />')
print("</head>")

cgitb.enable()
formulario = cgi.FieldStorage()
nome = formulario.getvalue('nome')
tel =  formulario.getvalue('tel')
email = formulario.getvalue('email')
try:
	novo = sorteio.Participante(nome,tel,email)
	sorteio.adicionar(novo)
	print("<body><h3>Participante Cadastrado.</h3><br /><br />")
	print('<a href="http://localhost:8080">Voltar</a></body></html>')
except Exception as err:
	print("<body><h2>ERRO: "+str(err)+"</h2><br /><br />")
	print('<A HREF="javascript:javascript:history.go(-1)">Voltar</A></body></html>')


