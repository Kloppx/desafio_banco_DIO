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
    data_atual = date.today().strftime("%d/%m/%Y")
    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado. R$ {valor:.2f}. no dia {data_atual}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor para depósito inválido, favor verificar.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  # função para realizar o saque
    data_atual = date.today().strftime("%d/%m/%Y")
    if saldo > valor:
        if saldo > 0:
            if numero_saques < limite_saques:
                if valor > 0 and valor <= 500:
                    saldo -= valor
                    extrato += f"Saque realizado. R$ {valor:.2f}. no dia {data_atual}\n"
                    print("Saque realizado com sucesso!")
                elif valor > limite:
                    print(f"O limite para saque é de R$ {limite:.2f}!")
                else:
                    print("Valor para saque inválido, favor verficar.")
            else:
                print("O limite diário de saques foi atingido.")
        else:
            print("Saldo zerado, não será possível sacar.")
    else:
        print(
            f"O valor inserido é maior que o saldo atual.\n Saldo: R$ {saldo:.2f}.\n Valor inserido: R$ {valor:.2f}.")
    return (saldo, extrato)

def exibir_extrato(saldo, /, *, extrato):
    print("\n============ EXTRATO ============")
    print("Não fora realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==================================")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe um usuário com este CPF!")
        return

    nome=input("Informe seu nome completo: ")
    data_nascimento=input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro , número - bairro - cidade-sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios)
    usuarios_filtrados= [usuario for usuario in usuarios if usuario["cpf"]== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário (Somente números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    print("Usuário não cadastrado, não será possível criar a conta.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']} 
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITES_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu().lower()

        if opcao == 'd':
            valor = float(
                input("Por favor informe o valor que deseja depositar: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor_sacado = float(input("Por favor informe o quanto quer sacar: "))
            numero_saques += 1
            saldo, extrato = sacar(saldo=saldo, valor=valor_sacado, extrato=extrato, limite=limite,
                numero_saques=numero_saques, limite_saques=LIMITES_SAQUES)
            
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario()

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'q':
            break

        else:
            print("Opção inválida, favor informar uma das citadas anteriormente!")

main()