from errors.errors import RepoError
class Repository(object):
    "crud operations"
    
    def __init__(self):
        self._elems = []
    
 
    def __len__(self):
        return len(self._elems) 
    
    def searchId(self,ident):
        for elem in self._elems:
            if elem == ident:
                return elem
        
    def addStud(self,Stud):
        '''Functie care adauga obiectul stud in lista 
        '''
        
        if Stud in self._elems:
            raise RepoError("existing element!")
        self._elems.append(Stud)

    
    def searchStud(self,Stud):
        '''Functie care cauta obiectul in lista si il returneaza sau returneaza o eroare in caz contrar
        '''
        if Stud not in self._elems:
            raise RepoError("inexisting element!")
        for x in self._elems:
            if x == Stud:
                return x


    
    def deleteStudent(self,Stud):
        '''Functie care sterge obiectul Stud din lista
        '''
        if Stud not in self._elems:
            raise RepoError("inexistent element!")
        for x in range (len(self._elems)):
            if self._elems[x] == Stud:
                del self._elems[x]
                return
    
    def updateStud(self,Stud):
        '''functie care innoieste atributele obiectului stud
        '''
        if Stud not in self._elems:
            raise RepoError("inexistent element!")
        for x in range(len(self._elems)):
            if self._elems[x] == Stud:
                self._elems[x] = Stud
                return

    
    def getAll(self):
        '''functie care returneaza o copie a listei de elemente
        '''
        return self._elems[:]
    
    def getEntityNotaSub5(self):
        newlist = []
        for elem in self._elems:
            if elem.get_nota()<5:
                newlist.append(elem)
        return newlist        
    def dellist(self):
        while (len(self._elems)!= 0):
            self._elems.pop(0)
    
                
    
    
        


