import os
import subprocess
from datetime import datetime, timedelta

repo = r"D:\PYTHON"

folders = sorted([f for f in os.listdir(repo) if os.path.isdir(os.path.join(repo, f))])

start = datetime(2026, 2, 11)

for folder in folders[:24]:
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = start.strftime("%Y-%m-%d 10:00:00")
    env["GIT_COMMITTER_DATE"] = start.strftime("%Y-%m-%d 10:00:00")

    subprocess.run(["git", "add", folder], cwd=repo)
    subprocess.run(["git", "commit", "-m", f"Added {folder}"], cwd=repo, env=env)

    start += timedelta(days=1)

subprocess.run(["git", "push", "origin", "main"], cwd=repo)