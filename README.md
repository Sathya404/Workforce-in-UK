# Workforce-in-UK

# 🇬🇧 Workforce-in-UK

The **Workforce Analysis Application** is a comprehensive dashboard solution developed to aid workforce planning, trend analysis, and strategic decision-making across various sectors in the UK. This project is part of my **portfolio** to showcase skills in data analysis, visualization, and full-stack application development using Python-based frameworks.

## 📊 Project Overview

This application integrates:
- **Flask** for backend routing and serving the application,
- **Dash** for building interactive and insightful dashboards,
- **Machine Learning** models to uncover patterns and generate predictions.

It enables users to explore:
- Regional and industrial segmentation of jobs
- Gender distribution across employment categories
- Full-time vs part-time job comparisons
- Historical trends and time-series forecasts

## 🎯 Why this Repository?

As a passionate data enthusiast and aspiring data professional, I created this project to demonstrate my ability to:
- Combine backend services with rich, dynamic dashboards
- Analyze and visualize real-world employment datasets
- Build meaningful applications that offer data-driven insights

## 🗂️ What's Inside?

### **Workforce Analysis of UK Application**  

## Introduction

The **Workforce Analysis Application** is a comprehensive dashboard solution designed for workforce planning, analysis, and decision-making.  
The application integrates **Flask** for backend routing and multiple **Dash** dashboards for data visualization.  
By leveraging machine learning models, it provides actionable insights into workforce trends, gender distribution, regional statistics,  
industrial segmentation, full-time versus part-time job distribution, and time-series analyses.

#### **Overview**  
This application analyzes workforce data across the UK, offering insights into employment trends, regional distributions, and industry-specific details. It features five interactive dashboards:  

1. **Workforce Dashboard**: Displays occupational distributions across UK countries.  
2. **Regional/Gender Dashboard**: Examines employment and unemployment by region and gender.  
3. **Industrial Dashboard**: Highlights employment trends across industries and regions.  
4. **Full-Time & Part-Time Dashboard**: Analyzes full-time vs. part-time employment.  
5. **Time Series Dashboard**: Tracks employment trends over time.  

---

### **Workforce Analysis Application Structure**

This is the directory structure of the Workforce Analysis Application:

```
workforce_analysis_app/
├── dashboards/
│   ├── workforce_dash.py
│   ├── regional_dash.py
│   ├── industrial_dash.py
│   ├── full_part_dash.py
│   └── timeseries_dash.py
├── db_files/
│   ├── rgn2024.geojson
│   ├── EmploymentDatabase.sql
│   ├── sql_database.py
├── utils/
│   ├── regional_utils.py
│   ├── industrial_utils.py
│   ├── timeseries_utils.py
│   └── workforce_utils.py
│   └── full_part_utils.py
│   └── db_utils.py
├── __init__.py
├── app.py
├── main.py
├── config.py
├── requirements.txt
└── README.md
```

### **Directory Structure Description**

#### **1. `workforce_analysis_app/`**
This is the root directory of the application, which organizes various components into subdirectories based on functionality.

---

#### **2. `dashboards/`  
Contains scripts for creating individual dashboards using Dash, each representing different aspects of workforce analysis.

- **Files**:
  - `workforce_dash.py`: A dashboard focused on overall workforce metrics.
  - `regional_dash.py`: Visualizes data related to regional workforce distribution.
  - `industrial_dash.py`: Analyzes workforce trends in various industries.
  - `full_part_dash.py`: Compares metrics for full-time and part-time employment.
  - `timeseries_dash.py`: Displays time-series visualizations for workforce trends.

---

#### **3. `db_files/`  
Houses files related to database management and structure.

- **Files**:
  - `rgn2024.geojson`: Geographic data for mapping regions.
  - `EmploymentDatabase.sql`: SQL script defining the employment database schema and/or sample data.
  - `sql_database.py`: Python script for interacting with the SQL database, including connection management and queries.

---

#### **4. `utils/`  
Contains utility scripts to handle data processing and application-specific logic.

- **Files**:
  - `regional_utils.py`: Functions for processing regional workforce data.
  - `industrial_utils.py`: Utilities for handling data on industrial sectors.
  - `timeseries_utils.py`: Tools for managing time-series workforce data.
  - `workforce_utils.py`: General utilities for workforce data processing.
  - `full_part_utils.py`: Functions for analyzing full-time and part-time workforce trends.
  - `db_utils.py`: Utility functions for database operations, such as CRUD (Create, Read, Update, Delete).

---

#### **5. `__init__.py`**
- Marks the directory as a Python package.
- Typically initializes the application, sets up configurations, or imports submodules.

---

#### **6. `app.py`**
- The main Flask application setup file.
- Initializes the Dash apps and registers them with the Flask server.

---

#### **7. `main.py`**
- Entry point to start the application.
- Integrates the Flask app and the Dash dashboards.

---

#### **8. `config.py`**
- Stores configuration settings for the application, such as database credentials, API keys, and environment-specific variables.

---

#### **9. `requirements.txt`**
- Lists all the Python dependencies required to run the application.
- Common entries may include:
  ```
  Flask
  Dash
  pandas
  plotly
  SQLAlchemy
  ```

---

#### **10. `README.md`**
- Documentation file providing an overview of the application.
- Includes setup instructions, a brief description of each component, and how to run the app.

---

### **How It Works**:
1. **Dashboards (`dashboards/`)**:
   Each script corresponds to a specific dashboard and uses the utility functions to process and visualize data.

2. **Utilities (`utils/`)**:
   Scripts here handle data preprocessing, making the dashboard scripts cleaner and more modular.

3. **Database (`db_files/`)**:
   The SQL file and GeoJSON data support the application's database layer, and the `sql_database.py` script interacts with the database.

