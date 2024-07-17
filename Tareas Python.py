#_______________________________________________________________-
#CLASE 16 de Julio, analizar el código y explicar que hace cada linea, luego reemplazarlo por otra condición
#WHILE
n = 10 # Declaro la variable "n" y le asigno 10 como dato.
while n<10: # Uso la sentencia WHILE para indicar que mientras la variable n sea menor que 10 entre al bloque de código.
    if (n%2)==0: # Uso la sentencia if(tomo el signo como divisible, nose si es porcentaje), con la condición que si la varibale n, sea divisible por 2 y el resultado sea igual a 0.
        print(n,"Es un numero par")# Aca escribo lo que quiero que imprima en pantalla, o lo que quiero que ejecute el programa en caso de que la condición del if se cumpla, en este caso 
                                   #imprime el valor de la variable n, seguido del string "Es un numero par".
    else: # Acá uso la sentencia else por si la condicion del IF arroja como resultado false, entonces ejucutará el bloque del else.
        print(n,"es un numero impar")# Acá escribo lo queiro que que se ejecue en pantalla o la porcion del código qu quiera que se ejecue en caso de que el resultado de la condicón del IF
                                     # ejecute si es falso/false. En este caso va imprimir por consola que es impar ya que la condicion del if sea !=(distinto) 0
    n+=1 # Aca le digo que le vaya sumando de a uno e incremento de la variable n.



#  IF ELSE ELIF
# Construir un algoritmo con lo viste en clase bajo el mismo diagrama de flujo de la imagen que está en la carpeta assets del repo