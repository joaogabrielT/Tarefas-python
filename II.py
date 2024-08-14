velocidade = float(input('qual sua velocidade?'))
if velocidade <= 80:
    print('ok, sem problemas:')
elif velocidade >80:
    print('voce sera multado!!!')
    qtdemulta = velocidade - 80.0
    valormulta = 7.0 * qtdemulta
    print('voce pagara R${:.2f}'.format(valormulta))
print('fim do programa')