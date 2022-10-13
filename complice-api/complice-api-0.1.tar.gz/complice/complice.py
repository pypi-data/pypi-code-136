import requests
import re


class CompliceAPI:

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def _get(self, url):
        return requests.get(url, params={'auth_token': self.auth_token})

    def _post(self, url, data=None):
        return requests.post(url,
                             params={'auth_token': self.auth_token},
                             data=data)

    def get_userinfo(self):
        """Returns the user's name and username"""
        r = self._get('https://complice.co/api/v0/u/me/userinfo.json')
        return r.json()

    def get_goals(self):
        """Gets the user's list of goals, including each goal's current top priority"""
        r = self._get('https://complice.co/api/v0/u/me/goals/active.json')
        return r.json()

    def print_goals(self):
        """Prints the user's goals to the console"""
        response = self.get_goals()
        # for each item in [goals], print [name]
        print('Goals:')
        print('------')
        for goal in response['goals']:
            print(goal['name'])

    def get_today(self):
        """Returns most of the data used to render the user's today page"""
        r = self._get('https://complice.co/api/v0/u/me/today/full.json')
        return r.json()

    def get_timer(self):
        """Returns the user's current timer state"""
        r = self._get('https://complice.co/api/v0/u/me/today/timer/all')
        return r.json()

    def start_pomodoro(self, duration=None):
        """Starts a pomodoro timer"""
        url = 'https://complice.co/api/v0/u/me/today/timer/startpomodoro'
        if duration is not None:
            url += f'?duration={duration}'
        r = self._post(url)
        return r.json()

    def start_break(self, duration=None):
        """Starts a break timer"""
        url = 'https://complice.co/api/v0/u/me/today/timer/startbreak'
        if duration is not None:
            url += f'?duration={duration}'
        r = self._post(url)
        return r.json()

    def start_hourglass(self, duration=None):
        """Starts an hourglass timer"""
        url = 'https://complice.co/api/v0/u/me/today/timer/hourglass'
        if duration is not None:
            url += f'?duration={duration}'
        r = self._post(url)
        return r.json()

    def pause_timer(self):
        """Pauses the timer"""
        r = self._post('https://complice.co/api/v0/u/me/today/timer/pause')
        return r.json()

    def unpause_timer(self):
        """Unpauses the timer"""
        r = self._post('https://complice.co/api/v0/u/me/today/timer/unpause')
        return r.json()

    def _get_intentions(self, strip_goal_num=False):
        """Returns the user's intentions"""
        intentions = []
        for item in self.get_today()['core']['list']:
            if strip_goal_num:
                intentions.append(item['text'].split(' ', 1)[1])
            else:
                intentions.append(item['text'])

        return intentions

    def add_intention(self, intention):
        """Adds an intention to the user's list"""
        # if intention does not start with "<number>) ", print error
        if not re.match(r'^\d+\) ', intention):
            print(
                'Intention must start with a goal number and a closing parenthesis'
            )
            return
        url = 'https://complice.co/api/v0/u/me/intentions'
        # set parameters
        params = {'raw': intention}
        r = self._post(url, data=params)
        return r.json()
