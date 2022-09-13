#pegando o ano atual
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
tempo = idade - 18

#if else
if idade < 18:
    print('Voce é muito novo pra carpinar um lote')
    tempo = tempo * -1
    if tempo == 1:
        print('Volte daqui a {} ano'.format(tempo))
    else:
        print('Volte daqui a {} anos'.format(tempo))

elif idade > 18:
    print("Voce ja carpinou  um lote")
    if tempo == 1:
        print('Voce carpinou lotes ha {} ano'.format(tempo))
    else:
        print('Voce carpinou lotes ha {} anos'.format(tempo))

else:
    print('Vai carpinar um lote')
