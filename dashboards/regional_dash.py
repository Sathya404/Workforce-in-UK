from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from utils.regional_utils import *

def create_regional_dash(dash_app):
    # Create choropleth map
    fig = px.choropleth(
        unemployment_total,
        geojson=regions,
        locations="GEOGRAPHY_CODE",
        featureidkey="properties.areacd",
        color="OBS_VALUE",
        hover_name="GEOGRAPHY_NAME",
        title="Click on any region",
        scope='europe',
        color_continuous_scale="Viridis",
        labels={"OBS_VALUE": "Unemployment"}  # Rename the color legend
    )
    fig.update_geos(fitbounds="locations", visible=False)

    # Layout for the dashboard
    dash_app.layout = html.Div([
        html.H1(
            "Employment & Unemployment Analysis in UK by Region, Industry, and Sex",
            style={'fontSize': '22px', 'fontWeight': 'bold', 'fontFamily': 'Arial'}
        ),
        # Region Analysis Toggle
        # Conditional display for the map and region-details

        html.Div(
                [
                    html.Div(
                        dcc.Graph(id="map", figure=fig),
                        style={
                            "flex": "1",
                            "height": "75vh",
                            "marginRight": "20px",
                            "border": "1px solid #ddd",
                            "borderRadius": "5px",
                            "padding": "10px"
                        }
                    ),
                    html.Div(
                        id="region-details",
                        className="p-3",
                        style={
                            "flex": "1",
                            "height": "75vh",
                            "border": "1px solid #ddd",
                            "borderRadius": "5px",
                            "padding": "10px",
                            "overflowY": "auto",
                            "backgroundColor": "#f9f9f9"
                        }
                    )
                ],
                style={
                    "display": "flex",
                    "flexDirection": "row",
                    "gap": "10px",
                    "marginTop": "20px"
                }
            ),
        # Graphs below the map and region-details
        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Graph(id="population-pie-chart"),
                        dcc.Graph(id="employment-pie-chart"),
                        dcc.Graph(id="male-pie-chart"),
                        dcc.Graph(id="female-pie-chart"),
                    ],
                    style={
                        "display": "flex",
                        "flexWrap": "wrap",
                        "justifyContent": "space-between",
                        "gap": "10px",
                    }
                ),
                dcc.Graph(id="industry-bar-graph", style={"height": "800px", "width": "100%"})
            ],
            style={"marginTop": "20px"}
        )
    ])

    @dash_app.callback(
        [
            Output("region-details", "children"),
            Output("population-pie-chart", "figure"),
            Output("employment-pie-chart", "figure"),
            Output("male-pie-chart", "figure"),
            Output("female-pie-chart", "figure"),
            Output("industry-bar-graph", "figure")
        ],
        [Input("map", "clickData")]
    )
    def update_graphs(clickData):
        # Check if a region is clicked, default to UK if not
        if clickData is None:
            region_name = "UK"
            male_employment_count = male_employment_by_industry_all_regions["OBS_VALUE"].sum()
            female_employment_count = female_employment_by_industry_all_regions["OBS_VALUE"].sum()
            unemployment_male_count = unemployment_male["OBS_VALUE"].sum()
            unemployment_female_count = unemployment_female["OBS_VALUE"].sum()

            employment_gender_df = employment_by_industry_all_regions_gender
            job_openings = job_postings_by_region["job_postings"].sum()
        else:
            region_code = clickData["points"][0]["location"]
            region_name = regions_df.loc[regions_df["region_codes"] == region_code, "region_names"].values[0]
            male_employment_count = male_employment_by_regions[region_name]["OBS_VALUE"].sum()
            female_employment_count = female_employment_by_regions[region_name]["OBS_VALUE"].sum()
            unemployment_male_count = unemployment_male.loc[
                unemployment_male['GEOGRAPHY_NAME'] == region_name, "OBS_VALUE"
            ].sum()
            unemployment_female_count = unemployment_female.loc[
                unemployment_female['GEOGRAPHY_NAME'] == region_name, "OBS_VALUE"
            ].sum()

            employment_gender_df = employment_by_regions_gender.loc[
                employment_by_regions_gender["GEOGRAPHY_NAME"] == region_name
            ]
            job_openings = job_postings_by_region.loc[job_postings_by_region["region"]==region_name, "job_postings"].sum()

        # Generate figures
        population_pie = px.pie(
            names=["Total Male", "Total Female"],
            values=[male_employment_count + unemployment_male_count, female_employment_count + unemployment_female_count],
            title="Population Breakdown"
        )
        employment_pie = px.pie(
            names=["Male", "Female"],
            values=[male_employment_count, female_employment_count],
            title="Employment by Gender"
        )
        male_pie = px.pie(
            names=["Employed", "Unemployed"],
            values=[male_employment_count, unemployment_male_count],
            title="Male Employment"
        )
        female_pie = px.pie(
            names=["Employed", "Unemployed"],
            values=[female_employment_count, unemployment_female_count],
            title="Female Employment"
        )
        industry_bar = px.bar(
            employment_gender_df,
            x="INDUSTRY_NAME",  # Truncate to first letter
            y="OBS_VALUE",
            color="SEX_NAME",
            title="Employment by Industry",
            labels={"x": "", "y": ""}  # Remove the axis labels
        )

        # Remove axis titles and labels
        industry_bar.update_layout(
            xaxis_title= "Industries",  # Remove x-axis label
            yaxis_title= "Count",  # Remove y-axis label
            xaxis=dict(showticklabels=False),  # Remove x-axis ticks and labels
            showlegend=False,  # Optionally, hide legend if not needed
            title_font_size=50,
            xaxis_title_font_size=30,
            yaxis_title_font_size=30
        )

        # Add hover info to bar chart
        industry_bar.update_traces(
            hovertemplate="<b>Industry:</b> %{x}<br>"
                          "<b>Gender:</b> %{customdata}<extra></extra>"
                          "<b>Employment:</b> %{y}<br>",
            customdata=employment_gender_df["SEX_NAME"]
        )

        # Return updated graphs and details
        region_details = html.Div([
            html.H4(f"Region: {region_name}", style={"fontSize": "50px", "fontWeight": "bold"}),
            html.P(f"Total Employment: {male_employment_count + female_employment_count:,}",
                   style={"fontSize": "30px"}),
            html.P(f"Total Unemployment: {unemployment_male_count + unemployment_female_count:,}",
                   style={"fontSize": "30px"}),
            html.P(f"Total Job_openings: {job_openings}", style={"fontSize": "30px"}),
            html.P("\n\n\n"),
            html.P("Note: Employment & Unemployment details fetched in June 2024 "
                   "and Job openings in December 2024", style={"fontSize": "10px"}),
            html.P("Scrolldown for more information", style={"fontSize": '20px'}),
            html.P("Refresh the page for UK region", style={"fontSize": '20px'})
        ])

        return (
            region_details,
            population_pie,
            employment_pie,
            male_pie,
            female_pie,
            industry_bar
        )
