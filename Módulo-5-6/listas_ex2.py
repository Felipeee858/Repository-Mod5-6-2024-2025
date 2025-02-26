"""Programa para gerir os livros de um biblioteca e os seus empréstimos"""

Livros=["Livro1","Livro2","Livro3","Livro4"]
emprestimos=[]

#ler o titulo do livro emprestar
Livro=" "
while Livro !=""and len(Livros)>0:
    Livro=input("Introduza o nome do livro: ")
    #o programa deve terminar quando é inserido um título em branco ou quando não há mais livros para emprestar
    if Livro != "" and len(Livros)>0:
        if Livro in Livros:
            #remover da lista de livros para a lista de emprestimo
            Livros.remove(Livro)
            emprestimos.append(Livro)
        elif Livro in emprestimos:
            print("O livro inserido está emprestado")
        else:
            print("O livro inserido é inexistente")
   
    #mostrar os livros e os emprestimos
    if len(Livros)==0:
        print(f"Não há mais livros disponíveis\nOs livros emprestados são: {emprestimos}")
    else:
        print(f"Os livros disponíveis são: {Livros}\nOs livros emprestados são: {emprestimos}")