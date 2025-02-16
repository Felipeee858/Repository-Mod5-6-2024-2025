"""Calcular quantos carros de cada marca existem num array guardando num dicionário
e nº de carros
ex:
{"bmw":2,
"tesla":2
"peugeot":1,
...}
"""
import numpy as np


carros=np.array(["bmw","tesla","peugeot","ford","tesla","mercedes","bmw","volvo"])
marcas={}


for carro in carros:
    #verificar se a marca já existe no dicionario
    if carro in marcas:
        marcas[carro]=marcas.get(carro,0)+1

    else:
        marcas[carro]=1

print(marcas)