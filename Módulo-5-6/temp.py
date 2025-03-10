numeros=[]
estrelas=[]
def Sortear(numeros,quantos,maximo):
    while len(numeros)!=quantos:
        n = random.randint(1,maximo)
        if n not in numeros:
            numeros.append(n)
            
    numeros.sort()



Sortear(numeros,5,50)
Sortear(estrelas,2,12)
print(numeros)
print(estrelas)