import random

def obtener_eleccion_usuario():
    print("\nElige una opción:")
    print("1) Piedra")
    print("2) Papel")
    print("3) Tijeras")
    opcion = input("Ingresa el número de tu elección: ")

    if opcion == "1":
        return "piedra"
    elif opcion == "2":
        return "papel"
    elif opcion == "3":
        return "tijeras"
    else:
        print("Opción no válida. Intenta de nuevo.")
        return obtener_eleccion_usuario()

def obtener_eleccion_pc():
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

def determinar_ganador(jugador, pc):
    if jugador == pc:
        return "empate"
    elif (jugador == "piedra" and pc == "tijeras") or \
         (jugador == "papel" and pc == "piedra") or \
         (jugador == "tijeras" and pc == "papel"):
        return "jugador"
    else:
        return "pc"

print("===== MINI-JUEGO: PIEDRA, PAPEL O TIJERAS =====")

seguir = "s"
while seguir.lower() == "s":
    jugador = obtener_eleccion_usuario()
    pc = obtener_eleccion_pc()

    print(f"\nTú elegiste: {jugador.capitalize()}")
    print(f"La computadora eligió: {pc.capitalize()}")

    resultado = determinar_ganador(jugador, pc)

    if resultado == "empate":
        print("Resultado: ¡Es un empate!")
    elif resultado == "jugador":
        print("Resultado: ¡Ganaste! 🎉")
    else:
        print("Resultado: La computadora gana 😢")

    seguir = input("\n¿Deseas jugar otra vez? (s/n): ")

print("\nGracias por jugar. Programa finalizado.")

