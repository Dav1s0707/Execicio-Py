num = int(input("qual o numero escolhido: "))
conv = int(input("""Qual a converção:
Digite 1 para Binario
Digite 2 para Octal
Digite 3 para Hexadecimal
"""))

if conv == 1:
    binario =bin(num)
    print(binario[2:])

elif conv == 2:
    octal = oct(num)
    print(octal[2:])

elif conv == 3:
    hexa = hex(num)
    print(hexa[2:])
else:
    print("Tu degitou o numero errado")