#conversão de listas de dicionarios e o inverso
meu_dicionario={"nome": "Joaquim","idade":15,"morada":"Viseu"}

minha_lista=list(meu_dicionario.items())

print(minha_lista)
#converter duas listas num dicionario 
chaves = ["nome","idade","morada"]
valores=["Joaquim",15,"Viseu"]

dicionario=dict(zip(chaves,valores))
print(dicionario)