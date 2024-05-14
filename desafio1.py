

menu = """

    SISTEMA DE BANCO SIMPLES

    [d] - depósito
    [s] - saque
    [e] - extrato
    [q] - sair

"""

saldo = 0

LIMITE = 500

LIMITE_DIARIO = 3

extrato = ""

numero_saques = 0

registro_saque = 0


while True:

    print(menu)

    opcao = input("\nEscolha sua opcao: ")

    if opcao == 'd':

        valor = float(input("Valor a ser depositado: "))

        saldo += valor

        print("\nDepósito concluído.\n")
    
    elif opcao == 's':

        valor = float(input("Valor para o saque: "))
        
        if valor > LIMITE:

            print("não pode sacar valor acima de 500 $RS.")
        
        elif numero_saques == LIMITE_DIARIO:

            print("Erro: não pode sacar acima de 3 saques por dia.")
        
        else:
            saldo -= valor

            numero_saques += 1

            registro_saque += valor

            print("\nSaque concluído\n")
    
    elif opcao == 'e':

        extrato = f"""

        Saldo: {saldo:.2f}
        Saque: {registro_saque:.2f}

"""
        print(extrato)
    
    elif opcao == 'q':

        print("saindo do sistema...\n")
        break
    
    else:

        print("Botão errado para operação bancária.\n")
