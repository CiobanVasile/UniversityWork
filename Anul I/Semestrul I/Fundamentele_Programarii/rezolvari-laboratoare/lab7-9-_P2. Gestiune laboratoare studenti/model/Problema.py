class Problema(object):
    
    def __init__(self,__nrlab, __nrpr, __dscr, __ddln):
        self.__nrlab = __nrlab
        self.__nrprobl = __nrpr
        self.__dscr = __dscr
        self.__ddln = __ddln 
        '''deadline-ul va fi ultima saptamana in care mai poate fi predata problema'''
    
    def __eq__(self,value):
        
        return self.__nrlab == value.__nrlab and self.__nrprobl == value.__nrprobl
    
    def get_nrlab(self):
        return self.__nrlab


    def get_nrprobl(self):
        return self.__nrprobl


    def get_dscr(self):
        return self.__dscr


    def get_ddln(self):
        return self.__ddln


    def set_dscr(self, value):
        self.__dscr = value


    def set_ddln(self, value):
        self.__ddln = value
    
    def __str__(self):
        return str(self.get_nrlab())+","+str(self.get_nrprobl())+"," + str(self.get_dscr()) +","+ str(self.get_ddln())
    
    
