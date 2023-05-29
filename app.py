cabecalho = " NERY BANK "
rodape = " DEVELOPED BY BABADUQUE "
menu = """
BEM-VINDO! SELECIONE A SUA OPERAÇÃO ABAIXO:

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair


"""

saldo = 0
limite_de_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(cabecalho.center(60, "="))
    opcao = input(menu)
    print(rodape.center(60, "="))

    if opcao == "d" or opcao == "D":
        print("SELECIONADO: Depósito")
        print(f"SALDO ATUAL: R$ {saldo:.2f}")

        deposito_parcial = float(input("\nInforme o valor a ser depositado em conta: "))
        saldo += deposito_parcial
        extrato.append(f"DEPOSITO: R$ {deposito_parcial:.2f}")
            
        print("\n\nVALOR DEPOSITADO COM SUCESSO!")
        print(f"NOVO SALDO: R$ {saldo:.2f}")
        print(rodape.center(60, "="))

        finalizar_programa = input("""[key] MENU PRINCIPAL\n[n] SAIR\n\n""")
        if finalizar_programa == "n" or finalizar_programa == "N":
            break
    elif opcao == "s" or opcao == "S":
        if numero_saques < 3:    
            print("SELECIONADO: Saque")
            print(f"SALDO ATUAL: R$ {saldo:.2f}")

            saque_parcial = float(input("\nInforma o valor a ser sacado da conta: "))

            if saque_parcial <= 500 and saque_parcial <= saldo:
                numero_saques = numero_saques + 1
                saldo -= saque_parcial
                extrato.append(f"SAQUE: R$ {saque_parcial:.2f}")

                print("\n\nVALOR LIBERADO! RETIRE O SEU DINHEIRO NA BOCA DO CAIXA.")
                print(f"\nNOVO SALDO: R$ {saldo:.2f}")
                print(rodape.center(60, "="))
            else:
                print("\n\nOPERAÇÃO INVÁLIDA! VOCÊ ULTRAPASSOU O LIMITE DE R$ 500 DE SAQUE OU O VALOR DO SAQUE É MAIOR QUE O SEU SALDO.\n")
                
        else:
            print("OPERAÇÃO INVÁLIDA! LIMITE DE SAQUE ATINGIDO.")

        finalizar_programa = input("""[key] MENU PRINCIPAL\n[n] SAIR\n\n""")
        if finalizar_programa == "n" or finalizar_programa == "N":
            break
    elif opcao == "e" or opcao == 'e':
        print("SELECIONADO: Extrato")
        print("\n\nEXTRATO DETALHADO DA CONTA: \n")
        for i, operacao in enumerate(extrato):
            print(f"{i + 1}. {operacao}")

        print(f"\nSALDO ATUAL: R$ {saldo:.2f}")
        print(rodape.center(60, "="))
        
        finalizar_programa = input("""[key] MENU PRINCIPAL\n[n] SAIR\n\n""")
        if finalizar_programa == "n" or finalizar_programa == "N":
            break
    elif opcao == "q" or opcao == "Q":
        break
    else:
        print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE...\n\n")
        
        finalizar_programa = input("""[key] MENU PRINCIPAL\n[n] SAIR\n\n""")
        if finalizar_programa == "n" or finalizar_programa == "N":
            break
