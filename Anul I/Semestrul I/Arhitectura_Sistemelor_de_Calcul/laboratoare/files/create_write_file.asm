; Codul de mai jos va crea un fisier numit "ana.txt" in directorul curent si va scrie un text in acel fisier.
; Programul va folosi functia fopen pentru deschiderea/crearea fisierului, functia fprintf pentru scrierea in fisier si functia fclose pentru inchiderea fisierului creat.
; Deoarece in apelul functiei fopen programul foloseste modul de acces "w", daca un fisier cu acelasi nume exista deja in directorul curent, continutul acelui fisier va fi suprascris. Detalii despre modurile de acces sunt prezentate in sectiunea "Suport teoretic"

bits 32 

global start        

; declare external functions needed by our program
extern exit, fopen, fprintf, fclose
import exit msvcrt.dll  
import fopen msvcrt.dll  
import fprintf msvcrt.dll
import fclose msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    nume_fisier db "ana.txt", 0  ; numele fisierului care va fi creat
    mod_acces db "w", 0          ; modul de deschidere a fisierului - 
                                 ; w - pentru scriere. daca fiserul nu exista, se va crea      
    text db "Ana are mere.", 0    ; textul care va fi scris in fisier
                                    
    descriptor_fis dd -1         ; variabila in care vom salva descriptorul fisierului - necesar pentru a putea face referire la fisier
                                    
; our code starts here
segment code use32 class=code
    start:
        ; apelam fopen pentru a crea fisierul
        ; functia va returna in EAX descriptorul fisierului sau 0 in caz de eroare
        ; eax = fopen(nume_fisier, mod_acces)
        push dword mod_acces     
        push dword nume_fisier
        call [fopen]
        add esp, 4*2                ; eliberam parametrii de pe stiva

        mov [descriptor_fis], eax   ; salvam valoarea returnata de fopen in variabila descriptor_fis
        
        ; verificam daca functia fopen a creat cu succes fisierul (daca EAX != 0)
        cmp eax, 0
        je final
        
        ; scriem textul in fisierul deschis folosind functia fprintf
        ; fprintf(descriptor_fis, text)
        push dword text
        push dword [descriptor_fis]
        call [fprintf]
        add esp, 4*2
        
        ; apelam functia fclose pentru a inchide fisierul
        ; fclose(descriptor_fis)
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
        
      final:
        
        ; exit(0)
        push    dword 0      
        call    [exit]       