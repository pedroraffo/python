import array 

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
     
   
   
