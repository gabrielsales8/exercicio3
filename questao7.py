class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.saude = 50
        self.idade = 0

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, novo_valor):
        self.fome = novo_valor

    def alterar_saude(self, novo_valor):
        self.saude = novo_valor

    def alterar_idade(self, novo_valor):
        self.idade = novo_valor

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def calcular_humor(self):
        humor = (self.fome + self.saude) / 2
        return humor

def main():
    nome = input("Informe o nome do Bichinho Virtual: ")
    bichinho = BichinhoVirtual(nome)

    while True:
        print("\n=== Bichinho Virtual ===")
        print("1. Alimentar")
        print("2. Cuidar da Saúde")
        print("3. Envelhecer")
        print("4. Mostrar Status")
        print("5. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            bichinho.alterar_fome(bichinho.retornar_fome() - 10)
        elif opcao == 2:
            bichinho.alterar_saude(bichinho.retornar_saude() + 10)
        elif opcao == 3:
            bichinho.alterar_idade(bichinho.retornar_idade() + 1)
        elif opcao == 4:
            print(f"\nNome: {bichinho.retornar_nome()}")
            print(f"Fome: {bichinho.retornar_fome()}")
            print(f"Saúde: {bichinho.retornar_saude()}")
            print(f"Idade: {bichinho.retornar_idade()}")
            print(f"Humor: {bichinho.calcular_humor()}")
        elif opcao == 5:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
