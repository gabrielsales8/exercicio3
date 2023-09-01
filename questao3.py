class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornar_lados(self):
        return self.lado_a, self.lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b

    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)

def main():
    lado_a = float(input("Informe o comprimento do local: "))
    lado_b = float(input("Informe a largura do local: "))
    piso_area = float(input("Informe a área de um piso: "))
    rodape_comprimento = float(input("Informe o comprimento de um rodapé: "))
    
    retangulo = Retangulo(lado_a, lado_b)
    area_local = retangulo.calcular_area()
    perimetro_local = retangulo.calcular_perimetro()
    
    quantidade_pisos = area_local / piso_area
    quantidade_rodapes = 2 * (lado_a + lado_b) / rodape_comprimento
    
    print(f"Área do local: {area_local} m²")
    print(f"Perímetro do local: {perimetro_local} m")
    print(f"Quantidade de pisos necessários: {quantidade_pisos:.2f}")
    print(f"Quantidade de rodapés necessários: {quantidade_rodapes:.2f}")

if __name__ == "__main__":
    main()
