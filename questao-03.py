# -*- coding: utf-8 -*-
# Questão 03

from datetime import date

"""
O comando acima realiza a importação 
da biblioteca de data para pegar a 
data atual pelo sistema.
"""

ano_atual = date.today()

nome = input("Digite seu nome:\n")
ano_nascimento = int(input("Digite o ano em que você nasceu:\n"))

idade = ano_atual.year - ano_nascimento

print("Olá", nome+", você tem", idade,"anos.")
