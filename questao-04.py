# -*- coding: utf-8 -*-
# Questão 04

from datetime import date

"""
O comando acima realiza a importação 
da biblioteca de data para pegar a 
data atual pelo sistema.
"""

ano_atual = date.today()

ano_nascimento = int(input("Digite o ano em que você nasceu:\n"))

idade = ano_atual.year - ano_nascimento

if(idade >= 18):
	print("Você tem", idade,"anos e já pode tirar carteira de motorista.")
else:
	print("Você tem", idade,"anos e não pode tirar carteira de motorista.")