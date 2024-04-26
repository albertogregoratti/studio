from google.cloud import bigquery

client = bigquery.Client()
dataset_id = 'my_dataset'
table_id = 'my_table'
gcs_uri = 'gs://my_bucket/my_file.csv'

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
)

load_job = client.load_table_from_uri(gcs_uri, f"{dataset_id}.{table_id}", job_config=job_config)
load_job.result()  # Wait for the job to complete
