
# Para trabajar iteradores, tenemos un ejemplo clave que es la sucesión de Fibonacci.
# Fue creada por leonardo de Pisa.
# Es una sucesión muy poderosa, también conocida como Fi, o el numero de Dios. Tiene muchas implicancias dentro de la informática.
# Esta sucesión infinita luce asi:
# 0 1 1 2 3 5 8 13 21 34 55 89 144
# Cada uno de los numeros de la sucesión es el resultado de sumar los dos anteriores.
# Esta misma sucesión podemos tenerla guardarla dentro de un iterador en Python. De hecho es asi como se hace en investigaciones científicas.
# Los iteradores si nos permiten guardar sucesiones completas como estas, pues en ellos creamos una formula que nos entrega siempre el siguiente.

import time

class FiboIter():

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

def __next__(self):
    if self.counter == 0:
        self.counter += 1
        return self.n1
    elif self.counter == 1:
        self.counter += 1
        return self.n2
    else:
        self.aux = self.n1 + self.n2
        # self.n1 = self.n2
        # self.n2 = self.aux
        self.n1, self.n2 = self.n2, self.aux
        self.counter += 1
        return self.aux

if __name__ == "__main__":
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.05)


# Si ejecutamos en consola, saldrá un chorrero de numeros que no entenderemos. Como podemos entender lo que esta pasando?
# En nuestro entry point, dentro del ciclo for, despues de print, utilizaremos el modulo que importamos al principio
# time.sleep(0.05)
# Esto es que despues de imprimir cada elemento, en cada vuelta del ciclo, vamos a pausar 0.05 segundos antes de seguir a la siguiente vuelta, y veremos lentamente como funciona la sucesión.

# RETO: Modificar el iterador que acabamos de crear, pero que en lugar de devolver los infinitos numeros de la sucesión de Fibonacci solo devuelva los numeros hasta un máximo. Una vez que esto pase, eleva el error StopIteration

import time

class FiboIter():

    def __init__(self, max= None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        
        else:
            if self.counter == 0 and self.n1 <= self.max:
                self.counter += 1
                return self.n1
            elif self.counter == 1 and self.n2 <= self.max:
                self.counter += 1
                return self.n2
            elif self.counter > 1:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux
                if self.aux >= self.max+1:
                    raise StopIteration
                self.counter += 1
                return self.aux

if __name__ == "__main__":
    fibonacci = FiboIter(987)
    for element in fibonacci:
        print(element)
        time.sleep(0)