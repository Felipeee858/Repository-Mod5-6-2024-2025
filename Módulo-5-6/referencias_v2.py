alunos=[
    {"nprocesso":123,"nome":"Maria","email":"maria@gmail.com"},
    {"nprocesso":124,"nome":"Joaquim","email":"joaquim@gmail.com"},
    {"nprocesso":125,"nome":"António","email":"antonio@gmail.com"}
]

notas=[
    {"nprocesso":123,"notas":[10,11,12,13]},
    {"nprocesso":124,"notas":[10,5,8,14]}
]


#mostrar o nome e as notas dos alunos
#os alunos sem notas não devem aparecer
#percorrer as notas
for nota in notas:
    #percorrer os aluno para encontrar o nprocesso correspondente
    for aluno in alunos:
        if nota["nprocesso"]==aluno["nprocesso"]:
            print(f"{aluno["nome"]} - {nota["notas"]}")


"""Considerações:
    -O que deve acontecer se tentar apagar o aluno 124? Apagar
    também as notas ou não deixar apagar o aluno?
    - Posso adicionar as notas do aluno 129?
    - Não devemos alterar nprocessos
    """