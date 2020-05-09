
"""ARCHIVO DONDE GUARDO LA FUNCION PARA CREAR CADA REGLAS"""

import Codificacion as C

#FALTA LA REGLA 1

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
    Regla2="" #AQUÍ SE GUARDA TODA LA REGLA SIN CODIFICAR
    #Pasar toda la regla a un archivo txt
    for prop in Regla_2_lista:
        Regla2+=prop;
        archivo.write(prop)
        archivo.write('\n')

    archivo.close()
    return C.CODIFICAR("Regla_2.txt")


def REGLA3():
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
    return C.CODIFICAR("Regla_3.txt")


def REGLA4():
    archivo=open("cuarto1.txt","w")
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["F1","F2","F3"]
    Turnos=["1","2","3","4","5","6","7","8"]
    i=0
    #M1,N
    while i<7:#para los turnos
        parentesis="["
        archivo.write(parentesis)
        for PX in Palos:
            for P in Posiciones:
                W="[("+PX+", 1, "+P+", "+Turnos[i]+")<>("+PX+", 1, "+P+", "+Turnos[i+1]+")]Y"
                archivo.write(W)
        archivo.write("\n")
        i+=1
    archivo.close()
    amix=open("cuarto1.txt","r")
    test=[]
    lista_de_cuarto1=[]
    lineas_de_cuarto1=amix.readlines()
    for linea in lineas_de_cuarto1:
        lista_de_cuarto1.append(linea)
    for linea in lista_de_cuarto1:
        nueva_linea=linea[0:-2]
        nueva_linea+="]"
        test.append(nueva_linea)
    amix.close()

    archivo_def=open("cuarto1def.txt","w")#en este archivo se encuentra M1,N definitivo    Esta todo unido con "y"
    for linea in test:
        archivo_def.write(linea)
        archivo_def.write('\n')
    archivo_def.close()




    archivo2=open("cuarto2.txt","w")
    Posiciones2=["Medio","Abajo"]
    #M2,n
    I=0
    while I<7:
        parentesis="["
        archivo2.write(parentesis)
        for PX in Palos:
            for P in Posiciones2:
                W="[("+PX+", 2, "+P+", "+Turnos[I]+")<>("+PX+", 2, "+P+", "+Turnos[I+1]+")]Y"
                archivo2.write(W)
        archivo2.write("\n")
        I+=1
    archivo2.close()
    amix2=open("cuarto2.txt","r")
    test2=[]
    lista_de_cuarto2=[]
    lineas_de_cuarto2=amix2.readlines()
    for linea in lineas_de_cuarto2:
        lista_de_cuarto2.append(linea)
    for linea in lista_de_cuarto2:
        nueva_linea=linea[0:-2]
        nueva_linea+="]"
        test2.append(nueva_linea)
    amix2.close()
    archivo_def2=open("cuarto2def.txt","w")#en este archivo se encuentra M2,N definitivo    Esta todo unido con "y"
    for linea in test2:
        archivo_def2.write(linea)
        archivo_def2.write('\n')
    archivo_def2.close()




    archivo3=open("cuarto3.txt","w")
    Posiciones3=["Abajo"]
    #M3,n
    I=0
    while I<7:
        parentesis="["
        archivo3.write(parentesis)
        for PX in Palos:
            for P in Posiciones3:
                W="[("+PX+", 3, "+P+", "+Turnos[I]+")<>("+PX+", 3, "+P+", "+Turnos[I+1]+")]Y"
                archivo3.write(W)
        archivo3.write("\n")
        I+=1
    archivo3.close()
    amix3=open("cuarto3.txt","r")
    test3=[]
    lista_de_cuarto3=[]
    lineas_de_cuarto3=amix3.readlines()
    for linea in lineas_de_cuarto3:
        lista_de_cuarto3.append(linea)
    for linea in lista_de_cuarto3:
        nueva_linea=linea[0:-2]
        nueva_linea+="]"
        test3.append(nueva_linea)
    amix3.close()
    archivo_def3=open("cuarto3def.txt","w")#en este archivo se encuentra M3,N definitivo    Esta todo unido con "y"
    for linea in test3:
        archivo_def3.write(linea)
        archivo_def3.write('\n')
    archivo_def3.close()


    #CREADOR DE LA REGLA5


    myfile = open("cuarto1def.txt","r")
    x = myfile.readlines()
    myfile2 = open("cuarto2def.txt","r")
    y = myfile2.readlines()
    myfile3=open("cuarto3def.txt","r")
    z=myfile3.readlines()
    archivo = open("Regla_4.txt", "w")
    archivo.seek(0)

    datos1=[]
    datos2=[]
    datos3=[]
    test_regla4=[]
    h=""
    for linea in x:
        datos1.append(linea)
    for linea2 in y:
        datos2.append(linea2)
    for linea3 in z:
        datos3.append(linea3)
    ind=0
    archivo.write("[")
    while ind<7:
        if ind<6:
            h="[-"+datos1[ind]+">"+"("+datos2[ind]+"Y"+datos3[ind]+")Y-"+datos2[ind]+">"+"("+datos1[ind]+"Y"+datos3[ind]+")Y-"+datos3[ind]+"("+datos1[ind]+"Y"+datos2[ind]+")]Y"+'\n'+'\n'
            test_regla4.append(h)
            ind+=1
        else:
            h="[-"+datos1[ind]+">"+"("+datos2[ind]+"Y"+datos3[ind]+")Y-"+datos2[ind]+">"+"("+datos1[ind]+"Y"+datos3[ind]+")Y-"+datos3[ind]+"("+datos1[ind]+"Y"+datos2[ind]+")]]"+'\n'+'\n'
            test_regla4.append(h)
            ind+=1

    for linea in test_regla4:
        archivo.write(linea)
    archivo.close()
    myfile.close()
    myfile2.close()
    arch=open("Regla_4.txt", "r")
    x=arch.readlines()

    Regla4="" #AQUÍ SE GUARDA LA REGLA SIN CODIFICAR
    for prop in x:
        Regla4+=prop
    arch.close()
    return C.CODIFICAR("Regla_4.txt")


