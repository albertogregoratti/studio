#######################################################################################################
## This script save in a csv file all datasets and tables in a project with other few table indicators
#######################################################################################################
from google.cloud import bigquery

# key_path = 'C:/Dev/bq/Looker/Usage/usage-data-reporting-89d67b6f773b.json'      # usage-data-reporting credentials
# key_path = 'C:/Dev/bq/Looker/BI_Prod/bi-production-239213-691c8d083291.json'     # bi-production credentials
key_path = 'C:/Dev/bq/Looker/BI_Team/bi-team-189611-5f3cc955630a.json'          # bi-team credentials

# initialise client with credentials
bq_client_ref = bigquery.Client.from_service_account_json(key_path)

with open('C:/Temp/bq_team_tables.csv', 'w') as out_file:
    print('Dataset; Table; Type; Created; Modified; Rows', file=out_file)
    for dataset in bq_client_ref.list_datasets():
        # if dataset.dataset_id == 'usage_bigquery_logs':     # excludes logs tables in usage-data-reporting
        #     continue
        # if dataset.dataset_id == 'MD_AuditLogging_DWH':       # excludes logs table in bi_production
        #     continue
        if dataset.dataset_id in ('audit_logs', 'bigquery_logs'):       # excludes logs table in bi_team
            continue
        for table in bq_client_ref.list_tables(dataset.dataset_id):
            tbl = bq_client_ref.get_table(table)
            line = (dataset.dataset_id + ";" + table.table_id + ";" + table.table_type + ";" + format(tbl.created)[:10] + ";" + format(tbl.modified)[:10] + ";" + format(tbl.num_rows))
            print(format(line), file=out_file)
out_file.close()

print('Done')
