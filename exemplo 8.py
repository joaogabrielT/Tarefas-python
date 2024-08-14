n = int(input("Digite o numero"))
print ("Sequencia de Fibonacci")
fib1=0
fib2=1
print (fib1,end=" ")
print (fib2,end=" ")
for i in range(2,n):
    fib = fib1+fib2
    fib1=fib2
    fib2=fib
    print(fib,end=" ")
