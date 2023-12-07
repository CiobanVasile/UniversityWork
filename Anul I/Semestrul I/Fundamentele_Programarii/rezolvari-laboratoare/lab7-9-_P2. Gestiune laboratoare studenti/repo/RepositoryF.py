from repo.Repository import Repository
from model.Problema import Problema
from model.Catalog import Catalog
from model.Student import Student
class RepositoryF(Repository):
    
    def __init__(self,fileName):
        Repository.__init__(self)
        self.__filename = fileName
        self.clearFileContent(fileName)
        self.__loadfromFile()
        
    def __loadfromFile(self):
        try:
            f = open(self.__filename,"r")
        except IOError:
            return
        
        #Repository.dellist(self)
        if len(self._elems) != 0:
            print("lista initiala nevida")
        line = f.readline().strip()
        while line != "":
            print(line," - ")
            line = line.split(",")
            #print(line[0],line[1],line[2])
            stud = Student(int(line[0]),line[1],int(line[2]))
            print(str(stud))
            Repository.addStud(self,stud)
            line = f.readline().strip()
        f.close()    
            
    def clearFileContent(self,fileName):
        """
          Clear the content of the file
          Post: the given file exist and is empty
        """
        f = open(fileName, "w")
        f.close()
        
    def __savetoFile(self):
        try:
            f = open(self.__filename,"w") 
        except IOError:
            return
        stud = self.getAll()
        for i in stud:
            s = str(i)+"\n"
            print(str(i))
            f.write(s)
        f.close()   
    
    def addStud(self,Stud):
        #self.__loadfromFile()
        Repository.addStud(self, Stud)
        self.__savetoFile()
        
    def deleteStudent(self,Stud):
        #self.__loadfromFile()
        Repository.deleteStudent(self, Stud)
        self.__savetoFile()
        
    def updateStud(self,Stud):
        #self.__loadfromFile()
        Repository.updateStud(self, Stud)
        self.__savetoFile()
    
    def getAll(self):
        return Repository.getAll(self)