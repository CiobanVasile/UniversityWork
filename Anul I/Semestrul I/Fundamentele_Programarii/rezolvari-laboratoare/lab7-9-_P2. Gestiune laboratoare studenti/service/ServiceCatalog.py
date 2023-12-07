from model.Catalog import Catalog
from dtos.Dtos import studenti
from model.Student import Student
from model.Problema import Problema
class ServiceCatalog(object):
    
    def __init__(self,__repoStud,__repoProbl,__repoCatalog,__validatorCatalog):
        self.__repoStud = __repoStud
        self.__repoProbl = __repoProbl
        self.__repoCatalog = __repoCatalog
        self.__validatorCatalog = __validatorCatalog
       
        
    def addCatalog(self,nrident, nrlab,nrprobl,nota):
        '''Functie care adauga o entitate noua 
        '''
        entity = Catalog(nrident,nrlab,nrprobl,nota)
        stud = Student(nrident,"Asd",213)
        list = self.__repoStud.getAll()
        self.__repoStud.searchStud(stud)
        probl = Problema(nrlab,nrprobl,"descriere",2)
        self.__repoProbl.searchStud(probl)
        
        self.__validatorCatalog.validateCatalog(entity)
        self.__repoCatalog.addStud(entity)
    
    def searchNrIdent(self,nrident):
        '''Functie care cauta un elem dupa id
        '''
        all = self.__repoCatalog.getAll()
        for elem in all:
            if elem.get_nrident() == nrident:
    
                return elem
    
    def searchNrProbl(self,nrlab,nrprobl):
        all = self.__repoCatalog.getAll()
        for elem in all:
            if elem.get_nrlab() == nrlab and elem.get_nrprobl() == nrprobl:
                
                return elem
    def getAllElems(self):
        '''Functie  care returneaza o copie a listei de catalog
        '''
        return self.__repoCatalog.getAll()
    
    def notaSub5(self):
        '''Functie care returneaza o lista care contine numele studentului si nota pe care a luat o la o problema
        '''
        
        newlist = self.__repoCatalog.getEntityNotaSub5()
        
        return newlist
    def statistica1(self,nrlab,nrprobl):
        '''Functie care returneaza o lista ce contine identificatorul studentului si nota pe care a luat o la o problema, sortata dupa nota
        '''
        newlist = []
        list = self.__repoCatalog.getAll()
        for x in list:
            if x.get_nrlab()== nrlab and x.get_nrprobl()== nrprobl:
                newlist.append(x)
        
    #   return sorted([Top3ActorDTO(x.get_nume(),rez[x]) for x in rez.keys() if x.get_nume().startswith("g")],key=lambda x:x[1],reverse=True)[:3]        

        
        return sorted([(x.get_nrident(),x.get_nota()) for x in newlist],key=lambda x:x[1],reverse=True )
    
    def statistica2(self,nrlab,nrprobl):
        '''Functie care returneaza o lista ce contine identificatorul studentului si nota pe care a luat o la o problema, sortata dupa nota
        '''
        newlist = []
        list = self.__repoCatalog.getAll()
        for x in list:
            if x.get_nrlab()== nrlab and x.get_nrprobl()== nrprobl:
                newlist.append(x)
        
        newlist = sorted([(self.__repoStud.searchId(x.get_nrident()).get_name(),x.get_nota()) for x in newlist],key=lambda x:x[1],reverse=True )
        
        #stud = Student(ident,"None",1)
        
        nume = []
        note = []
        for x in list:
            nume.append(self.__repoStud.searchId(x.get_nrident()).get_name())
            note.append(x[1])
        for i in range (len(nume)-1):
            for j in range (i+1,len(nume)):
                if nume[i]>nume[j]:
                    x1 = nume[i]
                    nume[i] = nume[j]
                    nume[j] = x1
                    x2 = note[i]
                    note[i] = note[j]
                    note[j] = x2    
        for i in range(len(nume)):
            print(nume[i]," ",note[i])
        
        '''
        nume = []
        note = []
        for x in newlist:
            nume.append(self.__repoStud.searchId(int(x[0])).get_name())
            note.append(x[1])
        for i in range (len(nume)-1):
            for j in range (i+1,len(nume)):
                if nume[i]>nume[j]:
                    x1 = nume[i]
                    nume[i] = nume[j]
                    nume[j] = x1
                    x2 = note[i]
                    note[i] = note[j]
                    note[j] = x2 
        newlist1 = []
        for i in range(len(nume)):
            x1 = nume[i]
            newlist1.append(str(nume[i])+" "+str(note[i]))
        return newlist1
       '''
    def grupe_restante(self):
        '''Functie care returneaza o lista sortata dupa nr de note sub 5 la fiecare grupa
        '''
        liststud = self.__repoStud.getAll()
        listcatalog = self.__repoCatalog.getAll()
        newlist = {}
        for x in liststud:
            
            if self.__repoCatalog.searchId(x.get_ident()).get_nota() < 6:
                if x.get_grup() in newlist.keys():
                    newlist[x.get_grup()] +=1
                else:
                    newlist[x.get_grup()] = 1
                    
        return sorted([(x,newlist[x]) for x in newlist.keys()],key=lambda x:x[1],reverse=True)
        
        #return newlist #sorted([()])    
            
    
    
    
    
    
    