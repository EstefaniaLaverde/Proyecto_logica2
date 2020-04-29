def codifica(f, c):
# Funcion que codifica la fila f y columna c
   #Nf = 9#Numero total de filas
    #Nc = 9#Numero total de columnas
    if ((f < 1) or (f > Nf)):
        print("Fila incorrecta! Debe ser un numero entre 1 y", Nf)
        return None
    elif ((c < 1) or (c > Nc)):
        print("Columna incorrecta! Debe ser un numero entre 1 y", Nc)
        return None
    else:
        n = Nc * (f - 1) + c
        return chr(255 + n)


def decodifica(x, Nf, Nc):
# Funcion que codifica un caracter en su respectiva
# fila f y columna c de la tabla
    n = ord(x) - 255
    if ((n < 1) or (n > Nf * Nc)):
        print("Caracter incorrecto! Debe estar entre 1 y", Nf * Nc)
        return None
    else:
        n = n - 1
        f = int(n / Nc) + 1
        c = n % Nc + 1
        return f, c


# Codificacion y decodificacion de una tabla
# de Nf filas y Nc columnas
Nf = 9 # Numero de filas
Nc = 9 # Numero de columnas
letrasProposicionales = [chr(i) for i in range(256, 256 + Nf*Nc)]
print("letrasProposicionales")
for i in range(Nc):
    print(letrasProposicionales[Nf*(i):Nf*(i+1)])

# Intente con varias opciones para fila y columna
fila = 9
columna = 5
print("La fila es", fila)
print("La columna es", columna)
n = codifica(fila, columna)
print("La codificacion es", n)
f, c = decodifica(n, Nf, Nc)
print("La decodificacion es fila", f, "columna", c)
