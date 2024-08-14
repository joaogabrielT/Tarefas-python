import math
num = int(input('Digite um numero:'))
raizquadrada= math.sqrt(num)
print('Raiz de {} e = {}'. format(num, raizquadrada))
print('Raiz de {} arredondada para proximo inteiro é {}'.format(num, math.ceil(raizquadrada)))
