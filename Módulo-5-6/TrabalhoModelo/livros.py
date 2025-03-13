"""Módulo de gestão dos livros"""
import utils
#lista de livros
livros=[]

#lista de livros de exemplo
exemplo_livros=[
        {"id":1,
        "titulo":"Livro1",
        "autor":"autor a",
        "assunto":"assunto 1",
        "editora":"editora a",
        "ano":2001,
        "estado":"disponível",
        "leitor":None,
        "nr_emprestimo":0},
    
        {"id":2,
        "titulo":"Livro2",
        "autor":"autor b",
        "assunto":"assunto 2",
        "editora":"editora b",
        "ano":2002,
        "estado":"disponível",
        "leitor":None,
        "nr_emprestimo":0},
    
    
        {"id":3,
        "titulo":"Livro3",
        "autor":"autor c",
        "assunto":"assunto 3",
        "editora":"editora c",
        "ano":2003,
        "estado":"disponível",
        "leitor":None,
        "nr_emprestimo":0}
    ]

def configurar():
    """Insere dados de exemplo"""
    livros.extend(exemplo_livros)
#Menu Livros
def MenuLivros():
    """Submenu para gerir os livros"""
    op=0
    while op !=6:
        op=utils.Menu(["Adicionar","Listar","Editar","Apagar","Pesquisar","Voltar"],"Menu de livros")
        if op == 6:
            break
        if op == 1:
            Adicionar()
        elif op == 2:
            Listar(livros)
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            Pesquisar()
#Adicionar Livro
def Adicionar():
    print("#### Adicionar Livro novo ####")
    #Título
    titulo=utils.ler_string(1,"Introduza o Título: ")
    #Autor
    autor=utils.ler_string(1,"Introduza o Autor: ")
    #Assunto
    assunto=utils.ler_string(1,"Introduza o Assunto: ")
    #Editora
    editora=utils.ler_string(1,"Introduza a Editora: ")
    #Ano Edição
    ano=utils.ler_numero_inteiro_limites(1500,2030,"Introduza o Ano de Edição: ")
    #id
    id=1
    if len(livros)>0:
        id=livros[len(livros)-1]["id"]+1 #gerar id a partir do id do ultimo livro
    novo={
        "id":id,
        "titulo":titulo,
        "autor":autor,
        "assunto":assunto,
        "editora":editora,
        "ano":ano,
        "estado":"disponível",
        "leitor":None,
        "nr_emprestimo":0
    }
    livros.append(novo)
    print(f"Livro registrado com sucesso. Tem {len(livros)} livros")

#Editar Livro

#Apagar Livro

#Listar Livros
def Listar(lista_a_listar):
    """Função para listar todos os livros"""
    print("#"*80)
    print("Lista de livros")
    print("#"*80)
    for livro in lista_a_listar:
        print(f"id:{livro["id"]} | Nome: {livro["titulo"]} | Assunto: {livro["assunto"]} | Estado: {livro["estado"]}")
        print("-"*80)
#Pesquisar Livros
def Pesquisar():
    """Devolver a lista dos livros que correspondem a um critério"""
    #Deixar o utilizar escolher o campo de pesquisa
    op=utils.Menu(["Autor","Título"],"Escolha o campo de pesquisa:")
    #criar uma lista para os resultados
    l_resultados=[]
    if op==1:
        campo="autor"
    else:
        campo="titulo"
    pesquisa=utils.ler_string(1,f"{campo} a pesquisar")
    for livro in livros:
        if pesquisa.lower() in livro[campo].lower():
            l_resultados.append(livros)
    Listar(l_resultados)
    #adicionar à lista os livros que correspondem ao resultado da pesquisa


if __name__=="__main__":
    MenuLivros()