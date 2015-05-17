# -*- coding: utf-8 -*-
# Questão 07

condicao = 2

while(condicao != 1):
	x = int(input("Digite um número:\n"))

	if(x % 2 == 0):
		print("Você digitou o número", x,"e ele é um número par.\n")
	else:
		print("Você digitou o número", x,"e ele é um número impar.\n")

	condicao = int(input("Você deseja encerrar o programa?\nDigite:\n1 para sim\n2 para não\n"))
