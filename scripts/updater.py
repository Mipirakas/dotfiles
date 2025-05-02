import os
import subprocess
import github_releases_checker as grc

# File to store repos
repo_file = "repos.txt"
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, repo_file)

if __name__ == "__main__":
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                l = line.split()
                code = grc.check_for_new_release(l[0], l[1])
                if code == 0:
                    subprocess.run(['bash', l[2]])