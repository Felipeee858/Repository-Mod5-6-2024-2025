from dicionario import Adicionar,Listar_Todas,Pesquisar,Apagar,Configurar,em_teste # from dicionario import funciona para importar coisas específicas

def menu():
    print("1. Adicionar Definição\n2. Listar Todas Definições\n3. Pesquisar Definição\n4. Apagar\n5. Terminar")
    dicionario={}
    if em_teste:
        Configurar(dicionario)
    
    op=0
    while op !=5:
        op=int(input("Introduza a sua opção: "))
        if op ==1:
            Adicionar(dicionario)
        elif op ==2:
            Listar_Todas(dicionario)
        elif op==3:
            Pesquisar(dicionario)
        elif op ==4:
            Apagar(dicionario)
        elif op==5:
            break
        else:
            print("Opção inválida")




if __name__=="__main__":
    menu()