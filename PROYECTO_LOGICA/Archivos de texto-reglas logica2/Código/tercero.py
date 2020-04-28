archivo=open("Regla_3_aux.txt", "w")
Posiciones=["Arriba","Medio","Abajo"]
Palos=["PA","PB","PC"]
Fichas=["F1","F2","F3"]
Turnos=["1","2","3","4","5","6","7","8"]


for T in Turnos:
    for PX in Palos:
        W="("+PX+",1,Abajo,"+T+")<>¬("+PX+",2,Medio,"+T+")Y"
        archivo.write(W)
        archivo.write("\n")

archivo.close()

archivo2=open("Regla_3_aux.txt", "r")
x=archivo2.readlines()

regla3=[]
for l in range(len(x)):

    if l==len(x)-1:
        new_line="("+"PC"+",1,Abajo,"+"8"+")<>¬("+"PC"+",2,Medio,"+"8"+")"
        regla3.append(new_line)
    else:
        regla3.append(x[l])
archivo2.close()
archivo_final=open("Regla_3.txt","w")
for linea in regla3:
    archivo_final.write(linea)

archivo_final.close()
