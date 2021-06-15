from ex3 import Retangulo

base_retangulo = float(input("Digite o tamanho da base: "))
altura = float(input("Digite o tamanho da altura: "))
retangulo = Retangulo(base_retangulo, altura)
print(retangulo.calcular_area())
print(retangulo.retornar_valor_lados())
print(retangulo.calcular_perimetro())
rodapes = int(retangulo.calcular_perimetro() / 0.15)
print(f"Você deverá comprar {rodapes} rodapés para concluir a casa")
pisos = int(retangulo.calcular_area() / 0.6)
print(f"Você deverá comprar {pisos} pisos para concluir a casa")