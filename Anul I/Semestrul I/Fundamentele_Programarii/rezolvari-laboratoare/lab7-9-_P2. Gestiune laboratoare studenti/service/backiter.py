from service.backrec import backRecursiv





def solutionFound(x, dim):
    print(x)

def ecuatie(opperators):
    '''
    Functie care calculeaza ecuatia candidat
    '''
    ecuatie=0
    for i in range(0,len(opperators)):
        if opperators[i] == 1:
            ecuatie -= list[i]
        else:
            ecuatie += list[i]
    return ecuatie

def sumaRamasa(opperators):
    '''
    Functie care calculeaza suma elementelor din lista care nu au fost inca implicate in ecuatia candidat
    '''
    suma = sumaTotala
    for i in range(0,len(opperators)):
        suma -= list[i]
    return suma


def consistent(opperators):
    '''
    Functie booleana
    true: lungimea listei de operatori este egala cu lungimea listei data de numere
    false: altfel
    '''    
    ecuatiaNumerelor = ecuatie(opperators)
    sumaElementelorRamase = sumaRamasa(opperators)
    return ecuatiaNumerelor + sumaElementelorRamase > 0

def solution(x, DIM):
    """
    The candidate x is a solution if
    we have all the elements in the permutation
    """
    return len(x)==DIM


def backIter(dim):
    x=[-1] #candidate solution
    while len(x)>0:
        choosed = False
        while not choosed and x[-1]<2:
            x[-1] = x[-1]+1 #increase the last component
            choosed = consistent(x)
        if choosed:
            if solution(x, dim):
                solutionFound(x, dim)
            x.append(-1) # expand candidate solution
        else:
            x = x[:-1] #go back one 


list1 =raw_input(">>")
list = list1.split(" ")
sumaTotala = 0
for i in range(len(list)):
    list[i] = abs(int(list[i]))
    sumaTotala +=list[i]

#backIter(3)







for i in range(len(list)):
    list[i] = abs(int(list[i]))

#############
DIM = len(list)
DOM = 2
backRecursiv([],DIM,DOM,list)