#juntar duas listas
meus_carros=["ford","bmw"]
teus_carros=["mercedes","vw"]


#junta as listas numa lista nova sem alterar as iniciais
nossos_carros=meus_carros + teus_carros
print(nossos_carros)

#junta na lista meus_carros todos os elementos da lista teus_carros (não altera esta)
meus_carros.extend(teus_carros) #junta o entre () com o de fora
print(meus_carros,teus_carros)
