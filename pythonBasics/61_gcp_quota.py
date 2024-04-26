from google.cloud import resourcemanager_v3


key_path = 'C:/Dev/bq/BI_Team-be18049eb10f.json'   # File containing GCP key
project_id = 'bi-team-189611'

client = resourcemanager_v3.ProjectsClient.from_service_account_file(key_path)
project = client.get_iam_policy(project_id)

#project_name = project.name()

print(project)