import pandas as pd
import plotly.express as px

df  =  pd.read_csv('data.csv')
pz = px.scatter(df, x='Country', y = 'Population')
pz.show()
