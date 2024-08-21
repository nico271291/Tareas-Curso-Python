# Trabajo Práctico Final - Curso Introductorio de Python

## Ejercicio 1: Números y Cadenas de Caracteres
'''1. Escribe un programa que pida al usuario dos números enteros y realice lo siguiente:
   - Muestra la suma de los dos números.
   - Muestra el producto de los dos números.
   - Muestra la concatenación de los dos números (como texto). '''
   
   
 
num1 = int(input('Introduce el primer número entero: ')) # Pido al Usuario dos números enteros.
num2 = int(input('Introduce el segundo número entero: '))

suma = num1 + num2 # Realizo la suma.
print('La suma de', num1, '+', num2, 'es:', suma) # Muestro el resultado de la suma.

producto = num1 * num2 # Realizo el producto.
print('El producto de', num1, '*', num2, 'es:', producto) # Muestro el resultado del producto.

concatenacion = str(num1) + str(num2) # Realizo la concatenación.
print('La concatenación de', num1, 'y', num2, 'es:', concatenacion) # Muestro el resultado de la concatenación. 
   

''' 2. Pide al usuario una cadena de texto. Luego muestra:
   - La cadena en mayúsculas.
   - La longitud de la cadena.
   - La cadena invertida.
   - La cantidad de veces que aparece una letra específica (elige una letra y pídesela al usuario). '''

cadena = input('Introduce una cadena de texto: ') # Pido al usuario una cadena de texto.

cadena_mayusculas = cadena.upper() # Convierto la cadena a mayúsculas.
print('La cadena en mayúsculas es:', cadena_mayusculas) # Muestro la cadena a mayúsculas. 


longitud_cadena = len(cadena) # Calculo la longitud de la cadena.
print('La longitud de la cadena es:', longitud_cadena) #Muestro la longitud de la cadena.


cadena_invertida = cadena[::-1] # Invierto la cadena.
print('La cadena invertida es:', cadena_invertida)


letra = input('Introduce una letra para contar cuántas veces aparece en la cadena: ') # Pido al usuario que elija una letra para contar su aparición.



cantidad_letra = cadena.count(letra) # Contar las apariciones de la letra en la cadena
print('La letra', letra, 'aparece', cantidad_letra, 'veces en la cadena.') # Muestro la cantidad de veces que aparece la letra elejida 

'''  3. Escribe un programa que convierta un número decimal a binario y viceversa. '''

### Este Punto lo tuve que buscar porque no sabía como encararlo, lo quise hacer en papel antes y cuando lo quería codear no sabia me mareaba y no me salía.

# Conversión de decimal a binario
def decimal_a_binario(decimal):
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario  # Añade el residuo de la división por 2 al inicio de la cadena
        decimal //= 2  # Divide el número por 2 para la siguiente iteración
    return binario

# Conversión de binario a decimal
def binario_a_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i]) * (2 ** (len(binario) - 1 - i))  # Multiplica cada bit por su peso correspondiente
    return decimal

# Pruebas de conversión
numero_decimal = int(input('Introduce el número decimal para pasar a binario: ')) # Elijo un número decimal para pasar a Binario.
print('Decimal', numero_decimal, 'a binario es:', decimal_a_binario(numero_decimal)) # Muestro el número pasado a Binario

numero_binario = input('Introduce el número binario para pasar a decimal: ') # Elijo un número en Binario.
print('Binario', numero_binario, 'a decimal es:', binario_a_decimal(numero_binario)) # Muestro el número pasado a Decimal.


''' 4. Pide al usuario una cadena y un número entero. Muestra la cadena repetida el número de veces indicado por el número entero. '''

cadena = input('Introduce una cadena: ') # Pido al usuario una cadena.

numero = int(input('Introduce un número entero: ')) # Pido al usuario un número entero.


resultado = cadena * numero
print(resultado) # Muestro la cadena repetida el número de veces indicado. 

## Ejercicio 2: Listas y Tuplas
'''1. Crea una lista con los nombres de tres frutas. Luego:
   - Añade dos frutas más a la lista.
   - Ordena la lista alfabéticamente.
   - Muestra la lista completa.
   - Elimina una fruta de la lista y muestra el resultado. '''
  
frutas = ['frutilla', 'banana', 'melón'] # Crear una lista con los nombres de tres frutas


frutas.append('sandía') # Añado dos frutas más a la lista
frutas.append('naranja')

frutas.sort() # Ordeno la lista alfabéticamente.


print('Lista de frutas ordenada:', frutas) # Muestro la lista ordenada. 

frutas.remove('naranja') # Elimino una fruta de la lista.

print('Lista de frutas después de eliminar una fruta:', frutas) # Muestro el resultado después de eliminar una fruta.


''' 2. Crea una tupla con los nombres de dos ciudades. Luego:
   - Muestra el primer y último elemento de la tupla.
   - Convierte la tupla en una lista, añade una nueva ciudad y muestra la lista resultante. '''

