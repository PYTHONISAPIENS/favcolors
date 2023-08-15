ropero = [
    {
        "prenda":"camisa",
        "color":"amarillo",
        "temporada":"verano",
        "mes de compra": 6,
        "año de compra": 2017,
        "material":"tencel",
        "precio":8
        
    },
    {
        "prenda":"falda",
        "color":"negro",
        "temporada":"todas",
        "mes de compra": 1,
        "año de compra": 2023,
        "material":"poliester",
        "precio":8
        
    },
    {
        "prenda":"top",
        "color":"blanco",
        "temporada":"verano",
        "mes de compra": 2,
        "año de compra": 2023,
        "material":"lycra",
        "precio":13
        
    },
    {
        "prenda":"pantalón",
        "color":"blanco",
        "temporada":"verano",
        "mes de compra": 2,
        "año de compra": 2023,
        "material":"algodón",
        "precio": 54
        
    },
    {
        "prenda":"vestido",
        "color":"rosa",
        "temporada":"verano",
        "mes de compra": 8,
        "año de compra": 2023,
        "material":"lino",
        "precio": 8
        
    }
]

print(ropero)
print(len(ropero))
print("-------------------------")

filtro= list(filter(lambda i:i["año de compra"]==2023,ropero))
print(filtro)
print(len(filtro))
