from errors.errors import ValidErrorP
class ValidatorProbl(object):
    
    def __init__(self):
        pass
    
    def ValidateProbl(self,Probl):
        errors = ""
        if Probl.get_nrlab() <1:
            errors +="bad nrlab!\n"
        if Probl.get_nrprobl() <1:
            errors +="bad nrprobl!\n"
        if Probl.get_dscr() =="":
            errors +="bad description!\n"
        if Probl.get_ddln() < 1:
            errors +="bad deadline!\n"
        if len(errors)>0:
            raise ValidErrorP(errors)
