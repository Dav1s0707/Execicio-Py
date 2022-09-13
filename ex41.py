import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
ano = (int(date.strftime("%Y")))
print(f"Ano atual -> {ano}")

#pegando o ano de nascimento
nasc = int(input("qual o seu ano de nascimento: "))

#calculando a idade
idade = ano - nasc
print('sua idade é {}'.format(idade))

if idade <=  9:
    print("voce é  MIRIM")

elif idade <= 14:
    print("Voce é INFATIL")

elif idade <= 19:
    print("Voce é JUNIOR")

elif idade <= 25:
    print("Voce é SÊNIOR")

else:
    print("voce é MASTER")