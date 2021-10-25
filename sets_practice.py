# Veremos las operaciones con sets, que básicamente son uniones, intersecciones y diferencias.

# La unión de los conjuntos, es el resultado de combinar todos los elementos que tienen ambos.
#Ejemplo

my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 | my_set2
print(my_set3) #OUTPUT: {3,4,5,6,7}

# La intersección, es el resultado de combinar ambos sets, pero quedan solo con los elementos que tienen en comuun.
#Ejemplo

my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 & my_set2
print(my_set3) #OUTPUT: {5}

# La diferencia es el resultado de tomar dos sets y de uno quitar todos los elementos que tiene el otro.
# Ejemplo

my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 - my_set2
print(my_set3) #OUTPUT: {3, 4}

my_set4 = my_set2 - my_set1
print(my_set4) #OUTPUT: {6, 7}

# La diferencia simétrica es lo contrario de la intereseccion. El resultado de quedarme con los elementos de ambos sets pero sin los que se comparten

my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 ^ my_set2
print(my_set3) #OUTPUT: {3, 4, 6, 7}


# RETO:
# Realizar dos sets y con esos sets realizar todas las operaciones.



pokemon_tipo_fuego = { 'Charizard', 'Moltres' }
pokemon_tipo_volador = { 'Charizard', 'Butterfree', 'Pidgeot', 'Fearow', 'Dodrio', 'Gyarados', 'Aerodactyl', 'Articuno', 'Zapdos', 'Moltres', 'Dragonite' }
pokemon_tipo_veneno = { 'Butterfree' }
pokemon_tipo_normal = { 'Pidgeot', 'Fearow', 'Dodrio' }
pokemon_tipo_agua = { 'Gyarados' }
pokemon_tipo_roca = { 'Aerodactyl' }
pokemon_tipo_hielo = { 'Articuno' }
pokemon_tipo_electrico = { 'Zapdos' }
pokemon_tipo_dragon = { 'Dragonite' }

my_set1 = pokemon_tipo_fuego | pokemon_tipo_agua
print(f'Pokemon tipo fuego | agua: {my_set1}')

my_set2 = pokemon_tipo_normal & pokemon_tipo_volador
print(f'Pokemon tipo normal & volador: {my_set2}')

my_set3 = pokemon_tipo_volador - pokemon_tipo_fuego
print(f'Pokemon tipo volador - fuego: {my_set3}')

my_set4 = pokemon_tipo_dragon ^ pokemon_tipo_electrico
print(f'Pokemon tipo dragon ^ electrico: {my_set4}')







# Eliminar repetidos de una lista es un ejercicio muy común. Vamos a hacerlo para practicar el uso de sets, o conjuntos.

# Es decir, muchas veces voy a tener listas, diccionarios, tuplas, donde se van a repetir elementos y voy a querer eliminarlos. 

# Es decir, muchas veces voy a tener listas, diccionarios, tuplas, donde se van a repetir elementos y voy a querer eliminarlos. Utilizaremos un ciclo for para esto.
# 1.	Vamos a crear una funcion que elimine los duplicados de una lista:
# funcion remove_duplicates y como parámetro una lista llamada some_list
# def remove_duplicates(some_list).
# 2.	Adentro crearemos un una lista llamada without_duplicates, que contendrá una lista vacia y sera la que contenga los elementos sin repetir.
# 3.	Vamos a crear un ciclo for element in some_list:
# ponemos una condicional si el elemento no esta en without_duplicates: entonces le agregaremos a esta lista without_duplicates con el método .append(element), el elemento
# 4.	Por ultimo cuando termine este ciclo, retornamos without_duplicates

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()

# RETO: Crea un programa que elimine los elementos repetidos de una lista, pero en lugar de utilizar un ciclo for, utiliza sets.
