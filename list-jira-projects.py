# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import os
import requests
from requests.auth import HTTPBasicAuth
import json

jira_username = os.environ.get("JIRA_USERNAME") 
jira_api_token = os.environ.get("JIRA_API_TOKEN")

url = "https://sukhijajatin.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth(jira_username, jira_api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
project_names = [project["name"] for project in output]

for name in project_names:
      print(f"Project Name: {name}")
