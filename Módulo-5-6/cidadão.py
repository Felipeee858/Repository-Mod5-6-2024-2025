#dicionário vazio
cidadao={}

def LerDados(cidadao):
    #cria a chave e le valor
    cidadao["nome"] = input("Introduza o nome: ")
    cidadao["Morada"] = input("Introduza o nome: ")
    cidadao["CP"] = input("Introduza o nome: ")
    cidadao["Idade"] =int(input("Introduza o nome: "))
    cidadao["Pai"] = input("Introduza o nome: ")
    cidadao["Mãe"] = input("Introduza o nome: ")
    op=input("Casado (s/n)")
    if op == "s":
        cidadao["Casado"]=True
    else:
        cidadao["Casado"]=False
    cidadao["nr_filhos"] = int(input("Nº de filhos: "))
    filhos={}
    for filho in range(cidadao["nr_filhos"]):
        chave = f"nome_{filho+1}"
        filhos[chave]=input("Introduza o nome do filho nº",filho+1)
        print(filhos)
        cidadao["filhos"]=filhos
LerDados(cidadao)
print(cidadao)
#mostrar o nome do primeiro filho
print(cidadao["filhos"]["nome_1"])