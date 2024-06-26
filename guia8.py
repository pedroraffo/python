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


    
#print (cantidad_de_elementos (miPila))  

 

#10
def buscar_el_maximo(p : Pila[int]) -> int:

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

#print (cantidad_de_elementos_cola (miCola))

#15
def buscar_el_maximo_cola(c : Cola[int]) -> int:
    p = Pila()
    i = 0
    res = 0

    while not (c.empty()):
        i = c.get()
        p.put(i)
        if i > res:
            res = i
    while  not p.empty(): 
        c.put(p.get())

    return res  

#print (buscar_el_maximo_cola (miCola)) 

# 16

def armarSecuenciaBingo() -> Cola[int]:
    c = Cola()
    l: list[int] = list(range(100))
    for i in range(len(l)):
        e:int = random.choice(l)
        l.remove(e)
        c.put(e)
    return c

##
def jugarCarton(carton: list[int], bolillero: Cola[int]) -> int:
    count: int = 0
      
    while not listaVacia(carton) and not bolillero.empty():
        e: int = bolillero.get()
        if pertenece_bingo (carton, e) == True:
            print("entre en",count)
            carton.remove(e)
        count += 1
    
    return count

def pertenece_bingo (list, numero :int) -> bool: 
    i : int = 0
    res = False 
    while (0 <= i < len (list)): 
        if (numero == list[i]): 
            res = True 
        
            i += 1 
    return res 

def listaVacia(l:list) -> bool:
    if l == []:
        return True
    return False

bolillero = armarSecuenciaBingo()
carton = [1,11,21,31,41,51,61,71,81,91,5,15]
#print(jugarCarton(carton,bolillero))

#falta hacer que sea de tipo in, ya que modifica tanto al bolillero como al carton. Tienen que quedar tal cual nos los dieron. 

#17 
fila_pacientes: Cola [int, str, str]= Cola()
fila_pacientes.put((1, "pedro", "pie"))
fila_pacientes.put((5, "lucas", "mano"))
fila_pacientes.put((3, "marto", "tobillo"))
fila_pacientes.put((6, "santi", "hombro"))
fila_pacientes.put((2, "tomi", "dedo"))
fila_pacientes.put((1, "jero", "rodilla"))  

def n_pacientes_urgentes (c : Cola [(int, str, str)]) -> int:
    p = Cola()
    res : int = 0 
    while not c.empty():
        paciente = c.get()
        p.put(paciente)
        if es_urgente (paciente) == True:
            res += 1 
    while not p.empty(): 
        c.put(p.get()) 

    return res     

def es_urgente (list) -> bool: 
    res : bool = False
    if (list[0] == 1 or list[0] == 2 or list[0] == 3):
        res = True 

    return res  

#print (n_pacientes_urgentes (fila_pacientes))

#18

fila_banco: Cola [str, int, bool, bool] = Cola()
fila_banco.put(("vilma", 21, False, True ))
fila_banco.put(("embarazada", 30, False, True))
fila_banco.put(("piba", 40, False, False))
fila_banco.put(("pibe", 42, False, False))
fila_banco.put(("viejo", 12, True, False))

def nivel_de_prioridad (list) -> int: 
    if list[3] == True:
        res = 1 
    elif list [2] == True:
        res = 2 
    else: 
        res = 3 
    return res 

