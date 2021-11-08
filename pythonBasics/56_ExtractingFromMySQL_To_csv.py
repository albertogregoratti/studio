#########################################################
# Export a MySQL table into a .csv file using a DataFrame
#########################################################
import MySQLdb
from datetime import datetime
import csv
from google.oauth2 import service_account


# Set variables
csvfile_out = 'C:/Temp/plm_outfile4.csv'

# Set GCP Credentials
key_path = 'C:/Dev/bq/PoC Appmaker/poc-appmaker-d4f8ca3f9d79.json'
credentials = service_account.Credentials.from_service_account_file(key_path)

def job():
    db = MySQLdb.connect(
        host='10.80.129.171',
        user='app_maker_rw',
        password='5xxrAJkEfJEf9gf5',
        database='Opportunity_Reporting'
    )
# Extract data from MySQL and store query results into a DataFrame
    print('Start Extracting from MySQL - ', datetime.now())
    #my_query = ('SELECT SalesRep, TYPE, BPID, GrossValue FROM Vw_Opportunity LIMIT 10;')
    cur = db.cursor()
    cur.execute("""SELECT SalesRep, TYPE, BPID, GrossValue FROM Vw_Opportunity LIMIT 10;""")
    print('Finished Extracting - ', datetime.now())
    print()
# Export query result into a .csv file
    print('Start Exporting to csv - ', datetime.now())
    outfile = open(csvfile_out, 'wt')
    outcsv = csv.writer(outfile)
    outcsv.writerow(x[0] for x in cur.description)
    outcsv.writerows(cur.fetchall())
    outfile.close()
    db.close()
    print('Finished Exporting - ', datetime.now())
    print()

job()

'''
# Instantiates a client
client_ref1 = storage.Client.from_service_account_json(key_path)    # Creates a client using the service_account_json credentials
project_ref1 = client_ref1.project
'''




