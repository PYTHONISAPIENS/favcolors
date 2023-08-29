import mod



def run():
    keys,values = mod.get_population()
    print(keys,values)

    print(mod.A)
    print(mod.B)
    print(mod.c)
    print(mod.cc)
    print(mod.bb)
    print(mod.mity)
    
if __name__ =='__main__':
    run()
    
datos=[
    {
        "barrio":"salamanca",
        "población":600
    },
    {
        "barrio":"arganda",
        "población":300
    },
    {
        "barrio":"aranjuez",
        "población":200
    }
]
barrio =input("escriba el barrio para saber población ")
resultado=mod.poblacion_barrios_madrid(datos,barrio)
print(resultado)