def REGLA5():
    archivo=open("quinto1.txt","w")
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["F1","F2","F3"]
    Turnos=["1","2","3","4","5","6","7","8"]
    i=0
    #M1,N
    while i<7:#para los turnos
        parentesis="["
        archivo.write(parentesis)
        for PX in Palos:
            for P in Posiciones:
                W="[("+PX+", 1, "+P+", "+Turnos[i]+")<>("+PX+", 1, "+P+", "+Turnos[i+1]+")]Y"
                archivo.write(W)
        archivo.write("\n")
        i+=1
    archivo.close()
    amix=open("quinto1.txt","r")
    test=[]
    lista_de_quinto1=[]
    lineas_de_quinto1=amix.readlines()
    for linea in lineas_de_quinto1:
        lista_de_quinto1.append(linea)
    for linea in lista_de_quinto1:
        nueva_linea=linea[0:-2]
        nueva_linea+="]"
        test.append(nueva_linea)
    amix.close()

    archivo_def=open("quinto1def.txt","w")#en este archivo se encuentra M1,N definitivo    Esta todo unido con "y"
    for linea in test:
        archivo_def.write(linea)
        archivo_def.write('\n')
    archivo_def.close()



    archivo2=open("quinto2.txt","w")
    Posiciones2=["Medio","Abajo"]
    #M2,n
    I=0
    while I<7:
        parentesis="["
        archivo2.write(parentesis)
        for PX in Palos:
            for P in Posiciones2:
                W="[("+PX+", 2, "+P+", "+Turnos[I]+")<>("+PX+", 2, "+P+", "+Turnos[I+1]+")]Y"
                archivo2.write(W)
        archivo2.write("\n")
        I+=1
    archivo2.close()
    amix2=open("quinto2.txt","r")
    test2=[]
    lista_de_quinto2=[]
    lineas_de_quinto2=amix2.readlines()
    for linea in lineas_de_quinto2:
        lista_de_quinto2.append(linea)
    for linea in lista_de_quinto2:
        nueva_linea=linea[0:-2]
        nueva_linea+="]"
        test2.append(nueva_linea)
    amix2.close()
    archivo_def2=open("quinto2def.txt","w")#en este archivo se encuentra M2,N definitivo    Esta todo unido con "y"
    for linea in test2:
        archivo_def2.write(linea)
        archivo_def2.write('\n')
    archivo_def2.close()

    archivo3=open("quinto3.txt","w")
    Posiciones3=["Abajo"]
    #M3,n
    I=0
    while I<7:
        parentesis="["
        archivo3.write(parentesis)
        for PX in Palos:
            for P in Posiciones3:
                W="[("+PX+", 3, "+P+", "+Turnos[I]+")<>("+PX+", 3, "+P+", "+Turnos[I+1]+")]Y"
                archivo3.write(W)
        archivo3.write("\n")
        I+=1
    archivo3.close()
    amix3=open("quinto3.txt","r")
    test3=[]
    lista_de_quinto3=[]
    lineas_de_quinto3=amix3.readlines()
    for linea in lineas_de_quinto3:
        lista_de_quinto3.append(linea)
    for linea in lista_de_quinto3:
        nueva_linea=linea[0:-2]
        nueva_linea+="]"
        test3.append(nueva_linea)
    amix3.close()
    archivo_def3=open("quinto3def.txt","w")#en este archivo se encuentra M3,N definitivo    Esta todo unido con "y"
    for linea in test3:
        archivo_def3.write(linea)
        archivo_def3.write('\n')
    archivo_def3.close()


    #CREADOR DE LA REGLA5
    myfile = open("quinto1def.txt","r")
    x = myfile.readlines()
    myfile2 = open("quinto2def.txt","r")
    y = myfile2.readlines()
    myfile3=open("quinto3def.txt","r")
    z=myfile3.readlines()
    archivo = open("Regla_5.txt", "w")
    archivo.seek(0)

    datos1=[]
    datos2=[]
    datos3=[]
    test_regla5=[]

    h=""
    for linea in x:
        datos1.append(linea)
    for linea2 in y:
        datos2.append(linea2)
    for linea3 in z:
        datos3.append(linea3)
    archivo.write("[")
    nuevos_turnos=["1","2","3","4","5","6","7"]
    ind=0
    while ind<7:
        for turno in nuevos_turnos:
            for Px in Palos:
                if ind!=6 and Px!="PC" and turno!="7":
                    h="[[[("+Px+", 2, Abajo, "+turno+")Y("+Px+", 1, Medio, "+turno+")]>"+datos2[ind]+"]Y[[("+Px+", 3, Abajo, "+turno+")Y("+Px+", 2, Medio,"+turno+")Y("+Px+", 1, Arriba, "+turno+")]>["+datos2[ind]+"Y"+datos3[ind]+"]]]Y"
                    test_regla5.append(h)
                else:
                    h="[[[("+Px+", 2, Abajo, "+turno+")Y("+Px+", 1, Medio, "+turno+")]>"+datos2[ind]+"]Y[[("+Px+", 3, Abajo, "+turno+")Y("+Px+", 2, Medio,"+turno+")Y("+Px+", 1, Arriba, "+turno+")]>["+datos2[ind]+"Y"+datos3[ind]+"]]]Y"
                    test_regla5.append(h)
            ind+=1

    ind2=0
    while ind<21:
        if ind!=20:
            archivo.write(test_regla5[ind2])
            archivo.write("\n"+"\n")
            ind+=1
        else:
            linea=test_regla5[ind]
            linea_nueva=linea[0:-1]
            linea_nueva+="]"
            archivo.write(linea_nueva)
            archivo.write("\n"+"\n")
            ind+=1


    archivo.close()
    myfile.close()
    myfile2.close()
    arch=open("Regla_5.txt","r")
    x=arch.readlines()

    Regla5="" #AQUÍ SE GUARDA LA REGLA SIN CODIFICAR

    for prop in x:
        Regla5+=prop

    arch.close()
    return C.CODIFICAR("Regla_5.txt")


def CrearReglas():
    return "("+REGLA2()+"Y"+REGLA3()+"Y"+REGLA4()+"Y"+REGLA5()+")"
