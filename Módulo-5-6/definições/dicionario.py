def Adicionar(dicionario):
    chave=input("Introduza a chave que deseja: ")
    if chave in dicionario:
        #Se existir perguntar se pretende atualizar
        pergunta=input("Esse termo já existe no dicionário. Pretende atualizar? ")
        if pergunta =="n":
            return
    
    definição=input("Introduza a sua definição da chave: ")
    dicionario[chave]=definição

            


def Listar_Todas(dicionario):
    pergunta=input("Pretende visualizar por ordem alfabética")
    if pergunta !="s":
        for chave,valor in dicionario.items(): #passa pelas chaves e valores
            print(f"{chave} -> {valor}") # e faz  print com setas de indicação
    else:
        #ordenar as chaves
        chaves=dicionario.keys()
        chave=sorted(chaves)
        #percorrer as chaves ordenadas e mostrar o valor correspondente
        for chave in chaves:
            print(f"{chave} -> {dicionario[chave]}")
    

def Pesquisar(dicionario):
    #ler o termo a pesquisar
    pergunta=input("Introduze o que deseja pesquisar: ")
    #percorrer o dicionario
    for chave,valor in dicionario.items():
        #se termo existir no inicio da chave mostrar o valor
        if pergunta == chave[:len(pergunta)]: #Slicing para so comparar o inicio da chave
            print(f"{chave} -> {valor}")

            


def Apagar(dicionario):
    pergunta=input("Introduza a chave que deseja apagar: ")
    #percorrer o dicionario
    for chave,valor in dicionario.items():
        #se o termo existir no inicio da chave mostrar o valor
        if pergunta==chave[:len(pergunta)]:#slicing para só comparar o inicio da chave
            print(f"{chave}->{valor}")
            op=input("Pretende remover esta palavra do dicionario? ")
            if op=="s":
                del dicionario[chave]
                return #uma vez que o dicionario foi alterado n podemos continuar o ciclo
    return

def Configurar(dicionario):
    dicionario["pera"]="fruta"
    dicionario["pc"]="computador pessoal"
    dicionario["bicicleta"]="meio de transporte"
#se o programa está em desenvolvimento deve ser:True
#se está terminado (em produção) deve ser:False

em_teste=True