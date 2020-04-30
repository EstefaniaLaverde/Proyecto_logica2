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
                W="[-("+PX+","+ "F1" +", "+ "Abajo" +","+ T +")"+"Y-("+PX+","+"F2,"+"Abajo,"+T+")"+"Y-("+PX+","+"F3,"+"Abajo,"+T+")->"+"["
                archivo.write(W)
                archivo.write("\n")
        i+=1

    archivo.close()

    archivo2=open("segundo2.txt","w")
    j=0
    while j<8:
        for PX in Palos:
            for T in Turnos:
                WW="-("+PX+","+ "F1" +","+ "Medio" +","+ T +")"+"Y-("+PX+","+"F2,"+"Medio,"+T+")"+" Y -("+PX+",F1, Arriba,"+T+")]]Y"
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
