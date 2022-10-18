from instagrapi import Client
from instagrapi.types import Media

from typing import List

class PeopleHelper:
    def __init__(self, session: Client):
        self.session = session
        
        self.friends_to_skip = []
        self.users_to_skip = []

    def skip_friends(self, usernames: List[str]):
        """
            Sets which users to skip when unfollowing. Commenting and liking will still occur.

            :param usernames: usernames=['friend 1', 'friend 2', 'friend 3']
        """
        self.friends_to_skip = usernames

    def skip_users(self, usernames: List[str]):
        """
            Sets which users to skip entirely. Commenting, following and liking will not occur.

            :param usernames: usernames=['username 1', 'username 2', 'username 3']
        """
        self.users_to_skip = usernames

    def following_user(self, media: Media) -> bool:
        user_id = self.session.user_id_from_username(username=media.user.username)
        relationship_status = self.session.user_friendship_v1(user_id=user_id)
        return relationship_status.following