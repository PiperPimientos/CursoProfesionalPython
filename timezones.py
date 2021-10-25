# En cada país la fecha es distinta, tendremos que utilizar los timezones.
# Hay que instalar con pip el modulo pytz, pues no viene de fabrica con Python.

# En cada país la fecha es distinta, tendremos que utilizar los timezones.
# Hay que instalar con pip el modulo pytz, pues no viene de fabrica con Python.
# pip install pytz
# 1.	from datetime import datetime
# 2.	import pytz
# 3.	Para trabajar con timezones tenemos que ver el link de database de time zones en el mundo.
# 4.	Haremos Bogota, Mexico y caracas
# 5.	Guardaremos en una variable bogota_timezone que tendrá asignado pytz.timezone(), este método timezone() recibirá como parámetro el Timezone de bogota que es (“America/Bogota”)
# 6.	Creamos otra variable para el date bogota_date = datetime.now(bogota_timezone)
# 7.	Lo imprimimos en pantalla con print(“Bogota: “, bogota_date.strftime('%d/%m/%Y, %H: %M: %S:')) y de una vez le damos el formato que queramos a la fecha con el método .strftime()


from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogota: ", bogota_date.strftime("%d/%m/%Y, %H: %M: %S:"))


# Despues, tendriamos que modularizar esto y meterlo dentro de una funcion para no tener que repetir código.

