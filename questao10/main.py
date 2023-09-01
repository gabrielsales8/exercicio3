from questão10 import *

def main():
    tipo_combustivel = input("Informe o tipo de combustível: ")
    valor_litro = float(input("Informe o valor por litro: "))
    quantidade_combustivel = float(input("Informe a quantidade de combustível: "))

    bomba = BombaCombustivel(tipo_combustivel, valor_litro, quantidade_combustivel)

    while True:
        print("\n=== Menu ===")
        print("1. Abastecer por Valor")
        print("2. Abastecer por Litro")
        print("3. Alterar Valor por Litro")
        print("4. Alterar Tipo de Combustível")
        print("5. Alterar Quantidade de Combustível")
        print("6. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            valor_abastecido = float(input("Informe o valor a ser abastecido: "))
            litros_abastecidos = bomba.abastecer_por_valor(valor_abastecido)
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros.")

        elif opcao == 2:
            litros_abastecidos = float(input("Informe a quantidade de litros a ser abastecida: "))
            valor_pagar = bomba.abastecer_por_litro(litros_abastecidos)
            print(f"O valor a ser pago é R${valor_pagar:.2f}")

        elif opcao == 3:
            novo_valor_litro = float(input("Informe o novo valor por litro: "))
            bomba.alterar_valor(novo_valor_litro)
            print("Valor por litro alterado com sucesso!")

        elif opcao == 4:
            novo_tipo_combustivel = input("Informe o novo tipo de combustível: ")
            bomba.alterar_combustivel(novo_tipo_combustivel)
            print("Tipo de combustível alterado com sucesso!")

        elif opcao == 5:
            nova_quantidade_combustivel = float(input("Informe a nova quantidade de combustível: "))
            bomba.alterar_quantidade_combustivel(nova_quantidade_combustivel)
            print("Quantidade de combustível alterada com sucesso!")

        elif opcao == 6:
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
