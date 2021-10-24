# Mejoraremos nuestra sucesion de Fibonacci con los generators.
# Teniamos este codigo con los iteradores:

# import time

# class FiboIter():

#     def __iter__(self):
#         self.n1 = 0
#         self.n2 = 1
#         self.counter = 0
#         return self

# def __next__(self):
#     if self.counter == 0:
#         self.counter += 1
#         return self.n1
#     elif self.counter == 1:
#         self.counter += 1
#         return self.n2
#     else:
#         self.aux = self.n1 + self.n2
#         # self.n1 = self.n2
#         # self.n2 = self.aux
#         self.n1, self.n2 = self.n2, self.aux
#         self.counter += 1
#         return self.aux

# if __name__ == "__main__":
#     fibonacci = FiboIter()
#     for element in fibonacci:
#         print(element)
#         time.sleep(0.05)

# Asi que empezaremos de nuevo para hacerlo con generadores:

# 1.	Importamos el modulo time
# 2.	Creamos una funcion fibo_gen(), a diferencia de los iteradores que se utilizan es clases
# 3.	En vez de usar atributos utilizaremos variables.
# a.	n1 = 0, n2 = 1, counter = 0
# Es decir nuestro numero 1 y 2 y nuestro contador que empieza en 0
# b.	Ahora haremos un ciclo while, pero True, para que sea una sucesión infinita. Con la siguiente lógica: si el valor de counter es igual a 0 le voy a sumar 1 a counter, y voy a devolver con yield el valor de mi primer numero,
# if counter == 0:
#        counter += 1
#       yield n1
# Luego va el elif, es decir que si counter es igual a 1, entonces aumenta uno al contador y con yield vamos a devolver el valor de nuestro segundo numero
# elif counter == 1:
#      counter += 1
# Ahora el else, es decir, si ya pase por la primera vuelta del ciclo while y devolví el primer numero, y despues volvi a llamar el generador, y pase por el elif en donde counter ya vale 1, agrego otro counter y ahora devuelvo el valor de n2. ENTONCES:
# Tal como lo hicimos con los iteradores voy a decir que aux vale n1 mas n2 y luego haremos el swaping, donde diremos que n1 va estar asignado a n2 y que n2 antes del =, va estar asignado a aux. Ya finalmente le sumamos 1 al contador y finalmente devolvemos con yield nuestro valor de aux
# else:
#       aux = n1 + n2
#       n1, n2 = n2, aux
#       counter += 1
#        yield aux
# CON ESTO, ya esta creado el generador
# 4.	Ahora tenemos que instanciar el generador. Creamos el entry point. Decimos que Fibonacci va vontener el resultado de ejecutar fibo_gen().
# Ahora recorremos cada uno de los elementos del generador con un ciclo for
# Imprimimos el elemento
# y Finalmente ponemos un tiempo del método .sleep para recorrer el generador lentamente.


import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

if __name__ == "__main__":
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(1)



# RETO: Modifica el generador que acabamos de crear, pero que en lugar de devolver los infinitos numeros de la sucesión de Fibonacci, solo devuelva los numeros hasta un maximo.

import time

def fibo_gen(max= None):
    n1 = 0
    n2 = 1
    counter = 0
    if not max:
        while True:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux
    else:
        while True:
            if counter == 0 and n1 <= max:
                counter += 1
                yield n1
            elif counter == 1 and n2 <= max:
                counter += 1
                yield n2
            elif counter > 1:
                aux = n1 + n2
                n1, n2 = n2, aux
                if aux >= max+1:
                    raise StopIteration
                counter += 1
                yield aux

if __name__ == "__main__":
    fibonacci = fibo_gen(987)
    for element in fibonacci:
        print(element)
        time.sleep(1)


# Y una solucion mucho mas compacta que encontre

from time import sleep
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    fibonacci = fibonacci_gen()
    for element in fibonacci:
        print(element)
        sleep(1)
