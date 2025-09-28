import requests
from requests.auth import HTTPBasicAuth
from get_secrets import get_jira_config

def get_changelog():
    jira_config = get_jira_config()
    JIRA_DOMAIN = jira_config['jira_domain']
    ISSUE_KEY = jira_config['issue_key']
    EMAIL = jira_config['email']
    API_TOKEN = jira_config['api_token']

    url = f"https://{JIRA_DOMAIN}/rest/api/2/issue/{ISSUE_KEY}/changelog"

    response = requests.get(
        url,
        auth=HTTPBasicAuth(EMAIL, API_TOKEN),
        headers={"Accept": "application/json"}
    )

    if response.status_code == 200:
        changelog = response.json()
        return changelog
    else:
        print("Error:", response.status_code, response.text)
        return None