alunos=[
    {"nprocesso":123,"nome":"Maria","email":"maria@gmail.com"},
    {"nprocesso":124,"nome":"Joaquim","email":"joaquim@gmail.com"},
    {"nprocesso":125,"nome":"António","email":"antonio@gmail.com"}
]

notas=[
    {"nprocesso":alunos[0],"notas":[10,11,12,13]},
    {"nprocesso":alunos[1],"notas":[10,5,8,14]}
]

#mostrar o nome e as notas dos alunos
#os alunos sem nota não devem aparecer
for nota in notas:
    print(f"{nota["nprocesso"] ["nome"]} - {nota["notas"]}")

#apagar o primeiro aluno
del alunos[0]
for nota in notas:
    print(f"{nota["nprocesso"] ["nome"]} - {nota["notas"]}")