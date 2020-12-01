numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
# for numero1 in range(numero2):
#     print(numero1 + 1)
while numero1 < numero2:
    if numero1 > numero2:
        print(numero2)
        numero2 -=1
    numero1+=1