num1 = int(input("numero1:  "))
num2 = int(input("numero2':  "))

cor={'limpa':'\033[m',
     'azul':'\033[36m',
     'roxo':'\033[35m'}

if  num1 > num2:
    print("o primeiro numero  é maior")
    print("{}{}{} > {}{}{}".format(cor['azul'],num1,cor['limpa'],
                                                              cor['roxo'],num2,cor['limpa']))

elif num2> num1:
    print('o segundo  numero é maior')
    print("{}{}{} < {}{}{}".format(cor['azul'],num1,cor['limpa'],
                                                              cor['roxo'],num2,cor['limpa']))
else:
    print("os numeros são iguais")
    print("{}{}{} = {}{}{}".format(cor['azul'],num1,cor['limpa'],
                                                              cor['roxo'],num2,cor['limpa']))
