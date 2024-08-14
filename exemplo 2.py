numero = int(input("Digite um numero menor que 100:"))
if numero >=100:
    print("O numero dever ser menor que 100.")
else:
    dezena = numero // 10
    unidade = numero % 10
    soma = dezena + unidade
    print("soma:",soma)
