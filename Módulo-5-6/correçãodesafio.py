Notas={"Aluno1":{"PT":0,"ING":0,"AI":0,"TIC":0},
       "Aluno2":{"PT":0,"ING":0,"AI":0,"TIC":0}}

for chave in Notas:
    Soma=0
    for Disciplina in Notas[chave]:
        nota=int(input(f"Nota de {Disciplina} de {chave}: "))
        Notas[chave][Disciplina]=nota
        Soma=Soma+nota
    Media=Soma/4
    Notas[chave]["Media"]=Media
    print(f"A média do aluno {chave} é {Media}")

Media_total=(Notas["Aluno1"]["Media"] + Notas["Aluno2"]["Media"])/2
print(Media_total)
for aluno in Notas:
    print(aluno)
    for disciplina in Notas[aluno]:
        print(disciplina,Notas[aluno][disciplina])



dicionario={} #dicionario do exercício
for cliente in dicionario:
    print(cliente) # codigo
    for visitas in dicionario[cliente]:
        print(f"{visitas} - {dicionario[cliente][visitas]}")

codigo=int(input("codigo"))
print(dicionario[codigo]["Visitas"])
codigo=int(input("Codigo Visitante: "))
dicionario[codigo]["Visitas"] +=1

maior=0
cidade_maior=0
for chave in dicionario:
    Tcidade=dicionario[chave]["cidade"]
    nrvisitas=dicionario[chave]["visitas"]
    for codigo in dicionario:
        if Tcidade==dicionario[codigo]["cidade"]:
            nrvisitas=dicionario[codigo]["visitas"]
        if nrvisitas>maior:
            cidade_maior=Tcidade
            maior=nrvisitas

            