def atencion_a_clientes (c : Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    f = Cola()
    p = Cola()
    s = Cola()
    t = Cola()
    n = Cola()
    while not c.empty():
        cliente = c.get()
        n.put(cliente)
        if nivel_de_prioridad (cliente) == 1: 
                p.put(cliente) 
        elif nivel_de_prioridad (cliente) == 2:
                s.put(cliente) 
        else: 
                t.put(cliente) 
    while not p.empty():
        f.put(p.get())
    while not s.empty():
        f.put(s.get())
    while not t.empty():
        f.put(t.get())
    while not n.empty():
        c.put(n.get())
    
    return  f 


#print (imprimirCola (atencion_a_clientes (fila_banco)))

###

#19 
""" def im_not_split(content:str) -> list[str]:
    res = []
    i = 0
    palabra = ""


    while i < len(content):
        if content[i] == " " or content[i] == "\n":
            if palabra != "":
                res.append(palabra)
                palabra = ""

        else: 
            palabra+= content[i]

        i+=1
    if i == len(content):
        res.append(palabra)
    return res """

def agrupar_por_longitud (archivo : str) -> dict:
    diccionario = {}
    archivo = open (archivo,"r") 
    contenido = archivo.read()
    palabras:list[str] = contenido.split()

    for palabra in palabras:
        if len(palabra) in diccionario:
            diccionario[len(palabra)] += 1
        else:
            diccionario[len(palabra)] = 1

    archivo.close()

    return diccionario

#print(agrupar_por_longitud("ocho.txt")) 

## para el 20 hay que hacer el 7 y no lo hice. 

#21 

 
def diccio_de_palabras (archivo : str) -> dict:
    diccionario = {}
    archivo = open (archivo,"r") 
    contenido = archivo.read()
    palabras:list[str] = contenido.split()

    for palabra in palabras: 
        if palabra in diccionario: 
             diccionario[palabra] += 1
        else: 
            diccionario[palabra] = 1
        
    archivo.close()

    return diccionario 

def  palabras_mas_frecuentes (archivo : str) -> str: 
    diccio = diccio_de_palabras (archivo) 
    cantidad = diccio.keys() 
    max : int = 0
    res : str = 'no hay palabras en el archivo'
    for clave in cantidad:
        if diccio [clave] > max:
            max = diccio [clave]
            res = clave  
    return res 

#print (palabras_mas_frecuentes ("ocho.txt"))

#22

historiales = {} 

def visitar_sitio (historiales : dict[str, Pila[str]], usuario : str, sitio : str): 
        if usuario not in historiales:
            historiales[usuario] =  Pila()
        
        historiales[usuario].put(sitio) 

def navegar_atras(historiales: dict[str, Pila[str]], usuario:str):

    if usuario in historiales:
        historiales[usuario].get() 
 
        

def imprimir_historial(historiales):
    items = historiales.items()

    for usuario, p in items:
        print(f"Historial de {usuario}: ")
        lista = []

        while not p.empty():
            lista.append(p.get())

        for sitio in lista:
            print(sitio)

        pilaProvisional = Pila()
        while lista:
            pilaProvisional.put(lista.pop())
        while not pilaProvisional.empty():
            p.put(pilaProvisional.get())

        print()


#visitar_sitio (historiales, "tomi", "plm")
#visitar_sitio (historiales, "tomi", "promiedos") 
#print (imprimir_historial(historiales))

##23

inventario = {}

def agregar_producto (inventario : dict, nombre : str, precio : int, cantidad : int): 
    masinfo = {}
    inventario[nombre] = masinfo
    masinfo["precio"]= precio
    masinfo ["cantidad"]= cantidad

agregar_producto (inventario, "airforce", 100, 9) 
agregar_producto (inventario, "vans", 99, 20) 
print (list(inventario.items()))

def actualizar_stock (inventario : dict, nombre : str, precio : int, cantidad : int):
    prod = inventario[nombre]
    if nombre in inventario:
        prod["cantidad"] = cantidad 
        
#actualizar_stock (inventario, "airforce", 100, 12) 
#print(list(inventario.items()))

def actualizar_precio (inventario : dict, nombre : str, precio : int, cantidad : int):
    nuevo = inventario[nombre]
    if nombre in inventario:
        nuevo["precio"] = precio 


#actualizar_precio (inventario, "airforce", 115, 12) 
#print(list(inventario.items()))

def calcular_valor_inventario (inventario : dict) -> float:
    res : float = 0.0
    excel = inventario.keys() 
    for k in excel:
        l = list(inventario[k].values())
        i : int = 0
        res += l[0] * l[1] 
        while i+2 < len(l):
            res += l[i] * l[i+1] 
    return res 
    
print (calcular_valor_inventario(inventario)) 
    

