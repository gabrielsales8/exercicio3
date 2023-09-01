class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto: ({self.x}, {self.y})")

class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrar_centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)

def main():
    retangulos = []

    while True:
        print("\n=== Menu ===")
        print("1. Criar Retângulo")
        print("2. Imprimir Centros")
        print("3. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            x = float(input("Informe o valor de x do ponto inicial: "))
            y = float(input("Informe o valor de y do ponto inicial: "))
            largura = float(input("Informe a largura do retângulo: "))
            altura = float(input("Informe a altura do retângulo: "))

            ponto_inicial = Ponto(x, y)
            retangulo = Retangulo(ponto_inicial, largura, altura)
            retangulos.append(retangulo)

            print("Retângulo criado com sucesso!")

        elif opcao == 2:
            for i, retangulo in enumerate(retangulos, start=1):
                centro = retangulo.encontrar_centro()
                print(f"Centro do Retângulo {i}:")
                centro.imprimir()

        elif opcao == 3:
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
