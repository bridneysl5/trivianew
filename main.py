import time
import random

#Colores y formatos
#Para aplicarlos poner un + junto con la variable

#Texto

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Fondo
F_BLACK = '\033[40m'
F_RED = '\033[41m'
F_GREEN = '\033[42m'
F_YELLOW = '\033[43m'
F_BLUE = '\033[44m'
F_MAGENTA = '\033[45m'
F_CYAN = '\033[46m'
F_WHITE = '\033[47m'
F_RESET = '\033[49m'

#Formatos
NEGRITA = '\033[1m'
DEBIL = '\033[2m'
CURSIVA = '\033[3m'
SUBRAYADO = '\033[4m'
OCULTO = '\033[6m'
TACHADO = '\033[7m'
FRESET = '\033[0m'

RC = NEGRITA + GREEN + "\nRespuesta correcta:" + RESET
RI = NEGRITA + RED + "\nRespuesta incorrecta:" + RESET

#PUNTAJE
puntaje = random.randint(5, 11)  #Numeos aleatorios
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0

#INTRODUCTION
print(MAGENTA + "Hola! bienvenidos al primer desafio de preguntas\n" + RESET)
time.sleep(1)

nombre = input(BLUE + "¿Cómo quieres que te llame?: " + RESET)

time.sleep(1)
#PRESENTANDO
print(GREEN + "\nHermoso nombre 😎 ", nombre, "\n" + RESET)
time.sleep(1)
print("", nombre, "te dare", puntaje, "puntos para que puedas empezar\n")

#INSTRUCCIONES
time.sleep(1)
print(BLUE + "Cargando Instrucciónes ... " + RESET)
time.sleep(2)
print(
    YELLOW +
    """Bien ahora responda las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta\n"""
    + RESET)

time.sleep(1)

import time
#COMPENZAR TRIVIA
time.sleep(1)
print(CYAN + "\nComenzando la trivia en \n3" + RESET)
time.sleep(1)
print(CYAN + "2" + RESET)
time.sleep(1)
print(CYAN + "1" + RESET)
print(YELLOW + """
.--.
|__| .-------.
|=.| |.-----.|
|--| ||START||
|  | |'-----'|
|__|~')_____('  
""" + RESET)
time.sleep(1)
print(CYAN + "\nLa trivia ha comenzado...\n" + RESET)
time.sleep(2)
while iniciar_trivia == True:  #  Mientras iniciar_trivia sea True, repite:
    intentos += 1
    puntaje = 0

    #PREGUNTA1

    print(MAGENTA +
          "1. ¿En qué año se desarrolló el lenguaje de programación C?" +
          RESET)
    print("a) 1968")
    print("b) 1970")
    print("c) 1972")
    print("d) 1971")
    #INGRESAR RESPUESTA
    respuesta_1 = input(BLUE + "Ingresa tu respuesta: " + RESET)
    # RESPUESTA INVALIDA
    while respuesta_1 not in ("a", "b", "c", "d"):
        print(RED + "\nRespuesta invalida:" + RESET)
        print("Debes responder a, b, c o d.")
        respuesta_1 = input(BLUE + "Ingresa nuevamente tu respuesta: " + RESET)

#VERIFICAR RESPUESTA
    if respuesta_1 == "c":
        puntaje += random.randint(5, 10)
        print(RC)
    else:
        print(RI)
        puntaje -= random.randint(1, 5)

    print(
        YELLOW +
        """ C fue creado en 1972 por Dennis M. Ritchie en los Laboratorios Bell como evolución del anterior lenguaje B."""
        + RESET)
    #PUNTOS ACUMULADOS
    time.sleep(1)
    print(GREEN + "Acumulaste", puntaje, "puntos\n\n" + RESET)

    #PREGUNTA 2
    time.sleep(2)
    print(
        MAGENTA +
        "2. ¿Recuerdas cuál fue la contraseña para los controles informáticos durante 8 años de los misiles nucleares estadounidenses?"
        + RESET)
    print("a) 12345678")
    print("b) 00000000")
    print("c) qwerty123")
    print("d) @W#)hfl~4")

    #INGRESAR RESPUESTA
    respuesta_2 = input(BLUE + "Ingresa tu respuesta: " + RESET)

    #RESPUESTA INVALIDA
    while respuesta_2 not in ("a", "b", "c", "d"):
        print(RED + "\nRespuesta invalida:" + RESET)
        print("Debes responder a, b, c o d.")
        respuesta_2 = input(BLUE + "Ingresa nuevamente tu respuesta: " + RESET)

