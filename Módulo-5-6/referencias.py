dicionario1={"a":1,"b":2}
dicionario2={"c":2,"d":3}
#esta linha não faz uma cópia do dicionario
#as duas variaveis dicionario2 e dicionario3 apontam para a mesma
#memória (partilha os mesmos dados)
dicionario3=dicionario2
dicionario3["e"]=4
print(dicionario2)
#E SE EU QUISER FAZER UMA CÓPIA DE UM DICIONÁRIO?
#dicionario4={}
#for chave,valor in dicionario1.items():
#    dicionario4[chave]=valor
dicionario4=dicionario1.copy()
dicionario4["z"]=10
print(dicionario1)
