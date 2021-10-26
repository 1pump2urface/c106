import plotly.express as px
import csv
with open("C:/Users/Administrator/Desktop/Python/c106/Size of TV,_Average time spent watching TV in a week (hours).csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Size", y ="Average" )
    fig.show()