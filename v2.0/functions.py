def exibir_cabecalho(cabecalho=" NERY BANK "):
    cabecalho_formatado = print(cabecalho.center(80, "="))
    return cabecalho_formatado

def exibir_menu():
    menu = """
BEM-VINDO! SELECIONE A SUA OPERAÇÃO ABAIXO:

[d] Depósito
[s] Saque
[e] Extrato
[cu] Criar Usuário
[cc] Criar Conta
[lc] Listar Contas
[q] Sair

=> """
    return input(menu)

def exibir_rodape(rodape=" DEVELOPED BY BABADUQUE "):
    rodape_formatado = print(rodape.center(80, "="))
    return rodape_formatado

def exibir_agradecimento(agradecimento=" OBRIGADO POR UTILIZAR O NERY BANK! VOLTE SEMPRE :) "):
    agradecimento_formatado = print(agradecimento.center(80, " "))
    return agradecimento_formatado

def finalizar_programa():
    finalizar_programa = """[key] MENU PRINCIPAL\n[n] SAIR\n\n=> """
    return input(finalizar_programa)

def depositar(saldo, deposito_parcial, extrato, /):
    if deposito_parcial > 0:
        saldo += deposito_parcial
        extrato.append(f"DEPOSITO: R$ {deposito_parcial:.2f}")
        
        print("\n\nOPERAÇÃO REALIZADA! VALOR DEPOSITADO.")
        print(f"NOVO SALDO: R$ {saldo:.2f}\n")
        exibir_rodape()
    else:
        print("\n\nOPERAÇÃO NÃO REALIZADA! O VALOR INFORMADO PARA DEPÓSITO É INVÁLIDO.\n")
    return saldo, extrato

def sacar(*, saldo, saque_parcial, extrato, limite_por_saque, numero_saques, limite_saque_diario):
    excedeu_saldo = saque_parcial > saldo
    excedeu_limite_por_saque = saque_parcial > limite_por_saque
    excedeu_limite_saque_diario = numero_saques >= limite_saque_diario

    if excedeu_saldo:
        print("\n\nOPERAÇÃO NÃO REALIZADA! O VALOR DO SAQUE É MAIOR QUE O SEU SALDO.\n")
        exibir_rodape()
    elif excedeu_limite_por_saque:
        print("\n\nOPERAÇÃO NÃO REALIZADA! O VALOR ULTRAPASSA O LIMITE DE R$ 500,00 POR SAQUE.\n")
        exibir_rodape()
    elif excedeu_limite_saque_diario:
        print("\n\nOPERACAO NÃO REALIZADA! VOCÊ JÁ UTILIZOU OS 3 SAQUES DISPONÍVEIS PARA O DIA. TENTE NOVAMENTE AMANHÃ...\n")
        exibir_rodape()
    elif saque_parcial > 0:
        saldo -= saque_parcial
        extrato.append(f"SAQUE: R$ {saque_parcial:.2f}")
        numero_saques += 1

        print("\n\nOPERAÇÃO REALIZADA! RETIRE O SEU DINHEIRO NA BOCA DO CAIXA.")
        print(f"VALOR: R$ {saque_parcial:.2f}")
        print(f"\nNOVO SALDO: R$ {saldo:.2f}\n")
        exibir_rodape()
    else:
        print("\n\nOPERAÇÃO NÃO REALIZADA! O VALOR INFORMADO PARA SAQUE É INVÁLIDO.\n")
        exibir_rodape()
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n\nEXTRATO DETALHADO DA CONTA:\n")
    if extrato:
        for i, operacao in enumerate(extrato):
            print(f"{i + 1}. {operacao}")
    else:
        print("NÃO HOUVERAM MOVIMENTAÇÕES NA CONTA.\n\n")
    
    print(f"\nSALDO ATUAL: R$ {saldo:.2f}")
    exibir_rodape()

