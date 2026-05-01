

import looker_sdk
from looker_sdk import models40 as mdls

sdk = looker_sdk.init40("C:/Dev/Looker/uuw1494.ini")      # replace with appropriate ini file
# response = sdk.all_git_branches(project_id="bi_prod")
response = sdk.search_dashboards(
    id="4650",
    fields="id, title, hidden, created_at, deleted_at")
print(response)