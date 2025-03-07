def jugar_juego(player1, eleccion1, player2, eleccion2):
    if eleccion1 == eleccion2:
        return f"Empate"

    opciones= {"piedra": "tijera", 
               "papel": "piedra", 
               "tijera": "papel"}
    if opciones[eleccion1] == eleccion2:
        return f"{player1} gana"
    else:
        return f"{player2} gana"
    
player1= input("Nombre del primer jugador: ")
player2= input("Nombre del segundo jugador: ")

eleccion1= input("elija su opcion: ").lower()
eleccion2= input("elija su opcion: ").lower()

opciones_validas = ["piedra", "papel", "tijera"]
if eleccion1 not in opciones_validas or eleccion2 not in opciones_validas:
    print("opcion invalida")
else:
    print(jugar_juego (player1, eleccion1, player2, eleccion2))