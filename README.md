# Programación Orientada a Objetos - UNAL

## Clase 13: Estructuras de datos en python y Queues

## Almacenando datos en objetos
En principio es posible crear instancias de la clase `object` y de esta manera ir guardando datos como atributos....pero esta instancia no tendría atributos predefinidos y no se pueden agregar atributos arbitrarios (por una cuestión de manejo de memoria).

```python 
o = object()
# Probar!
o.x = 5
```

```python 
# revisted
o = object()
try:
  o.x = 5
except AttributeError:
  print("No se pueden agregar atributos a objetos vacíos")
```

Y entonces qué hacer?...Pues la clásica definir una clase y ponerle atributos (mehhh).

```python 
class MiObjeto:
  pass

m = MiObjeto()
m.x = 5
print(m.x)
```
Aunque técnicamente se pueden crear objetos vacíos de la clase `object`o incluso crear clases para almacenar ciertos tipos de datos más complejos, se aconseja utilizar estructuras de datos más eficientes como construidas (*built-ins*) en Python.

## Tuplas y tuplas con con nombre
### Tuplas
Las tuplas son **colecciones ordenadas e inmutables de elementos**. Esto significa que una vez creada una tupla, no se pueden agregar, eliminar o modificar sus elementos. Las tuplas se derivan de la clase `tuple` y se definen usando paréntesis (), los elementos se separan por comas.

Las tuplas son útiles para almacenar **datos que no necesitan ser modificados** y que representan un conjunto relacionado de valores. Son eficientes para almacenar datos heterogéneos (de diferentes tipos, enteros, reales, otras tuplas, etc) y su inmutabilidad las hace adecuadas para utilizarlas como claves en diccionarios (se puede usar como llave que sirve de índice de búsqueda).

```python 
# Tupla con valores de diferentes tipos
datos_personales = ("Juan Pérez", 30, "ingeniero")  # Nombre, edad, profesión

# Tupla que representa coordenadas geográficas
ubicacion = (4.609174, -74.066031)  # Latitud, longitud

# Tupla vacía
vacia = ()
```

#### Casos de uso 
+ Almacenar una colección de elementos relacionados que no deben cambiar
+ Usar un conjunto de valores como clave en un diccionario 
+ Retornar múltiples valores desde una función
+ Pasar grupos de datos como argumentos a funciones sin riesgo de que sean alterados dentro de la función.

#### Contrapartes
+ La inmutabilidad puede ser una limitación si se necesita modificar los datos almacenados.
+ La falta de nombres para los elementos individuales puede dificultar la lectura del código, especialmente para tuplas con muchos elementos.

### Named tuples
Las tuplas con nombre son una variante de las tuplas que permiten asignar nombres a cada elemento. Esto mejora la legibilidad del código y facilita el acceso a los elementos por su nombre.

Para crear una tupla con nombre, se utiliza `namedtuple` del módulo `collections`.
```python 
from collections import namedtuple

# Tupla con nombre para representar un libro
Libro = namedtuple("Libro", ["titulo", "autor", "anio"])

# Creación de un objeto Libro
libro = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)

# Acceso a los elementos por nombre
print(f"Título: {libro.titulo}")
print(f"Autor: {libro.autor}")
print(f"Año: {libro.anio}")
```
**Expliación:** El proceso no dista mucho de instanciar una clase. El primer argumento es el nombre de la tupla, y luego una lista con los argumentos, cabe realtar que también se podría instanciar así: `namedtuple("Libro", "titulo autor anio")`

#### Ventajas 
+ Mejoran la legibilidad del código al nombrar los elementos de la tupla.
+ Facilitan el acceso a los elementos por su nombre en lugar de por índice.

#### Contrapartes
+ Siguen siendo inmutables, por lo que no se pueden modificar los elementos una vez creada la tupla con nombre.

Y si necesita cambiar los datos almacenados...Pues para eso tenemos los diccionarios.

## Diccionarios, default diccionaries, json
### Diccionarios
Los diccionarios son **colecciones desordenadas que almacenan pares clave-valor**. Las claves actúan como identificadores únicos (*hashes*) para acceder a los valores asociados. Los diccionarios se utilizan para almacenar información relacionada y son eficientes para realizar búsquedas. Los diccionarios se derivan de la clase `dict`, se pueden declarar usando corchetes {key: value}. 

