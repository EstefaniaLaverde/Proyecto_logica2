letras_prop=[]
inicializador=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"]
inicializador2=["1","2","3","4","5","6","7","8"]
for n in inicializador2:
    for l in inicializador:
        letras_prop.append(l+n)

nuevo_lp=[]
for i in letras_prop:
    nuevo_lp.append(i[0]+"_"+"{"+i[1]+"}")


#Inicializador
posiciones=["arriba","medio","bajo"]
fichas=["1","2","3"]
turnos=inicializador2
palos=["A","B","C"]
#ficha,pos,palo,tueno
posiciones2=["medio","bajo"]
posiciones3=["bajo"]
#Codificación de la ficha 1
ficha_1=[]
for turno in turnos:
    for pos in posiciones:
        for palo in palos:
            ficha_1.append("("+"1"+","+pos+","+palo+","+turno+")")

#Codificación de la ficha 2
ficha_2=[]
for turno in turnos:
    for pos in posiciones2:
        for palo in palos:
            ficha_2.append("("+"2"+","+pos+","+palo+","+turno+")")

#Codificación de la ficha 3
ficha_3=[]
for turno in turnos:
    for pos in posiciones3:
        for palo in palos:
            ficha_3.append("("+"3"+","+pos+","+palo+","+turno+")")


PaloBC=["PB","PC"]
R=""
b="P(1,arriba,PA,1)->-"
R=R+b
for pos in posiciones:
    for p in PaloBC:
        a="(P(1,"+pos+","+p+",1)O"
        R=R+a
fin=")"
R=R+fin
print(R)

for cod in ficha_1:
    lista_aux=ficha_1
