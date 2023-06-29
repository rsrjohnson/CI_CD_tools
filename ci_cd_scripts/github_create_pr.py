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
SOURCE_BRANCH = "feature/auto_pr"
DESTINATION_BRANCH = args.destination


print(SOURCE_BRANCH)
print(DESTINATION_BRANCH)


url=f"https://api.github.com/repos/{REPO_SLUG}/pulls"

print(url)

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {AUTH_TOKEN}"
    }



# Check if the pull request already exists with the same source and target branches
params={
        'head': SOURCE_BRANCH,
        'base': DESTINATION_BRANCH
    }



response = requests.request(
    "POST",
    url,
    data=params,
    headers=headers
    )



# If a pull request already exists, print a message and exit
if response.ok:
    pull_requests = response.json()
    for pull_request in pull_requests:
        if pull_request['head']['ref'] == SOURCE_BRANCH and pull_request['base']['ref'] == DESTINATION_BRANCH:
            print('Pull request already exists with the same source and target branches.')
            pull_request_data = response.json()
            print(json.dumps(pull_request_data))
            
        else:

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

            if response.status_code == 201:
                pull_request_data = response.json()
                print(json.dumps(pull_request_data))
            else:
                print(f'Failed to create pull request: {response.text}')