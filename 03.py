import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    dcc.Graph(id='scatter-plot'),
    html.Label('Select the number of points:'),
    dcc.Slider(
        id='points-slider',
        min=10,
        max=100,
        step=10,
        value=50,
        marks={i: str(i) for i in range(10, 101, 10)}
    )
])

# Define callback to update scatter plot based on slider value
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('points-slider', 'value')]
)
def update_scatter_plot(num_points):
    # Generate random data points
    x = np.random.randn(num_points)
    y = np.random.randn(num_points)

    # Create scatter plot
    scatter_plot = go.Figure(
        data=[go.Scatter(x=x, y=y, mode='markers')],
        layout=go.Layout(
            title='Random Scatter Plot',
            xaxis=dict(title='X-axis'),
            yaxis=dict(title='Y-axis'),
            showlegend=False
        )
    )

    return scatter_plot

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
