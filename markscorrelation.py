import plotly.express as px
import csv
import numpy as np

def getDataSource(datapath):
    marks = []
    days = []
    with open(datapath) as f:
        csvReader = csv.DictReader(f)

        for row in csvReader:
            marks.append(float(row["Marks"])) 

            days.append(float(row["Days"]))
        
    return{"x":marks, "y":days}

def FindCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlaton between marks and days present ",correlation[0,1])

def setup():
    datapath = "C:/Users/Administrator/Desktop/Python/c106/Student Marks vs Days Present.csv"
    datasource = getDataSource(datapath)

    FindCorrelation(datasource)

setup()