Los diccionarios son una estructura de datos flexible que permite asociar un valor a una clave única. A diferencia de las listas ordenadas por índice, los diccionarios se basan en claves para recuperar elementos. Las claves deben ser inmutables y únicas (como cadenas o tuplas) para garantizar búsquedas eficientes.

```python 
# Diccionario de precios de acciones con símbolo como clave y tupla de valores
precios_acciones = {
  "GOOG": (613.30, 625.86, 610.50),  # Precio actual, máximo, mínimo
  "MSFT": (30.25, 30.70, 30.19)
}

# Diccionario con información de contacto
contactos = {
  "Juan Pérez": {"telefono": "555-1234", "correo": "juan.perez@ejemplo.com"},
  "Ana Lopez": {"telefono": "555-5678", "correo": "ana.lopez@ejemplo.com"}
}
```

#### Casos de uso 
+ Almacenar y acceder a datos utilizando claves únicas
+ Implementar estructuras de datos como objetos, caches, tablas hash
+ Contar la frecuencia de ocurrencia de elementos
+ Representar objetos complejos con atributos y valores asociados
+ Almacenar configuraciones o preferencias del usuario

#### Métodos útiles
+ `get(clave, valor_por_defecto)`: Obtiene el valor asociado a una clave. Si la clave no existe, devuelve el valor_por_defecto (opcional).
+ `setdefault(clave, valor_por_defecto)`: Similar a get, pero si la clave no existe, la agrega al diccionario con el valor_por_defecto.
+ `keys()`: Devuelve un iterador sobre las claves del diccionario.
+ `values()`: Devuelve un iterador sobre los valores del diccionario.
+ `items()`: Devuelve un iterador sobre pares (clave, valor) del diccionario.

#### Contrapartes
+ Las claves deben ser inmutables para un hash eficiente.
+ El orden de los elementos no está definido (a diferencia de las listas).


### defaultdict
`defaultdict` es una subclase del diccionario estándar en Python. Se utiliza para evitar el tedioso manejo de claves inexistentes en un diccionario.

Un problema habitual con los diccionarios convencionales es que al acceder a una clave inexistente se genera un error `KeyError`. `defaultdict` soluciona esto al permitir establecer un valor predeterminado que se devuelve cuando se intenta acceder a una clave ausente.

```python 
from collections import defaultdict

def letter_frequency_normal(sentence):
  frequencies = {}  # Diccionario normal
  for letter in sentence:
    frequency = frequencies.setdefault(letter, 0)  # Verifica si la clave existe
    frequencies[letter] = frequency + 1
  return frequencies


def letter_frequency_default(sentence):
  frequencies = defaultdict(int)  # defaultdict con valor por defecto int(0)
  for letter in sentence:
    frequencies[letter] += 1
  return frequencies # defaultdict se puede indexar igual que un diccionario normal

if __name__ == '__main__':
  print(letter_frequency_normal("hola mundo"))
  print(letter_frequency_default("hola mundo")) 
```
#### Casos de uso
+ Conteo de elementos: defaultdict es ideal para contar la frecuencia de elementos en una colección (ej. palabras en un texto).
+ Creación de diccionarios con valores por defecto: Permite crear diccionarios donde las claves ausentes tengan un valor inicial definido (ej. listas vacías).
+ Evitar errores KeyError: defaultdict previene el error KeyError al acceder a claves inexistentes.

### Counters
Counter es una subclase especializada del diccionario en Python diseñada específicamente para contar elementos repetitivos en un iterable.

Si bien `defaultdict(int)` es útil para asignar valores por defecto a claves inexistentes en un diccionario, resulta tedioso para contar elementos. Counter simplifica esta tarea al funcionar como un **diccionario optimizado para conteo**. Las claves representan los elementos a contabilizar, y los valores son la cantidad de veces que aparecen en el iterable.

