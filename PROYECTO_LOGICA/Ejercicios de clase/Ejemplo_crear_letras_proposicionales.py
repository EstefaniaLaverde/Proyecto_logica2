#TORRES DE HANOI-PROYECTO DE LÓGICA

#Crear todas las letras proposicionales:
#   Como hay diez cilindros se crean 6 letras proposicionales por cada una

letras_prop=[chr(i) for i in range(97, 157)]#Se crean las letras proposicionales, 60 en total


# Reglas del juego:
#   1. Solo se puede mover un cilindro a la vez
#   2. No puede haber un cilindro de mayor radio encima de uno de menor radio

#1.
regla1=' '
inicial = True # Para inicializar la primera conjuncion
aux1 = [x for x in letras_prop] # Inicializa aux1
for p in letras_prop:
    aux1 = [x for x in aux1 if x != p] # Todas las letras excepto p
    aux2 = [x for x in aux1] # Inicializa aux2
    for q in aux1:
        aux2 = [x for x in aux2 if x != q] # Todas las letras excepto p y q
        for r in aux2:
            literal = r + q + p + 'Y'
            aux3 = [x + '-' for x in letras_prop if (x != r and x != q and x != p)]
            for k in aux3:
                literal = k + literal + 'Y'
                if inicial: # Inicializar la primera conjuncion
                    regla1 = literal
                    inicial = False
                else: # Continua incluyendo conjuncion
                    regla1 = literal + regla1 + 'O'

print(regla1)
