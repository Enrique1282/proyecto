# and, or, not

gas = True
encendido = True
edad = 17

 # los 2 deben ser True
if gas and encendido: 
    print("puedes avanzar")            
    print("puedes avanzar") 
    
# con 1 solo True ya da True, solo da False si los 2 son False
if gas or encendido:              
    print("puedes avanzar") 

# toma su valor y lo cambia a lo opuesto
if not gas and encendido and edad > 17:   
    print("puedes avanzar")

if gas and encendido and edad > 17:
    print("puedes avanzar") 
    