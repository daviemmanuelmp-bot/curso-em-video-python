b1 = float(input('Largura da parede: '))
h1 = float(input('Altura da parede: '))
print('Sua parede tem dimensão de {}x{} e sua área é de {:.2f}m².'.format(b1, h1, (b1 * h1)))
print('Para pintar essa parede, você precisa de {:.2f}l de tinta!'.format((b1 * h1) / 10))
