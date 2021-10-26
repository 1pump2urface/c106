import plotly.express as px
import csv
import numpy as np

def getDataSource(datapath):
    temp = []
    icecreamsales = []
    with open(datapath) as f:
        csvReader = csv.DictReader(f)

        for row in csvReader:
            temp.append(float(row["Temperature"])) 

            icecreamsales.append(float(row["Ice-cream"]))
        
    return{"x":temp, "y":icecreamsales}

def FindCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlaton between temperature and icecream sales",correlation[0,1])

def setup():
    datapath = "C:/Users/Administrator/Desktop/Python/c106/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource = getDataSource(datapath)

    FindCorrelation(datasource)

setup()