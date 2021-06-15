class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostra_cor(self):
        print(self.cor)

    def troca_cor(self, cor_nova):
        self.cor = cor_nova

bola = Bola("Azul", 68, "Couro")
bola.mostra_cor()
bola.troca_cor("Branca")
bola.mostra_cor()
