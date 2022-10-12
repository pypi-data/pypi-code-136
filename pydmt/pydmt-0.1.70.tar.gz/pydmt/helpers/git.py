import subprocess

git_last_tag = subprocess.check_output(
    ["git", "describe", "--abbrev=0", "--tags"], stderr=subprocess.DEVNULL
).decode().rstrip()
git_describe = subprocess.check_output(
    ["git", "describe"], stderr=subprocess.DEVNULL
).decode().rstrip()
git_version = ".".join(git_describe.split("-"))
