nome = str(input("Qual seu nome: "))

if nome == 'rato':
    print("rato sexo")
elif nome == 'matue':
    print('comedor de prima')
elif nome in "pedro tue paulo":
    print('isso não é um nome')
else:
    print('voce é broxa')

print("Tenha um otimo, dia {}".format(nome))