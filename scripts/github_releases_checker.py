import requests
import json
import os
import sys

# File to store last known release
last_releases_file = "last_releases.json"
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, last_releases_file)

def get_latest_release(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["tag_name"]
    else:
        print(f"Failed to fetch release info: {response.status_code}")
        return None

def load_last_releases():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return None

def save_last_releases(release):
    with open(file_path, "w") as file:
        json.dump(release, file, sort_keys = True)

def check_for_new_release(owner, repo):
    latest_release = get_latest_release(owner, repo)
    if not latest_release:
        return 2

    last_releases = load_last_releases()
    if not last_releases:
        last_releases = {}
    last_release = last_releases.get(f"{owner}/{repo}")
    
    if latest_release != last_release:
        print(f"New release detected: {owner}/{repo} {latest_release} from {last_release}")
        last_releases.update({f"{owner}/{repo}": latest_release})
        save_last_releases(last_releases)
        return 0
    else:
        print(f"No new release for {owner}/{repo}, current release is {last_release}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <owner> <repo>")
        sys.exit(1)

    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]

    code = check_for_new_release(repo_owner, repo_name)
    sys.exit(code)
