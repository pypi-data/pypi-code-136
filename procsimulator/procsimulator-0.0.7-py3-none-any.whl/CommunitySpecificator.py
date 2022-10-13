import json

"""
Fill json configuration house
(In the future should be replaced with a graphical user interface)
"""

class CommunitySpecificator:


  def __init__(self, configuration_file):
    """
    This class creates the json configuration file

    Args:
      configuration_file: path of the JSON community configuration file
    """
    self.configuration_file = configuration_file



  def execute(self):
    """
    Creates a json file with the configuration file (houses, people of each house, appliances, schedules and activities)
    """
    self.num_houses = 5
    self.community = []
    self.people = ["Ann", "Billy"]
    self.appliances = ["Fridge", "Vaccuum cleaner", "Washing machine", "Drying machine"]
    self.schedules = []
    self.activities = [
      {
        "activity": "activity_tv",
        "model": "LEISURE/watch_tv.conf",
        "daily_runs": 2,
        "schedule": [
          {
            "day": "monday",
            "schedule": ["16:00-23:30"]
          },
          {
            "day": "tuesday",
            "schedule": ["16:00-23:30"]
          },
          {
            "day": "wednesday",
            "schedule": ["16:00-23:30"]
          },
          {
            "day": "thursday",
            "schedule": ["15:00-22:30"]
          },
          {
            "day": "friday",
            "schedule": ["15:00-18:00"]
          },
          {
            "day": "saturday",
            "schedule": ["13:00-24:00"]
          },
          {
            "day": "sunday",
            "schedule": ["09:00-23:30"]
          }
        ]
      },
      {
        "activity": "activity_computer",
        "model": "LEISURE/use_pc.conf",
        "daily_runs": 2,
        "schedule": [
          {
            "day": "monday",
            "schedule": ["17:00-24:00"]
          },
          {
            "day": "tuesday",
            "schedule": ["18:00-23:00"]
          },
          {
            "day": "wednesday",
            "schedule": ["20:00-23:00"]
          },
          {
            "day": "thursday",
            "schedule": ["15:00-22:00"]
          },
          {
            "day": "friday",
            "schedule": ["15:00-19:00"]
          },
          {
            "day": "saturday",
            "schedule": ["13:00-22:00"]
          },
          {
            "day": "sunday",
            "schedule": ["09:00-23:30"]
          }
        ]
      },
      {
        "activity": "activity_music",
        "model": "LEISURE/listen_music.conf",
        "daily_runs": 0.8,
        "schedule": [
          {
            "day": "monday",
            "schedule": ["20:00-24:00"]
          },
          {
            "day": "tuesday",
            "schedule": ["18:00-23:00"]
          },
          {
            "day": "wednesday",
            "schedule": ["20:00-23:00"]
          },
          {
            "day": "thursday",
            "schedule": ["15:00-22:00"]
          },
          {
            "day": "friday",
            "schedule": ["15:00-19:00"]
          },
          {
            "day": "saturday",
            "schedule": ["13:00-22:00"]
          },
          {
            "day": "sunday",
            "schedule": ["09:00-23:30"]
          }
        ]
      },
      {
        "activity": "activity_breakfast",
        "model": "KITCHEN/preparing_breakfast.conf",
        "daily_runs": 1,
        "schedule": [
          {
            "day": "monday",
            "schedule": ["07:30-08:15"]
          },
          {
            "day": "tuesday",
            "schedule": ["07:30-08:15"]
          },
          {
            "day": "wednesday",
            "schedule": ["07:30-08:15"]
          },
          {
            "day": "thursday",
            "schedule": ["07:30-08:15"]
          },
          {
            "day": "friday",
            "schedule": ["07:30-08:15"]
          },
          {
            "day": "saturday",
            "schedule": ["07:30-08:15"]
          },
          {
            "day": "sunday",
            "schedule": ["08:30-09:15"]
          }
        ]
      },
      {
        "activity": "activity_lunch",
        "model": "KITCHEN/heating_lunch.conf",
        "daily_runs": 1,
        "schedule": [
          {
            "day": "saturday",
            "schedule": ["11:30-12:15"]
          },
          {
            "day": "sunday",
            "schedule": ["12:00-13:15"]
          }
        ]
      },
      {
        "activity": "activity_dinner",
        "model": "KITCHEN/preparing_dinner.conf",
        "daily_runs": 1,
        "schedule": [
          {
            "day": "monday",
            "schedule": ["18:30-19:15"]
          },
          {
            "day": "tuesday",
            "schedule": ["18:30-19:15"]
          },
          {
            "day": "wednesday",
            "schedule": ["18:30-19:15"]
          },
          {
            "day": "thursday",
            "schedule": ["18:30-19:15"]
          },
          {
            "day": "friday",
            "schedule": ["18:30-19:15"]
          },
          {
            "day": "saturday",
            "schedule": ["18:30-19:15"]
          },
          {
            "day": "sunday",
            "schedule": ["18:30-20:15"]
          }
        ]
      },
      {
        "activity": "activity_vacuum",
        "model": "HOUSEHOLD/vacuum.conf",
        "daily_runs": 0.7,
        "schedule": [
          {
            "day": "monday",
            "schedule": ["11:00-18:00"]
          },
          {
            "day": "tuesday",
            "schedule": ["11:00-18:00"]
          },
          {
            "day": "wednesday",
            "schedule": ["11:00-18:00"]
          },
          {
            "day": "thursday",
            "schedule": ["11:00-18:00"]
          },
          {
            "day": "friday",
            "schedule": ["18:30-19:15"]
          },
          {
            "day": "saturday",
            "schedule": ["11:00-14:00"]
          },
          {
            "day": "sunday",
            "schedule": ["11:00-14:00"]
          }
        ]
      },
      {
        "activity": "activity_laundry",
        "model": "HOUSEHOLD/wash_laundry.conf",
        "daily_runs": 0.3,
        "schedule": [
          {
            "day": "monday",
            "schedule": ["07:00-12:00", "17:00-23:00"]
          },
          {
            "day": "tuesday",
            "schedule": ["07:00-12:00", "18:00-22:00"]
          },
          {
            "day": "wednesday",
            "schedule": ["07:00-12:00"]
          },
          {
            "day": "thursday",
            "schedule": ["07:00-12:00,17:00-23:00"]
          },
          {
            "day": "saturday",
            "schedule": ["09:00-22:00"]
          },
          {
            "day": "sunday",
            "schedule": ["09:00-22:00"]
          }
        ]
      },
      {
        "activity": "activity_dishwashing",
        "model": "KITCHEN/dishwasher.conf",
        "daily_runs": 0.3,
        "schedule": [
          {
            "day": "monday",
            "schedule": ["18:00-22:00"]
          },
          {
            "day": "tuesday",
            "schedule": ["07:00-12:00", "17:00-22:00"]
          },
          {
            "day": "wednesday",
            "schedule": ["07:00-14:00"]
          },
          {
            "day": "thursday",
            "schedule": ["07:00-12:00", "17:00-22:00"]
          },
          {
            "day": "saturday",
            "schedule": ["09:00-22:00"]
          },
          {
            "day": "sunday",
            "schedule": ["09:00-20:00"]
          }
        ]
      }
    ]

    for x in range(len(self.people)):
      self.schedules.append({
        "presence": [
          {
            "day": "monday",
            "schedule": [
              "00:00-08:30",
              "14:00-24:00"
            ]
          },
          {
            "day": "tuesday",
            "schedule": [
              "00:00-08:30",
              "14:00-24:00"
            ]
          },
          {
            "day": "wednesday",
            "schedule": [
              "00:00-08:30",
              "14:00-24:00"
            ]
          },
          {
            "day": "thursday",
            "schedule": [
              "00:00-08:30",
              "14:00-24:00"
            ]
          },
          {
            "day": "friday",
            "schedule": [
              "00:00-08:30",
              "14:00-24:00"
            ]
          },
          {
            "day": "saturday",
            "schedule": [
              "00:00-08:30",
              "14:00-24:00"
            ]
          },
          {
            "day": "sunday",
            "schedule": [
              "00:00-24:00"
            ]
          }
        ],
        "activities": self.activities,
      })

    house = {
      "house": "John House",
      "num_people": 2,
      "contracted_power": 7.4,
      "people": self.people,
      "appliances": self.appliances,
      "schedules": self.schedules
    }

    for x in range(1, self.num_houses):
      self.community.append(house)

    print(json.dumps(self.community))

    with open(self.configuration_file, 'w') as outfile:
      json.dump(self.community, outfile)


if __name__ == '__main__':

  cs = CommunitySpecificator("../data.json")
  cs.execute();

