"""REGLA2: NO LEVITACIÓN"""

def REGLA2():
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["1","2","3"]
    Turnos=["1","2","3","4","5","6","7","8"]

    vacio_abajo=[]
    for T in Turnos:
        for PX in Palos:
            W="("+"-("+PX+","+"1, Abajo, "+T+" )Y-("+PX+","+"2, Abajo, "+T+")Y-("+PX+","+"3, Abajo, "+T+"))"
            vacio_abajo.append(W)

    vacio_medio=[]

    for T in Turnos:
        for PX in Palos:
            W="("+"-("+PX+","+"1, Medio, "+T+" )Y-("+PX+","+"2, Medio, "+T+"))"
            vacio_medio.append(W)


    vacio_arriba=[]
    for T in Turnos:
        for PX in Palos:
            W="("+"-("+PX+","+"1, Medio, "+T+" ))"
            vacio_arriba.append(W)

    it=0
    Regla_2_lista=[]
    while it<len(vacio_abajo): #todos tienen la misma longitud, así que no hay ningún problema
        if it==0:
            prop="["+"("+vacio_abajo[it]+">"+"("+vacio_medio[it]+"Y"+vacio_arriba[it]+"))Y"
            Regla_2_lista.append(prop)

        elif it==len(vacio_abajo)-1:
            prop="("+vacio_abajo[it]+">"+"("+vacio_medio[it]+"Y"+vacio_arriba[it]+"))"+"]"
            Regla_2_lista.append(prop)

        else:
            prop="("+vacio_abajo[it]+">"+"("+vacio_medio[it]+"Y"+vacio_arriba[it]+"))Y"
            Regla_2_lista.append(prop)
        it+=1

    archivo=open("Regla_2.txt","w")

    #Pasar toda la regla a un archivo txt
    for prop in Regla_2_lista:
        archivo.write(prop)
        archivo.write('\n')

    archivo.close()
