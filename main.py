"""
Here is the genius program behind this repository
"""
import requests
import time
import random
from github import Github


token = ""

gh = Github(token)

headers = {"Accept": "application/vnd.github.v3+json", "Authorization": f"token {token}"}

while True:
  repos = requests.get("https://api.github.com/users/PiggyAwesome/repos?per_page=100", headers=headers)
  for thingy in repos.json():
    if "updator" in thingy["name"].lower():
    repo = gh.search_repositories(thingy['name'])[0]
    repo.update_file("README.md", random.choice(messages), random.choice(messages), sha=sha)
    # print("Updated")
    time.sleep(86400)
