
# Python program for implementation of CombSort 
  
# To find next gap from current 
def getNextGap(gap): 
  
    # Shrink gap by Shrink factor 
    gap = (gap * 10)/13
    if gap < 1: 
        return 1
    return gap 
  
# Function to sort list[] using Comb Sort 
def combSort(list): 
    n = len(list) 
  
    # Initialize gap 
    gap = n 
  
    # Initialize swapped as true to make sure that 
    # loop runs 
    swapped = True
  
    # Keep running while gap is more than 1 and last 
    # iteration caused a swap 
    while gap !=1 or swapped == 1: 
  
        # Find next gap 
        gap = getNextGap(gap) 
  
        # Initialize swapped as false so that we can 
        # check if swap happened or not 
        swapped = False
  
        # Compare all elements with current gap 
        for i in range(0, n-gap): 
            if list[i] > list[i + gap]: 
                list[i], listi + gap]=list[i + gap], list[i] 
                swapped = True
  
  

    
            #######  Insertion Sort   ######
def insertionSort(list, key, reversed):
    '''
    insertion sort
    '''
    '''
    Complexitate:
    
    caz favorabil: elementele sunt deja sortate, T(n) = O(n) (complexitate liniara)
    caz nefavorabil: elementele sunt sortate in ordine inversa, T(n) = O(n^2)
    caz mediu/general: elementele sunt aranjate aleatoriu, complexitate medie: T(n) = O(n^2)
    '''
    rez = list
    
    for i in range(1,len(rez)):
        ind = i-1
        a = rez[i]
        '''crescator'''
        if reversed == False:
            while ind>=0 and key(a)<key(rez[ind]):
                rez[ind+1] = rez[ind]
                ind = ind-1
        '''descrescator'''
        if reversed == True:
            while ind>=0 and key(a)>key(rez[ind]):
                rez[ind+1] = rez[ind]
                ind = ind-1
        rez[ind+1] = a


            ####### Merge Sort ###############

#Exemplu: lista= mergesort(lista,keynota,int(params[2]))
        #///int(params[2] e reverse ul care e 1 pt cresc si -1 pt descr



def keyident(entity):
    return entity.get_ident()
    
    
def keyname(entity):
    return entity.get_name()
    
    
def keygrup(entity):
    return entity.get_grup()


def merge(l,r,key,rev):
    #rev -  1 pentru crescator si -1 pentru descrescator
    
    posl = 0
    posr = 0
    rez=[]
    if rev == 1:
        while posl < len(l) and posr < len(r):
            if key(l[posl])<=key(r[posr]):
                rez.append(l[posl])
                posl +=1
            else:
                rez.append(r[posr])
                posr +=1
        while posl<len(l):
            rez.append(l[posl])
            posl +=1
        while posr<len(r):
            rez.append(r[posr])
            posr +=1
        return rez
    
    elif rev == -1:
        while posl < len(l) and posr < len(r):
            if key(l[posl])>=key(r[posr]):
                rez.append(l[posl])
                posl +=1
            else:
                rez.append(r[posr])
                posr +=1
        while posl<len(l):
            rez.append(l[posl])
            posl +=1
        while posr<len(r):
            rez.append(r[posr])
            posr +=1
        return rez
        
def mergesort(v,key,rev):
    if v==[]:
        return [] 
    else:
        if len(v)==1:
            return [v[0]]
        else merge(mergesort(v[:len(v)//2],key,rev) , mergesort(v[len(v)//2:],key,rev),key,rev)

