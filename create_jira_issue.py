# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import os
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

@app.route("/createjira", methods=["POST"])
def createjira():
    jira_username = os.environ.get("JIRA_USERNAME") 
    jira_api_token = os.environ.get("JIRA_API_TOKEN")

    url = "https://sukhijajatin.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth(jira_username, jira_api_token)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My Jira Tickets.",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10009"
        },
        "project": {
        "key": "KAN"
        },
        "summary": "My first issue",
    },
    "update": {}
    } )

    # Create the issue in Jira if comment contains "create issue"
    if "create issue" in payload:
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0', port=8080)