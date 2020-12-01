letra = input("Digite um sexo (F ou M): ")
if letra.upper() == "F":
    print(letra,"- Feminino")
elif letra.upper() == "M":
    print(letra,"- Masculino")
else:
    print("Sexo inválido")