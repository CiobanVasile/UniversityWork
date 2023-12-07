
from errors.errors import RepoError, ValidError, ValidErrorP,ValidErrorC
from model.Student import Student
from model.Problema import Problema

class Console(object):
    pass
    
    def __init__(self,__serviceStud,__serviceProlb,__serviceCatalog):
        self.__serviceStud = __serviceStud
        self.__serviceProlb = __serviceProlb
        self.__serviceCatalog = __serviceCatalog
        

    def __uiAddStud(self,params):
        '''Functie care adauga o entitate student
        '''
        if len(params) != 3:
            print("invalid number of params")
            return 
        try:
            ident = int(params[0])
        except ValueError as ve:
            print("identificator invalid")
        try:
            name = str(params[1])
        except ValueError as ve:
            print("name invalid")
        try:
            grup = int(params[2])
        except ValueError as ve:
            print("grup invalid")
        
        try:
            
            self.__serviceStud.add(ident, name, grup)
        
        except UnboundLocalError as vue:
            print("params empty")
    
    
    def __uiAddProbl(self,params):
        '''Functie care adauga o entitate problema
        '''
        if len(params) != 3:
            print("invalid number of params")
            return 
        params1 = params[0].split("_")
        try:
            nrlab = int(params1[0])
        except ValueError as ve:
            print("nrlab invalid")
        try:
            nrprobl = int(params1[1])
        except ValueError as ve:
            print("nrprobl invalid")
        try:
            dscr= str(params[1])
        except ValueError as ve:
            print("description invalid")
        try:
            ddln = int(params[2])
        except ValueError as ve:
            print("deadline invalid")
        
        try:
        
            self.__serviceProlb.add(nrlab, nrprobl,dscr,ddln)
        
        except UnboundLocalError as vue:
            print("params empty")    
    
    
    
    def __uiPrintStud(self,params):
        '''Functie care printeaza lista de studenti
        '''
        if len(params) !=0:
            print("invalid number of params")
            return
        stud = self.__serviceStud.getAllStudents()
        if len(stud)==0:
            print("Empty list!")
            return
        s = ""
        for x in stud:
            print(str(x))
        
            #s+=str(x.get_ident())+" "+ str(x.get_name()) + " " + str(x.get_grup())+"\n"
        #print(s)
        #print(len(stud))

    
    def __uiPrintProbl(self,params):
        '''Functie care printeaza lista de probleme
        '''
        if len(params) !=0:
            print("invalid number of params")
            return
        probl = self.__serviceProlb.getAllProblems()
        if len(probl)==0:
            print("Empty list!")
            return
        s = ""
        for x in probl:
            s+=str(x.get_nrlab())+ "_"+str(x.get_nrprobl())+ " " + str(x.get_dscr())+ " " + str(x.get_ddln())+"\n"
        print(s)
    
    
    def __uiUpdateStud(self,params):
        '''Functie care face update la entitatea studennt
        '''
        if len(params) != 3:
            print("invalid number of params")
            return 
        try:
            ident = int(params[0])
        except ValueError as ve:
            print("identificator invalid")
        try:
            name = str(params[1])
        except ValueError as ve:
            print("name invalid")
        try:
            grup = int(params[2])
        except ValueError as ve:
            print("grup invalid")
        
        try:
        
            self.__serviceStud.update(ident, name, grup)
    
        except UnboundLocalError as vue:
                print("params empty")    
        
    def __uiUpdateProbl(self,params):
        '''Functie care face update la entitatea problema
        '''
        if len(params) != 3:
            print("invalid number of params")
            return 
        params1 = params[0].split("_")
        try:
            nrlab = int(params1[0])
        except ValueError as ve:
            print("nrlab invalid")
        try:
            nrprobl = int(params1[1])
        except ValueError as ve:
            print("nrprobl invalid")
        try:
            dscr= str(params[1])
        except ValueError as ve:
            print("description invalid")
        try:
            ddln = int(params[2])
        except ValueError as ve:
            print("deadline invalid")
        
        try:
            
            self.__serviceProlb.update(nrlab, nrprobl,dscr,ddln)
        
        except UnboundLocalError as vue:
            print("params empty")    
    
    
    def __uiDeleteStud(self,params):
        ''' Functie care sterge o entitate student cu identificatorul ident
        '''
        if len(params) != 1:
            print("invalid number of params")
            return 
        try:
            ident = int(params[0])
        except ValueError as ve:
            print("identificator invalid")
        '''try:
            name = str(params[1])
        except ValueError as ve:
            print("name invalid")
        try:
            grup = int(params[2])
        except ValueError as ve:
            print("grup invalid")
        '''
        try:
           
            self.__serviceStud.delete(ident)
        
        except UnboundLocalError as vue:
            print("params empty")    
    
    
    def __uiDeleteProbl(self,params):
        '''Functie care sterge entitatea problema cu nrlab_nrprobl
        '''
        if len(params) != 1:
            print("invalid number of params")
            return 
        params1 = params[0].split("_")
        try:
            nrlab = int(params1[0])
        except ValueError as ve:
            print("nrlab invalid")
        try:
            nrprobl = int(params1[1])
        except ValueError as ve:
            print("nrprobl invalid")
        ''' 
        try:
            dscr= str(params[1])
        except ValueError as ve:
            print("description invalid")
        try:
            ddln = int(params[2])
        except ValueError as ve:
            print("deadline invalid")
        '''
        try:
            
            self.__serviceProlb.delete(nrlab, nrprobl)
        
        except UnboundLocalError as vue:
            print("params empty")    
    
    
    def __uiSearchStud(self,params):
        '''Functie care afiseaza o entitate student care este cautata dupa ident
        '''
        if len(params) !=1:
            print("invalid number of params")
            return 
        try:
            ident = int(params[0])
        except ValueError as ve:
            print("identificator invalid")
        
        try:
            x = self.__serviceStud.search(ident)
        
            print(str(x.get_ident())+" "+ str(x.get_name()) + " " + str(x.get_grup())+"\n")
     
        except UnboundLocalError as vue:
            print("params empty")
        
    
    def __uiSearchProbl(self,params):
        '''Functie care afiseaza o entitate Problema care este cautata dupa nrlab_nrprobl
        '''
        if len(params) !=1:
            print("invalid number of params")
            return 
        params1 = params[0].split("_")
        try:
            nrlab = int(params1[0])
        except ValueError as ve:
            print("nrlab invalid")
        try:
            nrprobl = int(params1[1])
        except ValueError as ve:
            print("nrprobl invalid")
        try:
        
            x = self.__serviceProlb.search(nrlab, nrprobl)
            print(str(x.get_nrlab())+ "_"+str(x.get_nrprobl())+ " " + str(x.get_dscr())+ " " + str(x.get_ddln())+"\n")
            
        except UnboundLocalError as vue:
            print("params empty")    
    

    def __uiAddCatalog(self,params):
        '''Functie care adauga o entitate obiect
        '''
        if len(params) != 3:
            print("Invalid number of params")
            return
        param1 = params[1].split("_")
        
        try:
            ident = int(params[0])
        except ValueError as ve:
            print("identificator invalid")
        try:
            nrlab = int(param1[0])
        except ValueError as ve:
            print("invalid nr lab")
        try:
            nrprobl = int(param1[1])
        except ValueError as ve:
            print("invalid nr probl")
            
        try:
            nota = int(params[2])
        except ValueError as ve:
            print("invalid nota")    
            
        try:
        
            self.__serviceCatalog.addCatalog(ident, nrlab, nrprobl,nota)
        
        except UnboundLocalError as vue:
            print("params empty")       
    
    
    def __uiSearchCatalogIdent(self,params):
        '''Functie care afiseaza o entitate din Catalog care este cautata dupa ident
        '''
        if len(params) !=1:
            print("invalid number of params")
            return 
        try:
            ident = int(params[0])
        except ValueError as ve:
            print("identificator invalid")
            
        try:
            x = self.__serviceCatalog.searchNrIdent(ident)
        
            print(x)
     
        except UnboundLocalError as vue:
            print("params empty")
    
    
    def __uiSearchCatalogProbl(self,params):
        '''Functie care afiseaza o entitate din Catalog care este cautata dupa nrlab_nrprobl
        '''
        if len(params) !=1:
            print("invalid number of params")
            return 
        params1 = params[0].split("_")
        try:
            nrlab = int(params1[0])
            nrprobl = int(params1[1])
        except ValueError as ve:
            print("identificator invalid")
            
        try:
            x = self.__serviceCatalog.searchNrProbl(nrlab,nrprobl)
        
            print(x)
     
        except UnboundLocalError as vue:
            print("params empty")
    
    
    def __uiPrintCatalog(self,params):
        '''Functie care afiseaza lista catalog
        '''
        if len(params) !=0:
            print("invalid number of params")
            return
        elems = self.__serviceCatalog.getAllElems()
        if len(elems)==0:
            print("Empty list!")
            return
        s = ""
        for x in elems:
            nrident = x.get_nrident()
            nrlab = x.get_nrlab()
            nrprobl = x.get_nrprobl()
            stud = self.__serviceStud.search(nrident)
            print(str(stud.get_name())+" "+ str(nrlab)+"_"+str(nrprobl)+" " + str(x.get_nota()))
            

        

    
    
    def __uiGenerareStud(self,params):
        '''Functie care genereaza studenti
        '''
        if len(params) !=1:
            print("invalid number of params!")
            return
        try:
            a = int(params[0])
        except ValueError as ve:
            print("Valoare introdusa nu este numar intreg!")
        
        try:
            
            self.__serviceStud.generator(a)  
        
     
        except UnboundLocalError as vue:
            print("params empty")
          
    
    
    def __uiGenerareProbl(self,params):
        '''Functie care genereaza probleme
        '''
        if len(params) !=1:
            print("invalid number of params!")
            return
        try:
            a = int(params[0])
        except ValueError as ve:
            print("Valoare introdusa nu este numar intreg!")
        try:
            
            self.__serviceProlb.generator(a)  
        
     
        except UnboundLocalError as vue:
            print("params empty")
    

    def __uiNoteSub5(self,params):
        '''Functie care afiseaza studentii care au note sub 5
        '''
        if len(params) != 0:
            print("invalid number of params") 
        list = self.__serviceCatalog.notaSub5()
        for x in list:
            nrident = x.get_nrident()
            nrlab = x.get_nrlab()
            nrprobl = x.get_nrprobl()
            stud = self.__serviceStud.search(nrident)
            print(str(stud.get_name())+" "+ str(nrlab)+"_"+str(nrprobl)+" " + str(x.get_nota()))
    def __uiStatistica1(self,params):
        '''Functie care afiseaza lista de studenti si notele lor la o problema de laborator dat, ordonat: alfabetic dupa nume, dupa nota
        '''
        if len(params) != 2:
            print("invalid number of params")
            return
        if params[0]=="1":
            params1 = params[1].split("_")
            list = self.__serviceCatalog.statistica1(int(params1[0]),int(params1[1]))
            
            for  x in list:
                print( str(self.__serviceStud.search(x[0]).get_name()) + " "+str(x[1]) )
        if params[0] == "2":
            params1 = params[1].split("_")
            list = self.__serviceCatalog.statistica1(int(params1[0]),int(params1[1]))
            '''for x in list:
                print(x)
            '''
            nume = []
            note = []
            for x in list:
                nume.append(self.__serviceStud.search(x[0]).get_name())
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
            
    
    
    def __uiGrupeNotesub5(self,params):
        '''Functie care afiseaza o lista cu grupele si cate note sunt sub 5 ordonate dupa numarul de note
        '''
        if len(params) != 0 :
            print("invalid number of params")
        newlist = self.__serviceCatalog.grupe_restante()
        for x in newlist:
            print(str(x[0]) + " " + str(x[1]))
    
    def run(self):
        commands={"grupe":self.__uiGrupeNotesub5, "statistica1":self.__uiStatistica1, "notesub5":self.__uiNoteSub5, "generareP":self.__uiGenerareProbl, "generareS":self.__uiGenerareStud, "printC":self.__uiPrintCatalog, "searchCprobl":self.__uiSearchCatalogProbl, "searchCident":self.__uiSearchCatalogIdent,  "addC":self.__uiAddCatalog,"searchP":self.__uiSearchProbl, "searchS":self.__uiSearchStud, "deleteS":self.__uiDeleteStud,"deleteP":self.__uiDeleteProbl,"addS":self.__uiAddStud,"printS":self.__uiPrintStud,"addP":self.__uiAddProbl, "printP":self.__uiPrintProbl,"updateS":self.__uiUpdateStud,"updateP":self.__uiUpdateProbl}
        
        while True:
            cmd = input(">>")
            params = cmd.split(" ")
            
            if cmd == "exit":
                return 
            elif params[0] in commands:
                try:
                    commands[params[0]] (params[1:])
                except ValueError:
                    print("invalid numeric value given!")
                except RepoError as re:
                    print("Repository Error:")
                    print(re)
                except ValidError as ve:
                    print("ValidationStudent Error:")
                    print(ve)  
                except ValidErrorP as ve:
                    print("ValidationProblem Error:")
                    print(ve) 
                except ValidErrorC as ve:
                    print("ValidationCatalog Error:")
                    print(ve)   
            else:
                print("invalid command!")

