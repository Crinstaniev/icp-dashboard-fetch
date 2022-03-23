from time import sleep
import pandas as pd
import requests
import time
import matplotlib.pyplot as plt

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

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

cnt = 0

block_rate_dict = dict(
    blocks=[],
    block_rate=[],
    request_time=[]
)


@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph_scatter(n):
    data = pd.read_csv('record.csv')

    data = plotly.graph_objs.Scatter(
        x=data['request_time'],
        y=data['block_rate'],
        name='Scatter',
        mode='lines+markers'
    )

    return {'data': [data],
            'layout': go.Layout(xaxis=dict(
                range=[min(data['request_time']), max(data['request_time'])]), yaxis=dict(range=[min(data['block_rate']), max(data['block_rate'])]),
    )}


while True:
    res = requests.get(
        'https://ic-api.internetcomputer.org/api/metrics/block-rate').json()
    blocks = res['block_rate'][0][0]
    block_rate = float(res['block_rate'][0][1])
    block_rate_dict['block_rate'].append(block_rate)
    block_rate_dict['blocks'].append(blocks)
    block_rate_dict['request_time'].append(time.time())

    cnt += 1

    if cnt % 1 == 0:
        df = pd.DataFrame(block_rate_dict)
        df.to_csv('record.csv')
    sleep(1)
