#"""CREAR EL DICCIONARIO PARA LAS REGLAS"""

archivo=open("Regla_3.txt","r")
l=archivo.readlines()

Posiciones=["Arriba","Medio","Abajo"]
Palos=["PA","PB","PC"]
Fichas=["1","2","3"]
Turnos1=["1","2","3","4","5","6","7","8"]
Posiciones2=["Medio","Abajo"]
Posiciones3=["Abajo"]



#Codificación de la ficha 1
ficha_1=[]
for turno in Turnos1:
    for pos in Posiciones:
        for palo in Palos:
            ficha_1.append("("+palo+","+"1"+","+pos+","+turno+")")

#Codificación de la ficha 2
ficha_2=[]
for turno in Turnos1:
    for pos in Posiciones2:
        for palo in Palos:
            ficha_2.append("("+palo+","+"2"+","+pos+","+turno+")")

#Codificación de la ficha 3
ficha_3=[]
for turno in Turnos1:
    for pos in Posiciones3:
        for palo in Palos:
            ficha_3.append("("+palo+","+"3"+","+pos+","+turno+")")

lista_letras_largas=[] #ESTA LISTA VA A ACTUAR COMO lista_prop EN crear_diccionario
for p in ficha_1:
    lista_letras_largas.append(p)
for p in ficha_2:
    lista_letras_largas.append(p)
for p in ficha_3:
    lista_letras_largas.append(p)

print(len(lista_letras_largas))

def crear_diccionario(lista_prop, lista_letra):
    #lista_prop tiene la letra larga (PA, 1, Medio, 3), y lista_letra tiene un char
    #La llave va a ser prop y el valor el char
    dicc_letras={}
    i=0;
    while i<144:
        dicc_letras[lista_prop[i]]=lista_letra[i]
        i+=1;
    return dicc_letras
