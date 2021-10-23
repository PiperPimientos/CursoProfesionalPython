# Haremos nuestro clásico proyecto de palindrome.py pero de las maneras mas profesionales posibles y utilizando el static typing.
#  En nuestro venv, vamos a instalar el modulo que necesitamos para trabajar enn nuestro proyecto, que será mypy. Esto lo hacemos en al terminal con pip install mypy
#  El objetivo es crear una funcion que nos diga si un string es un palíndromo o no.
# 1.	nombre de la funcion: is_palindrome y lo tendremos que hacer con tipo, estonces la sintaxis quedaría asi
# def is_palindrome(string: str)
# Luego vamos a indicar con la flecha ->, que esta funcion devuelve un valor de tipo booleano.
# 	bool:
# a.	Adentro de este parámetro vamos a hacer una serie de tratamientos para averiguar si es un palíndromo o no.
# string = string.replace(“ “, “ “).lower() lo que hacemos con esto es reemplazar los espacios vacíos por la cadena vacia. Y finalmente, colocamos esa cadena de caracteres en minúscula con el método .lower()
# b.	Ahora retornaremos el resultado de la siguiente expresión.
# return string == string[::-1] con los slices. Que aqui lo que nos permiten decir es que string es igual a string al revez
# 2.	Ahora solo nos queda escribir nuestra funcion run, que contendrá el print llamando a la funcion con el parámetro, que si es palíndromo, será True y si no es aplinndromo, será Flase.
# def run()
#      print(is_palindrome(“ana”))
# 3.	entry point
# if __name__ == ‘__main__’:
#                  run()
# def is_palindrome(string: str) -> bool:
#     string = string.replace(" ", "").lower()
#     return string == string[::-1]

# def run():
#     #print(is_palindrome("ana")) RESULTADO: True
#     print(is_palindrome(1000)) #Resultado AtributeError, tenemos que utilizar el modulo mypy con la siguiente linea "mypy palindrome.py –check-untyped-defs" para que nos diga donde tuvimos el error de tipo

# if __name__ == '__main__':
#     run()


# 4.	Si ejecutamos, hasta el momento, vemos que esta bien. Pero que pasa si le pasamos el numero 1000? pues, tendremos un error que será un AttriubuteError, y nos dira que un objeto tipo int no tendrá el atributo replace. El error en realidad es que necesita un tipo str y le estamos pasando un numero int. Lo que necesitamos saber en realidad del error es que Python esperaba un valor tipo str. Esto lo hacemos utilizando el modulo mypy
# Abriremos la consola y ejecutaremos el comando mypy palindrome.py –check-untyped-defs
# Ese flag de –check-untype-defs, nos permite ver los errores de tipo, cuando estamos por ejemplo invocando a una función con un parámetro que no es del tipo que le corresponde. Y mypy nos va decir lo siguiente. 

 
# Nos lanza el traceback que nos dice que en is_palindrome, tenemos un tipo incompatible int¸ y que esperaba un str.


def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]

def run():
    #print(is_palindrome("ana")) RESULTADO: True
    print(is_palindrome(1000)) #Resultado AtributeError, tenemos que utilizar el modulo mypy con la siguiente linea "mypy palindrome.py –check-untyped-defs" para que nos diga donde tuvimos el error de tipo

if __name__ == '__main__':
    run()



# RETO:
# Crea un programa que verifique si un numero es primo o no, pero hazlo con tipado estático.

def es_primo(numero: int) -> bool:
    for i in range(2, numero):
        if numero % i == 0:
            # print(f"{numero} mod {i} ==",str(numero%i))
            return False
    return True


def run():
    print(es_primo(13))

if __name__ == '__main__':
    run()

