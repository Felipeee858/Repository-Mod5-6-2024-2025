#definir um dicionario utilizamos{chaves: valor}

dicionario={"nome" : "Joaquim"}

print(dicionario["nome"])

#alterar o valor de uma chave
dicionario["nome"] = input("Introduza um nome:")
print(dicionario["nome"])

#chaves e valores podem ser string ou números
dicionario["idade"]=10
#adicionar novas chaves:valores = "blabla" valores
dicionario[10] = "blabla"
print(dicionario)

#fazer um ciclo para percorrer os pares chaves: valores
chaves=dicionario.keys() #devolve uma lista com as chaves
valores=dicionario.values() #devole uma lista com os valores
elementos=dicionario.items() #devolve uma lista com os pares chaves:valores
print(chaves,valores)
for chave in dicionario.keys():
    print(dicionario[chave])
#ciclo percorre os items do dicionario (chave:valor)
for pares in dicionario.items():
    print(f"{pares[0]} : {pares[1]}")

#remover chaves valores do dicionario
valor = dicionario.pop("Idade",None)
print(f"Idade (removida) {valor}") #segunda vez devolve None porque a chave já não existe
#remover a chave indicada entre[]
del dicionario ["nome"]
print(dicionario)
    
