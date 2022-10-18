import pandas as pd
from .metadata import (_eventtypesdf,
                      _get_end_x, _get_end_y,
                      _get_shot, _get_goal,
                      _get_body_part, _get_xg,
                      _get_xgot, _get_pattern_of_play)

def transform_events(event_data: dict) -> pd.DataFrame:
    """Generate event dataframe from StatsPerform json event data

    Args:
        event_data (dict): StatsPerform .json events

    Returns:
        pd.DataFrame: StatsPerform event dataframe
    """
    match_info = event_data["matchInfo"]
    game_id = match_info["id"]
    description = match_info["description"]

    events = {}
    for element in event_data["liveData"]["event"]:
        timestamp = element.get("timeStamp")
        qualifiers = {
            int(q["qualifierId"]): q.get("value") for q in element.get("qualifier", [])
        }

        start_x = element.get("x")
        start_y = element.get("y")
        end_x = _get_end_x(qualifiers) or start_x
        end_y = _get_end_y(qualifiers) or start_y
        
        shot = _get_shot(qualifiers)
        goal = _get_goal(qualifiers)
        
        event_id = int(element.get("id"))
        
        event = dict(
            game_id =  game_id,
            event_id = event_id,
            type_id = element.get("typeId"),
            team_id = element.get("contestantId"),
            player_id = element.get("playerId"),
            player_name = element.get("playerName"),
            timestamp = timestamp,
            period_id = element.get("periodId"),
            minute = element.get("timeMin"),
            second = element.get("timeSec"),
            start_x = start_x,
            start_y = start_y,
            end_x = end_x,
            end_y = end_y,
            shot = shot,
            goal = goal,
            outcome = element.get("outcome"),
            qualifiers = qualifiers
        )
        events[(game_id, event_id)] = event

    df_events = (
        pd.DataFrame(list(events.values()))
        .merge(_eventtypesdf, on="type_id", how="left")
        .sort_values(["game_id", "period_id", "minute", "second", "timestamp"])
        .reset_index(drop=True)
    )
    return df_events

def transform_expected_goals(xg_data: dict) -> pd.DataFrame:
    """Generate expected goals dataframe from StatsPerform json expected goals data

    Args:
        xg_data (dict): StatsPerform .json events

    Returns:
        pd.DataFrame: StatsPerform event dataframe
    """
    match_info = xg_data["matchInfo"]
    game_id = match_info["id"]
    description = match_info["description"]

    events = {}
    for element in xg_data["liveData"]["event"]:
        timestamp = element.get("timeStamp")
        qualifiers = {
            int(q["qualifierId"]): q.get("value") for q in element.get("qualifier", [])
        }
        xg = _get_xg(qualifiers)
        xgot = _get_xgot(qualifiers)
        pattern_of_play = _get_pattern_of_play(qualifiers)
        
        start_x = element.get("x")
        start_y = element.get("y")
        end_x = _get_end_x(qualifiers)
        end_y = _get_end_y(qualifiers)
        
        shot = _get_shot(qualifiers)
        goal = _get_goal(qualifiers)
        
        event_id = int(element.get("id"))
        
        body_part = _get_body_part(qualifiers)
        
        event = dict(
            game_id =  game_id,
            event_id = event_id,
            type_id = element.get("typeId"),
            team_id = element.get("contestantId"),
            player_id = element.get("playerId"),
            player_name = element.get("playerName"),
            timestamp = timestamp,
            period_id = element.get("periodId"),
            minute = element.get("timeMin"),
            second = element.get("timeSec"),
            start_x = start_x,
            start_y = start_y,
            end_x = end_x,
            end_y = end_y,
            shot = shot,
            goal = goal,
            body_part = body_part,
            pattern_of_play = pattern_of_play,
            xg = xg,
            xgot = xgot,
            outcome = element.get("outcome"),
            qualifiers = qualifiers
        )
        events[(game_id, event_id)] = event

    df_events = (
        pd.DataFrame(list(events.values()))
        .merge(_eventtypesdf, on="type_id", how="left")
        .sort_values(["game_id", "period_id", "minute", "second", "timestamp"])
        .reset_index(drop=True)
    )
    return df_events

def transform_lineups(match_metadata: dict) -> pd.DataFrame:
    """Generate lineups dataframe from StatsPerform json match metadata

    Args:
        match_metadata (dict): StatsPerform .json match metadata

    Returns:
        pd.DataFrame: StatsPerform event dataframe
    """
    match_data = match_metadata["match"][0]
    match_live_data = match_data["liveData"]
    match_info = match_data["matchInfo"]
    
    game_id = match_info["id"]
    game_date = match_info["date"]
    match_description = match_info["description"]
    
    # get substitutions
    # match_substitutions = match_live_data["substitute"]
    
    match_lineups = match_live_data["lineUp"]
    
    lineups = {}
    for team_lineup in match_lineups:
        team_id = team_lineup["contestantId"]
        for player in team_lineup["player"]:
            player_id = player["playerId"]
            first_name = player["firstName"]
            last_name = player["lastName"]
            match_name = player["matchName"]
            number = player["shirtNumber"]
            position = player["position"]
    
            lineup = dict(
                game_id = game_id,
                game_date = game_date,
                team_id = team_id,
                player_id = player_id,
                first_name = first_name,
                last_name = last_name,
                match_name = match_name,
                number = number,
                position = position
            )
            lineups[(game_id, player_id)] = lineup
            
    df_lineups = (
        pd.DataFrame(list(lineups.values()))
        .sort_values(["game_id", "game_date", "match_name", "position"])
        .reset_index(drop=True)
        )
    return df_lineups

