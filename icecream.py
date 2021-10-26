import plotly.express as px
import csv
with open("C:/Users/Administrator/Desktop/Python/c106/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Temperature", y ="Ice-cream" )
    fig.show()