import math

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

print (apariciones ("ocho.txt", "va"))
        

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

sin_comentarios ("come.txt") 