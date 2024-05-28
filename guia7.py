import array 
import math 

# eje 1 
def pertenece (seq : list , n : int) -> bool: 
  res : bool = n in seq  
  return (res) 

pertenece ([1, 2, 3], 4)

#1.2
def divide_a_todos (seq : list, e : int) -> bool: 
    i : int = 0  
    res : bool = True 
    while ((i < len (seq)) and (res == True)):
       if (seq[i] % e != 0):
          res = False 
       i += 1 
    return res 

#1.3 
def suma_total (seq : list) -> int: 
   i : int = 0 
   res : int = 0
   while (i < len (seq)): 
      res += seq[i] 
      i +=  1 
   return (res) 

#1.4 
def ordenados (seq : list) -> bool: 
   i : int = 0 
   res : bool = True 
   while (i < len (seq)-1):
        if (seq [i] > seq [i+1]): 
           res = False 
        i += 1 
   return (res) 

#1.5 
#def palabras7 (l : list [str]) -> bool:
 #   res: bool = False
  #  for i in range(0,len(l)-1,1):
   #     if (len(l[i]) > 7):
    #        res = True
    #return res
     
#1.6 
def capicua (texto : str) -> bool: 
   i : int = 0 
   e : int = len (texto) - 1 
   res : bool = True 
   while ((i < len (texto)) and (res == True)):
      if (texto[i] != texto[e]):
         res = False 
      i += 1 
      e -= 1 
   return (res) 

#print (capicua ("neuquen")) 
   
#1.7 

def tiene_minuscula (c : str) -> bool:
   for char in c: 
      if ("a" <= char <= "z"):
         res = True
      else: 
         res = False 
   return res 

def tiene_mayus (c : str)  -> bool: 
   for char in c: 
      if ("A" <= char <= "Z"):
         res = True
      else: 
         res = False
   return res 

def tiene_numero (c : str) -> bool:
   for num in c: 
      if ("0" <= num <= "9"):
         res = True
      else: 
         res = False
   return res 

def es_verde (c : str) -> bool: 
   if ((len (c) > 8) and (tiene_minuscula(c) == True) and (tiene_mayus(c) == True) and (tiene_numero(c) == True)):
      res = True
   else: 
      res = False 
   return res 

def fortaleza_de_contrasena (c : str) -> str: 
   if (es_verde(c) == True): 
      res = "VERDE" 
   else: 
      if (len (c) < 5):
         res = "ROJA"
      else: 
         res = "AMARILLA" 
   return res 

#print (fortaleza_de_contrasena ("123Ar2565y"))    
   
#1.8
def cuenta_bancaria (movimientos : list) -> float: 
   res : float = 0 
   for tuplas in movimientos: 
      if tuplas[0] == "I": 
         res += tuplas[1] 
      else: 
         if tuplas[0] == "R": 
            res -= tuplas [1]
   return res 
      
#print (cuenta_bancaria ([("I", 2000), ("R", 20), ("R", 1000), ("I", 300)])) 
 
#1.9 

def esVocal(letra:str) -> bool:
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    if pertenece(vocales, letra):
        return True
    return False

def vocales(palabra:str) -> bool:
    vocales: int = 0
    
    for letra in palabra: 
        if esVocal(letra):
            vocales+=1
    
    if vocales >= 3:
        return True
    return False

#print(vocales("Alamo")) 

#2.1 

def tuvieja (list : int) ->  None : 
   for i in range(0,len(list),1): 
      if (i % 2 == 0): 
         list[i] = 0 
      
#listaaux : list [int] =  ([1, 2, 3, 4])   
#print (listaaux)
#tuvieja (listaaux) 
#print  (listaaux)

# 2.3

def sinvocales (list) -> list: 
   nueva : list = [] 
   for letra in list: 
      if (esVocal (letra) == False): 
         nueva.append (letra)
        
   return nueva 
   
#print (sinvocales (["h", "o", "l", "a"]))   

#2.4

def reemplazar_vocales (list) -> list: 
   nueva : list = []
   for letra in list: 
      if (esVocal (letra) == True): 
         nueva.append ('-')
      else: 
         nueva.append (letra)
   return nueva 

#print (reemplazar_vocales (["h", "o", "l", "a"])) 

#2.5 

def da_vuelta (s : list) -> list: 
   nueva : list = []
   i : int = 0
   while (0 <= i < len (s)): 
      nueva.append (s[len (s) - i - 1]) 
      i += 1   
   return nueva 

#print (da_vuelta(["h", "o", "l", "a"])) 

#2.6

def eliminar_repe (s : list) -> list: 
   nueva : list = []
   i : int = 0 
   while (0 <= i < len (s)):  
      if (pertenece (nueva, s[i]) == False): 
         nueva.append (s[i]) 
      i += 1 
   return nueva 

#print (eliminar_repe (["h","a", "a", "a", "o", "l", "a", "a", "a"]))


# 3

def promedio (list) -> int: 
   i : int = 0 
   res : int = 0 
   while (0 <= i < len (list)):
       res += list [i] 
       i += 1
   return (res / len (list)) 

#print (promedio ([8, 6, 5])) 

def menos_de_cuatro (list) -> bool: 
   i : int = 0 
   res : bool = False 
   while (0 <= i < len (list)): 
      if (list[i] < 4): 
         res = True 
      i += 1 
   return res 

#print (menos_de_cuatro ([5, 4, 3])) 


def notas (list) -> int: 
   res : int = 0
   if ((menos_de_cuatro (list) == True) or (promedio (list) < 4)):
      res = 3
   else: 
      if (4 <= promedio (list) < 7): 
         res = 2
      else: 
         res = 1 
   return res 

#print (notas ((7, 7, 4))) 

### 

# 5.2 
def pertenece_each_one2 (seq : list, e : int ) -> list [bool]: 
   nueva : list = [] 
   for secuencias in seq: 
      if pertenece (secuencias, e) == True: 
         nueva.append (True) 
      else: 
         nueva.append (False) 
   return nueva 

#print (pertenece_each_one2 ([[1, 7, 2], [4, 5, 2]], 1))       
      