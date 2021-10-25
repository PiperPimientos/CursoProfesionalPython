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