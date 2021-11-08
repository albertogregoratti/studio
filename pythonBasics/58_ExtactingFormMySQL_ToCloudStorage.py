##########################################################################################
# Export a MySQL table into Cloud Storage as a file
##########################################################################################

##########################################################################################
from datetime import datetime
import csv
import pymysql
from google.cloud import storage

# Instantiates a gcp storage client
client_sto = storage.Client.from_service_account_json(key_path)    # Creates a client using the service_account_json credentials
project_sto = client_sto.project
dest_bucket = client_sto.get_bucket('mysql_plm')

