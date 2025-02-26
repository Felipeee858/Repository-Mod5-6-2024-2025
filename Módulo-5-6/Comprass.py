"""Pretendemos criar um sistema de recomendações para compras
Para isso deevemos recomendar produtos que o joão ainda não comprou mas que pertencem a uma categoria de produtos que já tenha"""

#compras do joão
João={"TV","Sapatos","Tablet"}
#produtos por categoria
Roupa={"Calções","Casaco","Tshirt"}
Calçado={"Sapatos","Botas","Sapatilha"}
eletrónica={"TV","Tablet","Pc","Xbox"}

#recomendar produtos cuja a categoria pertence a um produto que o João já comprou mas cujo produto ainda não comprou

Roupas=João.intersection(Roupa)
if len(Roupas)>0:
    #os produtos de roupa que o joão ainda não comprou
    dif_roupa=Roupa.difference(João)
    print(dif_roupa)

Calçados=João.intersection(Calçado)
if len(Calçados)>0:
    #os produtos de Calçado que o joão ainda não comprou
    dif_Calçado=Calçado.difference(João)
    print(dif_Calçado)

eletrónicas=João.intersection(eletrónica)
if len(eletrónicas)>0:
    #os produtos de eletrónica que o joão ainda não comprou
    dif_eletrónica=eletrónica.difference(João)
    print(dif_eletrónica)

