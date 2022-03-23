import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id='live-graph',
                  animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1000,
            n_intervals=0
        ),
    ]
)


@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph_scatter(n):
    dat = pd.read_csv('record.csv')
    # print(dat)

    data = plotly.graph_objs.Scatter(
        x=dat['request_time'],
        y=dat['block_rate'],
        name='Scatter',
        mode='lines+markers'
    )

    return {'data': [data],
            'layout': go.Layout(xaxis=dict(
                range=[min(dat['request_time']), max(dat['request_time'])]), yaxis=dict(range=[min(dat['block_rate']), max(dat['block_rate'])]),
    )}


app.run_server()
