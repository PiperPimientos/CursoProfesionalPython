# Los closures son un concepto avanzado de las funciones y se utilizan mucho para las pruebas técnicas de los trabajos. De hecho, Que es un closure?
# Pero primero tenemos que entender que son las Nested functions, o funciones anidadas, es decir que están creadas dentro de otras funciones. Veamos el ejemplo:

def main():
    a = 1

    def nested():
        print(a)
    
    nested()

main()

# Aquí tenemos una funcion main, que tiene una variable asignada al valor de 1. Luego tenemos la funcion anidada o nested que dentro de si imprime esa variable a. El resultado es claro, al llamar la funcion nested() y llamar su funcion main(), donde esta anidada, se va imprimir la variable a.

# Y si en vez de ejecutar a nested dentro de la funcion main() yo la retorno?
def main():
    a = 1

    def nested():
        print(a)
    
    return nested

my_func = main()
my_func()

# Lo que va pasar es que igual va imprimir el valor de la variable a en pantalla. Esto quiere decir que yo despues podría crear otras variables como por ejemplo my_func, a las cuales les asigno el resultado de lo que pase en la ejecución de la funcion main(). Y que va pasar en la ejecución de la funcion main()? Pues se crea la variable a, luego la funcion nested y dentro se imprime la variable a. Luego dentro de main, retornamos la funcion nested, es decir que en ultimas estamos ejecutando una nested function y el print que para este ejemplo contiene. Esta técnica mediante la cual los valores que están en scopes superiores son recordados, es conocida como Closure. Un closure en definitiva se da cuando una variable que esta en scope superior es recordada por un scope inferior, aunque el scope superior sea eliminado despues. Veamos el ejemplo


def main():
    a = 1

    def nested():
        print(a)
    
    return nested

my_func = main()
my_func()

del(main)

my_func()

# En este caso lo que se va imprimir en pantalla será dos veces el valor de la variable a, es decir, dos veces 1. Esto por que pasa? Porque la nested function esta recordando una variable, de un scope superior y por lo tanto, se da un Closure.
# Reglas para encontrar un closure
# 1.	debemos tener una nested function, sino, no es un closure.
# 2.	la nested function debe referenciar un valor de un scope superior
# 3.	la función que envuelve la nested debe retornarla también
# cuando tenemos una clase que tiene solo un método
# cuando trabajamos con decoradores

# Veamos algún caso clásico de los closures, tenemos este código


def make_multiplier(x):

    def multiplier(n):
        return x * n
    
    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))

# La impresión en pantalla en este caso será, 30, 20, 80.
# Pero fijémonos, tenemos una funcion que recibe un parámetro x en el scope global. Luego tenemos una nested function que tiene como parámetro n, esta funcion recuerda un valor de un scope superior, porque lo que hace es retornar el resultado de multiplicar x * n. Y por ultimo, dentro de la funcion de scope global, se retorna multiplier, que es esa funcion nested. Cumplimos con las condiciones de los Closures. 
# Con esto se pueden crear funciones personalizadas como por ejemplo times10, que va ser igual que multiplicar make_multiplier, con el valor de 10; lo que pasara es que se ejecutara make_multiplier, es decir, ese parámetro x ahora tendrá el valor de 10, y luego ejecutara multiplier que multiplicaría ese 10, por n que es un valor que hasta ahora no conocemos y, finalmente, se va retornar multiplier. Por lo tanto times10 va contener una funcion del tipo multiplier que esta recordando al valor 10 como x. Lo mismo pasa con la siguiente funcion times4, que tiene el 4.
# Ahora cuando vamos a imprimir en pantalla y hago por ejemplo times10 con el numero 3; como el numero 10 ya esta recordado, lo que va pasar es que yo le voy a estar dando el valor de n¸ que es el valor que recibe la funcion nested, multiplier, porque recordemos que al retornar a multiplier, times10, queda siendo una funcion del tipo multiplier. Por lo tanto se va multiplicar x por n y este valor se va a retornar, es decir 10 * 3 = 30.
# E incluso se pueden combinar las funciones, y ver que podemos multiplicar al resultado de times10, por el resultado de times4 con un 2 asignado a el parámetro n. Esto seria una clase 

# Los closures los vamos a encontrar en dos casos particulares:
# 1.	Cuando tengamos una clase que tiene solamente un método, aplicaremos Closures, para que esto sea mucho mas elegante (hablando en términos de POO)
# 2.	Y un segundo caso donde aparecen los closures, es cuando trabajamos con Decoradores.
# Pero antes de trabajar con decoradores, veremos una clase practica de Closures.
