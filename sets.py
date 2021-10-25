# Los Sets, o en español, los Conjuntos son una estructura especial de Datos en Python.
# Los sets son una estructura de datos muy similares a las listas en cuanto a su forma, pero presentan ciertas características particulares:
# •	Los sets son inmutables
# •	Cada elemento del set es único, esto es que no se admiten duplicados, aun si durante la definición del set se agregan elementos repetidos pyhton solo guarda un elemento
# •	los sets guardan los elementos en desorden
# Para declararlos se utilizan los {} parecido a los diccionarios solo que carece de la composición de conjunto {a:b, c:d}


# Sintaxis:
# Creo una variable llamada my_set = y entre llaves coloco los elementos del set. Y aunque sabemos que las llaves se utilizan para definir diccionarios, cuando no colocamos ningún dos puntos dentro de las llaves Python entiende que esto es un set, conjunto.

 

# Si repetimos un elemento dentro de una set, al imprimirlo, Python automáticamente suprime el elemento repetido.

# Y las los sets no pueden contener elementos mutables como las listas, por lo que si incluimos por ejemplo una tupla, si podrá guardarla dentro de un set.

# si queremos crear un set vacio, no podemos simplemente dejar las llaves vacias, porque Python lo tomara como si fuera un diccionario

empty_set = {}
print(type(empty_set)) # Sale que es de tipo dict

# Tenemos que utilizar la palabra clave set

empty_set = set()
print(type(empty_set)) # Sale que es un set


# Tambien Podemos hacer casting, es decir, pasar un tipo de estructura de datos cualquiera a un set y veremos que incluso los elementos repetidos se eliminan.

my_list = [1,1,2,3,4,4,5]
my_set = set(my_list)
print(my_set) #OUTPUT {1,2,3,4,5}

my_tuple = ("Hola", "Hola", "Hola", 1)
my_set2 = set(my_tuple)
print(my_set2) #OUTPUT {'Hola', 1}


# Veamos ejemplos:


# set de enteros
my_set = {1, 3, 5}
print(my_set)

# set de diferentes tipos de datos
my_set = {1.0, "Hi", (1, 4, 7)}
print(my_set)
# Los sets no pueden ser leídos como las listas o recorridos a través de slices, esto debido a que no tienen un criterio de orden. Sin embargo si podemos agregar o eliminar items de los sets utilizando métodos:
# •	add(): nos permite agregar elementos al set, si se intenta agregar un elemento existente simplemente python los ignorara
# •	update(): nos permite agregar múltiples elementos al set
# •	remove(): permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python elevará un error
# •	discard(): permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python dejará el set intacto, sin elevar ningún error.
# •	pop(): permite eliminar un elemento del set, pero lo hará de forma aleatoria.
# •	clear(): Limpia completamente el set, dejándolo vació.
#ejemplo de operaciones sobre sets 
my_set = {1, 2, 3} 
print(my_set) #Output {1, 2, 3} 

#añadiendo un elemento al set 
my_set.add(4) 
print(my_set) #Output {1, 2, 3, 4}

#añadiendo varios elementos al set, python ignorará elementos repetidos 
my_set.update([1, 5, 6]) 
print(my_set) #Output {1, 2, 3, 4, 5, 6}

# eliminado elementos del set 
my_set.discard(1) 
print(my_set) #Output {2, 3, 4, 5, 6}

# borrando un elemento aleatorio 
my_set.pop()
print(my_set) #Output el set menos un elemento aleatorio 

#limpiar el set 
my_set.clear()
print(my_set) # Output set() 
# Podemos utilizar estructuras de datos existentes para transformarlas a sets utilizando el método set:
#usando listas para crear sets
my_list = [1, 2, 3, 3, 4, 5]
my_set = set(my_list)
print(my_set)  #output {1, 2, 3, 4, 5}

#usando tuplas para crear sets 
my_tuple: ('hola', 'hola', 1, 2)
my_set2: set(my_tuple)
print(my_set2) #Output {'hola', 1}
