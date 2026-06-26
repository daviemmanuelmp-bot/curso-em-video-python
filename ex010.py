n1 = float(input('Quantos reais você têm na carteira? R$'))
print('Com R${:.2f} você pode comprar US${:.2f} ou €${:.2f}!'.format(n1, (n1 / 5.15), (n1 / 5.97)))
