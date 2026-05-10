import dash
from dash import html
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/', title='Stocks', name='Home')

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Img(src="assets/stocks-and-indices.png", style={"height":"80%","width":"80%"})
        ])
    ])
])