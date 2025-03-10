"""
Listas por compreensão - criar uma lista com base num código que gera a lista a partir de outra lista ou uma função
geradora
"""
import random
lista_Carros=["ford","bmw","mercedes","renault","ferrari"]

#criar uma lista dos carros cuja a marca começa por f
"""listas_marcas_f=[]
for marca in lista_Carros:
    if marca[0] == "f":
        listas_marcas_f.append(marca)
"""
#Lista aplicando um filtro a lista das marcas
listas_marcas_f = [marca for  marca in lista_Carros if marca[0] == "f"]
print(listas_marcas_f)

#lsita de numeros sorteados
lista_numeros=[random.randint(1,100) for i in range(10)]
print(lista_numeros)
