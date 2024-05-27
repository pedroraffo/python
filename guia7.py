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
def palabras7 (l : list [str]) -> bool:
    res: bool = False
    for i in range(0,len(l)-1,1):
        if (len(l[i]) > 7):
            res = True
    return res
     
   
## 

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
      
listaaux : list [int] =  ([1, 2, 3, 4])   
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

print (pertenece_each_one2 ([[1, 7, 2], [4, 5, 2]], 1))       
      
