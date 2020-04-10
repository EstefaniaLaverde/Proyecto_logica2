import random
lista = []

myfile = open("Letras.txt","r")
x = myfile.readlines()

for q in x:
    q=q.rstrip('\n')
    lista.append(q)

myfile.close()

def Inter():
    dicc ={}
    for x in lista:
        y = random.choice(["0","1"])
        dicc.setdefault(x,y)

    inter_ver=[]

    for x,y in dicc.items():
        if y=="1":
            inter_ver.append(x)
    print(len(inter_ver))

    if len(inter_ver)<25:
        return("Posiblemente")
    else:
        return("Paila Socio")

R=Inter()


"""
count=0
while R!="Posiblemente":
    R=Inter()
    print(R," X",count)
    count+=1
"""
