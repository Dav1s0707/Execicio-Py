valorcasa = int(input('Qual o valor da casa: R$'))
salario = int(input("Qual o seu salario: R$"))
anos = int(input("Em quantos anos voce vai pagar: "))

mes = anos*12

prestação = valorcasa/mes

#print(mes)
#print(prestação)

salario30 = salario/100 *30

#print(salario30)
print('A prestação sera de {:.2f}'.format(prestação))

if prestação > salario30:
    print("Emprestimo negado")
else:
    print('Emprestimo aprovado')