def criar_usuario(usuarios):
    cpf = input("INFORME O SEU CPF (APENAS NÚMEROS): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("OPERAÇÃO NÃO REALIZADA! O CPF INFORMADO ENCONTRA-SE VINCULADO A UM USUÁRIO EXISTENTE.")
        return
    
    nome = input("INFORME O NOME COMPLETO: ")
    data_nascimento = input("INFORME A DATA DE NASCIMENTO (DD/MM/AAAA): ")
    endereco = input("INFORME O ENDEREÇO (LOGRADOURO, NRO - BAIRRO - CIDADE/ESTADO): ")
    print("\n\nOPERAÇÃO REALIZADA! USUÁRIO CRIADO.\n")
    exibir_rodape()

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

def filtrar_usuario(cpf, usuarios):
    ususarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return ususarios_filtrados[0] if ususarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("INFORME O SEU CPF (APENAS NÚMEROS): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\nOPERAÇÃO REALIZADA! CONTA CRIADA.\n")
        exibir_rodape()
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("\n\nOPERAÇÃO NÃO REALIZADA! NÃO HÁ USUÁRIO VINCULADO AO CPF INFORMADO. CRIE UM USUÁRIO PARA ESSE CPF E TENTE NOVAMENTE...\n")
        exibir_rodape()

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """

        print(linha)
    exibir_rodape()

def main():
    LIMITE_SAQUE_DIARIO = 3
    LIMITE_POR_SAQUE = 500
    AGENCIA = "0001"

    saldo = 0
    numero_saques = 0
    extrato = []
    usuarios = []
    contas = []
    
    while True:
        exibir_cabecalho()
        opcao = exibir_menu()
        exibir_rodape()

        if opcao.lower() == "d":
            print("SELECIONADO: Depósito")
            print(f"SALDO ATUAL: R$ {saldo:.2f}")

            deposito_parcial = float(input("\nInforme o valor a ser depositado em conta: R$ "))
            saldo, extrato = depositar(saldo, deposito_parcial, extrato)
            finalizar = finalizar_programa()
            if finalizar.lower() == "n":
                print("")
                exibir_agradecimento()
                exibir_rodape()
                break
        elif opcao.lower() == "s":
            print("SELECIONADO: Saque")
            print(f"SALDO ATUAL: R$ {saldo:.2f}")

            saque_parcial = float(input("\nInforme o valor a ser retirado da conta: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                saque_parcial=saque_parcial,
                extrato=extrato,
                limite_por_saque=LIMITE_POR_SAQUE,
                numero_saques=numero_saques,
                limite_saque_diario=LIMITE_SAQUE_DIARIO,
            )

            finalizar = finalizar_programa()
            if finalizar.lower() == "n":
                print("")
                exibir_agradecimento()
                exibir_rodape()
                break
        elif opcao.lower() == "e":
            print("SELECIONADO: Extrato")
            exibir_extrato(saldo, extrato)
        
            finalizar = finalizar_programa()
            if finalizar.lower() == "n":
                print("")
                exibir_agradecimento()
                exibir_rodape()
                break
        elif opcao.lower() == "cu":
            criar_usuario(usuarios)

            finalizar = finalizar_programa()
            if finalizar.lower() == "n":
                print("")
                exibir_agradecimento()
                exibir_rodape()
                break
        elif opcao.lower() == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
            finalizar = finalizar_programa()
            if finalizar.lower() == "n":
                print("")
                exibir_agradecimento()
                exibir_rodape()
                break
        elif opcao.lower() == "lc":
            listar_contas(contas)
            
            finalizar = finalizar_programa()
            if finalizar.lower() == "n":
                print("")
                exibir_agradecimento()
                exibir_rodape()
                break
        elif opcao.lower() == "q":
            break
        else:
            print("\nOPÇÃO INVÁLIDA! POR FAVOR SELECIONE NOVAMENTE A OPÇÃO DESEJADA.\n")
