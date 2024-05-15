import math 
#primeros pasos 
a = 1 
b = 1 
c = a + b 
print (c) 
#eje 1 
def imprimir_hola_mundo(): 
 print ("Hola Mundo")

imprimir_hola_mundo() 

#eje 2 
def imprimir_un_verso(): 
 print ("el Don Don Don \n don don")
imprimir_un_verso() 

# eje3 
def raiz_de_2() -> float:
 
 x : float = 2 
 exp : float = 0.5 
 return round (x**exp, 4) 

print (raiz_de_2())

#eje 4 
def fact_de_dos() -> int:
 x : int = 2 
 y : int = 1 
 return (x * y) 

print (fact_de_dos()) 

#eje 4 
def perimetro() -> float: 
 x : float = 2 
 return round (x * math.pi, 2)  

print (perimetro())

#2. 1 
def imprimir_saludo (nombre:str) :
 print ("hola", nombre) 

imprimir_saludo ("pedro")

# 2.2 
def raiz_cuadrada_de (numero:float): 
 print (math.sqrt (numero)) 

raiz_cuadrada_de (4) 

#2.3
def faren_a_celsius (numero:float) -> float: 
 return print (((numero - 32) * 5)/9)

 

#2.4 
def imp_dos_veces (estribillo:str) -> str :
 print ((estribillo) * 2) 

imp_dos_veces ("dududu dudadada ") 

#2.5 
def es_multiplo (n:int, m:int) -> bool: 
    if ( n % m == 0): 
      print (True)
    else:
      print (False) 

es_multiplo (6, 3)

#2.6 

def es_par (numero:int) -> bool :
    if (es_multiplo (numero, 2) == True): 
      print (True) 
    else:  
      print (False) 

es_par (5) 

#2.7 
def min_cant_porciones (numero:int) -> bool: 
    if (numero >= 2): 
      print (True) 
    else: 
      print (False) 

   
def cantidad_de_pizzas (comensales:int, porciones:int) -> int: 
    if ((comensales * porciones) % 8 == 0): 
      print ((round (((comensales * porciones)/8), )) + 1) 
    else: 
      print (round (((comensales * porciones)/8), ))
cantidad_de_pizzas (8, 3)

#eje 3.1 
def alguno_es_0 (x: int, y: int) -> bool:
  res : bool = x == 0 or y == 0 
  print (res) 

alguno_es_0 (1, 2) 

# eje 3.2 
def ambos_son_0 (x: int, y: int) -> bool: 
  res : bool = x == 0 and y == 0 
  print (res) 

ambos_son_0 (1, 0) 