# MusQlus

MusQlus es una aplicacion que será capaz de realizar consultas y modificar los ficheros .rdf de los cromosomas del raton (mus musculus) y ademas será capaz de hacer queries en UnitProt sobre este

## Obtencion de los archivos

Primero clonaremos el repositorio:

* `git clone https://github.com/miguegallardo16/Order66.git`

A continuacion nos dirigiremos a UniProt y descargaremos los cromosomas que deseemos consultar.
Lo podras descargar desde este enlace:

* `[http://www.uniprot.org/proteomes/UP000000589](http://www.uniprot.org/proteomes/UP000000589)`

## Ejecucion del programa

Una vez tenemos todo preparado, lo que tendremos es que abrir el cmd en el directorio en el que estemos trabajando.

Ejecutaremos el comando:

* `python ./ConsultasApp.py`

Por defecto esta puesto para trabajar con un archivo .rdf que nosotros hemos cogido del primero chromosoma y al que hemos llamado 'chromosome.rdf', asi que si no lo llamais de esta manera debereis cambiar el nombre del archivo con el que vayais a trabajar. Esto se hace modificando la lines de comando que dice:

* `g.parse('chromosome.rdf')`

## Adaptacion a la interfaz

Encontraremos diferentes apartados, entre ellos:

### Realizar consultas manualmente

En este apartado tenemos la primera caja de texto, en la cual podremos escribir nosotros mismos una consulta SPARQL y realizarla pulsando el boton que se encuentra debajo 'Realizar consulta'

### Busqueda de proteina por secuencia de aminoacidos

Encontraremos un boton 'Busqueda por secuencia' y debajo una caja de texto, en esta podremos introducir una secuencia o parte de una secuencia de aminoacidos y nos devolvera su correspondiente proteina. La secuencia debe introducirse en mayusculas.

### Busqueda de proteina por comentario relazcionado a esta

Parecido a lo anterior, tendremos un boton 'Busqueda por comentario' y una caja de texto, en la cual podremos poner una palabra clave y nos devolvera el comentario correspondiente y tambien la proteina asociada a este.

### Cambiar cadenas de aminoacidos

Ahora encontraremos un boton 'Cambiar cadena' y dos cajas de texto, en una de ella pondremos la secuencia de aminoacidos que queremos introducir, y en la otra la que va a ser sustituida. Esta sustitucion se guardará en el fichero .rdf.

### Botones de consultas

Ahora encontraremos 4 botones, 'Identificadores', 'Etiquetas', 'Publicaciones' y 'Comentarios'.
Estos podran realizar consultas de muestras sobre esos atributos en el fichero o sobre la consulta que nosotros hayamos realizado con anterioridad.

### Consultas en la web UniProt

Encontraremos una gran caja de texto, otra mas pequeña y debajo un boton 'Consulta UNIPROT'. En la caja de texto que se encuentra encima del boton podremos poner el nombre del idedentificar de la proteina que deseamos buscar y se nos cargará la pagina correspondiente a esta en la caja de texto superior.

### Seleccion de fichero .RDF

Si deseamos cambiar de fichero desde la aplicacion, tan solo tendremos que escribir el nombre de este en la caja de texto que se encuentra encima del boton 'Seleccionar RDF', el cual pulsaremos para cargar dicho fichero. El nombre de este se tendrá que poner sin extension y estar en el mismo directorio en el que estemos ejecutando la aplicacion.