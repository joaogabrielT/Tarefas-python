#Produtos em estoque
estoque = {
    "tomate": [1000, 2.30],
    "alface": [500, 0.45],
    "batata": [2001, 1.20],
    "feijão": [100, 1.50],
}

total = 0

print("Vendas:\n")
#Comando para selecionar o produto para a compra
while True:
    produto = input("Nome do produto (fim para sair): ")
#Comando para finalizar a compra
    if produto == "fim":
        break
    if produto in estoque:
#Comando para selecionar a quantidade para a compra
        quantidade = int(input("Quantidade: "))
        if quantidade <= estoque[produto][0]:
            preço = estoque[produto][1]
            custo = preço * quantidade
#Comando para calcular o preço da compra
            print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
#Comando caso a quantidade solicitada ultrapasse o estoque
            print("Quantidade solicitada não disponível")
    else:
#Comando caso o nome do produto esteja errado
        print("Nome de produto inválido")
#Comando para mostrar o custo da compra
print(f"\nCusto total: {total:21.2f}\n")
#Comando para mostrar todo o estoque e o preço
print("Estoque:\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
