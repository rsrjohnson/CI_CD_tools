import json
import requests
import argparse

# Initialize the Parser
parser = argparse.ArgumentParser()

# Adding Arguments
parser.add_argument('--repo_owner', type= str)
parser.add_argument('--repo_slug', type= str)
parser.add_argument('--auth_token', type= str)
parser.add_argument('--source', type= str)
parser.add_argument('--destination', type= str)

args = parser.parse_args()

_REPO_OWNER = args.repo_owner
_REPO_SLUG = args.repo_slug
_AUTH_TOKEN = args.auth_token
SOURCE_BRANCH = args.source
DESTINATION_BRANCH = args.destination


url = f"https://api.github.com/repos/{_REPO_OWNER}/{_REPO_SLUG}/pulls"


headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {_AUTH_TOKEN}"
    }


payload = json.dumps(
    {
        "title": f"Auto PR from {SOURCE_BRANCH} to {DESTINATION_BRANCH}",
        "head": SOURCE_BRANCH,
        "base": DESTINATION_BRANCH
    }
)


