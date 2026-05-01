from google.cloud import bigquery
from google.oauth2 import service_account

# ***********************************************************************************
# Environment variables, Filters and Folders
# ***********************************************************************************
# Set GBQ Project-Dataset-Table
project_id = 'bi-team-189611'
dataset_id = 'ag_test'
table_id = 'fd_in'

# Set GCP Credentials
key_path = 'C:/Dev/fd/bi-team-189611-c78f094e47ef.json'
credentials = service_account.Credentials.from_service_account_file(key_path)

# Set GBQ client
client = bigquery.Client(credentials=credentials, project=credentials.project_id)
# client_ref = bigquery.Client(project=project_id)
dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)

file_name = 'C:/Dev/freshdesk/gbq_in.csv'

# GBQ Table schema:
table_schema = [
        bigquery.SchemaField('cc_emails', 'STRING', mode='REPEATED', description='cc emails'),
        bigquery.SchemaField('fwd_emails', 'STRING', mode='REPEATED', description='fwd emails'),
        bigquery.SchemaField('reply_cc_emails', 'STRING', mode='REPEATED', description='reply cc emails'),
        bigquery.SchemaField('ticket_cc_emails', 'STRING', mode='REPEATED', description='ticket cc emails'),
        bigquery.SchemaField('fr_escalated', 'BOOLEAN', description='Ticket escalated'),
        bigquery.SchemaField('spam', 'BOOLEAN', description='Spam'),
        bigquery.SchemaField('email_config_id', 'INTEGER', description='Email config id'),
        bigquery.SchemaField('group_id', 'INTEGER', description='Group Id'),
        bigquery.SchemaField('priority', 'INTEGER', description='Priority'),
        bigquery.SchemaField('requester_id', 'INTEGER', description='Requester Id'),
        bigquery.SchemaField('responder_id', 'INTEGER', description='Responder Id'),
        bigquery.SchemaField('source', 'INTEGER', description='Source'),
        bigquery.SchemaField('company_id', 'INTEGER', description='Company Id'),
        bigquery.SchemaField('status', 'INTEGER', description='Status'),
        bigquery.SchemaField('subject', 'STRING', description='Subject'),
        bigquery.SchemaField('product', 'STRING', description='Product'),
        bigquery.SchemaField('association_type', 'INTEGER', description='Association Type'),
        bigquery.SchemaField('to_emails', 'STRING', mode='REPEATED', description='to emails'),
        bigquery.SchemaField('product_id', 'INTEGER', description='Product Id'),
        bigquery.SchemaField('id', 'INTEGER', description='Ticket Id'),
        bigquery.SchemaField('type', 'STRING', description='Type'),
        bigquery.SchemaField('due_by', 'TIMESTAMP', description='Ticket due-by date'),
        bigquery.SchemaField('fr_due_by', 'TIMESTAMP', description='Ticket due-by date'),
        bigquery.SchemaField('is_escalated', 'BOOLEAN', description='Ticket escalated'),
        bigquery.SchemaField(
            'custom_fields',
            'RECORD',
            mode='REPEATED',
            fields=(
                bigquery.SchemaField('cf_query_type', 'STRING'),
                bigquery.SchemaField('cf_subtype', 'STRING'),
                bigquery.SchemaField('cf_bpid', 'INTEGER'),
                bigquery.SchemaField('message_type', 'STRING'),
                bigquery.SchemaField('cf_access_issue_root_cause', 'STRING'),
                bigquery.SchemaField('followup_by', 'DATE'),
                bigquery.SchemaField('cf_book_brands', 'STRING'),
                bigquery.SchemaField('cf_additional_services', 'STRING'),
                bigquery.SchemaField('cf_articlebookchapter_id', 'STRING'),
                bigquery.SchemaField('cf_journal_brands', 'STRING'),
                bigquery.SchemaField('cf_journal_name', 'STRING'),
                bigquery.SchemaField('cf_platforms', 'STRING'),
                bigquery.SchemaField('cf_journal_portfolio', 'STRING'),
                bigquery.SchemaField('cf_category', 'STRING'),
                bigquery.SchemaField('platform_or_service', 'STRING'),
                bigquery.SchemaField('crm_ticket_id', 'INTEGER'),
                bigquery.SchemaField('cf_order_number', 'INTEGER'),
                bigquery.SchemaField('cf_ecommercewebshop', 'BOOLEAN'),
                bigquery.SchemaField('cf_customer_service', 'BOOLEAN'),
                bigquery.SchemaField('cf_logistics', 'BOOLEAN'),
                bigquery.SchemaField('cf_offset_vendor', 'BOOLEAN'),
                bigquery.SchemaField('cf_pod_vendor', 'BOOLEAN'),
                bigquery.SchemaField('cf_major_group', 'STRING'),
                bigquery.SchemaField('cf_warehouse', 'BOOLEAN'),
                bigquery.SchemaField('cf_survey_sent_out', 'BOOLEAN'),
                bigquery.SchemaField('cf_interaction_id', 'STRING'),
                bigquery.SchemaField('cf_salesforce_quoteopp_id', 'STRING'),
                bigquery.SchemaField('cf_wf_invoice_number', 'INTEGER'),
                bigquery.SchemaField('cf_sap_contract_id', 'INTEGER'),
                bigquery.SchemaField('cf_comments', 'STRING'),
                bigquery.SchemaField('cf_access_issue_comments', 'STRING', description='Institutional License Access'),
                bigquery.SchemaField('cf_type', 'STRING', description='Titles/ Products Missing'),
                bigquery.SchemaField(
                    'cf_comments867284', 'STRING', description='Title/content on License Agreement not activated'
                ),
                bigquery.SchemaField('cf_manuscript_status', 'STRING'),
                bigquery.SchemaField('cf_role', 'STRING'),
            ),
        ),
        bigquery.SchemaField('created_at', 'TIMESTAMP', description='Ticket creation date'),
        bigquery.SchemaField('updated_at', 'TIMESTAMP', description='Ticket updated date'),
        bigquery.SchemaField('associated_tickets_count', 'INTEGER', description='Associated tickets Count'),
        bigquery.SchemaField('tags', 'STRING', mode='REPEATED', description='Tags'),
        bigquery.SchemaField(
            'stats',
            'RECORD',
            mode='REPEATED',
            fields=(
                bigquery.SchemaField('agent_responded_at', 'TIMESTAMP'),
                bigquery.SchemaField('requester_responded_at', 'TIMESTAMP'),
                bigquery.SchemaField('first_responded_at', 'TIMESTAMP'),
                bigquery.SchemaField('status_updated_at', 'TIMESTAMP'),
                bigquery.SchemaField('reopened_at', 'TIMESTAMP'),
                bigquery.SchemaField('resolved_at', 'TIMESTAMP'),
                bigquery.SchemaField('closed_at', 'TIMESTAMP'),
                bigquery.SchemaField('pending_since', 'TIMESTAMP'),
            ),
        ),
        bigquery.SchemaField('internal_agent_id', 'INTEGER', description='Internal Agent Id'),
        bigquery.SchemaField('internal_group_id', 'INTEGER', description='Internal Group Id'),
        bigquery.SchemaField('nr_due_by', 'TIMESTAMP', description='nr Due by'),
        bigquery.SchemaField('nr_escalated', 'BOOLEAN', description='nr escalated'),
    ]

# Job config
# job_config = bigquery.LoadJobConfig(
#     source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
#     autodetect=False  # or set schema explicitly if you prefer
# )

job_config = bigquery.LoadJobConfig()
# job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE  # Loading after truncating
job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
job_config.schema = table_schema
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
job_config.ignore_unknown_values = True
job_config.max_bad_records = 10

# Load the file
with open(file_name, 'rb') as source_file:
    job = client.load_table_from_file(
        source_file,
        table_ref,
        job_config=job_config
    )

# Wait for the job to complete
job.result()

print(f"Loaded {job.output_rows} rows into {dataset_id}.{table_id}.")
