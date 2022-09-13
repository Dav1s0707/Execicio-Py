peso = int(input('qual o seu peso: '))
altura = int(input("qual a sua altura: "))

peso = peso * 10000

imc = peso / (altura**2)

print("seu IMC é {}".format(imc))

if imc < 18.5:
    print("Ta magro, fio")

elif imc >18.5 and imc < 25:
    print('ta bao')
elif imc > 25 and imc < 30:
    print('ta pesadinho')
elif imc >30 and imc < 40:
    print('ta pesado')
elif imc >40 :
    print('baleia')