preco = int(input("qual o preço do produto: R$"))
pagamento = int(input("""Qual a forma de pagamento:
Digite 1 para dinheiro/cheque
Digite 2 para 1x no cartão
Digite 3 para 2x no cartão
Digite 4 para 3x ou mais no cartão
"""))

if pagamento == 1:
    mudanca = preco/10
    preco = preco - mudanca
    print('preço {}'.format(preco))

elif pagamento == 2:
    mudanca = preco / 20
    preco = preco - mudanca
    print('preço {}'.format(preco))

elif pagamento == 3:
    print('preço {}'.format(preco))

elif pagamento == 4:
    mudanca = preco / 100 *20
    preco = preco + mudanca
    print('preço {}'.format(preco))