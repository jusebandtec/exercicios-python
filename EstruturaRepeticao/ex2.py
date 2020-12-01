import time

usuario = input("Digite um nome de usuario:\n")
senha = input("Digite uma senha:\n")
while usuario == senha:
    time.sleep(1)
    print("Usuario e senha iguais. Tente novamente.")
    time.sleep(0.5)
    usuario = input("Digite um nome de usuario:\n")
    senha = input("Digite uma senha:\n")
