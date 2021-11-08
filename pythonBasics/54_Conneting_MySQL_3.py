# This file contains all the code used in the codelab.
import sqlalchemy
import pandas as pd
import pandas_gbq as pd_gbq

# Depending on which database you are using, you'll set some variables differently.
# In this code we are inserting only one field with one value.
# Feel free to change the insert statement as needed for your own table's requirements.

# Uncomment and set the following variables depending on your specific instance and database:
connection_name = "poc-appmaker:us-central1:springernature-appmaker"
# table_name = ""
# table_field = ""
# table_field_value = ""
db_name = "Opportunity_Reporting"
db_user = "opps_viewer"
db_password = "opps_viewer"

# If your database is MySQL, uncomment the following two lines:
driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})


# If the type of your table_field value is a string, surround it with double quotes.

def agtest():
    #request_json = request.get_json()
    stmt = sqlalchemy.text('SELECT SalesRep, TYPE, BPID, GrossValue FROM Vw_Opportunity LIMIT 10')

    db = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername=driver_name,
            username=db_user,
            password=db_password,
            database=db_name,
            query=query_string,
        ),
        pool_size=5,
        max_overflow=2,
        pool_timeout=30,
        pool_recycle=1800
    )
    try:
        with db.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return 'ok'

print('Start')
agtest()
print('End')
