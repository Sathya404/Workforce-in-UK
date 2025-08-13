# 🇬🇧 Workforce in UK

The **Workforce Analysis Application** is a full-stack dashboard solution for analyzing UK employment trends, supporting workforce planning, and enabling data-driven decisions.  
Built with **Flask** (backend) and **Dash** (interactive dashboards), it integrates **machine learning** for predictions and insights.

---

## 📊 Overview

This application allows users to explore:

- Regional and industrial job segmentation
- Gender distribution in employment
- Full-time vs part-time comparisons
- Historical trends and forecasts

**Key technologies**: Flask, Dash, Pandas, Plotly, Scikit-learn, SQLAlchemy

---

## 🎯 Purpose

Developed as part of my **portfolio**, this project demonstrates my ability to:

- Integrate backend services with dynamic dashboards
- Perform data wrangling and exploratory analysis
- Apply machine learning for forecasting
- Build clear, user-friendly analytical tools

---

## 🗂️ Application Structure

```
workforce_analysis_app/
├── dashboards/         # Individual Dash dashboards
├── db_files/           # Database scripts and geo-data
├── utils/              # Data processing utilities
├── app.py              # Flask + Dash setup
├── main.py             # Application entry point
├── config.py           # App configuration
├── requirements.txt    # Dependencies
└── README.md
```

**Highlights:**

- **dashboards/**: Five interactive dashboards (Workforce, Regional/Gender, Industrial, Full-Time vs Part-Time, Time Series)
- **db_files/**: SQL database schema + GeoJSON for regional mapping
- **utils/**: Modular functions for data cleaning, aggregation, and visualization

---

## 🚀 Running the Application

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**  
   ```bash
   python main.py
   ```

3. Access in your browser at:  
   **http://127.0.0.1:5000/**

---

## 📈 Dashboards & Visuals

1. **Workforce Dashboard** – Occupational distribution across UK countries  
2. **Regional/Gender Dashboard** – Regional employment/unemployment with gender splits  
3. **Industrial Dashboard** – Employment by industry and region  
4. **Full-Time & Part-Time Dashboard** – Trends in working patterns  
5. **Time Series Dashboard** – Historical workforce trends

---

## 🛠 Skills Demonstrated

- **Python**: Flask, Pandas, Plotly, Scikit-learn
- **Dashboarding**: Dash
- **Data Wrangling** & Cleaning
- **Exploratory Data Analysis**
- **Machine Learning**: Classification & forecasting
- **End-to-End Deployment**

---

## 📄 License

For educational and portfolio purposes only.
