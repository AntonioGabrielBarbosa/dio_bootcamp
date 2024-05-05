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

# Defina as variáveis fora do loop while
cliente = {}
conta_corrente = {}
saldo = 0
extrato = ""
numero_saques = 0

while True:
    print(menu)
    opcao = input("\nEscolha sua opcao: ")

    if opcao == 'd':
        valor = float(input("Valor a ser depositado: "))
        print(f"Depósito realizado. Seu saldo atual é {bc.deposito(saldo, valor, extrato)}.")
    
    elif opcao == 's':
        valor = float(input("Valor para o saque: "))
        print(f"Saque realizado. Seu saldo atual é {bc.saque(saldo=saldo, valor=valor, extrato=extrato, limite=LIMITE, numero_saques=numero_saques, limite_saques=LIMITE_DIARIO)}.")
    
    elif opcao == 'e':
        print(bc.historico_bancario(extrato=extrato, saldo=saldo))
    
    elif opcao == 'cli':
        nome = input("Nome: ")
        nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        print(f"Cliente {bc.criar_cliente(cliente, nome, nascimento, cpf, endereco)} criado com sucesso.")
    
    elif opcao == 'co':
        conta = 0
        conta += 1
        print(f"Conta corrente {bc.criar_conta_corrente(conta_corrente, cliente, conta, AGENCIA)} criada com sucesso.")
    
    elif opcao == 'q':
        print("Saindo do sistema...\n")
        break
    
    else:
        print("Botão errado para operação bancária.\n")