```python 
from collections import Counter

def letter_frequency(sentence):
  # Con defaultdict
  # frequencies = defaultdict(int)
  # for letter in sentence:
  #   frequencies[letter] += 1
  # return frequencies

  # Con Counter (una línea)
  return Counter(sentence)

if __name__ == '__main__':
  print(letter_frequency("hola mundo"))
```
#### Casos de uso
+ Análisis de texto: Conteo de frecuencia de palabras en documentos o corpus.
+ Encuestas y votaciones: Contabilizar las opciones elegidas por los participantes.
+ Análisis de datos: Contar elementos únicos y repetitivos en colecciones.

## Listas y sorting lists
### Listas
Las listas son una estructura de datos fundamental en Python. Se utilizan para almacenar una **colección ordenada de elementos**. Las listas se derivan de la clase `list`, se pueden crear usando *brackets* [] y separando elementos por comas. Se recorren usando bucles *for*. La principal característica de las listas es su mutabilidad, esto es, se pueden modificar la cantidad de elementos y los elementos perse contenidos en ella.

#### Caracteristicas
+ Almacenar elementos del mismo tipo: listas de números, cadenas o incluso objetos personalizados - símil con *arrays*.
+ Mantener el orden de los elementos: la secuencia original de inserción o un orden personalizado mediante clasificación.
+ Modificar el contenido: insertar, eliminar o actualizar elementos en cualquier posición de la lista.

#### Métodos útiles:
+ append(elemento): Agrega un elemento al final de la lista.
+ insert(indice, elemento): Inserta un elemento en una posición específica de la lista. El primer argumento indica la posición (índice) donde se insertará el elemento.
+ count(elemento): Cuenta el número de veces que aparece un elemento dentro de la lista.
+ index(elemento): Devuelve el índice de la primera aparición de un elemento en la lista. Genera un error (exception) si el elemento no se encuentra.
+ find(elemento): Similar a index, busca el elemento y devuelve su índice. Si no lo encuentra, retorna -1 en lugar de un error.
+ reverse(): Invierte el orden de los elementos de la lista. El primer elemento pasa al final, el segundo al penúltimo, y así sucesivamente.
+ sort(): Ordena los elementos de la lista. Por defecto, ordena de menor a mayor para números y alfabéticamente para cadenas. Se puede personalizar el criterio de ordenación utilizando funciones.

```python 
# Crear una lista
numeros = [1, 2, 3, 4, 5]

# Acceder a elementos
print(numeros[2])  # 3

# Modificar elementos
numeros[2] = 10
print(numeros)  # [1, 2, 10, 4, 5]

# Iterar sobre una lista
for numero in numeros:
  print(numero)

# Operaciones con listas
numeros.append(6)  # Agregar un elemento al final
numeros.insert(2, 7)  # Insertar un elemento en una posición específica
numeros.remove(2)  # Eliminar un elemento por su valor
print(numeros)  # [1, 10, 7, 4, 5, 6]
```

#### Casos de uso:
+ Almacenar y manipular colecciones de elementos ordenados.
+ Implementar otras estructuras de datos como pilas, colas, etc -> se verá más adelante.
+ Realizar operaciones de cálculo sobre secuencias numéricas.

#### Copia superficial y copia profunda
En Python, existen dos métodos principales para copiar objetos: copy y deepcopy. Si bien ambos sirven para crear una nueva referencia a un objeto existente.

#### Copia superficial - copy
La copia superficial crea una nueva referencia al objeto original, pero no a sus subobjetos. Esto significa que si el objeto original contiene listas, diccionarios u otros objetos, la copia superficial solo replicará la referencia a esos subobjetos, no su contenido. Cualquier modificación realizada en los subobjetos de la copia también afectará al objeto original.

```python 
original_lista = [1, 2, 3, [4, 5]]
copia_superficial = original_lista.copy()

print(original_lista)  # Salida: [1, 2, 3, [4, 5]]
print(copia_superficial)  # Salida: [1, 2, 3, [4, 5]]

copia_superficial[3][0] = 10  # Modificar la lista anidada en la copia
print(original_lista)  # Salida: [1, 2, 3, [10, 5]]  # El original también se modifica
print(copia_superficial)  # Salida: [1, 2, 3, [10, 5]]
```

