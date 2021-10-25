# Tenemos que aprender a trabajar con fechas dentro de Python, esto es importante porque cuando hagamos aplicaciones, vamos a necesitar manejar las fechas en las que se hacen algunas acciones. Por ejemplo manejar fechas en las que se crean, modifican, eliminan usuarios.
# Para esto utilizaremos un modulo llamado datetime.

#Ejemplo
import datetime
from time import daylight

my_time = datetime.datetime.now()

print(my_time) #OUTPUT 2021-10-24 20:28:30.394950

# Para entender, este modulo datetime, contiene una clase con el mismo nombre, datetime. Para yo ejecutar esta operación necesito llamar al modulo, con un punto acceder a la clase y con otro punto el método now, para que la hora sea la del momento preciso
# Esto si nos trae la fecha y la hora, pero la trampa es nos trae la hora de nuestro PC, pero si no hay fecha configurada nos trae la hora Universal Time Coordinated, UTC.

import datetime

my_day = datetime.date.today()

print(my_day) #OUTPUT 2021-10-24
# incluso poemos acceder a las diferentes partes de las fechas, con las clases .year, .month, .day
print(f'Year: {my_day.year}')

# Formateo de fechas:
# En todas partes los formatos de fechas pueden ser distintos
# por ejemplo en latam es dd/mm/yyyy
# En cambio en Usa es normal mm/dd/yyyy
# Si queremos cambiar el formato:
# Tenemos que aprendernos esta tabla:


# %Y ------ Year
# %m ------ Month
# %d ------ Day 
# %H ------ Hour
# %M ------ Minute
# %S ------ Second

#Y la utilizaremos asi:

from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str}')


# Comentario útil:
# Es importante evitar usar datetime.now() porque toma la hora local. Mejor usar datetime.utcnow() para usar la hora universal. Nosotros trabajamos con equipos de todo el mundo, no podemos usar hora local
