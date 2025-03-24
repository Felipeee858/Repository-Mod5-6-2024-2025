"""Módulo Empréstimos e devoluções"""

import utils
import livros
import leitores
import os
from datetime import datetime,timedelta
#livro ({}),leitor([]),data do emprestimo,data da devolução,
emprestimos=[]
def MenuEmprestimos():
    op=0
    while op !=4:
        op=utils.Menu(["Empréstimos","Devolução","Listar","Voltar"],"Menu de empréstimos/devoluções")
        if op == 4:
            break
        if op==1:
            Emprestimo()
        if op==2:
            Devolucao()
        elif op==3:
            Listar()

def Emprestimo():
    #dados do novo emprestimo a adicionar a lista
    novo={}
    #ler qual o livro a emprestar
    print("Indique o Livro a emprestar: ")
    livros_emprestar=livros.Pesquisar()
    if len(livros_emprestar)==0:
        print("Nenhum livro encontrado. Tente novamente")
        return
    elif len(livros_emprestar)>1:
        #mostrar os livros encontrados
        livros.Listar(livros_emprestar)
        #pedir o id do livro a emprestar
        id=utils.ler_numero_inteiro("Introduza o id do livro a emprestar: ")
        for livro in livros_emprestar:
            if livro["id"] == id:
                if livro["estado"]!= "disponível":
                    print("Esse livro está emprestado")
                    return
                novo["livro"]=livro
                break
        if "livro" not in novo:
            print("O id indicado não existe")
            return
    else:
        #só encontrou um livro
        if livros_emprestar[0]["estado"]!= "disponível":
            print("Esse livro está emprestado")
            return
        novo["livro"]=livros_emprestar
 

    #ler qual o leitor que leva o livro
    print("Indique o leitor a levar o livro: ")
    leitor_livro=leitores.Pesquisar()
    if len(leitor_livro) == 0:
        print("Leitor não encontrado")
        return
    elif len(leitor_livro) > 1:
        leitores.Listar(leitor_livro)
        id=utils.ler_numero_inteiro("Introduza o id do leitor: ")
        for leitor in leitor_livro:
            if leitor["id"] == id:
                novo["leitor"]=leitor
                break
        if "leitor" not in novo:
            print("O id indicado não existe")
    else:
        novo["leitor"] = leitor_livro[0]

                

    #TODO: verificar se o leitor pode levar o livro
    #registar o empréstimo com data de devolução
    data_atual=datetime.now()
    data_entrega=data_atual + timedelta(days=30)
    str_data_atual=data_atual.strftime("%Y-%m-%d")
    str_data_entrega=data_entrega.strftime("%Y-%m-%d")
    novo["data_emprestimo"] = str_data_atual
    novo["data_devolucao"] = str_data_entrega
    novo["estado"]=True #Emprestimo está a decorrer
    emprestimos.append(novo)
    #atualizar o estado do livro
    novo["livro"]["estado"] = "emprestado"
    novo["livro"]["leitor"]=novo["leitor"]
    print("Empréstimo registrado com sucesso")
    print(f"Livro emprestado: {novo["livro"]}")
    print(f"Leitor: {novo["leitor"]}")
def Devolucao():
    #ler o id do livro a devolver
    id_livro=utils.ler_numero_inteiro("Introduza o id do livro a devolver: ")
    #verificar se o livro está emprestado
    livro=livros.GetLivros(id_livro)
    if livro == None:
        print("Não existe nenhum livro com id indicado")
    if livro["estado"] != "emprestado":
        print("Esse livro não está emprestado")
    #verificar se a devolução está dentro prazo
    emprestimo_devolver= None
    for emprestimo in emprestimos:
        if emprestimo["livro"] == livro and emprestimo["estado"]==True:
            emprestimo_devolver=emprestimo 
    if emprestimo_devolver == None:
        print("Emprestimo não encontrado")
        return
    data_devoluçao= emprestimo_devolver["data_devolucao"]
    data_atual= datetime.now()
    idata_atual=int(data_atual.strftime("%Y%m%d"))
    idata_devoluçao=int(datetime.strptime(data_devoluçao,"%Y-%m-%d").strftime("%Y%m%d"))
    if idata_atual>idata_devoluçao:
        print("Devolução fora de prazo")
        #registas se houve infração do leitor
        emprestimo_devolver["leitor"]["Infrações"] += "Entrega fora do prazo"
    #atualizar o nr de empréstimo do livro
    livro["nr_emprestimo"]+=1
    #mudar o estado do livro
    livro["estado"]="disponível"
    livro["leitor"]=None
    #mudar o estado do empréstimo
    emprestimo_devolver["estado"] = False
    print("Devolução concluída com sucesso")

def Listar():
    #perguntar se pretende ver todos os empréstimos ou
    #só os empréstimos por concluir"
    op=utils.ler_string(1,"Listar [T]odos ou só por [C]oncluir")
    for emp in emprestimos:
        if op in "tT" or (op in "cC" and emp["estado"]==True):
            print(f"{emp["livro"]["titulo"]} {emp["leitor"]["nome"]}{emp["estado"]}")
