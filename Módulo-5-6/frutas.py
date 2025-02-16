frutas={}

for i in range(3):
    nomes=input("Introduza os nomes das frutas: ")
    quant=int(input("Introduza a quantidade: "))
    frutas[nomes]=quant #para colocar a informação no dicionario

gosto=input("Qual a fruta que não gosta? ")
if gosto in frutas:
    del frutas[gosto] #del deleta uma chave do dicionario
else:
    print("Essa fruta não existe no dicionário")

#listar frutas do dicionário
for chave,valor in frutas.items():
    print(f"{chave} -> {valor}")

#mostrar o nome da fruta com a maior quantidade
maior=0
maior_fruta=""
for chave,valor in frutas.items():
    if valor>maior:
        maior=valor
        maior_fruta=chave
    
print(f"A fruta com maior quantidade é {maior_fruta} com {maior}")
