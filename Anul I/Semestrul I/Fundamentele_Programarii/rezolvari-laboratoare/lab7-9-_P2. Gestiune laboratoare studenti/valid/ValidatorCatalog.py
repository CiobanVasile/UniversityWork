from errors.errors import ValidErrorC
class ValidatorCatalog(object):
    
    def __init__(self):
        pass
    
    def validateCatalog(self,element):
        errors = ""
        if element.get_nrident()<0:
            errors +="bad ident!\n"
        if element.get_nrlab()<0:
            errors +="bad nrlab!\n"
        if element.get_nrprobl()<0:
            errors += "bad nrprobl!\n"
        if element.get_nota()<0:
            errors += "bad nota!\n"
        if len(errors)>0:
            raise ValidErrorC(errors)


