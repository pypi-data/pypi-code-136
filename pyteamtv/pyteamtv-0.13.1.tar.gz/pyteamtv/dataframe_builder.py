from typing import List, Optional

from pyteamtv.models.observation_log import ObservationLog
from pyteamtv.models.person import Person
from pyteamtv.models.resource_group.team import TeamResourceGroup


class DataframeBuilder:
    def __init__(self, resource_group: TeamResourceGroup):
        # self.teams = {
        #     team.team_id: team for team in resource_group.get_teams()
        # }
        self.persons = {
            person.person_id: person for person in resource_group.get_persons()
        }

    def build_df(self, observation_logs: List[ObservationLog]):
        try:
            import pandas as pd
        except ImportError:
            raise Exception("You don't have pandas installed. Please install first")

        return pd.DataFrame.from_records(self.build_records(observation_logs))

    def _build_person_data(self,
                           attributes: dict,
                           key_prefix: Optional[str] = None):
        in_key = "person"
        out_prefix = ""
        if key_prefix:
            in_key = f"{key_prefix}Person"
            out_prefix = key_prefix + "_"

        pk_name = f"{in_key}Id"

        if in_key in attributes:
            person = {
                f"{out_prefix}person_id": attributes[pk_name],
                f"{out_prefix}first_name": attributes["person"]["firstName"],
                f"{out_prefix}last_name": attributes["person"]["lastName"],
                f"{out_prefix}number": attributes["person"]["number"],
                f"{out_prefix}full_name": attributes["person"]["firstName"] + " " + attributes["person"]["lastName"]
            }
        elif pk_name in attributes:
            person_: Optional[Person] = self.persons.get(attributes[pk_name])
            if person_:
                person = {
                    f"{out_prefix}person_id": attributes[pk_name],
                    f"{out_prefix}first_name": person_.first_name,
                    f"{out_prefix}last_name": person_.last_name,
                    f"{out_prefix}full_name": person_.name
                }
            else:
                person = dict()
        else:
            person = dict()
        return person

    def build_records(self, observation_logs: List[ObservationLog]):
        observations = []
        skip_attributes = {
            "teamId",
            "personId",
            "team",
            "person",
            "inPerson",
            "inPersonId",
            "outPerson",
            "outPersonId",
        }

        for observation_log in observation_logs:
            sporting_event = observation_log.sporting_event

            team = dict()
            for observation in observation_log:

                if observation.code in ("START-POSSESSION", "POSSESSION"):
                    if "team" in observation.attributes:
                        team_data = observation.attributes["team"]
                    else:
                        team_data = sporting_event.get_team(observation.attributes["teamId"])

                    team = dict(
                        team_id=observation.attributes["teamId"],
                        team_name=team_data["name"],
                        team_ground=team_data["ground"],
                        position=observation.attributes.get("position"),
                    )
                else:
                    person = self._build_person_data(observation.attributes)
                    opponent_person = self._build_person_data(observation.attributes, "opponent")

                    attributes = dict()
                    attributes.update(team)
                    attributes.update(person)
                    attributes.update(opponent_person)
                    for k, v in observation.attributes.items():
                        if k not in skip_attributes:
                            attributes[k] = v

                    if "angle" in attributes and "distance" in attributes:
                        attributes["x"], attributes["y"] = pol2cart(
                            attributes["angle"], attributes["distance"]
                        )

                    observation_dict = dict(
                        sporting_event_id=sporting_event.sporting_event_id,
                        sporting_event_name=sporting_event.name,
                        sporting_event_scheduled_at=sporting_event.scheduled_at,
                        observation_id=observation.observation_id,
                        clock_id=observation.clock_id,
                        start_time=observation.start_time,
                        end_time=observation.end_time,
                        code=observation.code,
                        description=observation.description,
                        **attributes
                    )

                    observations.append(observation_dict)

        return observations
