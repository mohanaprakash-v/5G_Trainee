import requests

PHABRICATOR_API_URL = "https://phabricator.fifthgentech.com/api/maniphest.query"
API_TOKEN = "api-fy2ucwk5nsdaoagf3qizbqe3m4yb"

response = requests.get(PHABRICATOR_API_URL, params={'api.token': API_TOKEN})
data = response.json()
print(data)
