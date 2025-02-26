"""Um programa que calcula:
-os alunos que estiveram presentes todos os dias
-os alunos que faltaram pelo menos um dia
-os alunos que estiveram presentes na segunda e na sexta"""

segunda={"Ana","Carlos","Pedro","Maria"}
terça={"Ana","João","Pedro","Clara"}
quarta={"Maria","Pedro","Ana","Paulo"}
quinta={"João","Clara","Paulo","Ana"}
sexta={"Ana","Maria","Carlos","Paulo"}

#os alunos que estiveram presentes todos os dias
presentes_todos_dias=segunda.intersection(terça,quarta,quinta,sexta)
print(f"Presente todos os dias: {presentes_todos_dias}")

#os alunos que faltaram pelo menos um dia
faltaram_um_dia=segunda.union(terça,quarta,quinta,sexta)-presentes_todos_dias
print(faltaram_um_dia)

#os alunos que estiveram presentes na segunda e na sexta, mas não estiveram na terça, quarta ou quinta 
união_t_q_qta=terça.union(quarta,quinta) #|união
união_s_sx=segunda.intersection(sexta) #& interseção
presentes_segunda_sexta=união_s_sx.difference(união_t_q_qta) #- diferença
print(presentes_segunda_sexta)



