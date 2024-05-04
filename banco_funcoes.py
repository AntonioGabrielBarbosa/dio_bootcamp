

def saque (*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > limite:

        print(f"Saque maior que o limite de {valor:.2f} $RS.")
    
    elif numero_saques == limite_saques:

        print("Números de saques excederam o limite de saques.")
    
    saldo -= valor

    numero_saques += 1

    extrato = f"""
        SALDO: {saldo:.2f} $RS
"""

    return extrato

def deposito(saldo, valor, extrato, /):

    if valor < 0:

        print("Valores negativos não são permitidos.")
    
    saldo += valor

    extrato =  f"""
        SALDO = {saldo:.2f} $RS
    """

    return extrato

def criar_cliente(cliente, nome, nascimento, cpf, endereco):

    cliente = {"nome": nome, "nascimento" : nascimento, "CPF": cpf, "endereço": endereco}

    for chave, valor in cliente.items():

        print(chave, valor)
    
    return "Cliente foi criado."

def criar_conta_corrente(corrente, usuario, conta, agencia):

    corrente = {"Usuário": usuario, "Conta": conta, "Agência": agencia}

    for chave, valor in corrente.items():

        print(chave, valor)
    
    return "Conta corrente criada."

def historico_bancario(extrato, saldo):

    
    extrato = f"""
        SALDO: {saldo:.2f} $RS
"""
    
    return extrato