from datetime import datetime

def depositar(conta: dict, valor: float):

    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f} as {datetime.today()}")
        return(f"Operação depósito conclúido com sucesso! R$ {valor}")

    else:
        return("Operação falhou! O valor informado é inválido.")

def sacar(conta, valor: float):
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["numero_saques"] >= conta["LIMITE_SAQUES"]

    if excedeu_saldo:
        return("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        return("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        return("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"].append(f"Saque: R$ {valor:.2f} as {datetime.today()}")
        conta["numero_saques"] += 1
        return(f"Operação saque conclúido com sucesso! R$ -{valor}")

    else:
        return("Operação falhou! O valor informado é inválido.")

def extrato(conta):
    return conta["extrato"]

def menu(conta: dict):
    while True:
        opcao = input("""

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            print(depositar(conta=conta, valor=valor))
            
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            print(sacar(conta=conta, valor=valor))

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            lista_extrato = extrato(conta=conta)
            if len(lista_extrato) == 0:
                print("Não foram realizadas movimentações.")
            else:
                for movimentacao in lista_extrato:
                    print(movimentacao)
            print("==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__=='__main__':
    conta = {
        "LIMITE_SAQUES":3,
        "saldo":0,
        "limite":500,
        "extrato":[],
        "numero_saques":0
    }

    menu(conta)