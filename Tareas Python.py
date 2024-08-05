#_______________________________________________________________-
#CLASE 16 de Julio, analizar el código y explicar que hace cada linea, luego reemplazarlo por otra condición
#WHILE
"""
n = 10 # Declaro la variable "n" y le asigno 10 como dato.
while n<10: # Uso la sentencia WHILE para indicar que mientras la variable n sea menor que 10 entre al bloque de código.
    if (n%2)==0: # Uso la sentencia if, con la condición de que sí el módulo entre n dividido 2 es igual a cero, y si esta condicion es verdadera entre al bloque del código del if.
        print(n,"Es un numero par")# Aca escribo lo que quiero que imprima en pantalla, o lo que quiero que ejecute el programa en caso de que la condición del if se cumpla, en este caso 
                                   #imprime el valor de la variable n, seguido del string "Es un numero par".
    else: # Acá uso la sentencia else por si la condicion del IF arroja como resultado false, entonces ejucutará el bloque del else.
        print(n,"es un numero impar")# Acá escribo lo queiro que que se ejecue en pantalla o la porcion del código qu quiera que se ejecue en caso de que el resultado de la condicón del IF
                                     # ejecute si es falso/false. En este caso va imprimir por consola que es impar ya que la condicion del if sea !=(distinto) 0
    n+=1 # Aca le digo que le vaya sumando de a uno e incremento de la variable n.

numero_secreto = 6
intentos = 0

print("Bienvenido al juego Adivina el numero.")
print("El juego consiste en adivinar que numero del 1 al 10 estoy pensando.")
print("Tienes 3 intentos para adivinar el número.")

while intentos < 3:
    intento = int(input("Ingresa tu número: "))
    intentos += 1

    if intento == numero_secreto:
        print("¡Felicitaciones! ¡Adivinaste el número! :)")
        break
    elif intento < numero_secreto:
        print("Lo siento :(. El número que estás buscando es mayor.")
    else:
        print("Lo siento :(. El número que estás buscando es menor.")

if intentos == 3 and intento != numero_secreto:
    print("¡Lo siento! No lograste adivinar el número :(. El número correcto era:", numero_secreto)


#  IF ELSE ELIF
# Construir un algoritmo con lo viste en clase bajo el mismo diagrama de flujo de la imagen que está en la carpeta assets del repo
boca = "Boca"
racing = "Racing"
riber = "Riber"
river = "River"
independiente = "Independiente"
san_Lorenzo = "San lorenzo"
print("Bienvenido")
tu_equipo = input ("ingresa tu equipo con la primer letra en mayúscula:")
if tu_equipo == boca:
    print("Sos del club más ganador del mundo, el verdadero GRANDE.")
elif tu_equipo == riber:
    print("Te crées grande por una final ganda, pero sos un descendido 26/06/2011")
elif tu_equipo == river:
    print("Lo siento, no reconozco tu club. Quizás quiciste decir:", riber)
elif tu_equipo == independiente:
    print("Se creen grandes, pero descendieron tambien, al igual que Riber.")
elif tu_equipo == san_Lorenzo:
    print("Vos no sos grande, solo tenes una Libertadores. El que me programo dice que solo los propios hinchas se creen grandes.")
elif tu_equipo == racing:
    print("Sos considerado grande, pero un club que por 30 años no ganó nada, Im Sorry, pero no es grnade, ademas descendiste vos también.")
else:
    print("Es un buen club, por lo menos tienen mas huevos que Riber, San Lorenzo e Independiente, solo que les falta plata.")


Hola Profe soy Nicolás Blanco, perdon que suba esta tarea, pero las otras consignas las tengo en mi pc y no puedo subir a git as cosas, 
lo voy a desisntalar y volver a instalar para ver si las puedo subir, sino se las paso por mail como me dijo en la clase de ayer.
"""
























