menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
       deposito = float(input("Informe o valor do depósito:"))

       if deposito > 0:
           saldo += deposito
           extrato += f"Depósito: R$ {deposito:.2f}\n"
           print("\n[Despósito Bem Sucedido!]")
           print(f"\nFoi Depositado: R$ {deposito}\n") 

       else:
           print("[ERRO NO DEPÓSITO] O valor depositado é inválido")   
       
    elif opcao == "2":
        saque = float(input("Informe o valor do saque:"))

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

    elif opcao == "3":
        print("\n |               EXTRATO               | ")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n |               EXTRATO               | ")
        
    elif opcao == "0":
        print("Operação Encerrada!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")