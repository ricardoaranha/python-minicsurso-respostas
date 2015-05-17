# -*- coding: utf-8 -*-
# Questão 06

nomes = ["Ana", "Maria", "João", "Amanda", "Carol"]

x = 0

for i in nomes:
	if(i[0] == "A"):
		x += 1
		print(i)

print("Existem", x,"pessoas cuje os nomes ccomeção com a letra A.")