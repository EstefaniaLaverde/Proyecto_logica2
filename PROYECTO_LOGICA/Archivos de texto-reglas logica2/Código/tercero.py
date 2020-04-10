archivo=open("Regla_3.txt", "w")
Posiciones=["Arriba","Medio","Abajo"]
Palos=["PA","PB","PC"]
Fichas=["F1","F2","F3"]
Turnos=["1","2","3","4","5","6","7","8"]

i=0
while i<8:
    for T in Turnos:
        for PX in Palos:
            W="("+PX+", 1, Abajo, "+T+")<>¬("+PX+", 2, Medio, "+T+")Y"
            archivo.write(W)
            archivo.write("\n")
    i+=1

archivo.close()
