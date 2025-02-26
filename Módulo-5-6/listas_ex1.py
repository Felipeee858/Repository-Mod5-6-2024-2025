"""Programa para ler as marcas de carros de um stand. O programada
deve mostrar aual a marca com mais veículos
-Ler do utilizador as marcas e guardar numa lista
-Parar de ler quando o utilizador inserir uma marca vazia
-Calcular para cada marca quantos carros existem de cada marca
-Mostrar a marca com mais carros
(utilizar listas para guardar as marcas)"""

#ciclo para ler a marca e adicionar à lista
i=" "
carros=[]
while i != "":
    marcas=input("Introduza a marca: ")
    if marcas == "":
        i=""
        break
    carros.append(marcas)

#calcular para cada marca quantos carros existem de cada marca
marcas=set(carros) # cria um set com as marcas (sem repetições)
maior=0
mmmaior=""
for marca in marcas:
    contar=carros.count(marca)
    print(f"Da marca {marca} tem {contar} carros")
    if contar > maior:
        mmaior=marca
        maior=contar
print(f"A marca {mmaior} é que tem mais veículos com {maior} carros")

marca_remover=input("Introduza o veículo que deseja remover: ")

while marca_remover in carros:
    carros.remove(marca_remover)
print(carros)