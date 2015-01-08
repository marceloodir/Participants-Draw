#!/usr/bin/python3

import cgi
import cgitb
import sorteio

print("Content-type: text/html\n\n")
print("<html>")
print('<head><meta charset="UTF-8" /></head>')
print('<body>')

sorteado = sorteio.sortear()

if sorteado == -1:
	print("<h3>Não há participantes cadatrados para haver sorteio.</h3>")
else:
	print("<center><h1>O participante vencedor é:</h1><br />")
	print('<table border="1">')
	print("<tr>")
	print("<th>Nome</th><th>Telefone</th><th>Email</th><th>Data de Criação</th>")
	print("</tr>")
	print("<tr>")
	print("<td>"+sorteado.getNome()+"</td><td>"+sorteado.getTelefone()+"</td><td>"+sorteado.getEmail()+"</td><td>"+sorteado.getDataCadastro()+"</td>")
	print("</tr>")
	print("</table></center>")

print('<a href="http://localhost:8080">Voltar</a>')
print("</body>")
