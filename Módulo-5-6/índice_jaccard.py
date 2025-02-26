"""Calcular o Índice de Jaccard entre duas frases"""

A=input("Introduza a frase: ")
B=input("Introduza a frase: ")

A=A.lower().strip().split(" ")
A=set(A)

B=B.lower().strip().split(" ")
B=set(B)

fórmula=len((A.intersection(B))) / len((A.union(B)))
print(fórmula)



