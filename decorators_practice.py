# Ahora veremos un ejercicio práctico de decoradores y es algo sumamente útil que podremos llevar a cualquier proyecto en el que estemos trabajando. Nuestro proyecto consiste en: 

# 1.	Crear un decorador llamado execution_time(func), este es un decorador que nos sirve para averiguar cuanto tiempo tarda en ejecutarse una funcion, que sirve para medir la eficiencia de nuestros programas.
# 2.	Vamos a importar un modulo especial, datetime.
# from datetime import datetime
# Este modulo contiene una metodo con el mismo nombre, por eso hay que colocarlo entero. Con este calcularemos el tiempo que tarda en ejecutarse una funcion. 
# 3.	Dentro de nuestro decorador, definiremos nuestra funcion def wrapper que tendrá como funcionamiento, el tiempo que nuestra funcion se tarda en ejecutarse. Para esto tenemos una operación:
# Vamos a calcular el momento actual, del tiempo presente, creando una variable llamada initial_time que va estar asignada a datetime.now(), este método .now(), nos devuelve la hora y fecha exacta en la que se ejecuta esta línea de código.
# initial_time = datetime.now()
# Luego solo ejecutamos nuestra funcion decorator, con func()
# Y por ultimo calcularemos el tiempo final final_time
# final_time = datetime.now()
# Es decir, calculamos el tiempo, ejecutamos la funcion y luego calculamos el tiempo de nuevo.
# Que tenemos que hacer entonces para saber cuanto tardo en ejecutarse la funcion? Restar el tiempo final, del tiempo inicial, para saber que cantidad de microsegundos tardo la funcion en ejecutarse. Esto lo guardaremos en una variable
# time_elapsed = final_time – initial_time
# Por ultimo imprimiremos el mensaje que nos diga cuanto demoro
# print(“Pasaron” + time_elpased.total_seconds() + “ segundos”.
# El metodo .total_seconds() del objeto time_elapsed, que nos permite obtener la cantidad de segundos de esa diferencia temporal que calculamos.
# Finalmente, tenemos que corregir un posible error Typo, pues no podemos concatenar esos strings con las variables time_elapsed y su método, que son floats, entonces los convertiremos a string.
# print(“Pasaron” + str(time_elpased.total_seconds()) + “ segundos”.


# Finalmente, retornaremos la funcion wrapper() dentro de nuestro decorador, como nos lo dicen las reglas de los closures.
# 4.	Ahora crearemos una funcion llamada random_func() que será el objeto de nuestro experimento de cuanto tarda en ejecutarse una funcion. Que lo que hace es un ciclo for. 
# Cuando nosotros tenemos un ciclo for y no nos interesa tener en el código el valor de cada vuelta que recorremos en el ciclo se suele poner en la industria un guion bajo
# for _ in range(1, 1000000):
#             pass
# Es decir que no haremos nada, solo que de millon de vueltas a ver cuanto se demora en darlas. 
# Si a este punto ejecutaramos random__func() en consola, daría mil vueltas, pero no pasaría nada. Para saber cuanto tardo, tenemos que decorarla
# @execution_time
# def random_func():
#         for _ in range(1, 1000000):
#                      pass


# from datetime import datetime

# def execution_time(func):
#     def wrapper():
#         initial_time = datetime.now()
#         func()
#         final_time = datetime.now()
#         time_elapsed = final_time - initial_time
#         print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
#     return wrapper

# @execution_time
# def random_func():
#     for _ in range(1, 1000000):
#         pass

# random_func()

#Si ejecutamos en terminal veremos como efectivamente nos dice en cuanto tiempo se ejecuta

# Ahora comentaremos la ejecucion random_func() y que pasa si creamos otra funcion adicional, llamada suma, que suma los parámetros a y b.
# 1.	Ademas, lo haremos con tipado estatico, diciendo que nos retorna un int
# def suma(a: int, b: int) -> int:
#        return a + b
# 2.	Si decoramos esta funcion previamente con @execution_time, anticipamos que esto no va funcionar si no ejecutamos la funcion con los parámetros
# suma(5, 5)
# PERO, aun asi, nos sale un TypeError: wrapper() takes 0 positional arguments but 2 were given.
# Esto que es? pues basicamente que nuestro wrapper nos dice que no tiene parámetros, pero le pasamos dos. Es decir que la func, dentro del nested function, necesita tener parámetros a y b.
# Tenemos que tomar en cuenta que podremos tener funciones originales sin parámetros, como random_func(), en cambio, otras que si tienen parámetros como suma(a: int, b: int)
# Para solucionar esto, como parámetro de nuestro wrapper y dentro de func(), pasaremos
# def wrapper(*args, **kwargs):
# Esto, básicamente, es que le decimos a wrapper y a func, es que no importa la cantidad de argumentos posicionales que se le envíen, la funcion los va recibir. Y que no importa la cantidad de argumentos nombrados, la funcion también los va recibir. args, hace referencia a arguments, y el asterisco indica que son posicionales, que es el operador de desestructuración dentro de Python, Y **kwargs, es porque tenemos funciones como suma, u otra funcion hipotética como saludo() que lo que hace es recibir un parámetro nombrado o keyword argument al cual le ponemos por ejemplo un identificador y un valor por defecto nombre=”Cesar”. Y el print sea (“Hola “, nombre)


from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): #Es para poder decirle a las funciones que reciban los argumentos posicionales
        initial_time = datetime.now()
        func(*args, **kwargs) 
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre="Cesar"):
    print("Hola " + nombre)

suma(5, 5)
random_func()
saludo("Felipe")

#Nos va mostrar cuanto demoraron.
