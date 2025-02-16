"""
Pretende-se um programa para calcular o total a pagar por uma lista de compras com base na informação armazenada nas estruturas de dados apresentadas no código, nomeadamente, as listas produtos, precos e quantidades e ainda o dicionário com as percentagens de desconto de cada produto.
"""
#produtos comprados
produtos = ['bananas','maçãs','laranjas']
#preços unitários
precos = [2.5, 3.5, 4.5]
#quantidades compradas
quantidades=[2, 3, 3]
compras={}



#TODO: criar um dicionário que combina os dados das listas produtos, precos e quantidades
for p in range(len(produtos)):
    compras[produtos[p]]={"quantidade":quantidades[p],"preco":precos[p]} # bananas{preco:2.5/quantidade:2} #mostrar um espaço específico print(compras["Laranjas"]["preco"])
print(compras)
#percentagens de desconto
descontos={
    'bananas': 0,
    'maçãs': 15,
    'laranjas': 20
}
#ler do utilizador as quantidades para o dicionário das compras
for p in compras:
    compras[p]["quantidade"]=float(input(f"Qual a quantidade de {p}:"))
#adicionar um produto novo introduzido pelo utilizador
nome=input("Qual o produto: ")
preco=float(input("Qual o preço: "))
quantidade=float(input("Qual a quantidade"))
desconto=float(input("Qual a percentagem do desconto"))
#adicionar o desconto ao dicionários de descontos
descontos[nome]=desconto
#adicionar ao dicionário das compras o produto
compras[nome]={"preco":preco,"quantidade":quantidade}



#TODO: calcular o valor total a pagar pelas compras tendo em conta as quantidades compradas e percentagem de desconto de cada produto
valor_com_deconto=0
total=0
for p in compras:
    valor_pagar=compras[p]["preco"]*compras[p]["quantidade"]
    desconto=(descontos[p]/100) * valor_pagar
    valor_com_deconto=valor_pagar-desconto
    total=total+valor_com_deconto

total=round(total,2)
print(f"Valor a pagar pelas compras é de {total}€")

    