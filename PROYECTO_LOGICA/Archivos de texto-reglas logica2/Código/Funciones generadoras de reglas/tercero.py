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

    Regla3+=")" #final de la regla
    archivo.write(Regla3)
    archivo.close()
