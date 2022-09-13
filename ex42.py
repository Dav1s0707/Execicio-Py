reta1 = float(input("Medida da reta 1: "))
reta2 = float(input("Medida da reta 2: "))
reta3 = float(input("Medida da reta 3: "))

if reta1 + reta2 > reta3 and reta3 + reta2 > reta1 or reta1 + reta3 > reta2:
    print("Esse triangulo existe")

    if reta1 == reta2 == reta3:
        print("Esse triangulo é Equilatero")
    elif reta3 == reta2 or reta2 == reta1 or reta1 == reta3:
        print("Esse triangulo é Isoceles")
    else:
        print("Esse triangulo é Escaleno")

else:
    print('Esse triangulo não existe')
