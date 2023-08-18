def get_population():
    keys = ["col","bol"]
    values = [300, 400]
    return keys,values

A= "hola gatito"
B="HOLA PERRITO"
c="hola gato gordo"
cc="hosla gordisimo"
bb="hola bb"
mity="hola pelute"

def poblacion_barrios_madrid(datos,barrio):
    resultado = list(filter(lambda i: i["barrio"]==barrio,datos))
    return resultado