#### Copia profunda - deepcopy
La copia profunda crea una nueva referencia al objeto original y a **todos sus subobjetos de forma recursiva**. Esto significa que se generan nuevas copias de las estructuras de datos anidadas, aislando la copia de cualquier modificación en el objeto original.

```python 
import copy

original_lista = [1, 2, 3, [4, 5]]
copia_profunda = copy.deepcopy(original_lista)

print(original_lista)  # Salida: [1, 2, 3, [4, 5]]
print(copia_profunda)  # Salida: [1, 2, 3, [4, 5]]

copia_profunda[3][0] = 10  # Modificar la lista anidada en la copia profunda
print(original_lista)  # Salida: [1, 2, 3, [4, 5]]  # El original no se modifica
print(copia_profunda)  # Salida: [1, 2, 3, [10, 5]]
```
### Ordenando listas
La ordenación (suena mejor *sorting*) de listas es una operación fundamental para organizar elementos en un orden específico. La función `sort()` de Python permite ordenar listas de manera ascendente por defecto.

**Casos**: 
+ Orden por defecto:
  - Cadenas: orden alfabético (mayúsculas antes que minúsculas).
  - Números: orden numérico creciente.
  - Tuplas: orden por el primer elemento de cada tupla.
+ Parametro opcional key:
  - Permite definir una función personalizada para transformar los elementos de la lista antes de ordenarlos.
  - La función recibe un elemento de la lista y devuelve un valor comparable.
+ Objetos personalizados:
  - Para ordenar objetos definidos por el usuario, se debe implementar el método especial `__lt__` (menor que) en la clase.
  - Este método compara dos objetos y devuelve True si el objeto actual es menor que el parámetro recibido, False en caso contrario.

**Ejemplos:**
```python 
lista = [5, 2, 8, 1]
lista.sort()
print(lista)  # Salida: [1, 2, 5, 8]
```

```python 
lista = ["Hola", "mundo", "adios"]
lista.sort(key=str.lower)
print(lista)  # Salida: ["adios", "Hola", "mundo"]
```

```python 
from operator import itemgetter

lista = [('h', 4), ('n', 6), ('o', 5)]
lista.sort(key=itemgetter(1))
print(lista)  # Salida: [('h', 4), ('o', 5), ('n', 6)]
```

**Caso especial `__lt__`:**
El método __lt__ se implementa en clases personalizadas cuando se desea que sus instancias sean comparables entre sí y puedan ser ordenadas en listas. Esto es particularmente útil cuando se trabaja con objetos que representan datos con un orden natural, como números, fechas o palabras.

El método `__lt__` debe definirse dentro de la clase personalizada. Este método recibe un único argumento que representa la otra instancia con la que se está comparando la instancia actual. La implementación del método debe devolver `True` si la instancia actual se considera "menor que" la instancia pasada como argumento, y `False` en caso contrario.

```python 
class Estudiante:
  def __init__(self, nombre, edad, promedio):
    self.nombre = nombre
    self.edad = edad
    self.promedio = promedio

  def __lt__(self, otro_estudiante):
    if self.promedio < otro_estudiante.promedio:
      return True
    elif self.promedio == otro_estudiante.promedio:
      if self.edad < otro_estudiante.edad:
          return True
      else:
          return False
    else:
      return False

estudiantes = [
    Estudiante("Ana", 18, 9.5),
    Estudiante("Benito", 19, 8.7),
    Estudiante("Carmen", 17, 9.8),
]

estudiantes.sort()
print(estudiantes)
```
## Sets
Los conjuntos (*sets*) son **colecciones no ordenadas de elementos únicos**. A diferencia de las listas, los conjuntos no pueden contener elementos duplicados. Para declarar un conjunto se utilizan corchetes {} y los elementos se separan por comas, se puede drivar de la clase `set`.

```python 
artistas = {"Sarah Brightman", "Guns N' Roses", "Opeth"}
```

#### Características:
+ Unicidad: Los conjuntos garantizan que cada elemento exista solo una vez.
+ Objetos hashable: Los elementos de un conjunto deben ser hashable (objetos que se pueden utilizar como claves en diccionarios). Números, cadenas y tuplas son ejemplos de objetos hashable.

