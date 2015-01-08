#!/usr/bin/python3

import cgi
import cgitb
import sorteio
import operator

print("Content-type: text/html\n\n")
print("<html>")
print('<head><meta charset="UTF-8" />')
print("</head>")
print("<body>")
print("<center><h1>Lista de Participantes</h1></center>")
print("<br /><br />")
print('<table border="1">')
print("<tr>")
print("<th>Nome</th><th>Telefone</th><th>Email</th><th>Data de Criação</th>")
print("</tr>")

cgitb.enable()
participantes = sorteio.getParticipantes()
participantes.sort(key=operator.attrgetter('nome'))

for participante in participantes:
	print("<tr>")
	print("<td>"+participante.getNome()+"</td><td>"+participante.getTelefone()+"</td><td>"+participante.getEmail()+"</td><td>"+participante.getDataCadastro()+"</td>")
	print("</tr>")

print("</table>")
print("<br /><br />")
print('<a href="http://localhost:8080">Voltar</a>')
print("</html>")
