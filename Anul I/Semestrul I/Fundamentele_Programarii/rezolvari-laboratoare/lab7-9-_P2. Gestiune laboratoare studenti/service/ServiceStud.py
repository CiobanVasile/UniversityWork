from model.Student import Student
from errors.errors import ValidError, RepoError

class ServiceStud(object):
    
    def __init__(self, __repo, __valid):
        self.__repo = __repo
        self.__validator = __valid
    
    def add(self,ident, name, grup):
        stud = Student(ident,name,grup)
        self.__validator.ValidateStud(stud)
        self.__repo.addStud(stud)
        
    def update(self,ident,name,grup):
        stud = Student(ident,name,grup)
        self.__validator.ValidateStud(stud)
        self.__repo.updateStud(stud)
        
    def getAllStudents(self):
        return self.__repo.getAll()
    
    def delete(self,ident):
        stud = Student(ident,"None", 1)
        self.__validator.ValidateStud(stud)
        self.__repo.deleteStudent(stud)
    
    def search(self,ident):
        stud = Student(ident,"None",1)
        self.__validator.ValidateStud(stud)
        return self.__repo.searchStud(stud)
    
    def generator(self,a):
        from random import seed
        from random import randint
        vocale = ["a" , "e"  "i"  , "o" , "u"]
        consoane = ["b", "c", "d", "f", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "s", "t", "t", "v", "w", "x", "z", "y"]
        i = 0
        while(i<a):
            ident = randint(0,1000000)
            nrLitere = randint(5,12)
            nume1 = chr(randint(65,90))
            for j in range(0,int(nrLitere/2)):
                nume1 += vocale[randint(0,3)]
                nume1 += consoane[randint(0,21)]
            grupa = randint(0,300)
            stud = Student(ident,nume1,grupa)
            try:
                self.__validator.ValidateStud(stud)
            except ValidError as ve:
                a+=1
            try:
                self.__repo.addStud(stud)
            except RepoError as re:
                a += 1
            i += 1
            if i % 10000 == 0:
                print(i)