#### Métodos útiles
+ `add(elemento)`: Añade un elemento al conjunto.
+ `union(otro_conjunto)`: Devuelve un nuevo conjunto con la unión de elementos (presentes en uno u otro conjunto o en ambos). Equivalente al operador |.
+ `intersection(otro_conjunto)`: Devuelve un nuevo conjunto con la intersección de elementos (presentes en ambos conjuntos). Equivalente al operador &.
+ `difference(otro_conjunto)`: Devuelve un nuevo conjunto con la diferencia de elementos (presentes en el primer conjunto pero no en el segundo). Equivalente al operador -.
+ `symmetric_difference(otro_conjunto)`: Devuelve un nuevo conjunto con la diferencia simétrica de elementos (presentes en uno u otro conjunto pero no en ambos).
+ `issubset(otro_conjunto)`: Devuelve True si todos los elementos del primer conjunto están en el segundo.
+ `issuperset(otro_conjunto)`: Devuelve True si todos los elementos del segundo conjunto están en el primer conjunto.
+ `in`: Permite verificar si un elemento pertenece al conjunto.

```python 
# Crear un conjunto
numeros = {1, 2, 3, 4, 5, 5}  # El duplicado 5 se elimina automáticamente
print(numeros)  # {1, 2, 3, 4, 5}

# Agregar y eliminar elementos
numeros.add(6)
numeros.remove(2)
print(numeros)  # {1, 3, 4, 5, 6}

# Operaciones de conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union = conjunto1.union(conjunto2)  # {1, 2, 3, 4, 5}
interseccion = conjunto1.intersection(conjunto2)  # {3}
diferencia = conjunto1.difference(conjunto2)  # {1, 2}

# Probar pertenencia
print(2 in numeros)  # False
print(4 in numeros)  # True
```

#### Casos de uso
+ Eliminar duplicados de una colección
+ Realizar operaciones matemáticas de conjuntos
+ Probar la pertenencia de elementos de manera eficiente

## Extendiendo el poder de las estructuras propias de python
Python permite extender las estructuras de datos incorporadas mediante herencia. Esto puede ser útil cuando se necesita agregar funcionalidad adicional a una estructura de datos existente.

**Ejemplo:** Crear una clase *OrderedDict* que extienda el diccionario incorporado de Python y mantenga el orden de inserción de las claves.

*Contexto:* En Python 3.6 y versiones anteriores, la clase incorporada dict no garantizaba el orden de inserción. Los diccionarios eran considerados colecciones desordenadas de objetos. Esto significa que si insertabas pares clave-valor en un diccionario en un cierto orden, no podías confiar en que iterar sobre el diccionario te daría los pares clave-valor en ese mismo orden. A partir de Python 3.7, se hizo un cambio para que los diccionarios mantuvieran el orden de inserción, lo que significa que el orden en que insertas los elementos en el diccionario es el orden en que los obtienes cuando iteras sobre el diccionario. Este cambio se hizo oficial en la especificación del lenguaje Python en la versión 3.7.


```python 
from collections import KeysView, ItemsView, ValuesView

class DictSorted(dict):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.ordered_keys = []

  def __setitem__(self, key, value):
    '''self[key] = value syntax'''
    if key not in self.ordered_keys:
      self.ordered_keys.append(key)
    super().__setitem__(key, value)

  def setdefault(self, key, value):
    if key not in self.ordered_keys:
      self.ordered_keys.append(key)
    return super().setdefault(key, value)

  def keys(self):
    return KeysView(self)

  def values(self):
    return ValuesView(self)

  def items(self):
    return ItemsView(self)

  def __iter__(self):
    '''for x in self syntax'''
    return iter(self.ordered_keys)
```

