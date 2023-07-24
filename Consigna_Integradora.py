import random

import matplotlib.pyplot as plt

class Juego:

    
    def jugar_piedra_papel_tijera(self):
        opciones = ["piedra", "papel", "tijera"]
        jugador = input("Elige piedra, papel o tijera: ")
        computadora = random.choice(opciones)
        print("==========================")
        print("Jugador: ", jugador)
        print("==========================")
        print("Computadora: ", computadora)
        print("==========================")
        if jugador == computadora:
            print("=========")
            print("Empate !")
            print("=========")
        elif (jugador == "piedra" and computadora == "tijera") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijera" and computadora == "papel"):
            print("=========")
            print("¡Ganaste!")
            print("=========")
        else:
            print("==========")
            print("¡Perdiste!")
            print("==========")

    
    def adivinar_numero(self):
        numero_secreto = random.randint(1, 20)
        intentos = 0
        while True:
            intento = int(input("Adivina el número (1-20): "))
            intentos += 1
            if intento == numero_secreto:
                print("==================================================")
                print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
                print("==================================================")
                break
            elif intento < numero_secreto:
                print("=====================================")
                print("El número es mayor. Intenta de nuevo.")
                print("=====================================")
            else:
                print("=====================================")
                print("El número es menor. Intenta de nuevo.")
                print("=====================================")    
    

    def tirar_dado(self):
        resultado = random.randint(1, 6)
        print("===========================================")
        print("El resultado del lanzamiento es:", resultado)
        print("===========================================")
    

    def graficar_funcion(self):
        def funcion(x):
            return x**2
        x = range(-10, 11)
        y = [funcion(i) for i in x]
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráfico de la función cuadrática')
        plt.grid(True)
        plt.show()


juego = Juego()

while True:
    print("¿Qué acción quieres realizar?\n")
    print("1. Jugar piedra, papel, tijera\n")
    print("2. Adivinar un número\n")
    print("3. Tirar un dado\n")
    print("4. Graficar una función matemática\n")
    print("5. Salir\n")
    opcion = input("Ingresa el número de la acción: ")
    if opcion == "1":
        juego.jugar_piedra_papel_tijera()
    elif opcion == "2":
        juego.adivinar_numero()
    elif opcion == "3":
        juego.tirar_dado()
    elif opcion == "4":
        juego.graficar_funcion()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")