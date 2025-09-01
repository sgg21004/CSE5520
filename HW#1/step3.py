from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from plotly.graph_objects import Bar, Figure

def fibonacci_sequence(n):
    sequence = []
    n1, n2 = 0, 1
    for _ in range(n):
        sequence.append(n1)
        n1, n2 = n2, n1 + n2
    return sequence

def create_fib_figure(n_terms):
    sequence = fibonacci_sequence(n_terms)
    x_labels = list(range(1, n_terms + 1))

    fig = Figure(data=[
        Bar(x=x_labels, y=sequence, name="Fibonacci", marker_color="skyblue")
    ])
    fig.update_layout(
        title=f"Fibonacci Sequence ({n_terms} Terms)",
        xaxis_title="Term Index",
        yaxis_title="Fibonacci Number"
    )
    return fig

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Fibonacci Sequence Dashboard", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Select number of terms:"),
        dcc.Slider(
            id='term-slider',
            min=5,
            max=50,
            step=1,
            value=10,
            marks={i: str(i) for i in range(5, 51, 5)},
        ),
    ], style={'width': '60%', 'margin': 'auto', 'padding': '20px'}),
    dcc.Graph(id='fib-graph')
])

@app.callback(
    Output('fib-graph', 'figure'),
    Input('term-slider', 'value')
)
def update_chart(n_terms):
    return create_fib_figure(n_terms)

if __name__ == '__main__':
    app.run(debug=True)  # ✅ updated from run_server → run