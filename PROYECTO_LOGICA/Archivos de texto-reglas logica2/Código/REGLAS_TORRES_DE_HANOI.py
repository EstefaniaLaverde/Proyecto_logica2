
"""ARCHIVO DONDE GUARDO LA FUNCION PARA CREAR CADA REGLAS"""

import Codificacion as C

#FALTA LA REGLA 1
def REGLA1(): #Una situación por turno
    #Implementar aquí la regla 1
    pass


def REGLA2(): #No levitación
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
    Regla2="" #AQUÍ SE GUARDA TODA LA REGLA SIN CODIFICAR
    #Pasar toda la regla a un archivo txt
    for prop in Regla_2_lista:
        Regla2+=prop;
        archivo.write(prop)
        archivo.write('\n')

    archivo.close()
    retorno=C.CODIFICAR("Regla_2.txt")
    return retorno


def REGLA3(): #No mayor sobre menor
    archivo=open("Regla_3.txt", "w")
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["1","2","3"]
    Turnos=["1","2","3","4","5","6","7","8"]

    lista_aux=[]
    for T in Turnos:
        for PX in Palos:
            W="("+PX+",1,Abajo,"+T+")<>-("+PX+",2,Medio,"+T+")Y"
            lista_aux.append(W)

    Regla3="("
    i=0
    for i in range(len(lista_aux)):
        if i==len(lista_aux)-1:
            new_line="("+"PC"+",1,Abajo,"+"8"+")<>-("+"PC"+",2,Medio,"+"8"+")" #Regla sin Y final
            Regla3+=new_line
        else:
            Regla3+=lista_aux[i]
        i+=1

    Regla3+=")" #final de la regla-> AQUÍ SE GUARDA SIN CODIFICAR
    archivo.write(Regla3)
    archivo.close()
    retorno = C.CODIFICAR("Regla_3.txt")
    return retorno


def REGLA4(): #Un movimiento por turno
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["F1","F2","F3"]
    Turnos=["1","2","3","4","5","6","7","8"]

    #M1,N
    M1N=[]
    i=0
    while i<7:
        for PX in Palos:
            for P in Posiciones:
                W="[("+PX+", 1, "+P+", "+Turnos[i]+")<>("+PX+", 1, "+P+", "+Turnos[i+1]+")]"
                M1N.append(W)
        i+=1

    cont=0
    prop=""
    M1Ndef=[]
    for pp in M1N:
        if cont==0:
            prop+="["+pp+"Y"
            cont+=1
        elif cont<8:
            prop+=pp+"Y"
            cont+=1
        elif cont==8:
            cont=0
            prop+=pp+"]"
            M1Ndef.append(prop)
            prop=""

    """for p in M1Ndef:
        print(p)"""

    #LISTO M1N
    #==================================================================================================================
    #M2N

    #Para este hay otras Posiciones
    Posiciones2=["Medio","Abajo"]

    M2N=[]

    i=0
    while i<7:
        for PX in Palos:
            for P in Posiciones2:
                W="[("+PX+", 2, "+P+", "+Turnos[i]+")<>("+PX+", 2, "+P+", "+Turnos[i+1]+")]"
                M2N.append(W)
        i+=1

    cont=0
    prop=""
    M2Ndef=[]
    for pp in M2N:
        if cont==0:
            prop+="["+pp+"Y"
            cont+=1
        elif cont<5:
            prop+=pp+"Y"
            cont+=1

        elif cont==5:
            cont=0
            prop+=pp+"]"
            M2Ndef.append(prop)
            prop=""

    """for p in M2Ndef:
        print(p)"""

    #Listo M2N
    #==================================================================================================
    #M3N

    #Para este hay otras Posiciones
    Posiciones3=["Abajo"]
    M3N=[]

    i=0
    while i<7:
        for PX in Palos:
            for P in Posiciones3:
                W="[("+PX+", 3, "+P+", "+Turnos[i]+")<>("+PX+", 3, "+P+", "+Turnos[i+1]+")]"
                M3N.append(W)
        i+=1

    cont=0
    prop=""
    M3Ndef=[]
    for pp in M3N:
        if cont==0:
            prop+="["+pp+"Y"
            cont+=1
        elif cont<2:
            prop+=pp+"Y"
            cont+=1

        elif cont==2:
            cont=0
            prop+=pp+"]"
            M3Ndef.append(prop)
            prop=""

    #Listo M3N
    #==============================================================================================

    #UNIR LAS REGLAS

    regla=[]
    r=0

    while r<7: #Todas las listas tienen esta longitud
        prop="[-"+M1Ndef[r]+">"+"("+M2Ndef[r]+"Y"+M3Ndef[r]+")Y-"+M2Ndef[r]+">"+"("+M1Ndef[r]+"Y"+M3Ndef[r]+")Y-"+M3Ndef[r]+">("+M1Ndef[r]+"Y"+M2Ndef[r]+")]"
        regla.append(prop)
        prop=""
        r+=1

    archivo=open("Regla_4.txt","w")

    Regla4="" #String con toda la regla sin codificar

    r=0

    while r<7:
        if r==6:
            Regla4+=regla[r]+")"
            archivo.write(regla[r]+")")
        elif r==0:
            Regla4+="("+regla[r]+"Y"
            archivo.write("("+regla[r]+"Y"+'\n')
        else:
            Regla4+=regla[r]+"Y"
            archivo.write(regla[r]+"Y"+'\n')
        r+=1
    archivo.close()
    retorno=C.CODIFICAR("Regla_4.txt")
    return retorno


