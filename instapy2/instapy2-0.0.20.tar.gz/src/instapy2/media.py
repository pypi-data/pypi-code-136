from instagrapi.types import Media

from typing import List

class MediaUtil:
    def __init__(self):
        self.ignore_to_skip_if_contains = []
        self.required_hashtags = []
        self.to_skip = []

    def ignore(self, hashtags: List[str]): # ignore skip if caption contains any
        self.ignore_to_skip_if_contains = hashtags

    def require(self, hashtags: List[str]): # only like if all in caption
        self.required_hashtags = hashtags

    def skip(self, hashtags: List[str]): # don't like if any in caption, may still unfollow
        self.to_skip = hashtags

    def validated_for_interaction(self, media: Media) -> bool:
        if all(hashtag in media.caption_text for hashtag in self.required_hashtags):
            if any(hashtag in media.caption_text for hashtag in self.to_skip):
                return any(hashtag in media.caption_text for hashtag in self.ignore_to_skip_if_contains)
            else:
                return True
        else:
            return False