def transform_possession(possession_data: dict) -> pd.DataFrame:
    """Generate lineups dataframe from StatsPerform json match metadata

    Args:
        possession_data (dict): StatsPerform .json match metadata

    Returns:
        pd.DataFrame: StatsPerform event dataframe
    """
    match_info = possession_data["matchInfo"]
    game_id = match_info["id"]
    description = match_info["description"]

    events = {}
    for element in possession_data["liveData"]["event"]:
        timestamp = element.get("timeStamp")
        qualifiers = {
            int(q["qualifierId"]): q.get("value") for q in element.get("qualifier", [])
        }
        
        start_x = element.get("x")
        start_y = element.get("y")
        end_x = _get_end_x(qualifiers) or start_x
        end_y = _get_end_y(qualifiers) or start_y
        
        shot = _get_shot(qualifiers)
        goal = _get_goal(qualifiers)
        
        sequenceId = element.get("sequenceId")
        possessionId = element.get("possessionId")
        
        event_id = int(element.get("id"))
        
        event = dict(
            game_id =  game_id,
            event_id = event_id,
            type_id = element.get("typeId"),
            team_id = element.get("contestantId"),
            player_id = element.get("playerId"),
            player_name = element.get("playerName"),
            timestamp = timestamp,
            period_id = element.get("periodId"),
            minute = element.get("timeMin"),
            second = element.get("timeSec"),
            start_x = start_x,
            start_y = start_y,
            end_x = end_x,
            end_y = end_y,
            shot = shot,
            goal = goal,
            outcome = element.get("outcome"),
            sequenceId = sequenceId,
            possessionId = possessionId,
            qualifiers = qualifiers
        )
        events[(game_id, event_id)] = event

    df_poss = (
        pd.DataFrame(list(events.values()))
        .merge(_eventtypesdf, on="type_id", how="left")
        .sort_values(["game_id", "period_id", "minute", "second", "timestamp"])
        .reset_index(drop=True)
    )
    return df_poss

def transform_calendar(calendar: dict) -> pd.DataFrame:
    """Generate calendar dataframe from StatsPerform json calendar

    Args:
        calendar (dict): StatsPerform calendar

    Returns:
        pd.DataFrame: StatsPerform calendar dataframe
    """
    df_calendar = pd.json_normalize(calendar["competition"],
                                    record_path=["tournamentCalendar"],
                                    meta_prefix="_",
                                    meta=["id", "ocId", "opId",
                                          "competitionCode", "country",
                                          "countryId", "competitionFormat",
                                          "type", "competitionType"])
    return df_calendar

def transform_schedule(schedule: dict) -> pd.DataFrame:
    """Generate calendar dataframe from StatsPerform json calendar

    Args:
        schedule (dict): StatsPerform schedule json

    Returns:
        pd.DataFrame: StatsPerform calendar dataframe
    """
    competition_info = schedule["competition"]
    tournament_info = schedule["tournamentCalendar"]
    competition_id = competition_info["id"]
    competition_name = competition_info["name"]
    tournament_id = tournament_info["id"]
    tournament_name = tournament_info["name"]
    tournament_start_date = tournament_info["startDate"]
    tournament_end_date = tournament_info["endDate"]

    games = {}
    for match_date in schedule["matchDate"]:
        for match in match_date["match"]:
            
            game_id = match["id"]
            game_date = match["date"]
            game_time = match["localTime"]
            
            match_dict = dict(
                competition_id = competition_id,
                competition_name = competition_name,
                tournament_id = tournament_id,
                tournament_name = tournament_name,
                tournament_start_date = tournament_start_date,
                tournament_end_date = tournament_end_date,
                game_id = game_id,
                game_date = game_date,
                game_time = game_time,
                home_team_id = match["homeContestantId"],
                away_team_id = match["awayContestantId"],
                home_team_name = match["homeContestantName"],
                away_team_name = match["awayContestantName"],
                home_official_name = match["homeContestantOfficialName"],
                away_official_name = match["awayContestantOfficialName"],
                home_team_short_name = match["homeContestantShortName"],
                away_team_short_name = match["awayContestantShortName"]
            )
            games[(tournament_id, game_id)] = match_dict
    df_schedule = (
        pd.DataFrame(list(games.values()))
        .sort_values(["game_id", "game_date", "game_time"])
        .reset_index(drop=True)
    )
    return df_schedule