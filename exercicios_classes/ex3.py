class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudar_valor_dos_lados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def retornar_valor_lados(self):
        return [self.base, self.altura]

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (self.base*2) + (self.altura*2)

    