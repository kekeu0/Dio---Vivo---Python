menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[0] Sair

=> """


def depositar(saldo, deposito, extrato, /):

            if deposito > 0:
                saldo += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
                print("\n[Despósito Bem Sucedido!]")
                print(f"\nFoi Depositado: R$ {deposito}\n") 

            else:
                print("[ERRO NO DEPÓSITO] O valor depositado é inválido")
                 
            return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, LIMITE_SAQUES):
            excedeu_saque = numero_saques >= LIMITE_SAQUES

            excedeu_limite = saque > limite

            sem_saldo = saque > saldo

            if excedeu_saque:
                print("[OPERAÇÃO BLOQUEADA] Você atingiu o número limete de saque...\n Por favor, tente amanhã")

            elif excedeu_limite:
                print("[OPERAÇÃO BLOQUEADA] Você atingiu o valor limete de saque...\n Tente com um valor menor")

            elif sem_saldo:
                print("[OPERAÇÃO BLOQUEADA] Saldo insificiente...\n Seu saldo não é compatível com essa operação")

            elif saque > 0:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1
                print("\n[Saque Bem Sucedido!]")
                print(f"\nFoi Sacado: R$ {saque}\n")

            else:
                print("[OPERAÇÃO FALHOU] O Valor Informado é Inválido")
            return saldo, extrato     

def exibir_extrato(saldo, /, *, extrato):
            print("\n |               EXTRATO               | ")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("\n |               EXTRATO               | ")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n[OPERAÇÃO INTERROMPIDA!] Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n[erro!]Usuário não encontrado, fluxo de criação de conta encerrado!")



def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    while True:

        opcao = input(menu)

        if opcao == "1":
            deposito = float(input("Informe o valor do depósito:"))

            saldo, extrato = depositar(saldo, deposito, extrato)    
        
        elif opcao == "2":
             saque = float(input("Informe o valor do saque:"))

             saldo, extrato = sacar(
             saldo=saldo, 
             saque=saque,
             extrato=extrato, 
             limite=limite, 
             numero_saques=numero_saques, 
             LIMITE_SAQUES=LIMITE_SAQUES,)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif opcao == "0":
            print("Operação Encerrada!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()