**Explicación:** LLa clase *DictSorted* es una subclase de la clase incorporada *dict* de Python. Esta clase se utiliza para crear un diccionario que mantiene el orden de inserción de las claves. Aquí está la explicación de sus métodos:

 + `__init__`: Este método inicializa una nueva instancia de DictSorted. Crea una lista vacía ordered_keys para almacenar las claves en el orden en que se insertan.

 + `__setitem__`: Este método se llama cuando se establece un valor con una clave. Si la clave no está ya en ordered_keys, la añade. Luego llama al método `__setitem__ de la clase base para establecer realmente el par clave-valor en el diccionario.

 + `setdefault`: Este método funciona de manera similar al método setdefault del diccionario incorporado. Si la clave no está ya en ordered_keys, la añade. Luego llama al método setdefault de la clase base.

 + `keys`, `values`, `items`: Estos métodos devuelven objetos de vista que muestran las claves, los valores y los pares clave-valor del diccionario, respectivamente.

+ `__iter__`: Este método se llama cuando se itera sobre el diccionario. Devuelve un iterador sobre ordered_keys, por lo que las claves se iteran en el orden en que se insertaron.

```python 
# Crear una instancia de DictSorted
d = DictSorted()

# Añadir algunos pares clave-valor
d['b'] = 2
d['a'] = 1
d['c'] = 3

# Imprimir las claves en el orden en que se insertaron
print(list(d.keys()))  # ['b', 'a', 'c']

# Imprimir los pares clave-valor en el orden en que se insertaron
print(list(d.items()))  # [('b', 2), ('a', 1), ('c', 3)]

# Iterar sobre las claves en el orden en que se insertaron
for key in d:
    print(key, d[key])  # imprime 'b 2', 'a 1', 'c 3'
```   

Este ejemplo demuestra cómo extender las estructuras de datos incorporadas de Python para agregar funcionalidad adicional. Sin embargo, es importante tener en cuenta que extender clases incorporadas puede tener implicaciones de rendimiento y complejidad, por lo que se debe considerar cuidadosamente antes de hacerlo.

## Queues
Las colas (*queues*) son estructuras de datos particulares porque, al igual que los conjuntos, su funcionalidad se puede manejar completamente usando listas. Si bien las listas son herramientas multipropósito extremadamente versátiles, ocasionalmente no son la estructura de datos más eficiente. Si la aplicación utiliza un conjunto de datos pequeño (hasta cientos o incluso miles de elementos), las listas probablemente cubrirán todos sus casos de uso. Sin embargo, si  se necesita escalar los datos a millones, es posible que se necesite un contenedor más eficiente. Por lo tanto, Python proporciona tres tipos de estructuras de datos de cola, según el tipo de acceso. Las tres utilizan la misma API, pero difieren tanto en el comportamiento como en la estructura de datos.

Antes de comenzar con las colas, consideremos la confiable estructura de datos de lista. Las listas de Python son la estructura de datos más ventajosa para muchos casos de uso:

+ Admiten un acceso aleatorio eficiente a cualquier elemento
+ Tienen un orden estricto de elementos
+ Admiten la operación de agregar de manera eficiente

Sin embargo, tienden a ser lentas si inserta elementos en cualquier lugar que no sea el final de la lista (especialmente si es al principio). Como se analizó en la sección sobre conjuntos, también son lentas para verificar si un elemento existe en la lista y, por extensión, para buscar, almacenar datos en un orden ordenado o reordenar los datos también pueden ser operaciones ineficientes.

### FIFO Queues
Las colas tipo **FIFO** (*First In, First Out*) son estructuras de datos que siguen el principio de que el primer elemento en ser insertado en la cola es el primero en ser eliminado. En otras palabras, los elementos se eliminan en el mismo orden en que se insertaron, similar al comportamiento de una fila en la vida cotidiana.

#### Características:
+ Los elementos se agregan al final de la cola (encolado - *put*).
+ Los elementos se eliminan desde el principio de la cola (desencolado - *get*).
+ La operación de encolado se realiza en el extremo opuesto al de desencolado.
Sigue el principio de *primero en entrar, primero en salir* (FIFO).

#### Ventajas:
+ **Orden:** Las colas FIFO mantienen el orden de inserción de los elementos. El elemento que se agrega primero será el primero en ser recuperado, y así sucesivamente.
+ **Acceso:** Las colas FIFO solo permiten el acceso a los elementos desde dos extremos: el frente (primero en entrar) y la parte posterior (último en entrar).
+ **Eficiencia:** Las colas FIFO son eficientes para agregar y eliminar elementos en los extremos. Agregar un elemento a la parte posterior o eliminar un elemento del frente se puede realizar en tiempo constante (O(1)).

#### Desventajas:
+ No se puede acceder directamente a los elementos en el medio de la cola.
+ Si se necesita priorizar elementos, se requiere una estructura de datos diferente.

#### Casos de uso
+ Administración de solicitudes de impresión en una impresora compartida.
+ Procesamiento de trabajos en un sistema operativo.
+ Manejo de solicitudes de red (HTTP, FTP, etc.).
+ Simulación de líneas de espera (por ejemplo, en un banco o en un supermercado).

**Ejemplo:** Usando *queue* de Python
```python 
from queue import Queue
# Crear una cola FIFO con capacidad máxima de 5 elementos
cola_fifo = Queue(maxsize=5)

