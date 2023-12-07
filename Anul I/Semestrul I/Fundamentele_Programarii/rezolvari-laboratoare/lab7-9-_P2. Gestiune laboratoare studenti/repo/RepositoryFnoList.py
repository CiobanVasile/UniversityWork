from repo.Repository import Repository
from model.Problema import Problema
from model.Catalog import Catalog
from model.Student import Student
class RepositoryFnoList(Repository):
    
    def __init__(self,fileName):
        Repository.__init__(self)
        self.__filename = fileName
        self.clearFileContent(fileName)
        #self.__loadfromFile()
    
    def clearFileContent(self,fileName):
        """
          Clear the content of the file
          Post: the given file exist and is empty
        """
        f = open(fileName, "w")
        f.close()
    
    def searchId(self,ident):
        f = open(self.__filename,"r")
        line = f.readline().strip()
        while line != "":
            print(line," - ")
            line = line.split(",")
            #print(line[0],line[1],line[2])
            stud = Student(int(line[0]),line[1],int(line[2]))
            if stud.get_ident() == ident:
                print (str(stud))
                return
            line = f.readline().strip()
        f.close()   
        print("element inexistent!")
        return
    def addStud(self, Stud):
        f = open (self.__filename,"a")
        f.write(str(Stud))
        print(str(Stud))
        f.close()
        
    def searchStud(self, Stud):
        f = open(self.__filename,"r")
        line = f.readline().strip()
        while line != "":
            print(line," - ")
            line = line.split(",")
            #print(line[0],line[1],line[2])
            stud = Student(int(line[0]),line[1],int(line[2]))
            if stud.get_ident() == Stud.get_ident():
                print (str(stud))
                return
            line = f.readline().strip()
        f.close() 
        print("element inexistent!")
        return
    
    def deleteStudent(self, Stud):
        f = open(self.__filename,"r")
        fTemp = open("temp.txt","w")
        line = f.readline().strip()
        while line != "":
            print(line," - ")
            #line = line.split(",")
            #print(line[0],line[1],line[2])
            stud = Student(int(line[0]),line[1],int(line[2]))
            if Stud == stud:
                continue
            fTemp.write(str(stud)+"\n")
        fTemp.close()
        f.close()
        fTemp = open("temp.txt", "r")
        f = open(self.__filename,"w")
        content = fTemp.read()
        f.write(content)
        fTemp.close()
        f.close()
        
    def updateStud(self, Stud):
        f = open(self.__filename,"r")
        fTemp = open("temp.txt","w")
        line = f.readline().strip()
        while line != "":
            print(line," - ")
            line = line.split(",")
            #print(line[0],line[1],line[2])
            stud = Student(int(line[0]),line[1],int(line[2]))
            if Stud == stud:
                fTemp.write(str(Stud)+"\n")
            else:
                fTemp.write(str(stud)+"\n")
        fTemp.close()
        f.close()
        fTemp = open("temp.txt", "r")
        f = open(self.__filename,"w")
        content = fTemp.read()
        f.write(content)
        fTemp.close()
        f.close()
    
    def getAll(self):
        f = open(self.__filename,"r")
        content = f.read()
        content = content.split("\n")
        return content
        
        
           
           
           
           
           