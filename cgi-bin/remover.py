#!/usr/bin/python3

import cgi
import cgitb
import sorteio

print("Content-type: text/html\n\n")
print("<html>")
print('<head><meta charset="UTF-8" /></head>')
print('<body>')

formulario = cgi.FieldStorage()
nome = formulario.getvalue('nome')

if sorteio.remover(nome) == 0:
	print('<h3>Participante apagado com sucesso.</h3><br /><br />')
	print('<a href="http://localhost:8080">Voltar</a></body></html>')
else:
	print('<h3>Participante não encontrado, verifique se digitou corretamente seu nome.</h3><br /><br />')
	print('<A HREF="javascript:javascript:history.go(-1)">Voltar</A></body></html>')

print("</body></html>")
