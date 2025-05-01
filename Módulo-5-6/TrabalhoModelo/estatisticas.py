"""Módulo Estatisticas"""

import utils
import devoluções_emprestimos
from datetime import datetime

def MenuEstatisticas():
    """Submenu para gerir as estatisticas"""

    op=0
    while op!=5:
        op=utils.Menu(["Livro + requisitado ","Leitor + requisições","Emprestimos em atraso","Top mês","Voltar"],"Menu Estatísticas")
        if op == 5:
            return
        if op==1:
            LivroMais()
        if op==2:
            LeitorMais()
        if op==3:
            EmprestimosForaPrazo()
        if op==4:
            MesMais()


def LivroMais():
    """Função para encontrar o livro mais requisitado no último mês (mês anterior ao mês atual)"""
    if len(devoluções_emprestimos.emprestimos) == 0:
        print("Não tem empréstimos")
        return
    #mês e ano a pesquisar
    data_atual = datetime.now()
    data_atual.strftime("%Y-%m-%d")
    partes = data_atual.split("-")
    ano = int(partes[0])
    mes = int(partes[1])
    mes = mes - 1
    if mes == 0:
        mes = 12
        ano = ano - 1
   
    #criar um dicionário { titulo: contagem}
    dicionario_livros={}
    #percorrer empréstimos
    for emprestimo in devoluções_emprestimos.emprestimos:
        #verificar se é do mês anterior (comparar mês e ano)
        data_emprestimo = emprestimo['data_emprestimo'].split("-")
        ano_emprestimo = int(data_emprestimo[0])
        mes_emprestimo = int(data_emprestimo[1])
        if ano_emprestimo == ano and mes_emprestimo == mes:
            #contar se sim
            if emprestimo['livro']['titulo'] in dicionario_livros:
                dicionario_livros[emprestimo['livro']['titulo']] += 1
            else:
                dicionario_livros[emprestimo['livro']['titulo']] = 1
    #percorrer o dicionário e encontrar o maior
    maior = 0
    titulo_maior =""
    for livro in dicionario_livros:
        if dicionario_livros[livro]>maior:
            titulo_maior = livro
            maior = dicionario_livros[livro]
    print(f"O livro mais emprestado no mês anterior ({mes}/{ano}) foi {titulo_maior} com {maior} empréstimos.")
 

def LivroMais():
    """Função para encontrar o livro mais requisitado no último mês (mês anterior ao mês atual)"""
    if len(devoluções_emprestimos.emprestimos) == 0:
        print("Não tem empréstimos")
        return
    #mês e ano a pesquisar
    data_atual = datetime.now()
    data_atual = data_atual.strftime("%Y-%m-%d")
    partes = data_atual.split("-")
    ano = int(partes[0])
    mes = int(partes[1])
    mes = mes - 1
    if mes == 0:
        mes = 12
        ano = ano - 1
   
    #criar um dicionário { titulo: contagem}
    dicionario_livros={}
    #percorrer empréstimos
    for emprestimo in devoluções_emprestimos.emprestimos:
        #verificar se é do mês anterior (comparar mês e ano)
        data_emprestimo = emprestimo['data_emprestimo'].split("-")
        ano_emprestimo = int(data_emprestimo[0])
        mes_emprestimo = int(data_emprestimo[1])
        if ano_emprestimo == ano and mes_emprestimo == mes:
            #contar se sim
            if emprestimo['livro']['titulo'] in dicionario_livros:
                dicionario_livros[emprestimo['livro']['titulo']] += 1
            else:
                dicionario_livros[emprestimo['livro']['titulo']] = 1
    #percorrer o dicionário e encontrar o maior
    maior = 0
    titulo_maior =""
    for livro in dicionario_livros:
        if dicionario_livros[livro]>maior:
            titulo_maior = livro
            maior = dicionario_livros[livro]
    print(f"O livro mais emprestado no mês anterior ({mes}/{ano}) foi {titulo_maior} com {maior} empréstimos.")
 


def EmprestimosForaPrazo():
    """Função para listar os empréstimos que ainda não acabaram e estão fora do prazo
    de entrega"""
    #criar uma variavel para a data atual
    data_atual=datetime.now()
    #converter para inteiro
    idata_atual=int(data_atual.strftime("%Y%m%d"))
    #percorrer a lista dos emprestimos
    #contar nº de empréstimos fora do prazo
    contar=0
    for emprestimo in devoluções_emprestimos.emprestimos:
        #converter a data de emprestimo em inteiro
        data_devolucao=emprestimo["data_devolucao"]
        idata_devolucao=int(datetime.strptime(data_devolucao,"%Y-%m-%d").strftime("%Y%m%d"))
        #comparar com a data atual
        if idata_atual > idata_devolucao and emprestimo["estado"] == True:
            dias_atraso=idata_atual- idata_devolucao
            print(f"o leitor {emprestimo["leitor"]["nome"]} tem o livro {emprestimo ["livro"]["titulo"]} por entregar fora do prazo há {dias_atraso} dias.")
            contar+=1
    if contar==0:
        print("Não há empréstimos em atraso")
        return
    percentagem=(contar/len(devoluções_emprestimos.emprestimos))*100
    print(f"{percentagem} % de empréstimos fora do prazo.")


def MesMais():
    """Mostra o mês em que existem mais requisições, independentemente do ano"""
    #criar uma lista com 12 posições
    meses=[]
    for i in range(12):
        meses.append(0)
    #Percorrer os empréstimos
    for emprestimo in devoluções_emprestimos.emprestimos():
        #extrair o mês da data de empréstimo
        partes=emprestimo["data_emprestimo"].split("-")
        mes_emprestimo=int(partes[1])
        #somar 1 na lista dos meses na posição do mês do empréstimo
        meses[mes_emprestimo-1]+=1
        #Percorrer a lista dos meses e encontrar o maior
        posicao_maior=0
        for i in range(len(meses)):
            if meses[i]>meses[posicao_maior]:
                posicao_maior=i
    #Mostrar a posição do maior +1
    print(f"O mês que tem mais empréstimos é {posicao_maior+1} com {meses[posicao_maior]} empréstimos")



