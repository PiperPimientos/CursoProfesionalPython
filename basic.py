# ¿Qué necesitas saber para tomar el curso? 1/21
# Lecturas recomendadas

 
# Curso de Python [Empieza Gratis] - Platzi
# https://platzi.com/cursos/python/

 
# Curso de Git y Github [Empieza Gratis] - Platzi
# https://platzi.com/cursos/git-github/

 
# Curso de Python Intermedio - Platzi
# https://platzi.com/cursos/python-intermedio/

 
# Curso de Programación Orientada a Objetos - Platzi
# https://platzi.com/cursos/oop/


# ¿Cómo funciona Python? 2/21

# Primero hay que entender como funcionan las clasificaciones a lenguajes de programación. Veamos el siguiente grafico que nos ilustrara.
 

# Python es un lenguaje interpretado
# lo que significa que tu código es transformado por el intérprete (máquina virtual de Python) a bytecode antes de ser ejecutado por un ordenador con x sistema operativo. El bytecodees un lenguaje de programación de más bajo nivel (si esto no te es claro, te recomiendo que vayas a tomar los cursos sobre lenguajes y paradigmas de programación y el de fundamentos de ing. de software. (Básicamente desde que corres tu programa hasta que la PC lo ejecuta hay una carrera de relevos de lenguajes o protocolos hasta llegar al transistor y la señal eléctrica)
# .
# Garbage collector
# Recuerda que el garbage collector toma los objetos y variables que no están en uso y los elimina.
# .
# pycache
# _pycache _ es el directorio (carpeta) que contiene el bytecode (el código intermedio) que crea Python para que lo pueda leer la máquina virtual.


# Cómo organizar las carpetas de tus proyectos 3/21
# Para saber como organizar las carpetas de nuestros proyectos de Python es necesario entender la dieferencia entre paquetes y modulos.
# 📁Un módulo es cualquier archivo de Python. Generalmente, contiene código que puedes reutilizar. Hemos visto diferentes modulos, como el modulo random, para trabajar con la aleatoriedad. 
# 🗄 Un paquete es un conjunto de módulos. Siempre posee el archivo __init__.py. When a new object is made, it is initialized by calling the init method on the object. __init__ is pronounced “dunder init”: dunder is short for “double-underscore”.
# Una ejemplo de organizar los archivos de 🐍Python es de la siguiente manera.



# ¿Qué son los tipados? 4/21
# Lecturas recomendadas

 
# Platzi English Academy
# https://platzi.com/idioma-ingles/

 
# terminology - Static/Dynamic vs Strong/Weak - Stack Overflow
# https://stackoverflow.com/questions/2351190/static-dynamic-vs-strong-weak

# ¿Qué son los tipados?
# Si recordamos cuales son los tipos o datos primitivos, recordaremos que tenemos strings, booleanos, numeros y arreglos.

 

# 💻 Los tipados es una clasificación de los lenguajes de programación, tenemos cuatro tipos:
# •	Estático:
# •	Dinámico
# •	Débil
# •	Fuerte
# El tipado del lenguaje depende de cómo trata a los tipos de datos.
# El tipado estático es el que levanta un error en el tiempo de compilación, ejemplo en JAVA:
# String str = "Hello" // Variable tipo String
# str = 5 // ERROR: no se puede convertir un tipo de dato en otro de esta forma.

# El tipado dinámico levantan el error en tiempo de ejecución, ejemplo en Python:
# str = "Hello" # Variable tipo String
# str = 5 # La variable ahora es de tipo Entero, no hay error

# ## TIPADO FUERTE
# x = 1
# y = "2"
# z = x + y # ERROR: no podemos hacer estas operaciones con tipos de datos distintos entre sí
# El tipado débil es el que hace un cambio en un tipo de dato para poder operar con el, como lo hace JavaScript y PHP.
# 🐍 Python es un lenguaje de tipado 👾 Dinámico y 💪 Fuerte.





