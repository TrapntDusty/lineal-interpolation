import math
from math import log
from dataclasses import dataclass
fact = 1 #nuestra bandera para saber si quiere seguir usando el programa 
base = 10 #los numeros estan a base 10 la cual tomamos a consideracion

@dataclass
class return_values: #En esta clase solo la usamos para guardar valores y moverlos entre funciones [ logs y Ins hacia pasos ]
    a:float
    b:float # los 3 valores estan guardados dentro de Vals y se acceden como Vals.parametro [ Vals.a ]
    c:float

def Logs(base,log1,log2,log3): # el procedimiento para calcularlo logs 
    ValorIncog = math.log(log1,base) # se saca el log del primero con la base 
    ValorA = math.log(log2,base) #se saca el log del segundo con base
    ValorB = math.log(log3,base) #se saca el log del tercero con base
    t = return_values(ValorIncog,ValorA,ValorB) #guardamos los 3 valores en la clase return_values como a,b,c flotantes para usarlos en la siguiente funcion "pasos"
    return t #regresamos lo guardado en el valor t 

def Ins(log1,log2,log3): #procedimiento para calcular si eligio ingresar Ins
    ValorIncog = log(log1)/log(2.71828) # se saca el log del primero entre 2.71
    ValorA = log(log2)/log(2.71828) #se saca el log del segundo entre 2.71
    ValorB = log(log3)/log(2.71828) #se saca el log del tercero entre 2.71
    t = return_values(ValorIncog,ValorA,ValorB) #guardamos los 3 valores en la clase return_values como a,b,c flotantes para usarlos en la siguiente funcion "pasos"
    return t #regresamos lo guardado en el valor t 

def pasos(log1,log2,log3,Vals): # la funcion de los pasos
    yp = Vals.b+((Vals.c-Vals.b)/(log3-log2))*(log1-log2) #sacamos los valores interpoladors 
    print('valores interpolados %0.4f' %(yp)) # imprimimos el resultado con .4 digitos flotantes
    ErrV = abs((Vals.a-yp)/Vals.a)*100 #sacamos el errorverdadero con los valores que teniamos y conseguimos
    print("Calculando Error Verdadero %.02f%%" %(ErrV)) # imprimimos el resultado con .2 digitos flotantes
    return

while (fact == 1): # una condicion para quedarnos dentro del programa hasta que el usuario lo quiera dejar
    eleccion = int(input("[ 1 ] - Usara Log  |  [ 2 ] - Usara In : ")) # imprimimos si quiere usar el log o el

    if eleccion == 1: #la condicion si se eligio los logaritmos
        print("No se necesita ingresar la palabra Log solo su base [ Default : 10 ] y valor")
        base = float(input('Ingrese la base del logaritmo: '))
        log1 = float(input('Ingrese el log a calcular: '))
        log2 = float(input('Ingrese el log a interpolar menor: '))
        log3 = float(input('Ingrese el log a interpolar mayor: '))
        Vals = Logs(base,log1,log2,log3) #vamos a la funcion Logs con los valores registrados y lo recibimos y guardamos en vals
        pasos(log1,log2,log3,Vals) # vamos a la funcion pasos con los valores que se habian registrados y el nuevo
    elif eleccion == 2:#la condicion si se eligio los Ins
        print("No se necesita ingresar la palabra In solo su valor")
        log1 = float(input('Ingrese el In a calcular: '))
        log2 = float(input('Ingrese el In a interpolar menor: '))
        log3 = float(input('Ingrese el In a interpolar mayor: '))
        Vals = Ins(log1,log2,log3) #vamos a la funcion Ins con los valores registrados y lo recibimos y guardamos en vals
        pasos(log1,log2,log3,Vals) # vamos a la funcion pasos con los valores que se habian registrados y el nuevo
    fact = int(input("Quieres seguir Usando el programa ? [ 1 ] - Yes  |  [ 2 ] - No : ")) #preguntamos si quiere seguir usando el programa , de ser asi se repetira todo de nuevo en limpio