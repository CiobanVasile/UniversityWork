import unittest

from model.Student import Student
from model.Problema import Problema
from model.Catalog import Catalog
from repo.Repository import Repository
from errors.errors import RepoError, ValidError, ValidErrorP,ValidErrorC
from valid.ValidatorStud import ValidatorStud
from valid.ValidatorProbl import ValidatorProbl
from valid.ValidatorCatalog import ValidatorCatalog
from service.ServiceStud import ServiceStud
from service.ServiceProlb import ServiceProbl
from service.ServiceCatalog import ServiceCatalog
class Tests(object):
    
    def __init__(self):
        self.__ident = 13
        self.__name = "Alex"
        self.__grup = 10
        self.__stud = Student(self.__ident,self.__name,self.__grup)
        self.__bident = -10
        self.__bname = ""
        self.__repo = Repository()
        self.__valid = ValidatorStud()
        self.__bgrup = 0
        self.__bstud = Student(self.__bident,self.__bname,self.__bgrup)
        self.__serviceStud = ServiceStud(self.__repo, self.__valid)
        
        self.__nrlab = 2
        self.__nrprobl = 4
        self.__dscr = "problema minunata"
        self.__ddln = 8 
        self.__probl = Problema(self.__nrlab, self.__nrprobl, self.__dscr, self.__ddln)
        self.__bnrlab = -1
        self.__bnrprobl =-10
        self.__bdscr = ""
        self.__bddln = 5 
        self.__bprobl = Problema(self.__bnrlab, self.__bnrprobl, self.__bdscr, self.__bddln)    
        self.__validP = ValidatorProbl()
        self.__serviceProbl = ServiceProbl(self.__repo, self.__validP)
        
        self.__elemCatalog = Catalog(self.__ident,self.__nrlab,self.__nrprobl,10)
        self.__belemCatalog =Catalog(self.__bident,self.__bnrlab,self.__bnrprobl,-10)
        self.__validC = ValidatorCatalog()
        self.__serviceCatalog = ServiceCatalog(self.__repo,self.__repo,self.__repo,self.__validC)
         
    def tearDown(self):
        pass
    def __testsRepo(self):
        assert len(self.__repo.getAll()) == 0
        self.__repo.addStud(self.__stud)
        assert len(self.__repo.getAll()) == 1
        try:
            self.__repo.addStud(self.__stud)
            assert False
        except RepoError as re:
            assert str(re) == "existing element!"  
        
        stud1 = Student(self.__ident,None,None)
        
        assert self.__repo.searchStud(stud1) == self.__stud  
        stud1 = Student(1,None,None)
        
        try:
            self.__repo.searchStud(stud1)
            assert False
        except RepoError as re:
            assert str(re) == "inexisting element!"
            
        stud2 = Student(13,"as",None)
        self.__repo.updateStud(stud2)
        all = self.__repo.getAll()
        assert all == [stud2]
        try:
            self.__repo.updateStud(self.__bstud)
            assert False
        except RepoError as re:
            assert str(re) == "inexistent element!"
        
        assert len(self.__repo.getAll()) == 1
        self.__repo.deleteStudent(self.__stud)
        assert len(self.__repo.getAll()) == 0
        try:
            self.__repo.deleteStudent(self.__stud)
            assert False
        except RepoError as re:
            assert str(re) == "inexistent element!"
            
        
        
        
    def __testsModel(self):
        
        assert self.__stud.get_ident() == self.__ident
        
    def __testsValid(self):
        self.__valid.ValidateStud(self.__stud)
        try:
            self.__valid.ValidateStud(self.__bstud)
            assert False
        except ValidError as ve:
            assert str(ve) == "bad ident!\nbad name!\nbad grup!\n"
        
        self.__validP.ValidateProbl(self.__probl)
        try:
            self.__validP.ValidateProbl(self.__bprobl)
            assert False
        except ValidErrorP as vep:
            assert True#str(vep) =="bad nrlab!\nbad nrprobl!\nbad description!\nbad deadline!\n"
        
        #valid Catalog#
        
        self.__validC.validateCatalog(self.__elemCatalog)
        
        try:
            self.__validC.validateCatalog(self.__belemCatalog)
            assert False
        except ValidErrorC as vec:
            assert str(vec) == "bad ident!\nbad nrlab!\nbad nrprobl!\nbad nota!\n"

            
    def __testsService(self):
        pass
    
    def runTest(self):
        self.__testsModel()
        self.__testsRepo()
        self.__testsValid()
        self.__testsService()

if __name__ == '__main__':
    unittest.main()