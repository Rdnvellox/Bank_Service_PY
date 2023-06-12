limite_saques = 3
saque_valor = 500
saldo = 0
extrato = ''

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

# ----------------------------------------

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Quanto gostaria de depositar?"))

        if valor_deposito > 0:
            print("{} depósito em sua conta!".format(valor_deposito))
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

        else:
            print("Não foi possível depósitar esse valor, favor repita o processo.")

    elif opcao == "s":
        if limite_saques > 0:
            valor_saque = float(input("Quanto gostaria de sacar?"))

            if valor_saque <= 0:
                print("Informe um valor válido")

            elif valor_saque > saldo:
                print("Saldo insuficiente")

            elif valor_saque > saque_valor:
                print('O valor desejado é maior que o limite por saque.')

            else:
                print("Saque efetuado com sucesso.")
                saldo -= valor_saque
                limite_saques -= 1
                extrato += f"Saque: R$ {valor_saque:.2f}\n"

        else:
            print("Limite de saques diários excedido")

    elif opcao == "e":
        print("\n ============== EXTRATO ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================================")

    elif opcao == "q":
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
