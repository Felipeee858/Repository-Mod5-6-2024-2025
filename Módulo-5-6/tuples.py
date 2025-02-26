"""Crie um tuplo com os nomes dos meses do ano"""
tuple=("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")



"""Mostrar o terceiro mês do ano"""
print(tuple[2])

"""Obtenha o tuple dos meses de verão(junho,julho,agosto,setembro)"""

print(tuple[5:9])

"""Verifique se "Junho" está presente no tuplo de meses de verâo.
"""
verão=("Junho","Julho","Agosto","Setembro")

if "Junho" in verão:
        print("Verdadeiro")
        
else:
    print("Falso")
        
"""Extra:
   Listar os meses por ordem alfabética"""

print(sorted(tuple))

"""Mostrar os meses cujo nome começa por j"""
for mes in tuple:
     if tuple[0]=="j":
          print(mes)

"""Mostrar o mes(es) com o maior nome"""

maior=tuple[0]
for i in tuple:
    if len(i)> len(maior):
        maior=i
print(maior)