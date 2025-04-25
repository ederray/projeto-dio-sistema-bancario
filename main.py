# carregamento de bibliotecas
import datetime as dt
import pandas as pd
from utils import *

# declaração de variáveis

TITULO = """Banco Austral"""
MENU = """Prezado(a) cliente, escolha uma das opções de operação disponíveis:

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

"""

# programa principal
# descrição do título para apresentação dos valores
print(f"{TITULO.center(64,'-')} \n")
print(MENU)

# escolha dos valores pelo usuário

# estrutura de repetição que ocorre enquanto o usuário interagir com o sistema
while True:

    # input do usuário para ação do programa.
    resposta = int(input())

    if resposta == 1:

        deposito = gerar_deposito()
        print(MENU)

    elif resposta == 2:

        saldo, numero_saque = gerar_saque()
        print(MENU)

    elif resposta == 3:

        tabela = gerar_extrato()
        print(tabela)

        print(MENU)

    elif resposta == 4:

        print("O banco Austral agradece sua visita.\nTenha um ótimo dia.")
        break

    else:

        print("Opção Inválida. Escolha uma opção de 1 a 4.")
