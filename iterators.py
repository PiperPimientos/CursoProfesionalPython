# Los iteradores son estructuras de datos avanzadas, aun mas que las listas, tuplas, diccionarios, etc. Y específicamente son estructuras de datos para guardar datos infinitos.

# La primera estructura de datos que veremos son los iteradores, sobre los cuales también nos pueden preguntar en entrevistas técnicas de trabajo.
# Para entender de que se tratan los iteradores, tenemos que saber que son los iterables. Los iterables son los objetos que podemos recorrer en un ciclo, como una lista, mediante un ciclo for accederemos a ellas, otro iterable son los strings, que podemos recorrer carácter a carácter.
# Cuando nosotros hacemos un ciclo, Python internamente no esta recorriendo el iterable, sino que para recorrerlo, Python debe convertirlo en un objeto especial llamado iterador. 
# Ejemplo:

# Creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

print(next(my_iter))

# Cuando no quedan datos, la excepcion StopIteration es elevada

# Tenemos una lista, que por si misma no puede ser recorrida por un ciclo for dentro de Python. Lo que hace el lenguaje es utilizar una funcion interna llamada iter para convertir los iterables en iteradores.
# Una vez que tenemos el objeto tipo iterador, puedo acceder a cada uno de los elementos utilizando el método built in, .next(), que lo que hará al llamarla, será entregarnos el numero 1, luego si la llamo otra vez, el numero 2, una vez finaliza, me saltara error, de tipo StopIteration.
# Podemos hacer eso de esta manera. Pero si tengo muchísimos elementos no podemos hacerlo manualmente. Como podríamos hacerlo?

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

# Si miramos este codigo, tenemos los mismos valores en my_iter y my_list, pero necesitamos un ciclo while para poder recorrer este iterador y es infinito, porque tiene el booleano True, es decir que while siempre va ser True y por lo tanto ejecutado.
# Tenemos un try, except, tratando de sacar el siguiente elemento de nuestro iterador con la funcion next(). En el caso en que exista el error StopIteration, cortaremos el ciclo con el break.


# Python tiene una manera de hacer esto mas fácil: Un ciclo for.

for element in my_list:
    print(element)

# Un ciclo for no es mas que sugar sintax o azúcar sintáctica, de lo que veíamos antes. El ciclo for, en realidad es un alias de ese ciclo while con try except que recorre el iterador.

# Como construyo un iterador? Aquí es donde se hace necesario el curso de Programacion Orientada a Objetos, pues necesitaremos construir clases y métodos.
# El protocolo del iterador nos dice que para construir uno debemos de tener una clase que contenga dos métodos importantes:
# El método dunder item y el método dunder next. Miremos un ejemplo:

class EvenNumbers:

    """Clase que implementa un iterador de todos los numeros pares,
    o los numeros pares hasta un maximo"""

    def __init__(self, max=None):
        self.max = max
    
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration

# Tenemos una clase llamada EvenNumbers(Even numbers quiere decir numeros pares), que posteriormente se convertirá en un iterador del mismo nombre. Esto se hace
# 1.	Para empezar tenemos un constructor que es el metodo dunder init y es necesario en Programacion orientada a objetos en Python para poder tener una clase, __init__. Como primer parámetro tenemos self que hace referencia al objeto futuro que crearemos con esta clase y tengo otro llamado max que tiene el valor de None por defecto, esto sirve para ponerle un máximo y que no se itere hasta el infinito. Entonces en el constructor se lee que el atributo max de este objeto que posteriormente va ser un iterador va ser igual al parámetro max. 
# 2.	Luego en los siguientes dos def, tenemos esos iteradores necesarios de los que hablamos que son dunder iter y dunder next (__iter__, __next__)
# 3.	El método def __iter__(self), sirve para tener elementos o atributos que yo voy a necesitar para que mi iterador funcione. En este caso el único atributo que yo necesito, es cada uno de los numeros de esa iteración. En este caso le llamamos num de number y por eso es self.num = 0 y le asignamos ese valor de 0 porque es el primer numero par. Y finalmente lo que hacemos dentro del método dunder iter, es retornar al objeto en si mismo, es decir un return de self. Es decir, este método dunder iter, se traduce en esa funcion built in, iter() que vimos en los ejemplos anteriores, que lo que hace, recordemos, es convertir un iterable en un iterador.
# 4.	Por ultimo tenemos el método dunder next, posteriormente convertido a la funcion built int next() en python. Este método nos permite extraer cada uno de los elementos de mi iterador. Y si queremos extraer todos los numeros pares o todos los numeros pares hasta un máximo.
# Para ello:
# a.	Tendremos una condicional con la siguiente sintaxis
# if not self.max or self.num <= self. max:
# que significa: Si no existe Self.max (no existe numero máximo como parámetro), o el numero que estoy recorriendo en esta vuelta del iterador es menor o igual a self.max, es decir, estoy recorriendo un numero y todavía no llegue al máximo o estoy ya en el máximo, lo que hago es lo siguiente :(…)
# Asignarle a una variable result = el valor de self.num. Porque result es la variable que yo despues voy a presentar en pantalla.
# Despues le sumo 2 a self.num, recordando que num es ese valor que va por cada vuelta del iterador, es decir que si el primer valor es 0, el siguiente valor va ser 2, el siguiente va ser 4, y asi sucesivamente.
# Por ultimo se hace un return de result, para que retorne siempre el siguiente elemento de mi iterador, es decir que lo que hago es asignarle a una variable result el valor del atributo num que teníamos (era 0 al comienzo), le sumo el valor de 2, y ese resultado lo retorno a result.

# Por ultimo esta el else, es decir que si el condicional no se cumple, pues que nos eleve raise, el error StopIteration.
# Las ventajas de usar iteradores:
# 1.	El iterador nos ahorra recursos, yo puedo almacenar secuencias matemáticas completas. En el iterador podemos guardar la totalidad de los numeros pares.
# 2.	Ocupan poca memoria
# 3.	Son una función matemática que nos permite extraer el siguiente elemento de una secuencia
