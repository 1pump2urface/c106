import plotly.express as px
import csv
with open("C:/Users/Administrator/Desktop/Python/c106/cups of coffee vs hours of sleep.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Coffee", y ="sleep" )
    fig.show()