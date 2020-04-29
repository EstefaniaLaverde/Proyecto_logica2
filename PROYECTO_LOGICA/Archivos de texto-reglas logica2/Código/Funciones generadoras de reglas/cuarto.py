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
    print("len(test1)= ",len(test))








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
    print("len(test2)= ",len(test2))








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
    print("len(test3)= ",len(test2))





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
            h="[¬"+datos1[ind]+">"+"("+datos2[ind]+"Y"+datos3[ind]+")Y¬"+datos2[ind]+">"+"("+datos1[ind]+"Y"+datos3[ind]+")Y¬"+datos3[ind]+"("+datos1[ind]+"Y"+datos2[ind]+")]Y"+'\n'+'\n'
            test_regla4.append(h)
            ind+=1
        else:
            h="[¬"+datos1[ind]+">"+"("+datos2[ind]+"Y"+datos3[ind]+")Y¬"+datos2[ind]+">"+"("+datos1[ind]+"Y"+datos3[ind]+")Y¬"+datos3[ind]+"("+datos1[ind]+"Y"+datos2[ind]+")]]"+'\n'+'\n'
            test_regla4.append(h)
            ind+=1
    print("len(test_regla4)= ",len(test_regla4))
    for linea in test_regla4:
        archivo.write(linea)
    archivo.close()
    myfile.close()
    myfile2.close()
