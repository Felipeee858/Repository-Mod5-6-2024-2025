"""Módulo de gestão dos leitores"""
import utils
leitores=[]
exemplo_leitores=[
    {"id":1,
    "nome":"Joaquim",
    "idade":15,
    "email":"Joaquim@gmail.com",
    "Infrações":None},
    {"id":2,
    "nome":"Maria",
    "idade":38,
    "email":"Maria@gmail.com",
    "Infrações":None},
    {"id":3,
    "nome":"João",
    "idade":56,
    "email":"João@gmail.com",
    "Infrações":None}
]
def configurar():
    """Insere dados de exemplo"""
    leitores.extend(exemplo_leitores)
lista_campos_privados=["id"]
#Menu leitores
def Menuleitores():
    """Submenu para gerir os leitores"""
    op=0
    while op !=6:
        op=utils.Menu(["Adicionar","Listar","Editar","Apagar","Pesquisar","Voltar"],"Menu leitores")
        if op ==6:
            break
        elif op==1:
            Adicionar()
        elif op ==2:
            Listar(leitores)
        elif op ==3:
            Editar()
        elif op == 4:
            Apagar()
        elif op==5:
            pesquisar_listar()

#Adicionar Leitor
def Adicionar():
    print("#### Adicionar Livro novo ####")
    #id
    id=1
    if len(leitores)>0:
        id=leitores[len(leitores)-1]["id"]+1 #gerar id a partir do id do ultimo leitor
    #Nome
    nome=utils.ler_string(1,"Introduza o Nome: ")
    #Idade
    idade=utils.ler_numero_inteiro_limites(1,None,"Introduza a Idade: ")
    #e
    email=utils.ler_string(1,"Introduza o email: ")
    novo={
        "id":id,
        "nome":nome,
        "idade":idade,
        "email":email,
        "Infrações":None
    }
    leitores.append(novo)

def Listar(lista_a_listar):
    """Função para listar todos os leitores"""
    print("#"*80)
    print("Listar Leitores")
    print("#"*80)
    for leitores in lista_a_listar:
        print(f"id:{leitores["id"]} | Nome: {leitores["nome"]} | Idade: {leitores["idade"]} | Email: {leitores["email"]} | Infrações: {leitores["Infrações"]}")

def Editar():
    #pesquisar o leitor a editar
    leitores_editar=Pesquisar()
    #mostrar os dados de cada leitor encontrado
    if len (leitores_editar)==0:
        print("Não foram encontrados leitores.")
        return
    #mostrar todos os leitores
    Listar(leitores_editar)
    #permitir alterar os dados
    nome=utils.ler_string(1,"Introduza o nome do leitor a editar ou 0 (zero) para cancelar: ")
    if nome ==0:
        return
    #leitor com nome indicado
    leitor=None
    for l in leitores_editar:
        if l["nome"] == nome:
            leitor=l
            break
    if leitor == None:
        print("O nome indicado não existe")
        return
    #escolher o campo a editar
    #lista_campos=list(leitor.keys())
    lista_campos=[]
    for i in leitor.keys():
        if i != leitor["id"]:
            lista_campos.append(i)
    #remover os campos privados
    for c in lista_campos_privados:
        lista_campos.remove(c)
    op=utils.Menu(lista_campos,"Qual o campo a editar? ")
    campo=lista_campos[op-1]
    #mostrar o valor atual do campo a editar
    print(f"o campo {lista_campos[op - 1]} tem o valor {leitor[campo]}")
    novo_valor=utils.ler_string(1,"Novo valor: ")
    #Guarda o novo valor
    leitor[campo]=novo_valor
def Apagar():
    #pesquisar se exite leitores
    if len(leitores)==0:
        print("Não Há leitores")
        return
    #pesquisar o leitor a apagar
    resultado=Pesquisar()
    #mostrar os dados de cada leitor encotrado
    if len(resultado)==0:
        print("Não foram encontrados leitores.")
        return
    #mostrar todos os leitores
    Listar(resultado)
def pesquisar_listar():
    resultado=Pesquisar()
    Listar(resultado)

#pesquisar leitores
def Pesquisar():
    """Devolver a lista dos leitores que corresponde a um critério"""
    #Deixar o utilizar escolher o campo de pesquisa
    op=utils.Menu(["Nome","id"],"Escolha o campo de pesquisa: ")
    #criar uma lista para os resultados
    l_resultados=[]
    if op ==1:
        campo="nome"
    else:
        campo="id"
    #Adicionar à lista o leitores que corresponde ao resultado da pesquisa
    if campo =="nome":
        pesquisa=utils.ler_string(1,f"{campo} a pesquisar: ")
        for leitor in leitores:
            if pesquisa.lower() in leitor[campo].lower():
                l_resultados.append(leitor)
        return l_resultados
    elif campo == "id":
        pesquisa=utils.ler_numero_inteiro(f"{campo} a pesquisar: ")
        for leitor in leitores:
            if pesquisa==leitor["id"]:
                l_resultados.append(leitor)
        return l_resultados
