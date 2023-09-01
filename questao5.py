class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor inválido para depósito.")

    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def mostrar_informacoes(self):
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Nome do Correntista: {self.nome_correntista}")
        print(f"Saldo: R${self.saldo:.2f}")

def main():
    numero_conta = input("Informe o número da conta: ")
    nome_correntista = input("Informe o nome do correntista: ")
    saldo_inicial = float(input("Informe o saldo inicial (opcional, pressione Enter para usar zero): ") or 0)

    conta = ContaCorrente(numero_conta, nome_correntista, saldo_inicial)

    print("\nConta criada:")
    conta.mostrar_informacoes()

    valor_deposito = float(input("\nInforme o valor para depósito: "))
    conta.deposito(valor_deposito)

    valor_saque = float(input("\nInforme o valor para saque: "))
    conta.saque(valor_saque)

    novo_nome = input("\nInforme o novo nome do correntista: ")
    conta.alterar_nome(novo_nome)

    print("\nConta após as operações:")
    conta.mostrar_informacoes()

if __name__ == "__main__":
    main()