ciudades = ('Buenos Aires', 'Río Negro') # Creo una tupla con los nombres de dos ciudades.

primer_ciudad = ciudades[0]
print('Primera ciudad:', primer_ciudad) # Muestro el primer elemento de la tupla.
ultima_ciudad = ciudades[-1] 
print('Última ciudad:', ultima_ciudad) # Muestro el último elemento de la tupla.

lista_ciudades = list(ciudades) # Convierto la tupla en una lista.

lista_ciudades.append('Rosario') # Añado una nueva ciudad a la lista.


print('Lista de ciudades después de añadir una nueva ciudad:')
print(lista_ciudades) # Mostrar el resutaldo de la lista.


''' 3. Crea una lista de números enteros y muestra:
   - El número mayor de la lista.
   - El número menor de la lista.
   - El promedio de los números en la lista. '''
   
numeros = [50, 12, 26, 23, 32] # Creo una lista de números enteros.

mayor_numero = max(numeros) # Muestro el número mayor de la lista.
print('El número mayor de la lista es:', mayor_numero)

menor_numero = min(numeros) # Muestro el número menor de la lista.
print('El número menor de la lista es:', menor_numero)

promedio = sum(numeros) / len(numeros) # Calculo el promedio de los números en la lista.

print('El promedio de los números en la lista es:', promedio) # Muestro el promedio sin limitar el número de decimales.


''' 4. Escribe un programa que reciba una lista de cadenas y muestre la lista con todas las cadenas en mayúsculas. '''

cadenas = ['boca', 'juniors', 'el', 'que', 'nunca', 'descendio'] # Definir una lista de cadenas.

cadenas_mayusculas = [cadenas.upper() for cadenas in cadenas] # Convertir cada cadena a mayúsculas.

print('Lista de cadenas en mayúsculas:', cadenas_mayusculas) # Mostrar la lista con todas las cadenas en mayúsculas.
 

## Ejercicio 3: Controladores de Flujo
''' 1. Escribe un programa que pida un número al usuario. Muestra si el número es par o impar. '''

numero = int(input('Introduce un número: ')) # Pido un número al usuario

if numero % 2 == 0: # Determinar si el número es par o impar
    print('El número es par.')
else:
    print('El número es impar.')
 

''' 2. Crea un programa que simule un menú simple con las siguientes opciones:
   1. Saludar
   2. Despedirse
   3. Salir
   - Dependiendo de la opción elegida, muestra un mensaje correspondiente. Si se elige 3, el programa debe terminar. '''
   
# Muestro y creo el menú simple.
print("Menú:")
print("1. Saludar")
print("2. Despedirse")
print("3. Salir")

opcion = int(input("Selecciona una opción (1, 2, o 3): ")) # Pido al usuario que elija una opción.

# Dependiendo de la opción elegida, mostrar un mensaje.
if opcion == 1:
    print("¡Hola! ¿Cómo estás?")
elif opcion == 2:
    print("¡Adiós! Que tengas un buen día.")
elif opcion == 3:
    print("Saliendo del programa. ¡Hasta luego!")
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")

   
'''  3. Escribe un programa que pida un número al usuario y determine si es positivo, negativo o cero.  '''

numero = int(input('Introduce un número: '))  # Pido un número al usuario.

# Determinar si el número es positivo, negativo o cero.
if numero > 0:
    print('El número es positivo.')
elif numero < 0:
    print('El número es negativo.')
else:
    print('El número es cero.') 

'''  4. Escribe un programa que muestre los números del 1 al 10 utilizando un bucle `for`.  '''

 # Mostrar los números del 1 al 10 utilizando un bucle for.
for numero in range(1, 11):
    print(numero)

# Otra posible manera de hacerlo es:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Crear una lista con los números del 1 al 10.

for numero in numeros:
    print(numero) # Muestro los números utilizando un bucle for.
 

'''  5. Escribe un programa que calcule la suma de los números del 1 al 100 utilizando un bucle `while`.   '''
 
# Inicializo las variables
suma = 0
numero = 1

# Uso el bucle while para sumar los números del 1 al 100
while numero <= 100:
    suma += numero
    numero += 1

print('La suma de los números del 1 al 100 es:', suma) # Muestro el resultado
 

 ## Ejercicio 4: Conjuntos y Diccionarios
'''  1. Crea dos conjuntos con algunos números. Luego:
   - Muestra la unión de los dos conjuntos.
   - Muestra la diferencia entre los dos conjuntos.
   - Muestra los elementos comunes en ambos conjuntos.  '''
   
conjunto1 = {10, 20, 30, 40, 50} # Creo un conjunto con algunos números.
conjunto2 = {40, 50, 60, 70, 80} # Creo otro conjuntos con algunos números.

union = conjunto1 | conjunto2  #Hago la unión de los dos conjuntos.
print('Unión de los dos conjuntos:', union) # Muestro la unión de los dos conjuntos.

