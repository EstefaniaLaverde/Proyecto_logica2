archivo2=open("quinto2.txt","w")
Posiciones2=["Medio","Abajo"]
Palos=["PA","PB","PC"]
Fichas=["F1","F2","F3"]
Turnos=["1","2","3","4","5","6","7","8"]
#M2,n
I=0
while I<7:
    for PX in Palos:
        for P in Posiciones2:
            W="[("+PX+", 2, "+P+", "+Turnos[I]+")<>("+PX+", 2, "+P+", "+Turnos[I+1]+")]"
            archivo2.write(W)
            archivo2.write("\n")
    I+=1

archivo2.close()
