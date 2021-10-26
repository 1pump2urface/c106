import plotly.express as px
import csv
with open("C:/Users/Administrator/Desktop/Python/c106/Student Marks vs Days Present.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Days", y ="Marks" )
    fig.show()
