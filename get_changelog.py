import requests
from requests.auth import HTTPBasicAuth

JIRA_DOMAIN = "your-domain.atlassian.net"
ISSUE_KEY = "ABC-123"
EMAIL = "your@email.com"
API_TOKEN = "your_api_token"

url = f"https://{JIRA_DOMAIN}/rest/api/2/issue/{ISSUE_KEY}/changelog"

response = requests.get(
    url,
    auth=HTTPBasicAuth(EMAIL, API_TOKEN),
    headers={"Accept": "application/json"}
)

if response.status_code == 200:
    changelog = response.json()
    print(changelog)
else:
    print("Error:", response.status_code, response.text)