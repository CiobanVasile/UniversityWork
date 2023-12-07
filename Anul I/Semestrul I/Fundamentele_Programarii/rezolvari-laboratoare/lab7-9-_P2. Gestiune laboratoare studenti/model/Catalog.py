class Catalog(object):
    
    def __init__(self,__nrident,__nrlab,__nrprobl,__nota):
        self.__nrident = __nrident
        self.__nrlab = __nrlab
        self.__nrprobl = __nrprobl
        self.__nota = __nota

    def __str__(self):
        return str( self.get_nrident() )+","+ str( self.get_nrlab() )+"_" +str( self.get_nrprobl() )+","+str( self.get_nota() )


    def __eq__(self, value):
        if type(value) == int:
            return self.get_nrident() == value
        return self.get_nrident() == value.get_nrident()


    
    def get_nrident(self):
        return self.__nrident


    def get_nrlab(self):
        return self.__nrlab


    def get_nrprobl(self):
        return self.__nrprobl


    def get_nota(self):
        return self.__nota


    def set_nrlab(self, value):
        self.__nrlab = value


    def set_nrprobl(self, value):
        self.__nrprobl = value


    def set_nota(self, value):
        self.__nota = value

    

    