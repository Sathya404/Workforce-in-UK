import pandas as pd
from config import TIMESERIES_API_URL, Config
from utils.db_utils import query_execution


# Extract data from NOMIS API and print data
try:
    data = pd.read_csv(f'{TIMESERIES_API_URL}', encoding='utf-8')
    print("\n\n\nData successfully loaded")
except pd.errors.ParserError:
    print("\n\n\nAn Error has occurred when parsing the CSV file. Check the file format.")
except Exception as e:
    print(f'\n\n\nThe following error: {e} has occurred.')

# Wrangle data

## Add observation code = 1
data['OBS_CODE'] = 1

# Create list of columns to keep under variable columns_to_keep
columns_to_keep=['DATE_SORTORDER', 'GEOGRAPHY_SORTORDER', 'INDUSTRY_CODE', 'EMPLOYMENT_STATUS_CODE',
                 'MEASURE_CODE','OBS_CODE','OBS_VALUE','URN']

df=data[columns_to_keep]   # Create a dataframe with columns




for index, row in df.iterrows():

    query = f"""
    INSERT INTO EmploymentData (DATE_SORTORDER, GEOGRAPHY_SORTORDER, INDUSTRY_CODE, EMPLOYMENT_STATUS_CODE,
                               MEASURE_CODE, OBS_CODE, OBS_VALUE, URN) 
    VALUES ('{row['DATE_SORTORDER']}', '{row['GEOGRAPHY_SORTORDER']}', '{row['INDUSTRY_CODE']}', 
            '{row['EMPLOYMENT_STATUS_CODE']}', '{row['MEASURE_CODE']}', '{row['OBS_CODE']}', 
            '{row['OBS_VALUE']}', '{row['URN']}');
    """

    query_execution(query)