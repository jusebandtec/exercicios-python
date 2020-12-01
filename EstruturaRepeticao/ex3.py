while True:
    while True:
        nome = input("Digite um nome com mais de 3 caracteres:\n")
        if len(nome) > 3:
            break
    while True:
        idade = int(input("Digite uma idade entre 0 e 150:\n"))
        if idade >= 0 and idade <= 150:
            break
    while True:
        salario = float(input("Digite um salario maior que 0:\n"))
        if salario >= 0:
            break
    while True:
        sexo = input("Digite seu sexo [F ou M]:\n")
        if sexo.upper() == "M" or sexo.upper() == "F":
            break
    while True:
        estadoCivil = input("Digite seu estado civil [S, C, V ou D]:\n")
        if estadoCivil.upper() == "S" or estadoCivil.upper() == "C" or estadoCivil.upper() == "V" or estadoCivil.upper() == "D":
            break
    break

print("\n\nNome: {}\nIdade: {}\nSalario: {}\nSexo: {}\nEstado Civil: {}".format(nome,idade,salario,sexo,estadoCivil))