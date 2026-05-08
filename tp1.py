# TP1 2026 
import random

# =========================
# VARIABLES
# =========================

nombre = ""

# Numero secreto
jugadas_ns = 0
ganadas_ns = 0
perdidas_ns = 0

# Par o impar
jugadas_pi = 0
ganadas_pi = 0
perdidas_pi = 0

# =========================
# JUEGO NUMERO SECRETO
# =========================

def numero_secreto():

    global jugadas_ns
    global ganadas_ns
    global perdidas_ns

    jugadas_ns = jugadas_ns + 1

    secreto = random.randint(1, 100)
    intentos = 6
    adivino = False

    print("\n========================")
    print("   NUMERO SECRETO")
    print("========================")

    for i in range(1, intentos + 1):

        print("\nIntentos restantes:", intentos - i + 1)

        numero = int(input("Ingrese un numero: "))

        if numero == secreto:
            print("\nGANASTE")
            print("Adivinaste en", i, "intentos")

            ganadas_ns = ganadas_ns + 1
            adivino = True

            break

        else:

            if numero < secreto:
                print("El numero secreto es MAYOR")
            else:
                print("El numero secreto es MENOR")

    if adivino == False:
        print("\nPERDISTE")
        print("El numero era:", secreto)

        perdidas_ns = perdidas_ns + 1

    input("\nPresione ENTER para volver al menu")

# =========================
# BLACKJACK
# =========================

def blackjack():

    print("\n========================")
    print("       BLACKJACK")
    print("========================")

    input("\nJuego en construccion. Presione ENTER para volver")

# =========================
# PAR O IMPAR
# =========================

def par_impar():

    global jugadas_pi
    global ganadas_pi
    global perdidas_pi

    jugadas_pi = jugadas_pi + 1

    print("\n========================")
    print("      PAR O IMPAR")
    print("========================")

    opcion = input("Ingrese PAR o IMPAR: ")
    opcion = opcion.lower()

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    suma = dado1 + dado2

    print("\nDado 1:", dado1)
    print("Dado 2:", dado2)
    print("Suma:", suma)

    if suma % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"

    if opcion == resultado:
        print("\nGANASTE")
        ganadas_pi = ganadas_pi + 1
    else:
        print("\nPERDISTE")
        perdidas_pi = perdidas_pi + 1

    input("\nPresione ENTER para volver al menu")

# =========================
# REPORTE
# =========================

def reporte():

    print("\n========================")
    print("        REPORTE")
    print("========================")

    print("\nJugador:", nombre)

    print("\nNUMERO SECRETO")
    print("Jugadas:", jugadas_ns)
    print("Ganadas:", ganadas_ns)
    print("Perdidas:", perdidas_ns)

    print("\nPAR O IMPAR")
    print("Jugadas:", jugadas_pi)
    print("Ganadas:", ganadas_pi)
    print("Perdidas:", perdidas_pi)

    input("\nPresione ENTER para volver")

# =========================
# MENU PRINCIPAL
# =========================

nombre = input("Ingrese su nombre: ")

opcion = 0

while opcion != 5:

    print("\n========================")
    print("      MENU PRINCIPAL")
    print("========================")

    print("1 - Numero secreto")
    print("2 - Blackjack")
    print("3 - Par o impar")
    print("4 - Reporte")
    print("5 - Salir")

    opcion = int(input("\nIngrese una opcion: "))

    if opcion == 1:
        numero_secreto()

    else:

        if opcion == 2:
            blackjack()

        else:

            if opcion == 3:
                par_impar()

            else:

                if opcion == 4:
                    reporte()

                else:

                    if opcion == 5:
                        print("\nGracias por jugar")
                        print("No apueste, juegue por diversion")

                    else:
                        print("\nOpcion incorrecta")
