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

cliente = {}

conta_corrente = {}

saldo = 0

numero_saques = 0

extrato = """"""

conta = 0


while True:
    print(menu)
    opcao = input("\nEscolha sua opcao: ")

    if opcao == 'd':
        valor = float(input("Valor a ser depositado: "))
        saldo, extrato = bc.deposito(saldo, valor, extrato)
        print(saldo)
    
    elif opcao == 's':
        valor = float(input("Valor para o saque: "))
        saldo, numero_saques, extrato = bc.saque(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITE, numero_saques=numero_saques, limite_saques=LIMITE_DIARIO)
        print(saldo)
    
    elif opcao == 'e':
        extrato, saldo = bc.historico_bancario(extrato, saldo)
        print(extrato)
    
    elif opcao == 'cli':
        nome = input("Nome: ")
        nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        cliente, nome, nascimento, cpf, endereco = bc.criar_cliente(cliente, nome, nascimento, cpf, endereco)
        print(cliente)
    
    elif opcao == 'co':
        conta_corrente, cliente, conta, AGENCIA = bc.criar_conta_corrente(conta_corrente, cliente, conta, AGENCIA)
        print(conta_corrente)
    
    elif opcao == 'q':
        print("Saindo do sistema...\n")
        break
    
    else:
        print("Botão errado para operação bancária.\n")
