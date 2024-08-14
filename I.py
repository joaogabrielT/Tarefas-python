import random
x = int(random.randint(0,5))
n = int(input('tente adivinhar qual numero foi sorteado:'))
if n == x:
    print(' voce acertou!!!!')
else:
    print('voce errou')

print('numero = {}'.format(x))
