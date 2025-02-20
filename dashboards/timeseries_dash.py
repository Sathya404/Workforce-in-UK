from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
from utils.timeseries_utils import timeseries_df as df

def create_timeseries_dash(dash_app):
    """Create a dashboard for employment analysis."""
    dash_app.layout = html.Div([
        html.Div(
            children='Employment Dashboard',
            style={
                'fontSize': '32px',  # Set the font size
                'fontWeight': 'bold',  # Make the text bold
                'textAlign': 'center',  # Center the title
                'marginBottom': '20px'  # Add some spacing below the title
            }
        ),
        html.Hr(),
        dcc.RadioItems(
            options=['Great Britain', 'England','Wales', 'Scotland', 'England and Wales','North East', 'North West', 'Yorkshire and The Humber', 'East Midlands', 'West Midlands',
                     'East','London','South East','South West'],
            # Automatically select GB by default
            value='Great Britain',
            id='controls-and-radio-item',
            style={'fontSize': '18px', 'fontFamily': 'arial'}
        ),
        html.Hr(),
        dcc.Dropdown(
            options=[{'label': 'Total employees', 'value': 'Total employees'},
                     {'label': 'Full-time employees', 'value': 'Full-time employees'},
                     {'label': 'Part-time employees', 'value': 'Part-time employees'}],
            value='Total employees',
            id='controls-and-dropdown-item',
            style={'fontSize': '18px', 'fontFamily': 'arial'}
        ),
        html.Hr(),
        # Create a flex container to allow the graph to expand
        html.Div(
            children=[
                dcc.Graph(id='controls-and-graph'),
            ],
            style={
                'display': 'flex',
                'flexDirection': 'row',  # Align items horizontally
                'justifyContent': 'space-between',  # Space out elements
                'alignItems': 'center',  # Center the content vertically
                'width': '100%',  # Ensure full width
                'marginTop': '20px',
            }
        )
    ])

    @dash_app.callback(
        Output(component_id='controls-and-graph', component_property='figure'),
        [Input(component_id='controls-and-radio-item', component_property='value'),
         Input(component_id='controls-and-dropdown-item', component_property='value')]
    )
    def update_graph(region_chosen, employee_status):
        if employee_status == 'Total employees':
            employee_status = 'Employees'

        filtered_df = df[
            (df['GEOGRAPHY_NAME'] == region_chosen) &
            (df['EMPLOYMENT_STATUS_NAME'] == employee_status)
        ]

        fig = px.line(
            filtered_df,
            x="DATE",
            y="OBS_VALUE",
            color="INDUSTRY_NAME",
            title=f'Employees in each industry from 2015 to 2023 - {region_chosen}'
        )

        fig.update_layout(
            xaxis_title="Year",
            yaxis_title="Number of employees",
            legend_title="Industry",
            width=1200,  # Set width to fill the available space
            height=600,  # Set the height of the graph
            showlegend=True
        )
        return fig