#VERIFICAR RESPUESTA
    if respuesta_2 == "b":
        puntaje += random.randint(5, 10)
        print(RC)
    else:
        print(RI)
        puntaje -= random.randint(1, 5)
    print(
        YELLOW +
        """ Así es, esta era la contraseña “súper segura” que estuvo ocho años activa y que daba acceso al control informático de las cabezas nucleares de Estados Unidos."""
        + RESET)

    #PUNTOS ACUMULADOS
    time.sleep(1)
    print(GREEN + "Acumulaste", puntaje, "puntos\n\n" + RESET)

    time.sleep(2)

    #PREGUNTA 3
    print(
        MAGENTA +
        "3. La primera unidad de disco duro de 1 GB se anunció en 1980, pesaba alrededor de 250 kilos y tenía costaba 40.000 dólares."
        + RESET)
    print("a) Verdadero")
    print("b) Falso")
    #INGRESAR RESPUESTA
    respuesta_3 = input(BLUE + "Ingresa tu respuesta: " + RESET)

    #RESPUESTA INVALIDA
    while respuesta_3 not in ("a", "b"):
        print(RED + "\nRespuesta invalida:" + RESET)
        print("Debes responder a o b")
        respuesta_3 = input(BLUE + "Ingresa nuevamente tu respuesta: " + RESET)

#VERIFICAR RESPUESTA
    if respuesta_3 == "a":
        puntaje += random.randint(5, 10)
        print(RC)
    else:
        print(RI)
        puntaje -= random.randint(1, 5)
    print(YELLOW + """La respuesta correcta es: Verdadero. ¡Así es!""" + RESET)

    #PUNTOS ACUMULADOS
    time.sleep(1)
    print(GREEN + "Acumulaste", puntaje, "puntos\n\n" + RESET)

    time.sleep(2)

    #PREGUNTA 4
    print(
        MAGENTA +
        "4. Un medio de codificación de texto en el que cada símbolo está representado por 16 bits es..."
        + RESET)
    print("a) LZW")
    print("b) ASCII")
    print("c) Unicode")
    print("d) Code")
    #INGRESAR RESPUESTA
    respuesta_4 = input(BLUE + "Ingresa tu respuesta: " + RESET)

    #RESPUESTA INVALIDA
    while respuesta_4 not in ("a", "b", "c", "d"):
        print(RED + "\nRespuesta invalida:" + RESET)
        print("Debes responder a, b, c o d.")
        respuesta_4 = input(BLUE + "Ingresa nuevamente tu respuesta: " + RESET)

#VERIFICAR RESPUESTA
    if respuesta_4 == "c":
        puntaje += random.randint(5, 10)
        print(RC)
    else:
        print(RI)
        puntaje -= random.randint(1, 5)
    print(
        YELLOW +
        """ La respuesta correcta es: Unicode es un sistema de codificación informático que tiene como objetivo unificar los intercambios de texto a nivel internacional. Cada carácter se describe con un nombre y un código que lo identifica de manera única, independientemente del medio informático o el software utilizado."""
        + RESET)

    #RESULTADO
    time.sleep(2)
    print(CYAN + "\n\n\n¡WOW ", nombre, "tu resultado es", puntaje,
          "puntos" + RESET)

    time.sleep(2)
    numero = int(input(BLUE + "\nIngresa tu número de la suerte: " + RESET))
    print(CYAN + "\nSu resultado final es: ", puntaje * numero,
          "\n\nGracias por jugar mi trivia!\n" + RESET)
    time.sleep(2)
    print(MAGENTA + "\n¿Deseas intentar la trivia nuevamente?" + RESET)
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar:\n "
    ).lower()

    if repetir_trivia != "si":  # != significa "distinto"
        print("\nNos vemos pronto", nombre, " y tome agua!")
        iniciar_trivia = False
