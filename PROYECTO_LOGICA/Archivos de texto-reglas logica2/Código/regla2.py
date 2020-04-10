archivo = open("segundo.txt", "w")

count=1
Posiciones=["Arriba","Medio","Abajo"]
Palos=["PA","PB","PC"]
Fichas=["F1","F2","F3"]
Turnos=["1","2","3","4","5","6","7","8"]
i=0
while i<8:
    for F in Fichas:
        for T in Turnos:
            for PX in Palos:
                if F=="F2" and P == "Arriba":
                    break
                elif F=="F3" and P == "Arriba":
                    break
                elif F=="F3" and P == "Medio":
                    break
                W="( "+PX+", "+ F +", "+ Posiciones[i] +", T"+ T +")"+"-> ¬["
                archivo.write(W)
                archivo.write("\n")
    i+=1

archivo.close()

"""myfile = open("segundo.txt","r")
x = myfile.readlines()
archivo = open("Regla_1.txt", "w")
archivo.seek(0)


for q in x:
    k=q.find("T")
    j=q.find("-")
    t = q[0:j] +  " V "

    h=""
    for P in Posiciones:
        for PX in Palos:
            e=q[6:8]
            if e=="F2" and P == "Arriba":
                break
            elif e=="F3" and P == "Arriba":
                break
            elif e=="F3" and P == "Medio":
                break
            h= h +"( "+PX+", "+ e +", "+ P +", "+ q[k:k+2] +")"+" V "

    h=h.replace(t,"")
    h= h[:184]
    W = q + h + "]"

    archivo.write(W)
    archivo.write("\n"+"\n")
    archivo.write("_"*50+"\n")



archivo.close()
myfile.close()"""
