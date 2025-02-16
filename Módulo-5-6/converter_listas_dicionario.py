nomes=["joaquim","Maria","carlos"]
idades=[30,25,33]


#fazer um dicionario com os nomes como chave e as idades com valor
dicionario=dict(zip(nomes,idades))
print(dicionario)

for chave,valor in zip(nomes,idades):
    print(f"{chave} > {valor}")