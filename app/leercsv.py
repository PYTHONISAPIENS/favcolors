import csv

def leercsv (ruta):
    with open(ruta, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        datos = []
        #print(header)
        for i in reader:
            iterable = zip(header,i)
            print("--------"*3)
            #print(i)
            #print(list(iterable))
            dicciopais ={key:value for key, value in iterable}
            #print(dicciopais)
            datos.append(dicciopais)
        return datos

if __name__ == "__main__":
    datos=leercsv("./data.csv")
    print(datos[3])
    
