
def sumaLista(x,list):
    x2 = 0
    for i in range(len(x),len(list)):
        x2+=list[i]
        
    x1 = 0
    for i in range(len(x)):
        if x[i] == 1:
            x1 -= list[i]# 1 pentru -
        else:
            x1 += list[i] # 0 pentru +
    return True if x1+x2>=0 else False  

def printList(x, list):
    
    for i in range(len(x)):
        if x[i] == 1:
            list[i] = list[i]*(-1)
    print(list)
            

def backRecursiv(x,DIM,DOM,list):
    if (len(x)==DIM):
        y = sumaLista(x, list)
        if y == True:
            printList(x,list)
        return
    x.append(0)
    for i in range(0,DOM):
        x[-1] = i
        backRecursiv(x,DIM,DOM,list)
    x.pop()


#############
'''
citim lista de la tastatura ca string si dupa ii facem split, transformand mai apoi in int-uri
si aplicandu-le modulul la fiecare in parte
 '''

list1 =raw_input(">>")
list = list1.split(" ")
for i in range(len(list)):
    list[i] = abs(int(list[i]))

#############
DIM = len(list)
DOM = 2 # vom avea de elemente doar cifre de 1 si 0 -> 1 pentru semnul -, iar 0 pentru +
backRecursiv([],DIM,DOM,list)

###################################################3




