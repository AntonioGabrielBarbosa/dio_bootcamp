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

saldo = 0

LIMITE = 500

LIMITE_DIARIO = 3

extrato = ""

numero_saques = 0

cliente = {}

conta_corrente = {}

AGENCIA = "0001"

conta = 0

while True:

    print(menu)

    opcao = input("\nEscolha sua opcao: ")

    if opcao == 'd':

        valor = float(input("Valor a ser depositado: "))

        deposito = bc.deposito(saldo, valor, extrato)

        print(deposito)
    
    elif opcao == 's':

        valor = float(input("Valor para o saque: "))

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

        novo_cliente = bc.criar_cliente(cliente, nome, nascimento, cpf, endereco)

        print(novo_cliente)
    
    elif opcao == 'co':

        conta += 1

        nova_conta_corrente = bc.criar_conta_corrente(conta_corrente, cliente, conta, AGENCIA)

        print(nova_conta_corrente)
    
    elif opcao == 'q':

        print("saindo do sistema...\n")
        break
    
    else:

        print("Botão errado para operação bancária.\n")