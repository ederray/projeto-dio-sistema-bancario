# Projeto Sistema Bancário

# carregamento de bibliotecas

import datetime as dt
import pandas as pd


# declaração de variáveis

TITULO = """Banco Austral"""
MENU = """Prezado(a) cliente, escolha uma das opções de operação disponíveis:

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

"""

limite = 500
extrato = 0
numero_saque = 0
data = dt.date.today()
saldo = 0
historico = {'data_operacao': [], 'valor': [],
             'saldo_atualizado': [], 'operacao': []}


# declaração de funções

def atualizar_historico(data, valor: float, saldo_atualizado: float, operacao: str):
    """ Função que atualiza a movimentação realizada pelo cliente e armazena os dados no objeto dicionário.

     Input:

     data: data da operação.
     valor: valor da transação.
     saldo_atualizado: saldo anterior - valor
     operação: operação de depósito ou saque.
       """

    historico['data_operacao'].append(data)
    historico['valor'].append(valor)
    historico['saldo_atualizado'].append(saldo_atualizado)
    historico['operacao'].append(operacao)


def gerar_deposito():
    """Função que realiza a operação de depósito na conta do usuário e armazena os dados no objeto dicionário.

    Input:

    valor: valor de depósito
    saldo: saldo anterior + valor

    Processo:

    Verificação de valor menor igual a zero.
    Registro dos dados no objeto dicionário.

        """

    global saldo

    valor = float(input("Informe o valor de depósito:"))
    saldo += valor

    # invocação da função que atualiza o dicionário que recebe os registros de histórico de transações.
    atualizar_historico(data=data, valor=valor,
                        saldo_atualizado=saldo, operacao='depósito')

    # processo de verificação de valores de depósito
    if valor < 0:

        print(f"Não é possível depositar um valor negativo.")

    else:

        print(
            f"Operação realizada com sucesso.\n Valor depositado: R${valor:.2f}\n Saldo atualizado: R${saldo:.2f}")

    return valor


def gerar_saque():
    """Função que realiza a operação de saque da conta do usuário e armazena os dados no objeto dicionário.

    Input:

    numero_saque: quantidade de saques realizados.
    limite: limite de saque diário.
    saque: valor de saque.
    saldo: saldo anterior - saque

    Processo:

    Verificação da quantidade de saque menor igual a 3.
    Operação de sucesso: Verificação do valor de saque menor ou igual ao limite e menor ou igual ao saldo.
    Verificação do valor de saque menor ou igual ao limite e menor ou igual ao saldo.
    Verificação do valor de saque menor ou igual ao limite e maior ou igual ao saldo.
    Verificação do valor de saque maior ao limite.
    Registro dos dados no objeto dicionário.

    """

    global numero_saque, saldo

    # verificação da quantidade de saques diários para liberar demais opções.

    if numero_saque >= 3:

        print("Operação não autorizada.\nPrezado(a) cliente, você já atingiu a quantidade de saques diária.")

    # saque diário em conformidade
    else:

        # apresentar saldo disponível para saque
        print(f"Seu saldo em conta é:R${saldo:.2f}")

        # valor para saque
        saque = float(input('Insira o valor:'))

        # verificação do limite diário de saque e saldo disponível

        if saque <= limite and saque <= saldo:

            # operação de sucesso

            # atualização do saldo da conta
            saldo -= saque

            # atualização da quantidade de saques diários
            numero_saque += 1

            # atualização do extrato da conta
            atualizar_historico(data, valor=-saque,
                                saldo_atualizado=saldo, operacao='saque')

            # retorno para o usuário
            print(
                f"Operação realizada com sucesso.\n Valor sacado: R${saque:.2f}\n Saldo atualizado: R${saldo:.2f}")

        elif saque <= limite and saque > saldo:

            print(
                f"Operação não autorizada.\nO valor desejado é maior que o saldo disponível: {saldo:.2f}.")

        else:

            print(
                f"Operação não autorizada.\nPrezado(a) cliente, o valor desejado é superior ao limite de saques diário:{limite:.2f}.")

    return saldo, numero_saque


def gerar_extrato():
    """Função que realiza a operação de geração de extrato em formato pandas Dataframe a partir do objeto dicionário.

    Input:

    numero_saque: quantidade de saques realizados.
    tabela: extrato em formato pandas Dataframe.

    Processo:

    Verificação da quantidade de saque igual a 0.
    Registro dos dados no objeto pandas Dataframe.

    """

    global numero_saque

    if numero_saque == 0:
        print('Prezado(a) cliente, você ainda não realizou movimentações na sua conta.')
        tabela = 0

    else:
        print('Prezado(a) cliente, segue o extrato detalhado da sua conta.\n')
        tabela = pd.DataFrame(historico)

    return tabela


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
