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
    pass

def LeitorMais():
    """Função para mostrar o leitor com mais empréstimos"""
    if len(devoluções_emprestimos.emprestimos)== 0:
        print("Não tem empréstimos")
        return
    lista_leitores=[]
    for emprestimo in devoluções_emprestimos.emprestimos:
        nome=emprestimo["leitor"]["nome"]
        if nome in lista_leitores:
            lista_leitores[nome] +=1
        else:
            lista_leitores[nome]=1
    nome_maior=lista_leitores[0].keys()[0]
    maior=0
    for leitor in lista_leitores:
        if leitor.values()[0] > maior:
            maior =leitor.values()[0]
            nome_maior= leitor.keys()[0]
    print(f"o leitor com mais empréstimos é {nome_maior}")


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