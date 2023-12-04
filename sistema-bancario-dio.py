print("""
            Bem Vindo ao Seu Banco
      """)

print("""
      Escolha qual operação deseja executar:
      
      
(s) Sacar
(d) Depositar
(e) Extrato)
(x) Sair
      """)


limite_por_saque = 500
saldo = 0
extrato = ""
saques_no_dia = 0
QTD_SAQUE = 3

while True:

    operacao = input("\nSelecione a operação: ")

    if operacao == "x":
        
        print("Você Saiu do Sistema.")
        break

    if operacao == "d":

        valor_deposito = float(input("Digite qual valor quer depositar: "))
        
        if valor_deposito > 0:
            
            saldo += valor_deposito
            print(f"Você depositou R$ {valor_deposito:.2f} com sucesso.\n")
            extrato += f"Depósito: R$ {valor_deposito:.2f};\n"
            print(f"Seu saldo atual é de {saldo:.2f}.\n")
        else:
            print("Falha na operação, o valor informado é inválido")
    
    elif operacao == "e":

        print("""==========EXTRATO==========""")
        print("Não foram encotradas Movimentações na sua conta.\n" if not extrato else extrato)
        print(f"Saldo Atual: R$ {saldo:.2f}.\n")
        print("""#####################################\n""")

    elif operacao == "s":

        valor = float(input("Qual valor deseja Sacar: "))

        sem_saldo = valor > saldo
        sem_saque_diario = saques_no_dia >= QTD_SAQUE
        limite_maior_saque = valor > limite_por_saque

        if sem_saldo:
            print("Você não tem saldo suficiente para realizar esta operação.")

        elif sem_saque_diario:
            print("Você ja realizou 3 saques hoje, retorne amanhã para realizar esta operação.")

        elif limite_maior_saque:
            print("Voçê pode sacar no máximo R$ 500.00 reais por vez. Tente novamente.")

        elif valor > 0:

            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f};\n"
            saques_no_dia += 1

        else:
            print("Operação Negada. Digite um valor válido.")

