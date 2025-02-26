"""
Listas Estrutura de dados dinâmica (nº de elementos pode aumentar e diminui),
não homogenea (pode ter elementos com diferentes tipos de dados, incluindo,
mutáveis - listas, dicionários, arrays, etc)"""


#Definir uma lista
minha_lista=[] #lista vazia
minha_lista2=[1,2,3,"quatro"]
minha_lista3=list({1,2,3})
lista_de_cinco=list(range(5))
print(minha_lista,minha_lista2,minha_lista3,lista_de_cinco)

#Listas são referências
x=10
y=x #cria uma variável nova e copia o valor para essa variável
x=11
print(x,y)
lista_x=[1,2,3]
lista_y=lista_x #as duas variáveis "apontam" para o mesmo conjunto de dados
lista_x[1]=10
print(lista_x,lista_y)
#para criar uma cópia da lista
lista_z=lista_x[:] #cria uma lista nova e copia todos os valores
lista_x[1]=5
print(lista_x,lista_z)
#listar valores da lista
print(lista_z[0]) #mostra o primeiro elemento da lista
lista_k=[1,2,[10,20]] #lista com uma lista incorporada
#mostrar o primeiro valor da lista incorporada
print(lista_k[2][0])
#dicionário incorporado
notas=[{"joaquim",10},{"maria:15"},{"antonio":12}]
print(notas[2]["antonio"])
notas[0]["faltas"]=10
print(notas[0])