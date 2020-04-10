class Tree():
    def __init__(self, label, left, right):
        self.label = label
        self.left = left
        self.right = right        
    
    
#EJERCICIO 2
        
letrasProposicionales = ['p','q']
interps = []#Lista con todos los diccionaros de interpretacion posible
aux = {}

for a in letrasProposicionales:
    aux[a]=1
interps.append(aux)
for a in letrasProposicionales:
    interps_aux = [i for i in interps]
    for i in interps_aux:
        aux1={}
        for b in letrasProposicionales:
            if a==b:
                aux1[b]=1-i[b]
            else:
                aux1[b]=i[b]         
        interps.append(aux1)
        
#print('Interpretaciones: ')
#for i in interps:
 #   print(i)
    
#La funcion mete en los diccionarios con todas las posibles interpretaciones de las letras propocicionales
def V(A:Tree):
    if A.right == None:
        return i[A.label]
    elif A.label == '¬':
        return 1-V(A.right)
    elif A.label=='Y':
        return V(A.left)*V(A.right)
    elif A.label == 'O':
        if V(A.left)>=V(A.right):
            return V(A.left)
        else:
            return V(A.right)
    elif A.label == '>':
        if 1-V(A.left)>=V(A.right):
            return 1-V(A.left)
        else:
            return V(A.right)
    elif A.label == '<>':
        return 1-(V(A.left)-V(A.right))**2
    
#EJERCICIO 3a
A = Tree('>',Tree('p',None, None),Tree('>',Tree('¬',None,Tree('p',None, None)),Tree('q',None,None)))    
    
for i in interps:
    if (V(A)==1):
        print("Verdadero para ",'\n', i)
    else:
        print("Falso para ",'\n', i)
print("-------------------------")        
#EJERCICIO 3b
        
B = Tree('Y',Tree('¬',None,Tree('p',None,None)),Tree('q',None,None))
for i in interps:
    I=i
    if V(B)==1:
        print("Verdadero para ",'\n', i)
    else:
        print("Falso para ",'\n', i)
print("-------------------------") 
#Ejercicio 3c
C =Tree('Y',Tree('Y',Tree('¬',None,Tree('p',None,None)),Tree('>',Tree('¬',None,Tree('p',None,None)),Tree('¬',None,Tree('q',None,None)))),Tree('q',None,None))
for i in interps:
    if V(C)==1:
        print("Verdadero para ",'\n', i)
    else:
        print("Falso para ",'\n', i)
print("-------------------------")     
    