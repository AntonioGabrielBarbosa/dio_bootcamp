import banco_funcoes as bc



menu = """

    SISTEMA DE BANCO SIMPLES

    [d] - depósito
    [s] - saque
    [e] - extrato
    [cli] - criar cliente
    [co] - criar conta corrente
    [q] - sair

"""


LIMITE = 500

LIMITE_DIARIO = 3

AGENCIA = "0001"



while True:

    print(menu)

    opcao = input("\nEscolha sua opcao: ")

    if opcao == 'd':

        valor = float(input("Valor a ser depositado: "))

        saldo = 0

        extrato = ""

        deposito = bc.deposito(saldo, valor, extrato)

        print(deposito)
    
    elif opcao == 's':

        valor = float(input("Valor para o saque: "))

        numero_saques = 0

        saque = bc.saque(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITE, numero_saques=numero_saques, limite_saques=LIMITE_DIARIO)

        print(saque)
    
    elif opcao == 'e':

        historico = bc.historico_bancario(extrato=extrato, saldo=saldo)

        print(historico)
    
    elif opcao == 'cli':

        nome = input("Nome: ")

        nascimento = input("data de nascimento: ")

        cpf = input("CPF: ")

        endereco = input("endereço: ")

        cliente = {}

        novo_cliente = bc.criar_cliente(cliente, nome, nascimento, cpf, endereco)

        print(novo_cliente)
    
    elif opcao == 'co':

        conta = 0

        conta += 1

        conta_corrente = {}

        nova_conta_corrente = bc.criar_conta_corrente(conta_corrente, cliente, conta, AGENCIA)

        print(nova_conta_corrente)
    
    elif opcao == 'q':

        print("saindo do sistema...\n")
        break
    
    else:

        print("Botão errado para operação bancária.\n")
