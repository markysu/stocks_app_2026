import dash
from dash import dcc, html, callback
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go


dash.register_page(__name__, path='/candlestick', title='Candlestick', name='Candlestick_chart')

df = pd.read_csv("./assets/data.csv")


stocks = ['AMZN','GOOGL','META','MSFT','NVDA']

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Stocks", className="card-title text-center"),
                    dcc.Dropdown(id="stock_selector", options=[{"label": stock, "value": stock} for stock in stocks], multi=False, value=stocks[0]),
                ]),
                className="h-100"
            ),
        ], width=12),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Chart", className="card-title"),
                    dcc.Graph(id="stock_selector_graph", figure={})
                ])
            )
        ]),
    ],
    className="custom_margin"
    )
],
fluid=True)

# stock='META'
# fig = go.Figure(data=[go.Candlestick(x=df['Date'],
#                         open=df[f'Open_{stock}'], high=df[f'High_{stock}'],
#                         low=df[f'Low_{stock}'], close=df[f'Close_{stock}'])
#                         ])
# fig.update_layout(xaxis_rangeslider_visible=False)


@callback(
    Output("stock_selector_graph", "figure"),
    Input("stock_selector", "value")
)
def update_graph1(stock):
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                        open=df[f'Open_{stock}'], high=df[f'High_{stock}'],
                        low=df[f'Low_{stock}'], close=df[f'Close_{stock}'])
                        ])
    fig.update_layout(xaxis_rangeslider_visible=False)

    return fig
