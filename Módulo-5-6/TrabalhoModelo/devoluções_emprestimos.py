"""Módulo Empréstimos e devoluções"""

import utils

def MenuEsprestimos():
    op=0
    while op !=3:
        op=utils.Menu(["Empréstimos","Devolução","Voltar"],"Menu de empréstimos/devoluções")
        if op == 3:
            break
        if op==1:
            Emprestimo()
        if op==2:
            Devolucao()

def Emprestimo():
    pass
    #ler qual o livro a emprestar
    #verificar se o livro pode ser emprestado
    #ler qual o leitor que leva o livro
    #verificar se o leitor pode levar o livro
    #registar o empréstimo com data de devolução~
    #atualizar o estado do livro

def Devolucao():
    pass