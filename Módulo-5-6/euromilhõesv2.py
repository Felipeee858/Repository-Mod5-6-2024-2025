import random

numeros=[*range(1,51)]

for i in range(5):
    x=random.choice(numeros)
    numeros.remove(x)
    print(x)

