from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

from utils.industrial_utils import *



def create_industrial_dash(dash_app):
    """Create a dashboard for employment full and part-time analysis."""
    dash_app.layout = html.Div([
    html.H1("Industrial Employment Analysis in UK", style={"textAlign": "center"}),

    # Dropdown for Industry Selection
    html.Div([
        dcc.Dropdown(
            id="industry-dropdown",
            options=[{"label": ind, "value": ind} for ind in industries],
            value=industries[0],
            placeholder="Select an Industry"
        )
    ], style={"width": "90%", "margin": "auto"}),

    # Bar Graph
    dcc.Graph(id="industry-bargraph"),

    # Choropleth Map
    dcc.Graph(id="choropleth-map"),
    ])

    # Callbacks
    @dash_app.callback(
        [Output("industry-bargraph", "figure"),
         Output("choropleth-map", "figure")],
        [Input("industry-dropdown", "value")]
    )
    def update_dashboard(selected_industry):
        # Filter data for the selected industry
        industry_data = employment_df[employment_df["INDUSTRY_NAME"] == selected_industry]
        map_data = employment_df_initial[employment_df_initial["INDUSTRY_NAME"]== selected_industry]

        # Bar Graph
        bar_fig = px.bar(
            industry_data,
            x="GEOGRAPHY_NAME",
            y="OBS_VALUE",
            color="SEX_NAME",
            labels={"OBS_VALUE": "Employment", "GEOGRAPHY_NAME": "Region", "SEX_NAME": "Sex"},
            title=f"Employment Distribution by Region for the industry/ies {selected_industry}"
        )

        # Choropleth Map
        map_fig = px.choropleth(
            map_data,
            geojson=regions,
            locations="GEOGRAPHY_NAME",
            featureidkey="properties.areanm",
            color="OBS_VALUE",
            title=f"Employment Density in UK for the industry/ies {selected_industry}",
            labels={"OBS_VALUE": "Employment"}
        )
        map_fig.update_geos(fitbounds="locations", visible=False)

        return bar_fig, map_fig

