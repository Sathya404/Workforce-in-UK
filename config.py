# Configuration file

WORKFORCE_API_URL = ("https://www.nomisweb.co.uk/api/v01/"
                     "dataset/NM_189_1.data.csv?geography=2092957698...2092957701,2092957703&date=latest&"
                     "industry=150994945...150994965&employment_status=1...3&measure=1,2&measures=20100")
WANTS_JOB_BY_SEX_URL = ("https://www.nomisweb.co.uk/api/v01/dataset/NM_181_1.data.csv?"
                        "geography=2013265921...2013265932&date=latest&c_sex=0...2&age=0&"
                        "einact=0&c_wants=2&measure=1&measures=20100,20701")
WORKFORCE_BY_INDUSTRY_URL = ("https://www.nomisweb.co.uk/api/v01/dataset/NM_131_1.data.csv?"
                             "geography=2013265921...2013265932&date=latest&industry=150994945...150994964&"
                             "sex=5...7&item=1&measures=20100")
TIMESERIES_API_URL = ("https://www.nomisweb.co.uk/api/v01/dataset/NM_189_1.data.csv?geography=2013265921...2013265931"
                      ",2092957698...2092957701,2092957703&industry=163577857...163577874&employment_status=1...3&"
                      "measure=1,2&measures=20100")

class Config:
    # Edit the below details accordingly
    DB_USER = 'root'
    DB_PASSWORD = ''
    DB_HOST = 'localhost'
    DB_NAME = 'EmploymentData'
