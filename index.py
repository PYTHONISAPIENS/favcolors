acorde_deseado = input("          POR FAVOR ELIJA DE LA SIGUIENTE LISTA DE EMOCIONES LA QUE DESEARÍA REPRESENTAR EN PINTURA, COMBINACIÓN DE VESTUARIO, ESCENA O IMPRESO: PASIÓN, CIENCIA, DEPORTE, CONFIANZA, DESCANSO, CALOR O ALEGRÍA: ➡️  ")
acorde_deseado = acorde_deseado.lower()
acorde_deseado = acorde_deseado.upper()

print("La paleta propuesta para la emoción "+acorde_deseado + " es la siguiente")

paletas = [
    ["ROJO: 1/2","NARANJA: 1/4","VIOLETA: 1/8","AMARILLO: 1/8"], #PASIÓN
    ["AZUL: 1/4", "BLANCO: 1/4", "GRIS: 1/4", "PLATEADO: 1/4"], #CIENCIA
    ["AZUL: 3/8", "BLANCO: 3/8", "VERDE: 1/8", "PLATEADO: 1/8"], #DEPORTE
    ["AZUL: 3/8", "VERDE: 3/8", "MARRÓN: 1/8","AMARILLO: 1/8"], #CONFIANZA
    ["AZUL: 3/8", "VERDE: 3/8","BLANCO: 1/8", "AMARILLO: 1/8"], #DESCANSO
    ["ROJO: 1/2", "AMARILLO: 3/8","NARANJA: 1/8"], #CALOR
    ["ROJO: 1/4", "AMARILLO: 1/4", "NARANJA: 1/4", "VERDE: 1/4"] #ALEGRÍA
    
]

if acorde_deseado == "PASIÓN":
    print(paletas[0])
elif acorde_deseado == "CIENCIA":
    print(paletas[1])
elif acorde_deseado == "DEPORTE":
    print(paletas[2])
elif acorde_deseado == "COFIANZA":
    print(paletas[3]) 
elif acorde_deseado ==  "DESCANSO":
    print(paletas[4])
elif acorde_deseado == "CALOR":
    print(paletas[5])
elif acorde_deseado == "ALEGRÍA":
    print(paletas[6])

else:
    print("EMOCIÓN NO RECONOCIDA")