# Agregar elementos a la cola
cola_fifo.put("Elemento 1")
cola_fifo.put("Elemento 2")
cola_fifo.put("Elemento 3")
cola_fifo.put("Elemento 4")
cola_fifo.put("Elemento 5")

# Verificar si la cola está llena
if cola_fifo.full():
    print("La cola está llena")
else:
    print("La cola no está llena")

# Recuperar y eliminar elementos de la cola
while not cola_fifo.empty():
    elemento = cola_fifo.get()
    print("Recuperando elemento:", elemento)
```  

**Ejemplo:** Implementación con listas.
```python 
class ColaFIFO:
  def __init__(self):
    self.items = []

  def encolar(self, elemento):
    self.items.append(elemento)

  def desencolar(self):
    if not self.esta_vacia():
      return self.items.pop(0)
    else:
      return None

  def esta_vacia(self):
    return len(self.items) == 0

cola = ColaFIFO()
cola.encolar("Elemento 1")
cola.encolar("Elemento 2")
cola.encolar("Elemento 3")
cola.encolar("Elemento 4")
cola.encolar("Elemento 5")

print("Elementos en la cola:")
while not cola.esta_vacia():
  print("Recuperando elemento:", cola.desencolar())
```  

### LIFO Queues
Las colas tipo LIFO (*Last In, First Out*) son una estructura de datos lineal en la que los elementos se agregan y eliminan desde el mismo extremo. El último elemento que se inserta en la cola será el primero en ser removido. Esta estructura sigue un orden inverso al de las colas FIFO, y es similar a una pila de platos, donde el último plato colocado será el primero en ser retirado.

#### Características:
+ Los elementos se agregan y eliminan desde el mismo extremo de la cola.
+ El último elemento insertado será el primero en ser removido.
+ Sigue el principio de *"último en entrar, primero en salir"* (LIFO).

#### Ventajas:
+ **Orden:** Las colas LIFO mantienen el orden de inserción de los elementos invertido. El elemento que se agrega más recientemente será el primero en ser recuperado, y así sucesivamente.
+ **Acceso:** Las colas LIFO solo permiten el acceso a los elementos desde un extremo: la cima (último en entrar).
+ **Eficiencia:** Las colas LIFO son eficientes para agregar y eliminar elementos en la cima. Agregar un elemento a la cima o eliminar el elemento de la cima se puede realizar en tiempo constante (O(1)).

#### Desventajas:
+ No permiten el acceso aleatorio a elementos en cualquier posición de la pila. Solo se puede acceder al elemento de la cima.


#### Casos de uso
+ Gestión de funciones de llamada (call stack) en programación.
+ Implementación de operaciones de "deshacer" y "rehacer" en editores de texto y aplicaciones gráficas.
+ Navegación web (pila de páginas visitadas en un navegador).

**Ejemplo:** Usando *queue* de Python
```python 
from queue import LifoQueue

# Crear una pila (cola LIFO) con capacidad máxima de 5 elementos
pila = LifoQueue(maxsize=5)

# Agregar elementos a la pila (apilar)
pila.put("Elemento 1")
pila.put("Elemento 2")
pila.put("Elemento 3")
pila.put("Elemento 4")
pila.put("Elemento 5")

