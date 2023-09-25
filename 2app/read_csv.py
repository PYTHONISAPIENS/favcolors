import csv

def read_csv(ruta):
    with open(ruta, "r")as docucsv:
        lector = csv.reader(docucsv,delimiter=",")
        titulo = next(lector)
        data = []
        for i in lector:
            iterable = zip(titulo,i)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
            return data
        
if __name__=="__main__":
    data=read_csv("./data.csv")
    print(data[0])