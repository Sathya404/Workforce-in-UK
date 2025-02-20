from app import create_flask_app, create_dash_app
from dashboards.regional_dash import create_regional_dash
from dashboards.timeseries_dash import create_timeseries_dash
from dashboards.industrial_dash import create_industrial_dash
from dashboards.full_part_dash import create_full_part_dash

def main():
    flask_app = create_flask_app()

    # Create Gender Dashboard
    regional_dash = create_dash_app(flask_app, "Gender Analysis",
                                  "/regional_dash/")
    create_regional_dash(regional_dash)

    # Create Industrial Dashboard
    industrial_dash = create_dash_app(flask_app, "Industrial Analysis",
                                    "/industrial_dash/")
    create_industrial_dash(industrial_dash)

    # Create Fulltime & Parttime Jobs Dashboard
    full_part_dash = create_dash_app(flask_app, "Full-time & Part-time jobs Analysis",
                                      "/full_part_dash/")
    create_full_part_dash(full_part_dash)

    # Create Timeseries Dashboard
    timeseries_dash = create_dash_app(flask_app, "Time Series Analysis",
                                "/timeseries_dash/")
    create_timeseries_dash(timeseries_dash)


    flask_app.run(debug=True)

if __name__ == "__main__":
    main()
