
"""ARCHIVO DONDE GUARDO LA FUNCION PARA CREAR CADA REGLAS"""

import Codificacion as C
import FNCj as F
import DPLL as D

#FALTA LA REGLA 1
def REGLA1(): #Una situación por turno
    #Implementar aquí la regla 1
    pass


def REGLA2(): #No levitación
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["1","2","3"]
    Turnos=["1","2","3","4","5","6","7","8"]

    vacio_abajo=[]
    for T in Turnos:
        for PX in Palos:
            W="(("+"-("+PX+","+"1, Abajo, "+T+" )Y-("+PX+","+"2, Abajo, "+T+"))Y-("+PX+","+"3, Abajo, "+T+"))"
            vacio_abajo.append(W)

    vacio_medio=[]

    for T in Turnos:
        for PX in Palos:
            W="("+"-("+PX+","+"1, Medio, "+T+" )Y-("+PX+","+"2, Medio, "+T+"))"
            vacio_medio.append(W)


    vacio_arriba=[]
    for T in Turnos:
        for PX in Palos:
            W="-("+PX+","+"1, Medio, "+T+" )"
            vacio_arriba.append(W)

    it=0
    Regla_2_lista=[]
    while it<len(vacio_abajo): #todos tienen la misma longitud, así que no hay ningún problema
        if it==0:
            x="("*(len(vacio_abajo)-2)
            prop="("+x+"("+vacio_abajo[it]+">"+"("+vacio_medio[it]+"Y"+vacio_arriba[it]+"))Y" #OJO
            #prop="("+x+"(p)Y"
            Regla_2_lista.append(prop)

        elif it==len(vacio_abajo)-1:
            prop="("+vacio_abajo[it]+">"+"("+vacio_medio[it]+"Y"+vacio_arriba[it]+"))"+")"#OJO
            #prop="(q))"
            Regla_2_lista.append(prop)

        else:
            prop="("+vacio_abajo[it]+">"+"("+vacio_medio[it]+"Y"+vacio_arriba[it]+")))Y"
            #prop="(r))Y"
            Regla_2_lista.append(prop)
        it+=1
    #print(len(Regla_2_lista))
    archivo=open("Regla_2.txt","w")
    Regla2="" #AQUÍ SE GUARDA TODA LA REGLA SIN CODIFICAR
    #Pasar toda la regla a un archivo txt
    for prop in Regla_2_lista:
        Regla2+=prop;
        archivo.write(prop)
        archivo.write('\n')

    archivo.close()
    retorno=C.CODIFICAR("Regla_2.txt")
    #print(retorno)
    return retorno


def REGLA3(): #No mayor sobre menor
    archivo=open("Regla_3.txt", "w")
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["1","2","3"]
    Turnos=["1","2","3","4","5","6","7","8"]

    lista_aux=[]
    for T in Turnos:
        for PX in Palos:
            W="(("+PX+",1,Abajo,"+T+")<>-("+PX+",2,Medio,"+T+"))Y"
            lista_aux.append(W)
    #for p in lista_aux:
    #    print(p)
    Regla3="("
    i=0
    for i in range(len(lista_aux)):
        if i==len(lista_aux)-1:
            new_line="(("+"PC"+",1,Abajo,"+"8"+")<>-("+"PC"+",2,Medio,"+"8"+"))" #Regla sin Y final
            Regla3+=new_line
        else:
            Regla3+=lista_aux[i]
        i+=1

    Regla3+=")" #final de la regla-> AQUÍ SE GUARDA SIN CODIFICAR
    archivo.write(Regla3)
    archivo.close()
    retorno = C.CODIFICAR("Regla_3.txt")
    return retorno


