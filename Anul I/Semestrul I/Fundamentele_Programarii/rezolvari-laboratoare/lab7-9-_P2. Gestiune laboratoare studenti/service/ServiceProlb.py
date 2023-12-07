from model.Problema import Problema

class ServiceProbl(object):
    
    def __init__(self,repo,valid):
        self.__repo = repo
        self.__validator = valid

    def add(self,nrlab, nrprobl, dscr, ddln):
        Probl = Problema(nrlab, nrprobl, dscr, ddln)
        self.__validator.ValidateProbl(Probl)
        self.__repo.addStud(Probl)
    
    def update(self,nrlab, nrprobl, dscr, ddln):
        Probl = Problema(nrlab, nrprobl, dscr, ddln)
        self.__validator.ValidateProbl(Probl)
        self.__repo.updateStud(Probl)
        
    def getAllProblems(self):
        return self.__repo.getAll()
    
    def delete(self,nrlab, nrprobl):
        Probl = Problema(nrlab, nrprobl, "dscr", 1)
        self.__validator.ValidateProbl(Probl)
        self.__repo.deleteStudent(Probl)
        
    def search(self,nrlab, nrprobl):
        Probl = Problema(nrlab,nrprobl," ",1)
        self.__validator.ValidateProbl(Probl)
        return self.__repo.searchStud(Probl)
    
    def generator(self,a):
        from random import seed
        from random import randint

        for i in range(0,a):
            nrlab = randint(1,8)
            nrprobl = randint(1,30)
            desc = "problema minunata"
            ddln = randint(1,8)
            probl = Problema(nrlab,nrprobl,desc,ddln)
            self.__validator.ValidateProbl(probl)
            self.__repo.addStud(probl)