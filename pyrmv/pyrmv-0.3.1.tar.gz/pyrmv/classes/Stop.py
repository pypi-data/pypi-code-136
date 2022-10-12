from datetime import datetime


class Stop():
    """Stop object."""    
    
    def __init__(self, data: dict):

        self.name = data["name"]
        self.id = data["id"]

        if "extId" in data:
            self.ext_id = data["extId"]
        else:
            self.ext_id = None

        if "description" in data:
            self.description = data["description"]
        else:
            self.description = None

        self.lon = data["lon"]
        self.lat = data["lat"]

        if "routeIdx" in data:
            self.route_index = data["routeIdx"]
        else:
            self.route_index = None

        if "arrTrack" in data:
            self.track_arrival = data["arrTrack"]
        else:
            self.track_arrival = None

        if "depTrack" in data:
            self.track_departure = data["depTrack"]
        else:
            self.track_departure = None

    def __str__(self) -> str:
        return f"Stop {self.name} at {self.lon}, {self.lat}"

class StopTrip(Stop):
    """Trip stop object. It's like a Stop object, but with a date and time."""    

    def __init__(self, data: dict):
        
        self.type = data["type"]
        self.date = datetime.strptime(data["date"], "%Y-%m-%d")
        self.time = datetime.strptime(data["time"], "%H:%M:%S")
        super().__init__(data)

    def __str__(self) -> str:
        return f"Stop {self.name} at {self.lon}, {self.lat} at {self.time.time()} {self.date.date()}"