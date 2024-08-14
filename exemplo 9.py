continua = True
while continua:
    n = int(input("Digite um numero:"))
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
    resposta=input("Deseja continuar (s/n)?")
    if resposta=="n":
        continua=false
