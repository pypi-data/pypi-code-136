from dataclasses import asdict
import json


def get_posts_as_dict(posts_data):
    """Turns list of Post object into list of dict objects."""
    return [asdict(post) for post in posts_data]


def print_posts_data(posts_data):
    """Prints posts data in a pleasant json format."""
    posts = get_posts_as_dict(posts_data)
    json_posts = json.dumps(posts, indent=4, ensure_ascii=False)
    print(json_posts)
    return json_posts
