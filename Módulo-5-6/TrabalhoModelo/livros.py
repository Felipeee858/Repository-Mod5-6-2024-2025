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
lista_campos_privados=["id","estado","leitor","nr_emprestimos"]
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
        elif op == 1:
            Adicionar()
        elif op == 2:
            Listar(livros)
        elif op == 3:
            Editar()
        elif op == 4:
            Apagar()
        elif op == 5:
            pesquisar_listar()
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
def Editar():
    #pesquisar o livro a editar
    livros_editar=Pesquisar()
    #mostrar os dados de cada livro encontrado
    if len(livros_editar)==0:
        print("Não foram encontrados livros.")
        return
    #mostrar todos os livros
    Listar(livros_editar)
    #permitir alterar os dados
    id=utils.ler_numero_inteiro("Introduza o id do livro a editar ou 0 (zero) para cancelar: ")
    if id == 0:
        return
    #livro com o id indicado
    livro=None
    for l in livros_editar:
        if l["id"] == id:
            livro=l
            break
    if livro == None:
        print("O id indicado não existe")
        return
    #escolher o campo a editar
    lista_campos=list(livro.keys())
    #remover os campos privados
    for c in lista_campos_privados:
        lista_campos.remove(c)
    op=utils.Menu(lista_campos,"Qual o campo a editar? ")
    campo=lista_campos[op-1]
    #mostrar o valor atual do campo a editar
    print(f"o campo {lista_campos[op - 1]} tem o valor {livro[campo]}")
    novo_valor=utils.ler_string(3,"Novo valor: ")
    #Guarda o novo valor
    livro[campo]=novo_valor
    
#Apagar Livro
def Apagar():
    #verificar se a lista está vazia
    if len(livros)==0:
        print("Não tem livros para remover.")
        return
    # pesquisar os livros com título semelhante
    print("Pesquisar o livro a remover:")
    l_livros = Pesquisar()
    #verificar se encontrou pelo menos 1
    if len(l_livros)==0:
        print("Não foi encontrado nenhum livro.")
        return
    # confirmar para cada um dos livros se deseja apagar
    for livro in l_livros:
        print(f"Título: {livro['titulo']} Autor: {livro['autor']} id: {livro['id']}")
        op = input("Deseja remover este livro (s/n)?")
        if op in "sS":
            #TODO: confirmar se o livro  não está emprestado
            livros.remove(livro)
            break
    print(f"Livro removido com sucesso. Tem {len(livros)} livros.")


def pesquisar_listar():
    resultado=Pesquisar()
    Listar(resultado)
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
    op=utils.Menu(["Autor","Título"],"Escolha o campo de pesquisa: ")
    #criar uma lista para os resultados
    l_resultados=[]
    if op==1:
        campo="autor"
    else:
        campo="titulo"
    pesquisa=utils.ler_string(3,f"{campo} a pesquisar: ")
    #adicionar à lista os livros que correspondem ao resultado da pesquisa
    for livro in livros:
        if pesquisa.lower() in livro[campo].lower():
            l_resultados.append(livro)
    return l_resultados


if __name__=="__main__":
    MenuLivros()