import requests

def get_mirrors():
    resp = requests.get("https://api.invidious.io/instances.json?pretty=1&sort_by=api")
    if resp.status_code != 200: return list()

    urls = list()
    for mirror in resp.json():
        if mirror[1]['api'] in [True, 'true']:
            url = f"https://{mirror[0]}"
            urls.append(url)
    return urls

HEADERS = ({
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
        "/75.0.3770.100 Safari/537.36"
    })

MIRRORS = get_mirrors()


