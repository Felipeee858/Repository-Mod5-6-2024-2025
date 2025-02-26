def ler_numero_inteiro(mensagem="Introduza um valor inteiro: ")->int:
    """Função que lè do utilizador de um nºinteiro.Afunção garante que o valor inserindo é um valor válido"""
    while True:
        dados = input(mensagem)
        if len(dados)==0:
            continue
        #verificar se existe um - no inicio da str(valor )
        if dados[0]=="-":
            testar = dados.replace("-","")
        else:
            testar=dados
        if testar.isdigit():
            return int(dados)
        print("Erro: o valor inserido não é válido.")

def ler_numero_inteiro_limites(valor_min,valor_max=None,mensagem="Introduza um valor inteiro: ")->int:
    """Função que recebe o valor minimo e maximo a ler do utilizador. A função 
    devolve o valor quando é um inteiro válido"""
    while True:
        numero=ler_numero_inteiro(mensagem)
        if numero >= valor_min and (valor_max is None or numero <= valor_max):
            return numero
        print("Erro: O valor não é valido")
        
def ler_numero_decimal(mensagem="Introduza um valor decimal: ") -> float:
    """Função para ler um nº decimal. A função garante que o valor é válido e aceita
    como separador das casas decimais . ou ,"""
    while True:
        dados = input(mensagem)
        if len(dados)==0:
            continue
        #substituir as virgulas por pontos
        dados=dados.replace(",",".") #replace substitui o primeiro pelo ultimo ou seja a "," vira "."
        #verificar se existe um - no inicio da str(valor )
        if dados[0]=="-":
            testar = dados.replace("-","")
        else:
            testar=dados
            #contar os pontos decimais
            pontos=testar.count(",") # quantas vezes existe a virgula
            #remover os pontos decimais
            testar=testar.replace(".","")
            #não pode ter mais do que 1 ponto decimal e só pode ter digitos
            if testar.isdigit() and pontos<=1: #devolve verdadeiro se for um digito se n for devolve falso
                return float(dados)
            print("Erro: o valor inserido não é válido.")

def ler_numero_decimal_limites(valor_min,valor_max=None,mensagem="Introduza um valor decimal: ") -> float:
    """Função para ler um valor decimal"""
    while True:
        valor=ler_numero_decimal(mensagem)
        if valor >= valor_min and (valor_max is None or valor <= valor_max):
            return valor
        print("Erro: valor não é válido")


def Menu(opçoes,titulo=""):
    """Função recebe as opções a mostrar de um menu. Lê a opção do utilizador e se for válida
    devolve essa opção"""

    #mostrar o titulo do menu
    if titulo!="":
        print(titulo)
    #mostrar as opções com um nª ao lado
    for i in range(len(opçoes)):
        print(f"{i+1}.{opçoes[i]}")
    #ler a Função do utilizador
    op=ler_numero_inteiro_limites(1,len(opçoes), "Opção:")
    #Se for válida devolvemos a opão escolhida
    return op

def Media(valores):
    """Devolve a média dos valores de um tuple ou lista"""
    
    return sum(valores)/len(valores)





