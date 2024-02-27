from datetime import datetime

saldo = 0
extratos = {
    "depositos": [],
    "saques": [],
}

while True:
    print("\n1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito

            dt = datetime.now()
            extratos["depositos"].append({
                'valor': valor_deposito,
                'data': dt.strftime('%d/%m/%Y'),
                'hora': dt.strftime('%H-%M-%S'),
            })

            print(f'Depósito de R${valor_deposito:.2f} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    elif opcao == '2':
        valor_saque = float(input("Digite o valor do saque: "))
        # -----------------------------------------
        # Desenvolva a lógica da validação do saldo
        # -----------------------------------------
        dt = datetime.now()
        extratos["saques"].append({
            'valor': valor_saque,
            'data': dt.strftime('%d/%m/%Y'),
            'hora': dt.strftime('%H-%M-%S'),
        })

    elif opcao == '3':
        print(f'\nExtrato bancário:')

        print("Saques".center(20, '-'))
        for saque in extratos["saques"]:
            print()
            print(saque["valor"])
            print(saque["data"])
            print(saque["hora"])
            print()

        print("Depositos".center(20, '-'))
        for deposito in extratos["depositos"]:
            print()
            print('Valor do Depósito:',deposito["valor"])
            print('Data do Depósito:',deposito["data"])
            print('Hora do Depósito:',deposito["hora"])
            print()

        print('-' * 20, '\n',f'Saldo atual: R${saldo:.2f}')

    elif opcao == '4':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
