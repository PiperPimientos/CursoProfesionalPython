# Hemos llegada a la parte mas complicada de funciones en Python, y es complejo de entender.
# Si comprendemos esto, estamos listos para programar en backend como por ejemplo en el framework Flask.
# Un decorador es un closure, pero con una funcionalidad adicional. Un decorador es una funcion que recibe como parámetro otra funcion, le agrega cosas, la ejecuta y luego retorna una funcion ya modificada, es decir diferente.
# Es una funcion que le agrega superpoderes a otra funcion.
# Asi se ve un decorador en código:

def decorador(func):
    def envoltura():
        print('Esto se agrega a mi funcion original')
        func()
    return envoltura

def saludo():
    print('Hola!')

saludo()
#Output
#Hola!

saludo = decorador(saludo)
saludo()
#Output
#Esto se agrega a mi funcion original
#Hola!

# Es una funcion que es un decorator, que recibe como parámetro a una func.
# La modifica creando una nested function, por eso también es un closure, y además recibe convencionalmente el nombre de envoltura o wrapper. Esta nested function modifica la original agregando algo que se imprime en pantalla como lo es ‘Esto se agrega a mi funcion original’.
# Luego tenemos la funcion saludo(), que imprime un Hola! en consola, y si ejecutamos a saludo, veremos que imprime normal el Hola!.
# Ahora lo que hacemos es que saludo va tener asignada la funcion decorador y como parámetro de decorador, esta la funcion saludo. Es decir que decorador quedara efectivamente como el decorador de saludo.
# Es decir, se va crear una funcion envoltura, se va imprimir en pantalla el decorador de la funcion original, luego se va ejecutar la funcion original, la cual imprime el Hola! y ahí se termina el programa porque se esta retornando a la funcion envoltura.
# Esto visto como un patron es crear una funcion, ejecutarla e inmediatamente la decoramos.
# Esto al ser un patron tan común se puede hacer de manera mas sencilla con azúcar sintáctica, que es básicamente, encontrarnos un código embellecido, para que nosotros lo veamos con mas estética. Cual es el sugar sintax de los decoradores?
# El siguiente:

def decorator(func):
    def envoltura():
        print('Esto se agrega a la funcion original')
        func()
    return envoltura

@decorador
def saludo():
    print('Hola!')

saludo()


# Lo que podemos hacer, es en vez de ejecutar la funcion inmediatamente despues, agragar con un arroba @ al principio de la funcion, en la línea inmediatamente superior, el decorador, con el cual, valga la redundacia, la queremos decorar. Es decir, podemos definir la funcion saludo, y justo antes, con el arroba @, agregarle el decorador. 
# La cualidad fundamental de un decorator, a diferencia de un closure, es que le agrega cosas a una funcion original.
# Veamos un ejemplo practico

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('Cesar'))


# 1.	Al decorador le ponemos de nombre mayúsculas, recibe como parámetro una funcion.
# 2.	Ademas crea una nested function que modifica la funcion original. En este caso recibe un texto, que es pasado como parámetro a mi funcion original y a la vez el resultado de ese return, le aplico el método .upper(), es decir, convierto todo lo que devuelve a mayúsculas.
# 3.	Por ultimo, retorna a esa funcion nested, envoltura. Tal y como nos dicen las reglas de los closures.
# 4.	Por ultimo tengo una funcion mensaje, que tiene un nombre como parámetro y retorna un string que dice {nombre}, recibiste un mensaje. Que además esta decorada previamente con el decorator @mayusculas.
# 5.	Luego hacemos el print, que imprimirá dicha funcion original, mensaje, y luego el nombre 
