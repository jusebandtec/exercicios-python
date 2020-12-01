num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))
if num1 > num2 and num1 > num3:
    print("O numero:",num1,"é maior")
elif num2 > num1 and num2 > num3:
    print("O numero:",num2,"é maior")
else:
    print("O numero:",num3,"é maior")

if num1 < num2 and num1 < num3:
    print("O numero:",num1,"é menor")
elif num2 < num1 and num2 < num3:
    print("O numero:",num2,"é menor")
else:
    print("O numero:",num3,"é menor")
