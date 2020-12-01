num1 = float(input("Digite o preço do primeiro produto: "))
num2 = float(input("Digite o preço do segundo produto: "))
num3 = float(input("Digite o preço do terceiro produto: "))
if num1 > num2 and num1 > num3:
    print("Compre o primeiro produto")
elif num2 > num1 and num2 > num3:
    print("Compre o segundo produto")
else:
    print("Compre o terceiro produto")