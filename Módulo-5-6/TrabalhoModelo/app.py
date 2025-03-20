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
import leitores
import devoluções_emprestimos

#Deve estar True quando em testes e False quando em produção
DEBUG=True
def MenuPrincipal():
    if DEBUG:
        livros.configurar()
        leitores.configurar()
    op=0
    while op!=5:
        op=utils.Menu(["Livros","Leitores","Empréstimos/devoluções","Estatísticas","Sair"],"Menu principal")
        if op==5:
            break
        if op==1:
            livros.MenuLivros()
        if op==2:
            leitores.Menuleitores()
        if op==3:
            devoluções_emprestimos.MenuEmprestimos()


if __name__=="__main__":
    MenuPrincipal()


