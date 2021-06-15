def soma(num1,num2,num3):
    numeros = [int(num1),int(num2),int(num3)]
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

print(soma(input("Digite o primeiro número: "), input("Digite o segundo número: "), input("Digite o terceiro número: ")))
