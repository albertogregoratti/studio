from google.cloud import bigquery
from google.cloud import resource_manager
from google.oauth2.service_account import Credentials
import subprocess

#################################################
## Settings
#################################################
# Create a BigQuery client
# key_path = 'C:/Dev/bq/BI_Team-be18049eb10f.json'  # File containing GCS credentials (service account, project, key)
# bq_client_ref = resource_manager.Client.from_service_account_json(key_path)
# base_credentials = Credentials.from_service_account_file(key_path)
# log_table = 'bi-team-189611.TR_aftership_raw.log'
#
# project_id = 'bi-team-189611'
# table_id = 'bi-team-189611.orders.bq_quota'

def run_gcloud_command(command):
    try:
        # Execute the gcloud command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        # Capture the output and error (if any)
        stdout, stderr = process.communicate()

        # Check if there's any error
        if process.returncode != 0:
            print("Error occurred:")
            print(stderr.decode('utf-8'))  # Decode bytes to string for printing
        else:
            print("Command executed successfully:")
            print(stdout.decode('utf-8'))  # Decode bytes to string for printing
    except Exception as e:
        print("Exception occurred:", str(e))


# Example usage
gcloud_command = '''gcloud alpha services quota list  \
   --service=bigquery.googleapis.com \
   --consumer=projects/bi-team-189611 \
   --filter="metric:usage" \
   --format=json'''

run_gcloud_command(gcloud_command)

