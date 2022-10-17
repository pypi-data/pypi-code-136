import os
import requests


def Query(operation_name, operation_doc, variables):

    if os.environ.get("MATCHMAKER_INSECURE_USE_HTTP"):
        url = "http://{}/v1/graphql".format(os.environ.get("MATCHMAKER_HASURA_URL"))
    else:
        url = "https://{}/v1/graphql".format(os.environ.get("MATCHMAKER_HASURA_URL"))
    data = {
        "query": str(operation_doc),
        "variables": variables,
        "operationName": operation_name,
    }

    headers = {
        "X-Hasura-Admin-Secret": os.environ.get("MATCHMAKER_HASURA_ADMIN_SECRET")
    }

    r = requests.post(url, json=data, headers=headers)

    return r.json()


def getMatchHistory(tourney_id):

    operation_name = "getMatchHistory"
    vars = {"tournament_id": str(tourney_id)}
    get_match_history_doc = """
        query getMatchHistory($tournament_id: uuid = "") {
            Match(where: {tournament_id: {_eq: $tournament_id}}) {
                Players {
                    player_id
                }
                round
            }
            Tournament(where: {id: {_eq: $tournament_id}}) {
                Ladder {
                    id
                    tournament_points
                    mov
                    sos
                }
            }
        }
    """

    match_history = Query(operation_name, get_match_history_doc, vars)

    return match_history


def createMatches(tourney_id, round, count):

    operation_name = "CreateMatches"
    matches_list = [{"tournament_id": tourney_id, "round": round} for _ in range(count)]
    vars = {"matches": matches_list}
    create_matches_doc = """
        mutation CreateMatches($matches: [Match_insert_input!] !) {
            insert_Match(objects: $matches) {
                returning {
                    id
                }
            }
        }
    """

    new_matches = Query(operation_name, create_matches_doc, vars)

    return new_matches


def createMatchPlayer(player, match_id):

    operation_name = "CreateMatchPlayer"
    vars = {"player_id": player, "match_id": match_id}
    create_matches_doc = """
        mutation CreateMatchPlayer($player_id: uuid = "", $match_id: uuid = "") {
        insert_MatchPlayer(
            objects: {
                player_id: $player_id,
                match_id: $match_id,
                points: 0,
                tournament_points: 0
            }) {
                affected_rows
            }
        }
    """

    success = Query(operation_name, create_matches_doc, vars)

    return success
