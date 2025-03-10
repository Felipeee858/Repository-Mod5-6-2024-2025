#Coleção F1
'''
PSI - Módulo 6
Coleções - F1
'''
 
GrandePremios = [
    {"Número": 1, "Grande Prêmio": "Barém", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 2, "Grande Prêmio": "Arábia Saudita", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 3, "Grande Prêmio": "Austrália", "Vencedor": "Carlos Sainz Jr.", "Equipe": "Ferrari"},
    {"Número": 4, "Grande Prêmio": "Japão", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 5, "Grande Prêmio": "China", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 6, "Grande Prêmio": "Miami", "Vencedor": "Lando Norris", "Equipe": "McLaren-Mercedes"},
    {"Número": 7, "Grande Prêmio": "Emília-Romanha", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 8, "Grande Prêmio": "Mônaco", "Vencedor": "Charles Leclerc", "Equipe": "Ferrari"},
    {"Número": 9, "Grande Prêmio": "Canadá", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 10, "Grande Prêmio": "Espanha", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 11, "Grande Prêmio": "Áustria", "Vencedor": "George Russell", "Equipe": "Mercedes"},
    {"Número": 12, "Grande Prêmio": "Grã-Bretanha", "Vencedor": "Lewis Hamilton", "Equipe": "Mercedes"},
    {"Número": 13, "Grande Prêmio": "Hungria", "Vencedor": "Oscar Piastri", "Equipe": "McLaren-Mercedes"},
    {"Número": 14, "Grande Prêmio": "Bélgica", "Vencedor": "Lewis Hamilton", "Equipe": "Mercedes"},
    {"Número": 15, "Grande Prêmio": "Países Baixos", "Vencedor": "Lando Norris", "Equipe": "McLaren-Mercedes"},
    {"Número": 16, "Grande Prêmio": "Itália", "Vencedor": "Charles Leclerc", "Equipe": "Ferrari"},
    {"Número": 17, "Grande Prêmio": "Azerbaijão", "Vencedor": "Oscar Piastri", "Equipe": "McLaren-Mercedes"},
    {"Número": 18, "Grande Prêmio": "Singapura", "Vencedor": "Lando Norris", "Equipe": "McLaren-Mercedes"},
    {"Número": 19, "Grande Prêmio": "Estados Unidos", "Vencedor": "Charles Leclerc", "Equipe": "Ferrari"},
    {"Número": 20, "Grande Prêmio": "Cidade do México", "Vencedor": "Carlos Sainz Jr.", "Equipe": "Ferrari"},
    {"Número": 21, "Grande Prêmio": "São Paulo", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 22, "Grande Prêmio": "Las Vegas", "Vencedor": "George Russell", "Equipe": "Mercedes"},
    {"Número": 23, "Grande Prêmio": "Catar", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 24, "Grande Prêmio": "Abu Dhabi", "Vencedor": "Lando Norris", "Equipe": "McLaren-Mercedes"}
]
 
# Quem ganhou o GP do São Paulo
#print(GrandePremios[20]["Vencedor"])

for i in GrandePremios:
    if i["Grande Prêmio"] == "São Paulo":
        print(GrandePremios[len(i)]["Vencedor"])

# Quais os grandes prémios que ganhou a Ferrari
contar=0
for i in GrandePremios:
    if i["Equipe"]=="Ferrari":
        contar+=1
print(f"A Ferrari foi Vencedor {contar} vezes")
 
#Quais os Grande Prémios que um determinado piloto ganhou (escolha do utilizador)
Nome=input("introduza o nome do piloto: ")
lista_grandepremios=[]
for i in GrandePremios:
    if i["Vencedor"]==Nome:
        lista_grandepremios.append(i["Grande Prêmio"])
print(f"Os Grades prêmios do {Nome} foram em {lista_grandepremios}")
        
# Lista de vencedores (só aparece uma vez)
lista_vencedores=[]
for i in GrandePremios:
    if i["Vencedor"] not in lista_vencedores:
        lista_vencedores.append(i["Vencedor"])
print(f"lista dos vencedores são {lista_vencedores}")

#Lista de equipes que ganharam provas (só aparece uma vez)
lista_equipes=[]
for i in GrandePremios:
    if i["Equipe"] not in lista_equipes:
        lista_equipes.append(i["Equipe"])
print(f"lista das Equipes são {lista_equipes}")
#Mostrar quantos grandes prémios ganhou cada um desses pilotos
#Lista com nomes dos vencedores
pilotos_vencedores=[]
for gp in GrandePremios:
    pilotos_vencedores.append(gp["Vencedor"])

for nome in set(pilotos_vencedores):
    vitorias=pilotos_vencedores.count(nome)
    print(f"{nome} - {vitorias}")

