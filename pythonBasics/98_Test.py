from google.cloud import bigquery
from google.oauth2 import service_account
import pandas_gbq
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

dataset_id = 'PROD_IFM_Usage'
project_id = 'usage-data-reporting'

# Set GCP Credentials
# key_path = 'C:/Dev/bq/Usage_Reporting_key/usage-data-reporting-0192446b1bb9.json'
client_ref = bigquery.Client.from_service_account_json(key_path)

dataset_ref = client_ref.dataset(dataset_id)

query2 = """
SELECT  Calendar_Year, Calendar_Year_Month, Platform, Sum(Downloads) As Download, Sum(Denials) As Denials, Sum(Clicks) As Total
FROM `usage-data-reporting.PROD_IFM_Usage.mv_usage_mat_monthly` 
WHERE Calendar_Year between 2015 and 2019
GROUP BY 1, 2, 3
ORDER BY 3, 1, 2
"""
df = pandas_gbq.read_gbq(query2, project_id = project_id, dialect = 'standard')

df.head()
