# -*- coding: utf-8 -*-
# Questão 09

print("* --- Calculadora --- *\n")

def operacao(x, y, z):
	if(z == 1):
		result = x + y
		print("\nA soma de", x,"+", y,"é igual a",result,"\n")
	elif(z == 2):
		result = x - y
		print("\nA subtração de", x,"-", y,"é igual a",result,"\n")
	elif(z == 3):
		result = x * y
		print("\nA multiplicação de", x,"*", y,"é igual a",result,"\n")
	elif(z == 4):
		result = x / y
		print("\nA divisão de", x,"/", y,"é igual a",result,"\n")
	else:
		print("\nERROR!!! Opção inválida.\n")

condicao = 2

while(condicao != 1):
	opcao = int(input("Que operação você deseja realizar?\nDigite:\n1 para soma\n2 para subtração\n3 para multiplicação\n4 para divisão\n"))
	num1 = int(input("Digite o primeiro número:\n"))
	num2 = int(input("Digite o segundo número:\n"))

	operacao(num1, num2, opcao)

	condicao = int(input("Você deseja encerrar o programa?\nDigite:\n1 para sim\n2 para não\n"))
