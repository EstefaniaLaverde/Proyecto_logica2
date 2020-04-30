"""=====FUNCIONES PARA PASAR LAS REGLAS A ARBOLES====="""


"""FUNCION QUE LA LISTA CON LAS LETRAS PROPOSICIONALES LARGAS"""

def crear_lista_letras_largas(): #Las letras "largas" tienen la forma (PA,1,Arriba,1)

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

    return lista_letras_largas

lista_letras_largas=crear_lista_letras_largas()

#Esta lista letras contiene la letra correspondiente a cada letra larga, que se unen en un diccionario
letras=['J', 'ħ', 'ί', 'ζ', 'É', 'j', 'Ắ', 'Ớ', 'Ẁ', 'Ī', 'ř', 'Ķ', 'Ễ', 'ớ', 'э', 'ⁿ', 'Ā', 'ы', 'c', 'ü', 'Ô', 'ł', 'K', 'đ', 'Ó', 'ь', 'Ŀ', 'Ề', 'Ð', 'ó', 'Ч', 'q', 'Ľ', 'Ј', 'ć', 'ý', 'ų', 'С', 'Р', 'o', 'Ę', 'Ҝ', 'у', 'В', 'H', 'Θ', 'О', 'ĉ', 'ν', 'Ң', 'А', 'z', 'ự', 'η', 'Ẵ', 'ẃ', 'ŷ', 'х', 'œ', 'Ä', '฿', 'Ằ', 'Ŏ', 'Ď', 'ј', 'ē', 'Z', 'ử', 'Ο', 'Ў', 'Ό', 'М', 'Ε', 'ŏ', 'Є', 'н', 'Ђ', 'ŵ', 'қ', 'Ŝ', 'ņ', 'д', 'п', 'Ö', 'Қ', 'Б', 'Ν', 'Ể', 'т', 'Ĺ', 'с', 'Ů', 'Џ', 'Х', 'h', 'Â', 'ї', 'Ò', '£', 'μ', 'Ă', 'Ặ', 'Ѓ', 'Ζ', 'о', 'ã', 'ĩ', 'ằ', 'ọ', 'Ŭ', 'ς', 'Ù', 'ð', 'Ъ', 'ö', 'Ҳ', 'Ç', 'n', 'ο', 'ů', 'è', 'Į', 'Ẃ', 'Μ', 'Á', 'Č', 'ŋ', 'υ', 'β', 'ī', 'Ş', 't', 'ª', 'ž', 'κ', 'ш', 'G', 'Í', 'Ї', '∑', 'ĸ', 'Ќ', 'ђ', 'Ģ']



"""FUNCIÓN QUE CREA EL DICCIONARIO FINAL CON LAS LETRAS PROPOSICIONALES"""

def crear_diccionario(lista_prop, lista_letra):
    #lista_prop tiene la letra larga (PA, 1, Medio, 3), y lista_letra tiene un char
    #La llave va a ser prop y el valor el char
    dicc_letras={}
    i=0;
    while i<144:
        dicc_letras[lista_prop[i]]=lista_letra[i]
        i+=1;
    return dicc_letras


Diccionario_final=crear_diccionario(lista_letras_largas, letras) #Aquí guardo el diccionario que voy a usar para cambiar las letras en las reglas
#print(len(Diccionario_final))
#print(Diccionario_final)


"""FUNCIÓN PARA TRANSFORMAR UNA REGLA CON LAS LETRAS CORTAS"""

def letras_largas_a_cortas(regla, diccionario_traducci):
    #input: un string con toda la regla y el diccionario para cambiar las letras
    #output: la misma regla pero con las nuevas letras proposicionales de un caracter.

    #Elimino los espacios si hay alguno
    regla=regla.replace(" ", "")
    #Elimino "[]" si hay alguno y los cambio por "()"
    regla=regla.replace("[","(")
    regla=regla.replace("]",")")
    #Elimino los saltos de linea
    regla=regla.rstrip('\n')

    long_regla=len(regla)
    contador=0

    while contador<long_regla:
        if(contador==len(regla)):
            break
        else:
            if regla[contador]=="(" and regla[contador+1]=="P": #Si está iniciando una letra proposicional (P....)

                if regla[contador+10]=="b": #Como arriba tiene más letras que medio y abajo toca hacer una distinción
                    letra_prop_larga=regla[contador:contador+15]
                    nueva_letra=diccionario_traducci[letra_prop_larga]

                    regla=regla[0:contador]+nueva_letra+regla[contador+15:]

                else: #Si la proposición contiene abajo o medio
                    letra_prop_larga=regla[contador:contador+14]
                    nueva_letra=diccionario_traducci[letra_prop_larga]

                    regla=regla[0:contador]+nueva_letra+regla[contador+14:]

            contador+=1

    return regla



#"""Prueba de la función"""
#regla_test="((PA, 1, Arriba, 6)Y((PA ,1 ,Medio ,2)Y(PB,1,Abajo,7)))"
#print("Regla inicial: ",regla_test)
#nueva_regla=letras_largas_a_cortas(regla_test,Diccionario_final)

#print("Regla final: ",nueva_regla)
#"""FUNCIONA!!"""


"""FUNCIÓN QUE PREPARA LA REGLA PARA CAMBIARLE LAS LETRAS"""

def preparar_regla_para_cambiar_letras(archivo_de_texto):
    #input: archivo de texto con la regla. El archivo debe tener la siguiente forma: "ejemplo.txt"
    #output: string con la regla sin saltos de linea
    archivo=open(archivo_de_texto,"r")
    lineas=archivo.readlines()

    str_regla=""

    for linea in lineas:
        contador=0
        while contador<len(linea):
            if contador==len(linea):
                contador=0
                break
            else:
                if linea[contador]=='\n':
                    linea=linea[:contador]+linea[contador+1:]
                contador+=1

        str_regla+=linea

    str_regla=str_regla.strip()
    archivo.close()
    return str_regla


#"""Prueba de la función""""
#regla_lista=preparar_regla_para_cambiar_letras("Regla_5_test.txt")
#regla_nuevos_char=letras_largas_a_cortas(regla_lista, Diccionario_final)

#print(regla_nuevos_char)
