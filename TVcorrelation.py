import plotly.express as px
import csv
import numpy as np

def getDataSource(datapath):
    size = []
    average = []
    with open(datapath) as f:
        csvReader = csv.DictReader(f)

        for row in csvReader:
            size.append(float(row["Size"])) 

            average.append(float(row["Average"]))
        
    return{"x":size, "y":average}

def FindCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlaton between size of TV and time spent",correlation[0,1])

def setup():
    datapath = "C:/Users/Administrator/Desktop/Python/c106/Size of TV,_Average time spent watching TV in a week (hours).csv"
    datasource = getDataSource(datapath)

    FindCorrelation(datasource)

setup()