def REGLA4(): #Un movimiento por turno
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["F1","F2","F3"]
    Turnos=["1","2","3","4","5","6","7","8"]

    #M1,N
    M1N=[]
    i=0
    while i<7:
        for PX in Palos:
            for P in Posiciones:
                W="(("+PX+", 1, "+P+", "+Turnos[i]+")<>("+PX+", 1, "+P+", "+Turnos[i+1]+"))"
                M1N.append(W)
        i+=1

    cont=0
    prop=""
    M1Ndef=[]
    #print(len(M1N))=63
    while cont<63:
        prop="(((((((("+M1N[cont]+"Y"+ M1N[cont+1]+")Y"+M1N[cont+2]+")Y"+M1N[cont+3]+")Y"+M1N[cont+4]+")Y"+M1N[cont+5]+")Y"+M1N[cont+6]+")Y"+M1N[cont+7]+")Y"+M1N[cont+8]+")"
        M1Ndef.append(prop)
        prop=""
        cont+=9

    #LISTO M1N
    #==================================================================================================================
    #M2N

    #Para este hay otras Posiciones
    Posiciones2=["Medio","Abajo"]

    M2N=[]

    i=0
    while i<7:
        for PX in Palos:
            for P in Posiciones2:
                W="(("+PX+", 2, "+P+", "+Turnos[i]+")<>("+PX+", 2, "+P+", "+Turnos[i+1]+"))"
                M2N.append(W)
        i+=1

    cont=0
    prop=""
    M2Ndef=[]
    while cont<42:
        prop="((((("+M2N[cont]+"Y"+M2N[cont+1]+")Y"+M2N[cont+2]+")Y"+M2N[cont+3]+")Y"+M2N[cont+4]+")Y"+M2N[cont+5]+")"
        M2Ndef.append(prop)
        prop=""
        cont+=6



    #Listo M2N
    #==================================================================================================
    #M3N

    #Para este hay otras Posiciones
    Posiciones3=["Abajo"]
    M3N=[]

    i=0
    while i<7:
        for PX in Palos:
            for P in Posiciones3:
                W="(("+PX+", 3, "+P+", "+Turnos[i]+")<>("+PX+", 3, "+P+", "+Turnos[i+1]+"))"#OJO
                M3N.append(W)
        i+=1

    cont=0
    prop=""
    M3Ndef=[]
    #print(len(M3N))=21
    while cont<21:
        prop="(("+M3N[cont]+"Y"+M3N[cont+1]+")Y"+M3N[cont+2]+")"
        M3Ndef.append(prop)
        prop=""
        cont+=3

    #Listo M3N
    #==============================================================================================

    #UNIR LAS REGLAS

    regla=[]
    r=0

    while r<7: #Todas las listas tienen esta longitud
        prop="(((-"+M1Ndef[r]+">"+"("+M2Ndef[r]+"Y"+M3Ndef[r]+"))Y"
        prop+="(-"+M2Ndef[r]+">"+"("+M1Ndef[r]+"Y"+M3Ndef[r]+")))Y"
        prop+="(-"+M3Ndef[r]+">"+"("+M1Ndef[r]+"Y"+M2Ndef[r]+")))"
        regla.append(prop)
        prop=""
        r+=1

    archivo=open("Regla_4.txt","w")


    Regla4="" #String con toda la regla sin codificar

    r=0
    #print("LEN(REGLA)=",len(regla))=7


    while r<7:
        Regla4+="(((((("+regla[r]+"Y"+regla[r+1]+")Y"+regla[r+2]+")Y"+regla[r+3]+")Y"+regla[r+4]+")Y"+regla[r+5]+")Y"+regla[r+6]+")"
        archivo.write(Regla4)
        r+=7

    archivo.close()
    retorno=C.CODIFICAR("Regla_4.txt")
    return retorno



    """===========================|PRUEBAS|========================"""


