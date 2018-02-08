# MusQlus

MusQlus es una aplicacion que será capaz de realizar consultas y modificar los ficheros .rdf de los cromosomas del raton (mus musculus) y ademas será capaz de hacer queries en UnitProt sobre este

## Obtención de los archivos

Primero clonaremos el repositorio:

* `git clone https://github.com/miguegallardo16/Order66.git`

A continuacion nos dirigiremos a UniProt y descargaremos los cromosomas que deseemos consultar.
Lo podras descargar desde este enlace:

* `http://www.uniprot.org/proteomes/UP000000589`

## Ejecución del programa

Una vez tenemos todo preparado, lo que tendremos es que abrir el cmd en el directorio en el que estemos trabajando.

Ejecutaremos el comando:

* `python ./ConsultasApp.py`

Por defecto esta puesto para trabajar con un archivo .rdf que nosotros hemos cogido del primero cromosoma y al que hemos llamado 'chromosome.rdf', asi que si no lo llamais de esta manera debereis cambiar el nombre del archivo con el que vayais a trabajar. Esto se hace modificando la lines de comando que dice:

* `g.parse('chromosome.rdf')`

## Adaptación a la interfaz

Encontraremos diferentes apartados, entre ellos:

### Realizar consultas manualmente

En este apartado tenemos la primera caja de texto, en la cual podremos escribir nosotros mismos una consulta SPARQL y realizarla pulsando el botón que se encuentra debajo 'Realizar consulta'.

### Busqueda de proteina por secuencia de aminoácidos

Encontraremos un botón 'Búsqueda por secuencia' y debajo una caja de texto, en esta podremos introducir una secuencia o parte de una secuencia de aminoácidos y nos devolverá su correspondiente proteína. La secuencia debe introducirse en mayúsculas.

### Busqueda de proteina por comentario relacionados a esta

Parecido a lo anterior, tendremos un botón 'Búsqueda por comentario' y una caja de texto, en la cual podremos poner una palabra clave y nos devolverá el comentario correspondiente y también la proteína asociada a este.

### Cambiar cadenas de aminoacidos

Ahora encontraremos un botón 'Cambiar cadena' y dos cajas de texto, en una de ella pondremos la secuencia de aminoácidos que queremos introducir, y en la otra la que va a ser sustituida. Esta sustitución se guardará en el fichero .rdf.

### Botones de consultas

Ahora encontraremos 4 botones, 'Identificadores', 'Etiquetas', 'Publicaciones' y 'Comentarios'. 
Estos podrán realizar consultas de muestras sobre esos atributos en el fichero o sobre la consulta que nosotros hayamos realizado con anterioridad.

### Consultas en la web UniProt

Encontraremos una gran caja de texto, otra más pequeña y debajo un botón 'Consulta UNIPROT'. En la caja de texto que se encuentra encima del botón podremos poner el nombre del identificar de la proteína que deseamos buscar y se nos cargará la página correspondiente a esta en la caja de texto superior.

### Selección de fichero .RDF

Si deseamos cambiar de fichero desde la aplicación, tan solo tendremos que escribir el nombre de este en la caja de texto que se encuentra encima del botón 'Seleccionar RDF', el cual pulsaremos para cargar dicho fichero. El nombre de este se tendrá que poner sin extensión y estar en el mismo directorio en el que estemos ejecutando la aplicación.
