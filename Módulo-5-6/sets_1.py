"""
Sets(conjuntos)
Únicos(os elementos repetidos são descartados), não ordenados(não têm uma ordem fixa), mutáveis (adicionar,remover), elementos imutáveis
(bool, int, float, string)
"""
#Definir
nomes_1={"maria","joão"}
nomes_2={"joão","joaquim","carlos"}
nomes_3={"joão","maria"}

#igualdade
if nomes_1==nomes_3: #iguais porque a ordem dos elementos não conta
    print("São Iguais")
else:
    print("São Diferentes")


#União
nomes=nomes_1.union(nomes_2)#faz a união e devolve sem alterar
print("União: ",nomes)
nomes_v2=nomes_1|nomes_2 #faz a união e devolve sem alterar
print("União: ",nomes_v2)
nomes_1.update(nomes_2) #faz a união e altera
print("União: ",nomes_1)

#Interseção comum aos dois
nomes_iguais=nomes_3.intersection(nomes_2)#devolve a interseção sem alterar
print("Interseção: ",nomes_iguais)
nomes_iguais_v2=nomes_3 & nomes_2 #devolve a interseção sem alterar
print("Interseção: ",nomes_iguais_v2)
nomes_1.intersection_update(nomes_3)#faz a interseção alterando
print("Interseção: ",nomes_1)

#Diferença (mostra os repetidos dos conjuntos dependo da ordem com for usada) devolve os que não existem
diferenca=nomes_3.difference(nomes_2) # devolve o que não existe no que esta FORA de parenteses
print(f"{nomes_2} - {nomes_3} => Diferença: ",diferenca)
diferenca=nomes_2 - nomes_3
print(f"{nomes_2} - {nomes_3} => Diferença: ",diferenca)

#diferença simétrica (mostra os repetidos dos conjuntos de ambos)
diferenca_simetrica=nomes_3.symmetric_difference(nomes_2)
print(f"{nomes_2}-{nomes_3}=> Diferença simétrica: ",
diferenca_simetrica)
diferenca_simetrica=nomes_2.symmetric_difference(nomes_3)
print(f"{nomes_3}-{nomes_2}=> Diferença simétrica: ",
diferenca_simetrica)
diferenca_simetrica=nomes_2^nomes_3
print(f"{nomes_3}-{nomes_2}=> Diferença simétrica")

#converter
valores=set([1,2,3,4,5,6,7,7,8])
for x in valores:
    print(x)
#print(valores[1]) #não funciona
for p,valor in enumerate(valores,start=1):
    print(f"Elemento da posição {p}: {valor}")

#testar se existe
if 2 in valores:
    print("Existe o valor 2")
else:
    print(f"Não Existe o valor 2")

#nº de elementos
print(len(nomes_3))



#Resumo
#difference devolve o que não esta em comum
#interseção devolve o que é comum
#união devolve pra juntando