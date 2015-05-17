# -*- coding: utf-8 -*-
# Questão 10

print("* --- Calculadora de IMC (Índice de massa corporal) --- *\n")

def imc(x, y):
	result = x / (y ** 2)
	result = round(result, 2)

	if(result < 17):
		print("\nSeu resultado foi", result,"e sua situação é:\nMuito abaixo de peso.\n")
	elif(result >= 17 and result <= 18.49):
		print("\nSeu resultado foi", result,"e sua situação é:\nAbaixo do peso.\n")
	elif(result >= 18.5 and result <= 24.99):
		print("\nSeu resultado foi", result,"e sua situação é:\nPeso normal.\n")
	elif(result >= 25 and result <= 29.99):
		print("\nSeu resultado foi", result,"e sua situação é:\nAcima do peso.\n")
	elif(result >= 30 and result <= 34.99):
		print("\nSeu resultado foi", result,"e sua situação é:\nObesidade I.\n")
	elif(result >= 35 and result <= 39.99):
		print("\nSeu resultado foi", result,"e sua situação é:\nObesidade II (Severa).\n")
	else:
		print("\nSeu resultado foi", result,"e sua situação é:\nObesidate III (Mórbida.\n")

condicao = 2

while(condicao != 1):
	num1 = float(input("Digite o seu peso (use ponto no lugar da virgula):\n"))
	num2 = float(input("Digite o sua altura (use ponto no lugar da virgula):\n"))

	imc(num1, num2)

	condicao = int(input("Você deseja encerrar o programa?\nDigite:\n1 para sim\n2 para não\n"))
