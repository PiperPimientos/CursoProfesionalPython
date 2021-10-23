# TIPADO ESTATICO: Lecturas recomendadas

 
# typing — Soporte para type hints — documentación de Python - 3.9.6
# https://docs.python.org/es/3/library/typing.html

 
# Getting started — Mypy 0.910 documentation
# https://mypy.readthedocs.io/en/stable/getting_started.html

# El Tipado dinamico es peligroso por la cantidad de errores de tipado a los que puede dar lugar en momento de ejecución. 
# Vamos a crear un archivo estatic_typing.py para entender mas sobre esto
# Para hacer que Python sea de tipado estático es necesario agregar algo de sintaxis adicional a lo aprendido, además, esta característica solo se puede aplicar a partir de la versión 3.6.
# # De esta manera se declara una variable, se colocan los dos puntos (:), el tipo de dato y para finalizar se usa el signo igual para asignar el valor a la variable.

# <variable> : <tipo_de_dato> = <valor_asignado>

a: int = 5
print(a)

b: str = "Hola"
print(b)

c: bool = True
print(c)
# Del mismo modo se puede usar esta metodología de tipado en Python a funciones adicionando el signo menos a continuación del signo mayor que para determinar el tipo de dato. Ejemplo:
def <nombre_func> ( <parametro1> : <tipo_de_dato>, <parametro2> : <tipo_de_dato> ) ->  <tipo_de_dato> :
	pass

def suma(a: int, b: int) -> int : #La flecha sirve para indicar que tipo va ser lo retornado
	return a + b

print(suma(1,2)) #aqui python nos devuelve los strings concatenados

# 3
Existe una librería de fabrica que viene preinstalada con Python que se llama typing, que es de gran utilidad para trabajar con tipado con estructuras de datos entre la versión 3.6 y 3.9, entonces:
.
from typing import Dict, List

positives: List [int] = [1,2,3,4,5]

users: Dict [str, int] = { #aqui se define el tipo de dato de las llaves y el tipo de dato de los valores
	"argentina": 1.
	"mexico": 34,
	"colombia": 45,
}

countries: List[Dict[str, str]] = [
	{
		"name" : "Argentina",
		"people" : "45000",
	},
	{
		"name" : "México",
		"people" : "9000000",
	},
	{
		"name" : "Colombia",
		"people" : "99999999999",
	}
]


#este ejemplo es un poco mas complejo
from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]] #es una lista que contiene diccionarios cuyas llaves son strings y sus valores son tuplas de dos enteros

coordinates: CoordinatesType = [
	{
		"coord1": (1,2),
		"coord2": (3,5)
	},
	{
		"coord1": (0,1),
		"coord2": (2,5)
	}
]

# Modulo mypy
# .
# El modulo mypy se complementa con el modulo typing ya que permitirá mostrar los errores de tipado debil en Python.


# comentario util:
# Recomiendo usar Optional[], de la libreria typing, es para cuando ocupamos retornar None u otra variable

# def foo() -> Optional[List]:
#   if b:
#     return []
#   else:
#     None