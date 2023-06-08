cabecalho = " NERY BANK "
cabecalho_formatado = print(cabecalho.center(60, "="))
rodape = " DEVELOPED BY BABADUQUE "
rodape_formatado = print(rodape.center(60, "="))
menu = """
BEM-VINDO! SELECIONE A SUA OPERAÇÃO ABAIXO:

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_de_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    cabecalho_formatado
    opcao = input(menu)
    rodape_formatado

    if opcao == "d" or opcao == "D":
        print("SELECIONADO: Depósito")
        print(f"SALDO ATUAL: R$ {saldo:.2f}")

        deposito_parcial = float(input("\nInforme o valor a ser depositado em conta: "))
        saldo += deposito_parcial
        extrato.append(f"DEPOSITO: R$ {deposito_parcial:.2f}")
            
        print("\n\nOPERAÇÃO REALIZADA! VALOR DEPOSITADO.")
        print(f"NOVO SALDO: R$ {saldo:.2f}")
        rodape_formatado

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

                print("\n\nOPERAÇÃO REALIZADA! RETIRE O SEU DINHEIRO NA BOCA DO CAIXA.")
                print(f"\nNOVO SALDO: R$ {saldo:.2f}")
                rodape_formatado
            else:
                print("\n\nOPERAÇÃO NÃO REALIZADA! O VALOR ULTRAPASSA O LIMITE DE R$ 500,00 POR SAQUE OU O VALOR DO SAQUE É MAIOR QUE O SEU SALDO.\n")
                
        else:
            print("OPERAÇÃO NÃO REALIZADA! VOCÊ JÁ UTILIZOU OS 3 SAQUES DISPONÍVEIS PARA O DIA. TENTE NOVAMENTE AMANHÃ...")

        finalizar_programa = input("""[key] MENU PRINCIPAL\n[n] SAIR\n\n""")
        if finalizar_programa == "n" or finalizar_programa == "N":
            break
    elif opcao == "e" or opcao == 'e':
        print("SELECIONADO: Extrato")
        print("\n\nEXTRATO DETALHADO DA CONTA: \n")
        for i, operacao in enumerate(extrato):
            print(f"{i + 1}. {operacao}")

        print(f"\nSALDO ATUAL: R$ {saldo:.2f}")
        rodape_formatado
        
        finalizar_programa = input("""[key] MENU PRINCIPAL\n[n] SAIR\n\n""")
        if finalizar_programa == "n" or finalizar_programa == "N":
            break
    elif opcao == "q" or opcao == "Q":
        break
    else:
        print("OPÇÃO INVÁLIDA! POR FAVOR SELECIONE NOVAMENTE A OPÇÃO DESEJADA.\n\n")
        
        finalizar_programa = input("""[key] MENU PRINCIPAL\n[n] SAIR\n\n""")
        if finalizar_programa == "n" or finalizar_programa == "N":
            break