def REGLA5(): #Solo se mueve el de arriba de la torre
    Posiciones=["Arriba","Medio","Abajo"]
    Palos=["PA","PB","PC"]
    Fichas=["F1","F2","F3"]
    Turnos=["1","2","3","4","5","6","7","8"]

    #M1,N no se necesita en esta regla


    #==================================================================================================================
    #M2N

    #M2N

    #Para este hay otras Posiciones
    Posiciones2=["Medio","Abajo"]

    M2N=[]

    i=0
    while i<7:
        for PX in Palos:
            for P in Posiciones2:
                W="(("+PX+", 2, "+P+", "+Turnos[i]+")<>("+PX+", 2, "+P+", "+Turnos[i+1]+"))"
                M2N.append(W)
        i+=1

    cont=0
    prop=""
    M2Ndef=[]
    while cont<42:
        prop="((((("+M2N[cont]+"Y"+M2N[cont+1]+")Y"+M2N[cont+2]+")Y"+M2N[cont+3]+")Y"+M2N[cont+4]+")Y"+M2N[cont+5]+")"
        M2Ndef.append(prop)
        prop=""
        cont+=6



    #Listo M2N
    #==================================================================================================
    #M3N

    #Para este hay otras Posiciones
    Posiciones3=["Abajo"]
    M3N=[]

    i=0
    while i<7:
        for PX in Palos:
            for P in Posiciones3:
                W="(("+PX+", 3, "+P+", "+Turnos[i]+")<>("+PX+", 3, "+P+", "+Turnos[i+1]+"))"#OJO
                M3N.append(W)
        i+=1

    cont=0
    prop=""
    M3Ndef=[]
    #print(len(M3N))=21
    while cont<21:
        prop="(("+M3N[cont]+"Y"+M3N[cont+1]+")Y"+M3N[cont+2]+")"
        M3Ndef.append(prop)
        prop=""
        cont+=3

    #==============================================================================================

    #UNIR LAS REGLAS
    Nturnos=["1","2","3","4","5","6","7"]

    regla=[]
    i=0

    while i<7:
        for T in Nturnos:
            for PX in Palos:
                pp="(((("+PX+", 2, Abajo, "+T+")Y("+PX+", 1, Medio, "+T+"))>"+M2Ndef[i]+")Y"
                pp+="(((("+PX+", 3, Abajo, "+T+")Y("+PX+", 2, Medio,"+T+"))Y("+PX+", 1, Arriba, "+T+"))>("+M2Ndef[i]+"Y"+M3Ndef[i]+")))"
                regla.append(pp)
            i+=1

    archivo=open("Regla_5.txt","w")

    Regla5="" #Aquí se guarda toda la regla sin codificar

    r=0

    while r<21:
        if r==20:
            Regla5+=regla[r]+")"
            archivo.write(regla[r]+")")
        elif r==0:
            Regla5+="("+regla[r]+"Y"
            archivo.write("("+regla[r]+"Y"+'\n')
        else:
            Regla5+=regla[r]+"Y"
            archivo.write(regla[r]+"Y"+'\n')
        r+=1

    archivo.close()
    retorno = C.CODIFICAR("Regla_5.txt")

    return retorno


def CrearReglas():
    #Archivo para guardar la regla completa por si se quiere ver
    #archivo=open("Regla_final.txt","w")

    regla_f="((("+REGLA2()+"Y"+REGLA3()+")Y"+REGLA4()+")Y"+REGLA5()+")"
    #archivo.write(regla_f)

    #archivo.close()
    return regla_f

#regla="("+REGLA3()+"Y"+REGLA5()+")"
regla=CrearReglas()

print("La formula usada fue: \n", regla)
letras_prop= C.ret_letras_usadas()
print("#####################################################")
ts= F.Tseitin(regla, letras_prop)

print("Tseitin: \n",ts)
l=D.conjunto_de_formulas(ts)
print(l)

"""
print("=====================================================")
lts=D.conjunto_de_formulas(ts)
#print("Lista de clausulas: \n", lts)
#val,I = D.unitPropagate(lts,{})
#print(val,I)
print(D.DPLL(lts,{}))
"""
"""
fClaus = F.formaClausal(ts)
print("Forma clausal: \n")
print(fClaus)
val,I = D.unitPropagate(fClaus,{})
print(val)
"""
