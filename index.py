acorde_deseado = input("POR FAVOR ELIJA DE LA SIGUIENTE LISTA DE EMOCIONES LA QUE DESEARÍA REPRESENTAR EN PINTURA, COMBINACIÓN DE VESTUARIO, ESCENA O IMPRESO: PASIÓN, CIENCIA, DEPORTE, CONFIANZA, DESCANSO, CALOR O ALEGRÍA: ➡️  ")
acorde_deseado = acorde_deseado.lower()
acorde_deseado = acorde_deseado.upper()

print(acorde_deseado)

colores = ["AMARILLO","AZUL","ROJO","VERDE","NARANJA","NEGRO","BLANCO","PLATA","VIOLETA","GRIS"]
emociones =["PASIÓN", "CIENCIA", "DEPORTE", "CONFIANZA", "DESCANSO", "CALOR", "ALEGRÍA"]

print(acorde_deseado in emociones)

acorde_pasion = [
    {
        'COLOR':"ROJO",
        'PORCENTAJE':"1/2"
                     
    },
    {
        'COLOR':"NARANJA",
        'PORCENTAJE':"1/4"        
    },
    {
        'COLOR':"VIOLETA",
        'PORCENTAJE':"1/8"
                     
    },
    {
        'COLOR':"AMARILLO",
        'PORCENTAJE':"1/8"
                     
    },
  
]

if acorde_deseado == "PASIÓN":
    print(acorde_pasion)
