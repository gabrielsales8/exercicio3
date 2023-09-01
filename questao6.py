class TV:
    def __init__(self):
        self.canal_atual = 1
        self.volume = 50

    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal_atual = novo_canal
            print(f"Canal alterado para {self.canal_atual}")
        else:
            print("Canal inválido.")

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}")
        else:
            print("Volume máximo atingido.")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}")
        else:
            print("Volume mínimo atingido.")

    def mostrar_status(self):
        print(f"Canal atual: {self.canal_atual}")
        print(f"Volume: {self.volume}")

def main():
    tv = TV()

    while True:
        print("\n=== Controle Remoto da TV ===")
        print("1. Mudar Canal")
        print("2. Aumentar Volume")
        print("3. Diminuir Volume")
        print("4. Mostrar Status")
        print("5. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            novo_canal = int(input("Informe o número do novo canal: "))
            tv.mudar_canal(novo_canal)
        elif opcao == 2:
            tv.aumentar_volume()
        elif opcao == 3:
            tv.diminuir_volume()
        elif opcao == 4:
            tv.mostrar_status()
        elif opcao == 5:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
