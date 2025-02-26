"""Ler do utilizador uma frase e contar quantas palavras únicas"""

#ler o texto do utilizador
texto=input("Introduza o texto: ")
#lista das palavras
texto=texto.strip().split(" ")
#converter a lista em set
texto=set(texto)
#len para contar
print(f"São: {len(texto)} palavras únicas")




