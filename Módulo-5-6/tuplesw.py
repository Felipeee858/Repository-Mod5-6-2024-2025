vencimentos=(1000,5000,2500,1350,4750,850)
nomes=("A","B","C","D","E","F")

#utilizando uma função~

def Função(vencimentos):
    """calcular e devolver a soma de todos os vencimentos, o maior e o menor"""
    Soma=sum(vencimentos)
    Maior=max(vencimentos)
    menor=min(vencimentos)
    
    return Soma,Maior,menor
Função(vencimentos)
#calcular e mostrar a média dos vencimentos
Media=Soma/len(vencimentos)

print(Media)
#mostrar o nome que tem o maior vencimento
posicao=vencimentos.index(Maior)
print(nomes[posicao])