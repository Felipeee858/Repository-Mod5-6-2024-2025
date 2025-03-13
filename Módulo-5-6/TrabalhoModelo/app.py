"""
Trabalho Modelo - Módulo 6
------------------------------------------
Um programa para gerir livros e empréstimos de um biblioteca
Requisítos funcionais:
    -Gestão livros(CRUD) criar,mostrar todos,editar,deletar
    -Gestão leitores(CRUD)
    -Empréstimos e devoluções
    -Estatísticas (empréstimos em atraso, top livros, top mes, top leitores, ...)"""
import utils
import livros

#Deve estar True quando em testes e False quando em produção
DEBUG=True
def MenuPrincipal():
    if DEBUG:
        livros.configurar()
    op=0
    while op!=5:
        op=utils.Menu(["Livros","Leitores","Empréstimos/devoluções","Estatísticas","Sair"],"Menu principal")
        if op==5:
            break
        if op==1:
            livros.MenuLivros()

if __name__=="__main__":
    MenuPrincipal()