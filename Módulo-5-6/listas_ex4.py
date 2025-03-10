alunos=["joaquim","antonio","maria","carlos"]
#inverter a ordem dos alunos
alunos=alunos[::-1]
#existem nomes repetidos?
if (len(alunos)) != set(alunos):
    print("Repetidos")
