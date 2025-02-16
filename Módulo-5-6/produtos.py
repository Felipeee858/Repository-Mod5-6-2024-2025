"""Referências entre dicionários e dicionários com arrays"""

marca1={"nome":"nike","tipo":"calçado","pais":"americano"}
marca2={"nome":"adidas","tipo":"roupa e calçado","pais":"alemão"}
marca3={"nome":"mimosa","tipo":"leite","pais":"português"}

produto1={"nome":"sapatilhas","preco":85.45,"marca":marca2}

#mostrar o país da marca
print(produto1["marca"]["pais"])
print(produto1)
produto2={"nome":"casaco","preco":100,"marca":marca2}
marca2={} #cria um dicionario novo mas a informação dos produto1 e 2 continua a ser referenciada
print(produto1)
print(produto2)