def REGLA5(): #Solo se mueve el de arriba de la torre
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["F1","F2","F3"]
    Turnos=["1","2","3","4","5","6","7","8"]

    #M1,N no se necesita en esta regla


    #==================================================================================================================
    #M2N

    #Para este hay otras Posiciones
    Posiciones2=["Medio","Abajo"]

    M2N=[]

    i=0
    while i<7:
        for PX in Palos:
            for P in Posiciones2:
                W="[("+PX+", 2, "+P+", "+Turnos[i]+")<>("+PX+", 2, "+P+", "+Turnos[i+1]+")]"
                M2N.append(W)
        i+=1

    cont=0
    prop=""
    M2Ndef=[]
    for pp in M2N:
        if cont==0:
            prop+="["+pp+"Y"
            cont+=1
        elif cont<5:
            prop+=pp+"Y"
            cont+=1

        elif cont==5:
            cont=0
            prop+=pp+"]"
            M2Ndef.append(prop)
            prop=""

    """for p in M2Ndef:
        print(p)"""

    #Listo M2N
    #==================================================================================================
    #M3N

    #Para este hay otras Posiciones
    Posiciones3=["Abajo"]
    M3N=[]

    i=0
    while i<7:
        for PX in Palos:
            for P in Posiciones3:
                W="[("+PX+", 3, "+P+", "+Turnos[i]+")<>("+PX+", 3, "+P+", "+Turnos[i+1]+")]"
                M3N.append(W)
        i+=1

    cont=0
    prop=""
    M3Ndef=[]
    for pp in M3N:
        if cont==0:
            prop+="["+pp+"Y"
            cont+=1
        elif cont<2:
            prop+=pp+"Y"
            cont+=1

        elif cont==2:
            cont=0
            prop+=pp+"]"
            M3Ndef.append(prop)
            prop=""

    #Listo M3N
    #==============================================================================================

    #UNIR LAS REGLAS
    Nturnos=["1","2","3","4","5","6","7"]

    regla=[]
    i=0

    while i<7:
        for T in Nturnos:
            for PX in Palos:
                pp="(((("+PX+", 2, Abajo, "+T+")Y("+PX+", 1, Medio, "+T+"))>"+M2Ndef[i]+")Y((("+PX+", 3, Abajo, "+T+")Y("+PX+", 2, Medio,"+T+")Y("+PX+", 1, Arriba, "+T+"))>("+M2Ndef[i]+"Y"+M3Ndef[i]+")))"
                regla.append(pp)
            i+=1

    archivo=open("Regla_5.txt","w")

    Regla5="" #Aquí se guarda toda la regla sin codificar

    r=0

    while r<21:
        if r==20:
            Regla5+=regla[r]+")"
            archivo.write(regla[r]+")")
        elif r==0:
            Regla5+="("+regla[r]+"Y"
            archivo.write("("+regla[r]+"Y"+'\n')
        else:
            Regla5+=regla[r]+"Y"
            archivo.write(regla[r]+"Y"+'\n')
        r+=1

    archivo.close()
    retorno = C.CODIFICAR("Regla_5.txt")

    return retorno


def CrearReglas():
    return "("+REGLA2()+"Y"+REGLA3()+"Y"+REGLA4()+"Y"+REGLA5()+")"


print(CrearReglas())
