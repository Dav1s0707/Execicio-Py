nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

print('Sua media foi: {}'.format(media))
if media <= 5:
    print("Rebrovado, burro")

if media > 5 and  media <= 6.9:
    print("Da pra amelhorar")

if media >= 7:
    print("fez o minimo")