menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
depositos_realizados = []
saques_realizados = []

while True:
    opcao = input(menu)

    if opcao == "d":
        print("============DEPÓSITO============")
        valor_deposito = float(input("Qual valor deseja depositar?\n "))
        if valor_deposito > 0:
            depositos_realizados.append(valor_deposito)
            saldo += valor_deposito
            print(f"Depósito realizado com sucesso!")
        else:
            print("Por favor insira valores positivos e maiores que 0 real.")


    elif opcao == "s":
        print("============SAQUE============")
        valor_saque = float(input("Qual valor deseja sacar?\n"))
        if valor_saque > saldo and valor_saque <= 500:
            print("Saldo insuficiente, tente novamente!")
        elif valor_saque > 500:
            print("Limite de saque foi excedido! Tente novamente respeitando o limite de saque.")
        elif numero_saques == LIMITE_SAQUES:
            print("Você atingiu o limite diário de saques, tente novamente mais tarde.")
        else:
            saques_realizados.append(valor_saque)
            numero_saques += 1
            saldo -= valor_saque
            print("Saque realizado com sucesso!")
      
  
    elif opcao == "e":
        print("============EXTRATO============")
        print(f"Seu saldo: R$ {saldo:.2f}")
        print("============DEPÓSITOS FEITOS============")
        for i in range(len(depositos_realizados)):
            print(f"{i}o. depósito R$ {depositos_realizados[i]:.2f}")        
        print("============SAQUES FEITOS============")
        for i in range(len(saques_realizados)):
            print(f"{i}o. saque R$ {saques_realizados[i]:.2f}")


    elif opcao == "q":
        break

    else:

        print("Operação, inválida, por favor  selecione novamente a operação desejada!")