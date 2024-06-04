import json
import requests
import argparse
import os

# Initialize the Parser
parser = argparse.ArgumentParser()

# Adding Arguments

parser.add_argument('--repo_slug', type= str)
parser.add_argument('--pr_numb', type= str)
parser.add_argument('--auth_token', type= str)


args = parser.parse_args()

REPO_SLUG = args.repo_slug
PR_NUMB = args.pr_numb
AUTH_TOKEN = args.auth_token

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"token {AUTH_TOKEN}"
    }


def mergePullRequest(url):

    params = {
        "commit_title": f"Merge PR",
        "commit_message": f"Merge pull request number {PR_NUMB}",
        "pull_number": PR_NUMB
    }

    response = requests.request(
        "PUT",
        url=url,
        headers=headers,
        data=json.dumps(params)
    )

    if response.status_code==200:
        print("PR merged successfully.")

        # pr_number = response.json()["number"]

        # print(json.dumps(response.json(),indent=4))

    else:
        raise(Exception(response.text))


api_url = f"https://api.github.com/repos/{REPO_SLUG}/"

api_action = "pulls/"

url = api_url + api_action + PR_NUMB + "/merge"

mergePullRequest(url)