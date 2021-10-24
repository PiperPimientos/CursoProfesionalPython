# Recordemos que los closures tienen 3 reglas:

# 1.	debemos tener una nested function, sino, no es un closure.
# 2.	la nested function debe referenciar un valor de un scope superior
# 3.	la función que envuelve la nested debe retornarla también

# Y que nos los podemos encontrar en dos casos:

# Los closures los vamos a encontrar en dos casos particulares:
# 1.	Cuando tengamos una clase que tiene solamente un método, aplicaremos Closures, para que esto sea mucho mas elegante (hablando en términos de POO)
# 2.	Y un segundo caso donde aparecen los closures, es cuando trabajamos con Decoradores.
# Pero antes de trabajar con decoradores, veremos una clase practica de Closures.

# Haremos un ejemplo con un closure que repita strings dependiendo de un numero posible. Por ejemplo, si yo doy la palabra Hola y luego el valor 3, me devuelva “HolaHolaHola”
# 1.	Vamos a crear la funcion global make_repeater_of(n): es decir, va ser un repetidor de n veces.
# 2.	Adentro voy a crear nuestra nested function, que se va llamar repeater y va recibir string como parámetro. Este scope va retornar el scope superior, es decir return string * n.
# 3.	La funcion nested debe estar retornada.
# 4.	Vamos a agregar complejidad con un assert statement
# assert type(string) == str, “Solo puedes utilizer strings”
# es decir que nosotros afirmamos que lo que nos llega a esta nested function es un string. Y Vamos a agregar el error de que solo se puede utilizar cadenas
# 5.	Ya solo nos falta crear una funcion run() que será la principal, y valli vamos a crear la funcion llamada repeat_5 que tendrá asignada la ejecucion de make_repeater_of con el valor de 5.
# repeat_5 = make_repeater_of(5)
# Hasta aquí lo que sucede es que se ejecuta la funcion de scope global, con el numero 5 como valor de n. Esta funcion ejecuta la nested function, que tendrá como parámetro string, luego la afirmación que nos permite asegurarnos de que string sea de tipo str y que de lo contrario mande un mensaje advirtiendo. Finalmente si efectivamente es un string, la nested function retornara el valor de string multiplicado por n. Por ultimo la funcion retorna repeater, es decir que repeat_5, será una funcion de repeater.
# 6.	Ahora, para que se ejecute solo queda imprimir el resultado de por ejemplo repeat_5, con el string “Hola” Y veremos que al ejecutar, la impresión será “HolaHolaHolaHolaHola”

# def make_repeater_of(n):
#     def repeater(string):
#         assert type(string) == str, "Solo puedes utilizar strings"
#         return string * n
#     return repeater

# def run():
#     repeat_5 = make_repeater_of(5)
#     print(repeat_5("Hola"))

# if __name__ == '__main__':
#     run()


# RETO: Miremos el siguiente código:

def make_division_by(n):
    """This closure returns a function that returns the division
    of an x number by n"""
    #have to code here
    def division(x):
        assert type(x) == int, "Solo puedes utilizar numeros enteros"
        return x / n
    return division

division_by_3 = make_division_by(3)
print(division_by_3(18)) #The expected output is 6

division_by_5 = make_division_by(5)
print(division_by_5(100)) #The expected output is 20

division_by_18 = make_division_by(18)
print(division_by_18(54)) #The expected output is 6



# Esta documentado, indicandonos que esste closure retorna una funcion que retorna la división de un numero x por n.

#Reto completado