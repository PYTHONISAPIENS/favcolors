import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv("./data.csv")
    country = input("inserte país ✈️  ")
    
    result= utils.population_by_country(data,country)
    
    if len(result)>0:
        country = result[0]
        labels, values = utils.saberpoblacion()
        print(labels,values)
        charts.generate_bar_chart(labels,values)
    
   
    
    
    print(result)
    
if __name__=="__main__":
    run()