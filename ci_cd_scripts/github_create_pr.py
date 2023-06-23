import json
import requests
import argparse

# Initialize the Parser
parser = argparse.ArgumentParser()

# Adding Arguments
parser.add_argument('--repo_slug', type= str)
parser.add_argument('--auth_token', type= str)
parser.add_argument('--source', type= str)
parser.add_argument('--destination', type= str)

args = parser.parse_args()

REPO_SLUG = args.repo_slug
AUTH_TOKEN = args.auth_token
SOURCE_BRANCH = args.source
DESTINATION_BRANCH = args.destination


print(SOURCE_BRANCH)
print(DESTINATION_BRANCH)


url=f"https://api.github.com/repos/{REPO_SLUG}/pulls"

print(url)

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {AUTH_TOKEN}"
    }


payload = json.dumps(
    {
        "title": f"Auto PR from {SOURCE_BRANCH} to {DESTINATION_BRANCH}",
        "head": SOURCE_BRANCH,
        "base": DESTINATION_BRANCH
    }
)

response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers
    )

print(response.status_code)