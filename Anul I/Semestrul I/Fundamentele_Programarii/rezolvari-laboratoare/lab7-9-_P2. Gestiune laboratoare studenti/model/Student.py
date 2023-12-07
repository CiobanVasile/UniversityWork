class Student(object):
    def __init__(self,__ident,__name,__grup):
        self.__ident = __ident
        self.__name = __name
        self.__grup = __grup

    def __str__(self):
        return (str(self.get_ident())+","+str(self.get_name())+"," + str(self.get_grup()))
    
    def __eq__(self,value):
        if type(value) == int:
            return self.__ident == value
        return self.__ident == value.__ident
     
   # def __str__(self):
    #    return (str(self.get_ident)+","+str(self.getname)+"," + str(self.get_grup))
    
    def get_ident(self):
        return self.__ident


    def get_name(self):
        return self.__name


    def get_grup(self):
        return self.__grup


    def set_name(self, value):
        self.__name = value


    
    

