import base64
import json
import logging
import os
from pathlib import Path

import requests
from pretalx.celery_app import app

dotenv_path = Path(__file__).parent

logger = logging.getLogger("Swarm-plugin-logger")

try:
    load_dotenv()
except Exception as e:
    logger.warning(
        "Problems loading .env file. Please check the structure and location of the file! See README for more."
    )

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_EMAIL = os.getenv("GITHUB_EMAIL")

repo = "datafund/web_devconagenda"
filename = "democon.zip"
url = "https://api.github.com/repos/{}/contents/{}".format(repo, filename)
token = "Bearer {}".format(GITHUB_TOKEN)
headers = {"Accept": "application/vnd.github+json", "Authorization": token}


@app.task
def post_to_swarm(zip_path):
    try:

        resp2 = requests.get(url, headers=headers)
        sha = json.loads(resp2.text)["sha"]

        with open(zip_path, "rb") as f:
            file = f.read()

        encoded = base64.b64encode(file)
        data = {
            "message": "upload agenda zip",
            "committer": {"name": GITHUB_USERNAME, "email": GITHUB_EMAIL},
            "content": encoded.decode(),
            "sha": sha,
            "branch": "main",
        }
        resp3 = requests.put(url, headers=headers, data=json.dumps(data))
        logger.info("Agenda succesfully exported to Swarm!")

    except Exception as e:
        logger.warning(str(e))