4. **Application Initialization (`app.py`, `main.py`)**:
   These files set up the Flask-Dash integration, allowing dashboards to be served as web applications.

---

### **How to Start the Application**

To run the **Workforce Analysis of UK Application**, follow these steps:

#### 1. **Install Dependencies**  
Before starting, ensure you have all the required libraries installed:

```
pip install flask dash pandas plotly
```

#### 2. **Set Up the Flask and Dash Application**  
In your project directory, navigate to the folder containing the Python files and execute the following command:

```
python main.py
```

This will start a Flask server and the Dashboards.

---

### **Data Wrangling Process**

Data wrangling is the process of cleaning and preparing data for analysis. Here's how it was done for the various datasets:

#### 1. **Regional Data Wrangling** (from `regional_utils.py`)
```python
# Extract employment data by region
employment_df = pd.read_csv(WORKFORCE_BY_INDUSTRY_URL)

# Filter out unwanted geographies (Scotland and Wales are duplicated)
employment_df = employment_df[~employment_df['GEOGRAPHY'].isin(['2013265930', '2013265931'])]

# Keep relevant columns and filter data for 'Total' employment status
employment_by_regions = {}
for region in employment_df['GEOGRAPHY_NAME'].unique():
    employment_by_regions[region] = employment_df.loc[
        (employment_df['SEX_NAME'] == 'Total') & 
        (employment_df['GEOGRAPHY_NAME'] == region), 
        ['INDUSTRY_NAME', 'OBS_VALUE']
    ]
```
- **Key Steps**:
  - Loaded data using `pd.read_csv`.
  - Removed duplicate regions (Scotland and Wales).
  - Filtered data for total employment and grouped by region and industry.

#### 2. **Industrial Data Wrangling** (from `industrial_utils.py`)
```python
# Filter data by industry and gender
employment_df_initial = pd.read_csv(WORKFORCE_BY_INDUSTRY_URL)
employment_df = employment_df_initial[employment_df_initial['SEX_NAME'] != 'Total']

# Group data by industry and region
jobs_by_industry = {}
for industry in employment_df['INDUSTRY_NAME'].unique():
    jobs_by_industry[industry] = employment_df[employment_df['INDUSTRY_NAME'] == industry]
```
- **Key Steps**:
  - Loaded the dataset and filtered by gender (`SEX_NAME != 'Total'`).
  - Created a dictionary to store employment data by industry.

#### 3. **Full-Time and Part-Time Data Wrangling** (from `timeseries_utils.py`)
```python
# Extract timeseries data
data = pd.read_csv(TIMESERIES_API_URL)

# Clean data by removing rows with percentage values and unwanted geographies
timeseries_df = data[
    ~data['MEASURE_CODE'].isin([2]) &  # Remove industry percentage rows
    ~data['GEOGRAPHY'].isin(['2013265930', '2013265931'])  # Remove duplicate geographies
]
```
- **Key Steps**:
  - Loaded the timeseries data.
  - Removed rows with industry percentage data and unwanted geographical entries.

---

### **Data Visualizations**

Here’s a summary of the key visualizations in each dashboard:

#### **1. Regional/Gender Dashboard**
- **Choropleth Map**: Visualizes unemployment by region across the UK.
- **Pie Charts**: Show the distribution of employment and unemployment by gender.
- **Bar Graph**: Displays industry-specific employment in selected regions.

**Link to Visualization**:  
[Regional/Gender Dashboard](http://127.0.0.1:5000/regional_dash/)

#### **2. Industrial Dashboard**
- **Bar Chart**: Displays employment distribution by region and gender for selected industries.
- **Choropleth Map**: Shows employment density by region for selected industries.

**Link to Visualization**:  
[Industrial Dashboard](http://127.0.0.1:5000/industrial_dash/)

#### **3. Workforce Dashboard**
- **Pie Chart**: Shows the occupational distribution across different UK countries.
- **Data Table**: Displays detailed employment statistics by occupation.

**Link to Visualization**:  
[Workforce Dashboard](http://127.0.0.1:5000/workforce_dash/)

#### **4. Full-Time & Part-Time Dashboard**
- **Line Chart**: Shows trends in full-time, part-time, and total employment across industries and regions.

**Link to Visualization**:  
[Full-Time & Part-Time Dashboard](http://127.0.0.1:5000/full_part_dash/)

#### **5. Time Series Dashboard**
- **Line Chart**: Displays employment trends across industries in different regions over time.

**Link to Visualization**:  
[Time Series Dashboard](http://127.0.0.1:5000/timeseries_dash/)

---

#### **Target Audience**
- **HR Professionals**: To analyze workforce data and identify trends.
- **Business Leaders**: To make informed decisions about workforce distribution and planning.
- **Data Analysts**: To derive insights from workforce data using advanced visualizations.
- **Policy Makers**: To explore workforce-related statistics for policy development.

---

#### **Agile Approach**  
Our group used Agile to develop this application:  
- **Sprints**: Weekly targets for dashboards and data integration.  
- **User Stories**: Focused on user needs for Business Leaders, Policy Makers, and HR professionals.  
- **Collaborative Standups**: Regular updates to resolve challenges.

---

### **Conclusion**  
This application provides actionable insights for policymakers and HR professionals, fostering informed decisions and workforce development.  
It is designed to be user-friendly, ensuring accessibility for both technical and non-technical users.


📷 Screenshots


🧠 Skills Demonstrated
Python (Flask, Pandas, Plotly, Scikit-learn)

Dashboarding with Dash

Data Wrangling and Cleaning

Exploratory Data Analysis

Machine Learning (Classification / Forecasting)

End-to-End Application Deployment

📄 License
This project is for educational and portfolio purposes only.