# Verificar si la pila está llena
if pila.full():
    print("La pila está llena")
else:
    print("La pila no está llena")

# Recuperar y eliminar elementos de la pila (desapilar)
while not pila.empty():
    elemento = pila.get()
    print("Recuperando elemento:", elemento)
``` 

**Ejemplo:** Implementación con listas.
```python 
class ColaLIFO:
  def __init__(self):
    self.items = []

  def apilar(self, elemento):
    self.items.append(elemento)

  def desapilar(self):
    if not self.esta_vacia():
      return self.items.pop()
    else:
      return None

  def esta_vacia(self):
    return len(self.items) == 0

cola = ColaLIFO()
cola.apilar("Elemento 1")
cola.apilar("Elemento 2")
cola.apilar("Elemento 3")
cola.apilar("Elemento 4")
cola.apilar("Elemento 5")

print("Elementos en la cola:")
while not cola.esta_vacia():
  print("Recuperando elemento:", cola.desapilar())
```  

### Priority Queues
Las colas priorizadas, también conocidas como colas de prioridad, son una estructura de datos que almacena elementos con una prioridad asociada. Los elementos son desencolados de acuerdo a su prioridad, es decir, el elemento con la prioridad más alta se desencolará primero, independientemente del orden de inserción.

#### Características:
+ Cada elemento en la cola tiene una prioridad asociada.
+ Los elementos son desencolados en orden de prioridad, desde la prioridad más alta a la más baja.
+ Si dos o más elementos tienen la misma prioridad, se siguen reglas adicionales (como orden de inserción) para desencolarse.
+ Suelen implementarse utilizando montículos (*heaps*), una estructura de datos especializada. Python proporciona el módulo heapq para trabajar con montículos.
+ La cola permite elementos con la misma prioridad. Sin embargo, el orden en que se devuelven no está garantizado.

#### Ventajas:
* **Flexibilidad:** Permiten gestionar elementos de manera eficiente en función de su importancia, adaptándose a diversos casos de uso.
* **Eficiencia:** Las operaciones de inserción y extracción de elementos se pueden realizar en tiempo logarítmico (O(log n)), lo que las hace adecuadas para manejar grandes conjuntos de datos.
* **Priorización Dinámica:** Se pueden agregar nuevos elementos o modificar la prioridad de elementos existentes en cualquier momento.

#### Desventajas:
+ **Complejidad:** La implementación interna de las colas priorizadas, utilizando montículos, puede ser más compleja que las colas FIFO o LIFO.
+ **Consumo de Memoria:** Los montículos pueden requerir más memoria que estructuras de datos simples, como las listas.

#### Casos de uso:
+ Programación de tareas en sistemas operativos.
+ Manejo de interrupciones y eventos en sistemas en tiempo real.
+ Algoritmos de enrutamiento y planificación de redes.
+ Procesamiento de solicitudes con diferentes niveles de importancia (por ejemplo, en un sistema de atención al cliente).

**Ejemplo:** Usando *heaps* de Python
```python 
import heapq

class ColaPriorizada:
  def __init__(self):
    self.heap = []

  def encolar(self, elemento, prioridad):
    heapq.heappush(self.heap, (prioridad, elemento))

  def desencolar(self):
    if not self.esta_vacia():
      return heapq.heappop(self.heap)[1]
    else:
      return None

  def esta_vacia(self):
    return len(self.heap) == 0

# Ejemplo de uso
cola_priorizada = ColaPriorizada()
cola_priorizada.encolar("Tarea 1", 3)
cola_priorizada.encolar("Tarea 2", 1)
cola_priorizada.encolar("Tarea 3", 2)

print("Elementos en la cola priorizada:")
while not cola_priorizada.esta_vacia():
    print(cola_priorizada.desencolar())
``` 

## Reto 7: 
1. The `restaurant class` *revisted* like for the third time. 
  + Add the proper data structure to manage multiple orders (maybe a FIFO queue)
  + Define a **named tuple** somewhere in the menu, e.g. to define a set of items.
  + Create an interface in the order class, to create a new menu, aggregate the functions for add, update, delete items. All the menus should be stored as JSON files. (use dicts for this task.)
