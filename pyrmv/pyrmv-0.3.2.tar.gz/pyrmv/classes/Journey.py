from pyrmv.classes.Stop import Stop
from pyrmv.classes.Message import Message

class Journey():
    """Journey object."""    

    def __init__(self, data: dict):
        self.stops = []
        self.ref = data["ref"]
        self.direction = data["Directions"]["Direction"][0]["value"]
        self.direction_flag = data["Directions"]["Direction"][0]["flag"]
        self.messages = []

        for stop in data["Stops"]["Stop"]:
            self.stops.append(Stop(stop))

        for message in data["Messages"]["Message"]:
            self.messages.append(Message(message))

    def __str__(self) -> str:
        return f"Journey with total of {len(self.stops)} stops and {len(self.messages)} messages heading {self.direction} ({self.direction_flag})"