from instagrapi import Client

class FollowUtility:
    def __init__(self, session: Client):
        self.session = session

        self.enabled = False
        self.percentage = 0
        self.times = 1

    def set_enabled(self, enabled: bool):
        self.enabled = enabled

    def set_percentage(self, percentage: int):
        self.percentage = percentage

    def set_times(self, times: int):
        self.times = times

    def follow(self, user_id: str, username: str):
        try:
            followed = self.session.user_follow(user_id=user_id)
            print(f'[INFO]: Successfully followed user: {username}.' if followed else f'[ERROR]: Failed to follow user: {username}.')
            return followed
        except:
            print(f'[ERROR]: Failed to follow user: {username}.')
            return False
        
    def unfollow(self, user_id: str, username: str):
        try:
            unfollowed = self.session.user_unfollow(user_id=user_id)
            print(f'[INFO]: Successfully unfollowed user: {username}' if unfollowed else f'[ERROR]: Failed to unfollow user: {username}.')
            return unfollowed
        except:
            print(f'[ERROR]: Failed to unfollow user: {username}.')
            return False