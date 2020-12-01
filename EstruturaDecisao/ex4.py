letra = input("Digite uma letra, vogal ou constante: ")
letra = letra.lower()
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("É vogal")
else:
    print("É consoante")