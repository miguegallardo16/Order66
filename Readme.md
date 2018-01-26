# MusQlus

MusQlus es una aplicacion que será capaz de realizar consultas y modificar los ficheros .rdf de los cromosomas del raton (mus musculus) y ademas será capaz de hacer queries en UnitProt sobre este

## Obtencion de los archivos

Primero clonaremos el repositorio:

* `git clone https://github.com/miguegallardo16/Order66.git`

A continuacion nos dirigiremos a UniProt y descargaremos los cromosomas que deseemos consultar.
Lo podras descargar desde este enlace:

* `ENLACEEEEEEEEEEEEEEEE`

## Ejecucion del programa

Una vez tenemos todo preparado, lo que tendremos es que abrir el cmd en el directorio en el que estemos trabajando.

Ejecutaremos el comando:

* `python ./ConsultasApp.py`

Por defecto esta puesto para trabajar con un archivo .rdf que nosotros hemos cogido del primero chromosoma y al que hemos llamado 'chromosome.rdf', asi que si no lo llamais de esta manera debereis cambiar el nombre del archivo con el que vayais a trabajar. Esto se hace modificando la lines de comando que dice:

* `g.parse('chromosome.rdf')`

