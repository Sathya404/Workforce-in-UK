from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

from utils.timeseries_utils import timeseries_df as df


# sample_data = df.head(1000)  # Use the first 10 rows as a sample
# fig = px.line(sample_data, x="DATE", y="OBS_VALUE", color="EMPLOYMENT_STATUS_NAME")
# fig.show()

def create_full_part_dash(dash_app):
    """Create a dashboard for employment full and part-time analysis."""
    dash_app.layout = html.Div([
        html.Div(
            children='Full and Part-time Employment Dashboard',
            style={
                'fontSize': '32px',  # Set the font size
                'fontWeight': 'bold',  # Make the text bold
                'textAlign': 'center',  # Center the title
                'marginBottom': '20px'  # Add some spacing below the title
            }
        ),
        html.Br(),
        html.Hr(),
        html.Br(),
        html.Div('Select an industry to display its employment type distribution data:',
                 style={'fontSize': '20px'}),
        html.Br(),
        html.Hr(),
        dcc.Dropdown(
            options=['1 : Agriculture, forestry & fishing (A)', '2 : Mining, quarrying & utilities (B,D and E)',
                     '3 : Manufacturing (C)', '4 : Construction (F)', '5 : Motor trades (Part G)',
                     '6 : Wholesale (Part G)', '7 : Retail (Part G)', '8 : Transport & storage (inc postal) (H)',
                     '9 : Accommodation & food services (I)', '10 : Information & communication (J)',
                     '11: Financial & insurance (K)', '12 : Property (L)',
                     '13 : Professional, scientific & technical (M)',
                     '14 : Business administration & support services (N)',
                     '15 : Public administration & defence (O)', '16 : Education (P)', '17 : Health (Q)',
                     '18 : Arts, entertainment, recreation & other services (R,S,T and U)'],
            value='17 : Health (Q)',
            id='controls-and-radio-item',
            style={'fontSize': '18px',
                   'fontFamily': 'arial'}
        ),
        html.Br(),
        html.Hr(),
        html.Br(),
        html.Div('Select a region/country to display its employment type distribution data:',
                 style={'fontSize': '20px'}),
        html.Br(),
        html.Hr(),
        dcc.Dropdown(
            id='controls-and-radio-item2',
            options=['Great Britain', 'England', 'Wales', 'Scotland', 'England and Wales', 'North East', 'North West',
                     'Yorkshire and The Humber', 'East Midlands', 'West Midlands',
                     'East', 'London', 'South East', 'South West'],
            value='Great Britain',
            style={'fontSize': '18px',
                   'fontFamily': 'arial'}
        ),
        html.Hr(),
        dcc.Graph(id='controls-and-graph',
                  style={
            'width': '100%',
            'height': '1000px',
            'marginTop': '0px',
            'marginBottom': '0px',
            'marginLeft': '0px',
            'marginRight': '0px',
            'fontFamily': 'arial'
        })
    ])

    @dash_app.callback(
        Output(component_id='controls-and-graph', component_property='figure'),
        [Input(component_id='controls-and-radio-item', component_property='value'),
         Input(component_id='controls-and-radio-item2', component_property='value')]
    )
    def update_graph(industry_chosen, region_chosen):
        # if employee_status == 'Total employees':
        #    employee_status = 'Employees'

        filtered_df = df[
            (df['INDUSTRY_NAME'] == industry_chosen) &
            (df['GEOGRAPHY_NAME'] == region_chosen)
            ]

        fig = px.line(
            filtered_df,
            x="DATE",
            y="OBS_VALUE",
            color="EMPLOYMENT_STATUS_NAME",
            title=f'Total, full & part-time employees from 2015 to 2023 - {industry_chosen}'
        )

        fig.update_layout(
            xaxis_title="Year",
            yaxis_title="Number of employees",
            legend_title="Employment type",
            width=800,
            height=600,
            showlegend=True
        )
        return fig