from errors.errors import ValidError
class ValidatorStud(object):
    
    
    def __init__(self):
        pass
    
    
    def ValidateStud(self,Stud):
        errors = ""
        if Stud.get_ident()<=0:
            errors += "bad ident!\n"
        ch = str(Stud.get_name())  
     
        if (Stud.get_name()==""):
            errors += "bad name!\n"
        #elif (ord(ch[0])>=65):
            # print(" ",ch[0])
            #errors += "bad name!\n"   
            #'''and  not any(char.isdigit() for char in Stud.get_name())  and ( ord(Stud.get_name()[0])>64 and ord(Stud.get_name()[0])<91)''':
        else:
             
            if not((ord(ch[0])>=65) and (ord(ch[0])<=90)):
                errors += "bad name!\n"
            else:
                
                if any(char.isdigit() for char in ch):
                    errors += "bad name!\n"
                    print(ch[0])     
        if Stud.get_grup()<1:
            errors += "bad grup!\n"
        if len(errors)>0:
            
            raise ValidError(errors)


