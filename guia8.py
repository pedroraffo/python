import math
from queue import Queue as Cola 


# 1 
def contar_lineas (archivo : str) ->  int: 
    file = open (archivo , "r") 
    texto : list [str] = file.readlines()
    return (len (texto)) 

#print (contar_lineas ("ocho.txt")) 

# 2 
def pertenece (list, palabra : str) -> bool: 
    i : int = 0
    res = False 
    while (0 <= i < len (list)): 
        if (palabra == list[i]): 
            res = True 
        
            i += 1 
    return res 

#print (pertenece (["hola", "como", "va"], "va")) 



def existe_palabra (palabra : str, archivo : str) -> bool: 
    file = open (archivo , "r") 
    texto : list [str]= file.readlines () 
    res : bool = True
    for lineas in texto:
        listaDeWords :list [str] = lineas.split(" ")
        if (palabra in listaDeWords): 
            res = True  
        else:   
            res = False 
    return res 

#print (existe_palabra ("va", "ocho.txt"))


#1.3 

def apariciones (archivo : str, palabra : str) -> int: 
     file = open (archivo , "r")
     texto : list [str]= file.readlines() 
     res : int = 0 
     i : int = 0 
     while  (i < len (texto)): 
        for elemento in texto [i].split(): 
                if elemento == palabra: 
                    res += 1 
        i += 1 
     return res 

#print (apariciones ("ocho.txt", "va"))
        

# 2 

def sin_comentarios (archivo : str): 
    file = open (archivo, "r")
    texto = file.readlines()
    messi = open ("messi.txt", "w")
    i = 0 
    res = []
    while i < len (texto): 
        linea = texto[i].split() 
        if linea[0] != "#": 
            res.append (texto[i])
        i += 1 

    messi.writelines(res) 
    messi.close() 

#sin_comentarios ("come.txt")

#3

def invertir_lineas (archivo : str): 
    file = open (archivo, "r")
    texto = file.readlines()
    revers = open ("reverso.txt", "w")
    i = len (texto) - 1 
    res = []
    while i >= 0: 
        res.append(texto[i] + '\n')
        i -= 1 

    revers.writelines(res) 
    revers.close() 

#invertir_lineas ("ocho.txt")

#4

def agregar_frase_al_final (archivo : str, frase : str):
    file = open(archivo, "r+")
    texto = file.read()

    file.write('\n' + frase)
    file.close() 

#agregar_frase_al_final("ocho.txt", "esta la agregamos")  

#5 
def agregar_al_principio (archivo : str, frase : str): 
    file = open(archivo, "r") 
    texto = file.read()
    file.close() 

    nuevo = open (archivo, "w") 
    nuevo.write(frase + '\n' + texto) 
    nuevo.close() 

#agregar_al_principio ("ocho.txt", "estoy aca arriba")

#6

def listarpalabras_de_archivo(archivo:str) -> list:
    permitidas = ["","1","2","3","4","5","6","7",
                  "8","9","0","a","b","c","d","e","f","g","h","i","j","k", "l",
                    "m","n" ,"ñ", "o","p","q","r","s","t","u","v","w","x","y","z",
                      "A", "B", "C" , "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                      "N" ,"Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    archivo = open("seis.zip", "rb")
    bytes = archivo.read()
    
    palabras = []
    palabra = ""

    for b in bytes:
        char = chr(b)
        if char in permitidas:
            palabra+= char
        elif (char == " ") and (len(palabra) < 5):
            palabra = ""
        elif ((char == " ") or (char == "\n" )) and (len(palabra) >= 5):
            palabras.append(palabra)
            palabra = ""
    
    return palabras 

#print (listarpalabras_de_archivo("seis.zip")) 
# falta conseguir que agregue la ultima palabra 

#7 
#def promedio_estudiante (archivo_promedios : str, lu : str) -> float: 





         
#8 
from queue import LifoQueue as Pila 
import random 

def generar_numero_al_azar(cantidad:int, desde:int,hasta:int) -> Pila[int]:
    p = Pila()

    for i in range(cantidad):
        p.put(random.randint(desde,hasta))


    return imprimirPila(p)

def imprimirPila(Pila):
    res = []
    while not (Pila.empty()):
        res.append(Pila.get())

    return res


#print( generar_numero_al_azar (69, 1,100) )

#9
miPila: Pila = Pila()
miPila.put(1)
miPila.put(2)
miPila.put(3)
miPila.put(4)
miPila.put(5)
miPila.put(6) 

def cantidad_de_elementos (p : Pila) -> int: 
    res : int = 0 
    c = Cola()

    while not p.empty(): 
            res += 1
            c.put(p.get())
    while not c.empty(): 
        p.put(c.get())

    return (res)  


    
print (cantidad_de_elementos (miPila))  

#esto esta mal xq te desarma la pila y hay que dejarla tal cual estaba  

#10
def bucar_el_maximo(p : Pila[int]) -> int:

    i = 0
    res = 0

    while not (p.empty()):
        i = p.get()
        if i > res:
            res = i

    return res  

#print (bucar_el_maximo (miPila)) 

#11

def esta_bien_balanceada (s : str) -> bool: 
    p = Pila 
    for letra in s: 
        if letra == '(': 
            p.put (letra)
        elif letra == ')': 
            if (p.empty()) or (p.get() != '('):
                return False
    return p.empty()          

#print(esta_bien_balanceada("(1+1)/2"))
#print(esta_bien_balanceada("1+1)/2"))
#print(esta_bien_balanceada("(1+1/2")) 


#12 


def evaluar_expresion (s : str) -> float:
    p = Pila()
    for letra in s: 
            if letra != '+' and letra != '-' and letra != '*' and letra != '/' and letra != ' ': 
                p.put(float(letra))
            elif letra != ' ': 
                scnd = p.get() 
                frst = p.get() 
                if letra == '+': 
                    p.put(frst + scnd) 
                elif letra == '-':
                    p.put(frst - scnd)
                elif letra == '*':
                    p.put(frst * scnd) 
                elif letra == '/':
                    p.put(frst / scnd) 

    return p.get() 
    
#print (evaluar_expresion ("3 4 + 5 * 2 -")) 
                    

#



#13

def generar_numero_al_azar_cola (cantidad:int, desde:int,hasta:int) -> Cola[int]:
    c = Cola()
    for i in range(cantidad):
        c.put(random.randint(desde,hasta))


    return imprimirCola(c)

def imprimirCola(Cola):
    res = []
    while not (Cola.empty()):
        res.insert(0, Cola.get())

    return res  

#print( generar_numero_al_azar_cola (69, 1,100) )

# 14 
miCola: Cola = Cola()
miCola.put(1)
miCola.put(2)
miCola.put(3)
miCola.put(4)
miCola.put(5)
miCola.put(6) 

def cantidad_de_elementos_cola (c : Cola) -> int: 
    res : int = 0 
    p = Pila()

    while not c.empty(): 
            res += 1
            p.put(c.get()) 
    while not p.empty(): 
        c.put(p.get())        
    return (res)   





