##########################################################################################
# Export a MySQL table into a .csv file
##########################################################################################
# https://stackoverflow.com/questions/35641893/best-way-for-python-to-interface-with-mysql
##########################################################################################
from datetime import datetime
import csv
import pymysql

# Set variables
csvfile_out = 'C:/Temp/plm_outfile4.csv'

def ExportFromMySQL():
    conn = pymysql.connect(
        host='10.80.129.171',
        port=3306,
        user='app_maker_rw',
        passwd='5xxrAJkEfJEf9gf5',
        db='Opportunity_Reporting'
    )
# Extract data from MySQL
    print('Start Extracting from MySQL - ', datetime.now())
    cur = conn.cursor()
    cur.execute('SELECT * FROM Vw_Opportunity LIMIT 10;')
    print('Finished Extracting - ', datetime.now())
    print()

# Export query result into a .csv file
    print('Start Exporting to csv - ', datetime.now())
    outfile = open(csvfile_out, 'wt',  encoding='utf-8', newline='')
    outcsv = csv.writer(outfile, delimiter=';')
    for row in cur:
        outcsv.writerow(row)
    cur.close()
    conn.close()
    print('Finished Exporting - ', datetime.now())



ExportFromMySQL()




