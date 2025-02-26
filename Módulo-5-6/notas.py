notas={"Joaquim":(10,12,14,8,25),"Maria":(14,10,13,8,15),"António":(10,11,12,10,11)}

disciplinas=("pt","ing","mat","psi","ef")

#calcular e mostrar a média das notas de cada aluno
mmedia=-1
nomemm=""
for aluno in notas: #alunos == chave
    media=sum(notas[aluno])/len(notas[aluno])
    print(f"A media das notas do(a) {aluno} é de {media}")
    if media>mmedia:
        nomemm=aluno
        mmedia=media

#mostrar o nome do aluno com a melhor média
print(f"O aluno com a mlehor média foi {nomemm} e teve {mmedia}")
#mostrar o nº de negativas de cada aluno
for aluno in notas:
    negativas=0
    for nota in notas[aluno]:
        if nota<10:
            negativas+=1
    #mostrar o nome dos alunos sem negativas
    if negativas==0:
        print(f"O {aluno} não tem negativas")
    else:
        print(f"O {aluno} tem {negativas} negativas")

#calcular e mostrar a média das notas de cada disciplina
for i in range(len(disciplinas)):
    soma=0
    for aluno in notas:
        soma+=notas[aluno][i]
    media=soma/len(notas.keys())
    print(f"A disciplina {disciplinas[i]} tem a média de {media}")
#criar um dicionário com o nome do aluno, o nome das disciplinas e a as respetivas notas de cada aluno
notas_v2={}
for aluno in notas:
    notas_v2[aluno]={}
    for i in range(len(disciplinas)):
        notas_v2[aluno][disciplinas[i]]=notas[aluno][i]

print(notas_v2)




