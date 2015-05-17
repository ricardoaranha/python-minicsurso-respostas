# -*- coding: utf-8 -*-
# Questão 08

from datetime import date

"""
O comando acima realiza a importação 
da biblioteca de data para pegar a 
data atual pelo sistema.
"""

ano_atual = date.today()

nome = input("Digite seu nome:\n")
ano_nascimento = int(input("Digite o ano em que você nasceu:\n"))

def mensagem(x, y):
	idade = ano_atual.year - x
	print("Olá", y,"você tem", idade,"anos.")

mensagem(ano_nascimento, nome)