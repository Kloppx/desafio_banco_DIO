import textwrap
from datetime import date

def menu():
    menu = '''
    Escolha a funcao que deseja utilizar:
    [d] - Deposito
    [s] - Saque
    [e] - Extrato
    [nc] - Nova conta
    [lc] - Listar contas
    [nu] - Novo usuario
    [Q] - Sair
'''
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado. R$ {valor:.2f}. no dia {data_atual}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor para depósito inválido, favor verificar.")
    return saldo, extrato

data_atual = date.today().strftime("%d/%m/%Y")
saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = menu().lower()

    if opcao == 'd':
        valor = float(input("Por favor informe o valor que deseja depositar: R$ "))
        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao == 's':
        valor_sacado = float(input("Por favor informe o quanto quer sacar: "))
        numero_saques += 1
        sacar(valor=valor_sacado, saldo=(saldo - valor_sacado))

        if valor_sacado > limite:
            print("O limite para saque é de R$ 500,00!")
    
            if valor_sacado > saldo:
                print(f"O valor solicitado para saque é maior que o saldo atual. Seu saldo é de R$ {saldo:.2f}! ")

        else:
            if numero_saques < 3:
                saldo = saldo - valor_sacado
                numero_saques += 1
                extrato += f"Saque no valor de R$ {valor_sacado:.2f} no dia {data_atual}\n"
            else:
                print("Você atingiu seu limite de saques por hoje! Favor tentar novamente amanhã.")

    
    elif opcao == 'e':
        print(extrato)
    
    elif opcao == 'Q':
        break

    else:
        print("Opção inválida, favor informar uma das citadas anteriormente!")

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    valor = input(float("Quanto você deseja sacar? "))