
def menu():
    menu = '''
    =-=-=-=-= MENU =-=-=-=-=
    [d]Depositar
    [s]Sacaropo
    [e]Extrato
    [q]Sair 
    ===> '''
    return input(menu)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t\tR$ {valor:.2f}\n"
        print(f"\nOperação realizada com sucesso! R$ {valor:.2f} depositado.")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, numero_saques, limite, limite_saques):
    if valor_saque <= 0:
        print("\nOperação falhou! O valor informado é inválido.")
    elif valor_saque > saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif valor_saque > limite:
        print(f"\nOperação falhou! O valor do saque excede o limite diário de R$ {limite:.2f}.")
    elif numero_saques >= limite_saques:
        print("\nOperação falhou! Você atingiu o limite de saques diários.")
    else:
        saldo -= valor_saque
        extrato += f"Saque:\t\t\tR$ {valor_saque:.2f}\n"
        numero_saques += 1
        print(f"\nOperação realizada com sucesso! Saque de R$ {valor_saque:.2f}.")

    return saldo, extrato, numero_saques


def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo:\t\t\tR$ {saldo:.2f}")
    print("==========================================")

def main():
    LIMITE_SAQUE = 500
    QUANTIDADE_SAQUE = 3
    saldo = 0
    extrato = ""
    numero_saques = 0

    while True:
             opcao = menu()
             if opcao == 'd':
                try:
                    valor = float(input('Digite o valor que deseja depositar: '))
                    saldo, extrato = deposito(saldo, valor, extrato)
                except ValueError:
                     print("\nOperação falhou! Valor inválido. Digite um número.")
             elif opcao == 's':
                 try:
                     valor = float(input('Informe o valor que deseja sacar: '))
                     saldo, extrato, numero_saques = sacar(
                        saldo=saldo,
                        valor_saque=valor,
                        extrato=extrato,
                        numero_saques=numero_saques,
                        limite=LIMITE_SAQUE,
                        limite_saques=QUANTIDADE_SAQUE
                     )
                 except ValueError:
                    print("\nOperação falhou! Valor inválido. Digite um número.")
             elif opcao == 'e':
                 extrato(saldo, extrato=extrato)
             elif opcao == 'q':
                 print('Transação finalizada! Até a próxima...')
                 break

             else:
                print("Operação inválida! Por favor, selecione uma opção válida.")


if __name__ == "__main__":
    main()