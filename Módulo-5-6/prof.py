
"""Um Programa que utiliza um dicionário para guardar os professores responsáveis
pelas salas do torneio tecla e o nº de alunos que cada
sala vai ter. As salas são C5,C6,C7,C8 e o dicionário deve guardar o nome do professor
e o nº de alunos de cada uma"""


"""dicionario={"C5":{"professor":"p1","n_alunos":10},
            "C6":{"professor":"p2","n_alunos":14},
            "C7":{"professor":"p3","n_alunos":12},
            "C8":{"professor":"p4","n_alunos":8}}"""
"""dicionario={}
for i in range(4):
    salas=input("Introduza as salas: ")
    professor=(input("Introduza o nome dos professores: "))
    alunos=int(input("Introduza o número de alunos: "))
    dicionario[salas]={"professor":professor,"alunos":alunos} #faz um dicionario dentro do outro sendo a chave principal as salas
                       #faz com que a professor seja uma chave e alunos tendo salas com chave principal

print(dicionario)"""



#ou

dados={"C5":{"professor":"p1","n_alunos":10},
            "C6":{"professor":"p2","n_alunos":14},
            "C7":{"professor":"p3","n_alunos":12},
            "C8":{"professor":"p4","n_alunos":8}}

#ler dados dos professores e alunos por sala
for sala in dados:
    professor=input(f"Nome do professor responsável pela sala {sala}?")
    nr_alunos=int(input(f"Nº de alunos para a sala {sala}?"))
    #atualizar o nome do professor
    dados[sala]["professor"]=professor
    #Atualizar o nº de alunos
    dados[sala]["n_alunos"]=nr_alunos
#listar os dados

"""for sala in dados:
    print(f"Sala: {sala} -> Professor responsável: {dados[sala]["professor"]} Nº de alunos: {dados [sala] ["n_alunos"]}")"""
#Adicionar uma sala, um professor e o nº de alunos introduzidos pelo utilizador
sala=input("Introduza a sala: ")
professor=input(f"Nome do professor responsável pela sala {sala}? ")
nr_alunos=input(f"Nº de alunos para a sala {sala}? ")
dados[sala]={"professor":professor,"n_alunos":nr_alunos}

#remover a sala C05 do dicionário
del dados ["C5"]
                        

for sala in dados:
    print(f"Sala: {sala} -> Professor responsável: {dados[sala]["professor"]} -> Nº de alunos: {dados [sala] ["n_alunos"]}")


























