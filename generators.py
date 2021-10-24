# Implementar iteradores es bastante complejo. Python entiende que es complejo y por lo tanto nos da una solución que son los Generadores, los sugar syntax de los iteradores.
# Los generadores son básicamente funciones que guardan un estado y no es tan difícil almacenar secuencias infinitas.
# Los generadores son funciones, a diferencia de los iteradores que son clases, una clase necesita mas sintaxis, mas densidad de código. etc.
# Aquí tenemos un generador llamado my_gen():

def my_gen():
    """Un ejemplo de generators"""

    print('Hello World')
    n = 0
    yield n

    print('Hello Heaven')
    n = 1
    yield n

    print('Hello Hell')
    n = 2
    yield n

a = my_gen()
print(next(a)) #Hello World
print(next(a)) #Hello Heaven
print(next(a)) #Hello Hell
print(next(a)) StopIteration

# Imprime Hello World, crea una variable interna dentro del scope local, llamada n, que contiene el valor 0 y hace un yield de n. Un Yield es exactamente lo mismo que la palabra clave return. Solo hay una diferencia, yield en lugar de terminar a la funcion como return, yield lo que hace es pausar a la funcion hasta donde estaba ese yield. Es decir que si yo vuelvo a llamar a la funcion, la funcion va empezar desde donde se llamo al ultimo yield.
# Como se menciono al principio, el yield guarda un estado, por lo que cuando se reanude la funcion, va guardar exactamente los mismos valores que tenia.
# Tambien, dijimos que un generator era sugar sintax de un iterador, por lo tanto también tenemos que instanciarlo, es decir, a partir de la funcion tenemos que crear el objeto de tipo generator. Por eso decimos que a esta asignado al resultado de ejecutar la funcion my_gen()
# a = my_gen()
# Es decir que en a se va guardar un objeto de tipo generator que contiene todo el código que vemos en pantalla
# Y finalmente si utilizamos la funcion built in, next(), en lugar de trabajar como si fuera un iterador e iterar el siguiente elemento, la funcion gen, va llevarnos al ultimo yield.

# Algo interesante: los generator expression:

my_list = [0,1,4,7,9,10]

my_second_list = [x*2 for x in my_list] #List comprehension
my_second_gen = (x*2 for x in my_list) #Generator expression

