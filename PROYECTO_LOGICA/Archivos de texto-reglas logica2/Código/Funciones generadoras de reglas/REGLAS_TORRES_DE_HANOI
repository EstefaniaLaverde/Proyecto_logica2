def REGLA2():
    archivo = open("segundo.txt", "w")

    count=1
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["F1","F2","F3"]
    Turnos=["1","2","3","4","5","6","7","8"]
    i=0
    while i<8:
        for PX in Palos:
            for T in Turnos:
                W="[¬("+PX+","+ "F1" +", "+ "Abajo" +","+ T +")"+"Y¬("+PX+","+"F2,"+"Abajo,"+T+")"+"Y¬("+PX+","+"F3,"+"Abajo,"+T+")->"+"["
                archivo.write(W)
                archivo.write("\n")
        i+=1

    archivo.close()

    archivo2=open("segundo2.txt","w")
    j=0
    while j<8:
        for PX in Palos:
            for T in Turnos:
                WW="¬("+PX+","+ "F1" +","+ "Medio" +","+ T +")"+"Y¬("+PX+","+"F2,"+"Medio,"+T+")"+" Y ¬("+PX+",F1, Arriba,"+T+")]]Y"
                archivo2.write(WW)
                archivo2.write("\n")
        j+=1

    archivo2.close()



    myfile = open("segundo.txt","r")
    x = myfile.readlines()
    myfile2 = open("segundo2.txt","r")
    y = myfile2.readlines()
    archivo = open("Regla_2.txt", "w")
    archivo.seek(0)

    datos1=[]
    datos2=[]
    h=""
    for linea in x:
        datos1.append(linea)

    for linea2 in y:
        datos2.append(linea2)
    for i in range(0,len(datos1)):
        h=datos1[i]+datos2[i]
        archivo.write(h)
        archivo.write("\n"+"\n")
        archivo.write("_"*50+"\n")


    archivo.close()
    myfile.close()
    myfile2.close()


def REGLA3():
    archivo=open("Regla_3_aux.txt", "w")
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["F1","F2","F3"]
    Turnos=["1","2","3","4","5","6","7","8"]


    for T in Turnos:
        for PX in Palos:
            W="("+PX+",F1,Abajo,"+T+")<>¬("+PX+",F2,Medio,"+T+")Y"
            archivo.write(W)
            archivo.write("\n")

    archivo.close()

    archivo2=open("Regla_3_aux.txt", "r")
    x=archivo2.readlines()

    regla3=[]
    for l in range(len(x)):

        if l==len(x)-1:
            new_line="("+"PC"+",F1,Abajo,"+"8"+")<>¬("+"PC"+",F2,Medio,"+"8"+")"
            regla3.append(new_line)
        else:
            regla3.append(x[l])
    archivo2.close()
    archivo_final=open("Regla_3.txt","w")
    for linea in regla3:
        archivo_final.write(linea)

    archivo_final.close()
