# Una variable solo está disponible dentro de la región donde fue creada. Scope es el alcance de las variables, es decir, hacia donde va una variable y hasta dónde llega.
# El primer scope es el Local Scope. Que es la región en donde vive una funcion en donde viven 1 o mas variables y tiene su propio alcance que es todo lo que está escrito hacia abajo.

#Local Scope
def my_func():
    y = 5
    print(y)

my_func()

#Global Scope
y = 5
def my_func():
    print(y)

def my_other_func():
    print(y)

my_func()
my_other_func()

# En donde basicamente vemos que tenemos variables que tienen alcance en todo el programa, como la variable y, que va poder ser accedida y leida dentro de todas las funciones que tenemos despues.

#Otro ejemplo

z = 5

def my_func():
    z = 3
    print(z)

my_func()

print(z)

# Aquí vemos que tenemos la variable z en el scope global asignada a 5 y luego dentro de la funcion reasignamos un 3 a la variable z. En esta pieza de código se imprima tanto el 3 como el 5, es porque ambas variables son distintas aunque tengan el mismo nombre. El alcance global tiene la variable z que tiene asignado el valor de 5, y existe el scope local que tiene una variable z asignado el valor de 3.

# Miremos otro ejemplo:

z = 5

def my_func():
    z = 3
    def my_other_func():
        z = 2
        print(z)
    
    my_other_func()
    print(z)

my_func()
print(z)

# El resultado que se imprimirá en consola en este caso es tanto 5, 3 y 2, esto es porque asi tengamos por ejemplo una funcion dentro de otra funcion, ambas asignando un nuevo valor para z, es porque las tres variables z son diferentes.



