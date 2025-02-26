cores=[]

#adicionar a cor vermelhor
cores.append("vermelho")
#adicionar uma cor introduzida pelo utilizador
cor=input("Indique uma cor: ")
cores.append(cor)
#inserir numa posição
cores.insert(0,"amarelo") #inserir o amarelo na posição 0
                          #os restantes elementos da lista
                          #são reorganizados
#remover itens
cores.remove("vermelho") #remove o primero e dá erro se não encontrar

cor_removida=cores.pop(0) #remove o elemento da posição indicada dá erro se a lista estiver vazia ou não existir a posição
print(f"Cor removida {cor_removida}")

carros=["Ford","ferrari","bmw","vw"]
del carros[1:3] #remove os elementos nas posições 1 e 2 
print(carros)

#remover todos
carros.clear()

#recriar a lista
carros=[]

print(cores)


#listar todos os elementos
for cor in cores:
    print(cor)

for posicao in range(len(cores)):
    print(cores[posicao])

