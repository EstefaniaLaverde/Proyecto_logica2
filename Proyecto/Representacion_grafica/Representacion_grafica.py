class Letra(object):
	def __init__(self,Ficha, Posicion , Palo, Turno):
		self.ficha = Ficha
		self.posicion =  Posicion
		self.palo = Palo
		self.turno = Turno

def Tablero():
    print(" "*7+"Tablero\n")
    print("    |     |     |   ")
    print("    |     |     |   ")
    print("    |     |     |   ")
    print("    |     |     |   ")
    print("|"+"T"*19+"|")

def crear_H():
    print("\n")
    print(" "*8+"Inicio"+"\n")
    print("    |     |     |   ")
    print("    1     |     |   ")
    print("   222    |     |   ")
    print("  33333   |     |   ")
    print("|"+"T"*19+"|")


def Mov(x,lf):
    print("\n")
    print(" "*6+x+"\n")
    print("    |     |     |   ")
    ar="    #     !     ?   "
    me="   !#!   ?#?   $#$  "
    ab="  ?!#!? !?#?! ?$#$? "
    for q in lf:
        if q.ficha == "1":
            if q.posicion == "Arriba":
                if q.palo == "PA":
                    ar=ar.replace("#", "1")
                elif q.palo == "PB":
                    ar=ar.replace("!", "1")
                elif q.palo == "PC":
                    ar=ar.replace("?", "1")

            elif q.posicion == "Medio":
                if q.palo == "PA":
                    ar="    |     |     |   "
                    me=me.replace("!#!", " 1 ")
                elif q.palo == "PB":
                    ar="    |     |     |   "
                    me=me.replace("?#?", " 1 ")
                elif q.palo == "PC":
                    ar="    |     |     |   "
                    me=me.replace("$#$", " 1 ")
            elif q.posicion == "Abajo":
                if q.palo == "PA":
                    ar="    |     |     |   "
                    ab=ab.replace("?!#!?", "  1  ")
                elif q.palo == "PB":
                    ar="    |     |     |   "
                    ab=ab.replace("!?#?!", "  1  ")
                elif q.palo == "PC":
                    ar="    |     |     |   "
                    ab=ab.replace("?$#$?", "  1  ")
        elif q.ficha == "2":
            if q.posicion == "Medio":
                if q.palo == "PA":
                    me=me.replace("!#!", "222")
                elif q.palo == "PB":
                    me=me.replace("?#?", "222")
                elif q.palo == "PC":
                    me=me.replace("$#$", "222")

            elif q.posicion == "Abajo":
                if q.palo == "PA":
                    ab=ab.replace("?!#!?", " 222 ")
                elif q.palo == "PB":
                    ab=ab.replace("!?#?!", " 222 ")
                elif q.palo == "PC":
                    ab=ab.replace("?$#$?", " 222 ")
        elif q.ficha == "3":
            if q.posicion == "Abajo":
                if q.palo == "PA":
                    ab=ab.replace("?!#!?", "33333")
                elif q.palo == "PB":
                    ab=ab.replace("!?#?!", "33333")
                elif q.palo == "PC":
                    ab=ab.replace("?$#$?", "33333")

    ar=ar.replace("#","|")
    ar=ar.replace("!","|")
    ar=ar.replace("?","|")
    me=me.replace("#","|")
    me=me.replace("!"," ")
    me=me.replace("?"," ")
    me=me.replace("$"," ")
    ab=ab.replace("#","|")
    ab=ab.replace("!"," ")
    ab=ab.replace("?"," ")
    ab=ab.replace("$"," ")


    print(ar)
    print(me)
    print(ab)
    print("|"+"T"*19+"|\n")

Mov1=[Letra("1", "Abajo", "PC", "Turno 1" ), Letra("2", "Medio", "PA", "Turno 1" ), Letra("3", "Abajo", "PA", "Turno 1" )]
Mov2=[Letra("1", "Abajo", "PC", "Turno 2" ), Letra("2", "Abajo", "PB", "Turno 2" ), Letra("3", "Abajo", "PA", "Turno 2" )]
Mov3=[Letra("1", "Medio", "PB", "Turno 3" ), Letra("2", "Abajo", "PB", "Turno 3" ), Letra("3", "Abajo", "PA", "Turno 3" )]
Mov4=[Letra("1", "Abajo", "PA", "Turno 4" ), Letra("2", "Abajo", "PB", "Turno 4" ), Letra("3", "Abajo", "PC", "Turno 4" )]
Mov5=[Letra("1", "Abajo", "PA", "Turno 5" ), Letra("2", "Abajo", "PB", "Turno 5" ), Letra("3", "Abajo", "PC", "Turno 5" )]
Mov6=[Letra("1", "Abajo", "PA", "Turno 6" ), Letra("2", "Medio", "PC", "Turno 6" ), Letra("3", "Abajo", "PC", "Turno 6" )]
Mov7=[Letra("1", "Arriba", "PC", "Turno 7" ), Letra("2", "Medio", "PC", "Turno 7" ), Letra("3", "Abajo", "PC", "Turno 7" )]


crear_H()
Mov("Movimiento 1",Mov1)
Mov("Movimiento 2",Mov2)
Mov("Movimiento 3",Mov3)
Mov("Movimiento 4",Mov4)
Mov("Movimiento 5",Mov5)
Mov("Movimiento 6",Mov6)
Mov("Movimiento 7",Mov7)
