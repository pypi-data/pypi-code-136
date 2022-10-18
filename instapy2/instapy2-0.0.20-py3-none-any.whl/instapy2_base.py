from .configuration import Configuration

from instagrapi import Client
from instagrapi.types import Media

from typing import List, Tuple

import random, os

class InstaPy2Base:
    def __init__(self, username: str = None, password: str = None, delay_range: Tuple[float, float] = None):
        if username is None:
            print('[ERROR]: Username has not been set.')
            return

        if password is None:
            print('[ERROR]: Password has not been set.')
            return

        if delay_range is not None:
            min, max = delay_range
        else:
            min, max = (1, 5)

        self.session = Client(delay_range=[min, max])
        if os.path.exists(path=os.getcwd() + f'{os.path.sep}files{os.path.sep}settings.json'):
            self.session.load_settings(path=os.getcwd() + f'{os.path.sep}files{os.path.sep}settings.json')
            logged_in = self.session.login(username=username, password=password)
        else:
            logged_in = self.session.login(username=username, password=password)
            self.session.dump_settings(path=os.getcwd() + f'{os.path.sep}files{os.path.sep}settings.json')

        print(f'[INFO]: Successfully logged in as: {self.session.username}.' if logged_in else f'[ERROR]: Failed to log in.')
        self.configuration = Configuration(session=self.session)

    def medias_location(self, amount: int, location: int, randomize_media: bool, skip_top: bool) -> List[Media]:
        medias = []
        if skip_top:
            while len(medias) < amount:
                medias += [media for media in self.session.location_medias_recent(location_pk=location, amount=amount * 2) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]
        else:
            medias += [media for media in self.session.location_medias_top(location_pk=location) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]
            while len(medias) < amount:
                medias += [media for media in self.session.location_medias_recent(location_pk=location, amount=(amount * 2) - len(medias)) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]

        if randomize_media:
            random.shuffle(x=medias)

        return medias[:amount]

    def medias_tag(self, amount: int, tag: str, randomize_media: bool, skip_top: bool) -> List[Media]:
        medias = []
        if skip_top:
            while len(medias) < amount:
                medias += [media for media in self.session.hashtag_medias_recent(name=tag, amount=amount * 2) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]
        else:
            medias += [media for media in self.session.hashtag_medias_top(name=tag) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]
            while len(medias) < amount:
                medias += [media for media in self.session.hashtag_medias_recent(name=tag, amount=(amount * 2) - len(medias)) if not any(username in media.user.username for username in self.configuration.people.users_to_skip)]

        if randomize_media:
            random.shuffle(x=medias)

        return medias[:amount]
    
    def medias_username(self, amount: int, username: str, randomize_media: bool) -> List[Media]:
        medias = self.session.user_medias(user_id=self.session.user_id_from_username(username=username), amount=amount)
        if randomize_media:
            random.shuffle(x=medias)
        return medias[:amount]