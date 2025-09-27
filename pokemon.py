import random

# Clase Entrenador
class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre

# Clase Pokemon
class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.max_ataque = random.randint(20, 100)
        self.vida_max = random.randint(150, 400)
        self.vida_actual = self.vida_max

    def recuperar(self):
        self.vida_actual = self.vida_max

# Variables globales
entrenador1 = Entrenador("Miguelina Dios")
pokemon1 = Pokemon("Dracoflame")
entrenador2 = None
pokemon2 = None
ganadas = 0
perdidas = 0

# Función para crear entrenador y pokemon
def crearEntrenadorPokemon(numero):
    global entrenador2, pokemon2
    if numero == 2:
        nombre_entrenador = input(f"Ingrese el nombre del entrenador {numero}: ")
        nombre_pokemon = input(f"Ingrese el nombre del pokemon de {nombre_entrenador}: ")
        entrenador2 = Entrenador(nombre_entrenador)
        pokemon2 = Pokemon(nombre_pokemon)

# Función para calcular el valor de ataque
def valorDeAtaque(numero):
    if numero == 1:
        return random.randint(0, pokemon1.max_ataque)
    else:
        return random.randint(0, pokemon2.max_ataque)

# Función para defender
def defender(numero, ataque):
    dado = random.randint(1, 6)
    if dado == 6:
        ataque = 0
        print("¡El ataque fue bloqueado!")
    if numero == 1:
        pokemon1.vida_actual -= ataque
        return pokemon1.vida_actual
    else:
        pokemon2.vida_actual -= ataque
        return pokemon2.vida_actual

# Menú principal
def menu():
    global ganadas, perdidas
    while True:
        print("\n--- MENÚ ---")
        print("P: Pelear")
        print("F: Finalizar")
        opcion = input("Elija una opción: ").upper()

        if opcion == "P":
            crearEntrenadorPokemon(2)
            pokemon1.recuperar()
            pokemon2.recuperar()

            print(f"\n{entrenador1.nombre} ({pokemon1.nombre}) VS {entrenador2.nombre} ({pokemon2.nombre})")
            print(f"{pokemon2.nombre} tiene {pokemon2.vida_max} de vida y ataque máximo {pokemon2.max_ataque}\n")

            turno = 1
            while pokemon1.vida_actual > 0 and pokemon2.vida_actual > 0:
                if turno == 1:
                    ataque = valorDeAtaque(1)
                    vida = defender(2, ataque)
                    print(f"{pokemon1.nombre} atacó con {ataque}. Vida de {pokemon2.nombre}: {vida}")
                    turno = 2
                else:
                    ataque = valorDeAtaque(2)
                    vida = defender(1, ataque)
                    print(f"{pokemon2.nombre} atacó con {ataque}. Vida de {pokemon1.nombre}: {vida}")
                    turno = 1

            if pokemon1.vida_actual <= 0:
                print(f"\n¡{entrenador2.nombre} y su {pokemon2.nombre} GANAN!")
                perdidas += 1
            else:
                print(f"\n¡{entrenador1.nombre} y su {pokemon1.nombre} GANAN!")
                ganadas += 1

        elif opcion == "F":
            print("\n=== FIN DEL JUEGO ===")
            print(f"Entrenador: {entrenador1.nombre}")
            print(f"Pokemon: {pokemon1.nombre}")
            print(f"Ataque máximo: {pokemon1.max_ataque}")
            print(f"Vida máxima: {pokemon1.vida_max}")
            print(f"Encuentros ganados: {ganadas}")
            print(f"Encuentros perdidos: {perdidas}")
            break

        else:
            print("Opción no válida")

# Programa principal
print("=== JUEGO DE POKEMON ===")
print(f"Entrenador 1: {entrenador1.nombre