diferencia = conjunto1 - conjunto2 #Hago la diferencia entre los dos conjuntos
print('Diferencia entre los dos conjuntos (conjunto1 - conjunto2):', diferencia) # Muestro la diferencia entre los dos conjuntos.

interseccion = conjunto1 & conjunto2 # Hago la interseccion entre los dos conjuntos.
print('Elementos comunes en ambos conjuntos:', interseccion) # Muestro los elementos comunes en ambos conjuntos.

   
'''  2. Crea un diccionario con tres nombres como claves y edades como valores. Luego:
   - Muestra la edad del primer nombre en el diccionario.
   - Añade un nuevo nombre y edad al diccionario.
   - Elimina un nombre del diccionario y muestra el resultado.
   - Muestra todas las claves y todos los valores del diccionario.  '''
   
   
edades = {'Ana': 25, 'Carlos': 30, 'Elena': 22} # Creo un diccionario con tres nombres como claves y edades como valores.

primer_nombre = list(edades)[0] # Obtener las claves del diccionario como una lista sin usar edades.keys()
print('La edad de', primer_nombre, 'es:', edades[primer_nombre]) # Muestro la edad del primer nombre en el diccionario.

edades.update({'Miguel': 27}) # Añado un nuevo nombre y edad al diccionario
print('Diccionario después de añadir a Miguel:', edades) # Muestro el diccionario despues de agregar el nombre y la edad.

edades.pop('Carlos') # Elimino un nombre del diccionario y mostrar el resultado.
print('Diccionario después de eliminar a Carlos:', edades) # Muestro el diccionario con el nombre eliminado.

# Mostrar todas las claves y todos los valores del diccionario
print('Claves del diccionario:', list(edades))
print('Valores del diccionario:', list(edades.values()))

   
'''  3. Crea un diccionario con los nombres de cinco productos como claves y sus precios como valores. Luego:
   - Muestra el precio de un producto específico.
   - Incrementa el precio de todos los productos en un 10%.
   - Muestra el diccionario actualizado.  '''
   
# Creo un diccionario con cinco productos y sus precios.
productos = {
    'Yerba': 1200,
    'Azúcar': 900,
    'Cafe': 700,
    'Té': 400,
    'Agua': 300
}

# Incremento el precio de todos los productos en un 10% con redondeo.
for producto in productos:
    productos[producto] = round(productos[producto] * 1.10, 2)  # Incrementa el precio en un 10% y redondea a 2 decimales.

print('Diccionario actualizado con precios incrementados en un 10%:', productos) # Muestro el diccionario actualizado.

   
'''  4. Crea un conjunto con los números del 1 al 5 y otro conjunto con los números del 4 al 8. Muestra:
   - La intersección de los dos conjuntos. 
   - La diferencia simétrica entre los dos conjuntos. '''
   
# Creo los dos conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

interseccion = conjunto1 & conjunto2 # Creo la intersección de los dos conjuntos.
print('Intersección de los dos conjuntos:', interseccion) # Muestro la intersección de los dos conjuntos.

diferencia_simetrica = conjunto1 ^ conjunto2 # Creo la diferencia simétrica de los dos conjuntos.
print('Diferencia simétrica entre los dos conjuntos:', diferencia_simetrica) # Muestro la diferencia simétrica entre los dos conjuntos.

 ## Ejercicio 5: Funciones
'''  1. Define una función `saludar(nombre)` que reciba un nombre y muestre un saludo. Luego llama a esta función con tu propio nombre. 
 '''
# Defino la función saludar.
def saludar(nombre):
    print('¡Hola, ' + nombre + '! ¿Cómo estás?')

saludar('Nico') # Llamo a la función con tu propio nombre.

'''  2. Define una función `suma(a, b)` que reciba dos números y retorne su suma. Luego prueba la función con dos números diferentes.  '''

# Defino la función suma.
def suma(a, b):
    return a + b

resultado = suma(5, 3)# Pruebo la función con dos números diferentes.
print('La suma de 5 y 3 es:', resultado) 

resultado = suma(10, 15) # Otra prueba con diferentes números.
print('La suma de 10 y 15 es:', resultado)


''' 3. Define una función `es_mayor_de_edad(edad)` que reciba una edad y retorne `True` si la edad es mayor o igual a 18 y `False` en caso contrario. Prueba la función con diferentes edades.  '''

# Defino la función es_mayor_de_edad
def es_mayor_de_edad(edad):
    return edad >= 18

# Pruebo la función con diferentes edades.
print(es_mayor_de_edad(20))  
print(es_mayor_de_edad(17))  
print(es_mayor_de_edad(18))  
print(es_mayor_de_edad(15))  
print(es_mayor_de_edad(30))  
print(es_mayor_de_edad(10))  
print(es_mayor_de_edad(13))  
print(es_mayor_de_edad(22))  
