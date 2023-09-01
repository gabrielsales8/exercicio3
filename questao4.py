class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.altura += anos * 0.5

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura:.2f} cm")

def main():
    nome = input("Informe o nome da pessoa: ")
    idade = int(input("Informe a idade da pessoa: "))
    peso = float(input("Informe o peso da pessoa (kg): "))
    altura = float(input("Informe a altura da pessoa (cm): "))

    pessoa = Pessoa(nome, idade, peso, altura)

    anos_passados = int(input("Informe quantos anos se passaram: "))
    pessoa.envelhecer(anos_passados)

    peso_ganho = float(input("Informe quantos quilos a pessoa engordou: "))
    pessoa.engordar(peso_ganho)

    peso_perdido = float(input("Informe quantos quilos a pessoa emagreceu: "))
    pessoa.emagrecer(peso_perdido)

    altura_crescida = float(input("Informe quantos centímetros a pessoa cresceu: "))
    pessoa.crescer(altura_crescida)

    pessoa.mostrar_informacoes()

if __name__ == "__main__":
    main()
