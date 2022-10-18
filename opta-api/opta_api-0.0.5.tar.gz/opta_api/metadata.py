import pandas as pd

# StatsPerform Event Mapping
_eventtypesdf = pd.DataFrame(
    [
        (1, "pass"),
        (2, "offside pass"),
        (3, "take on"),
        (4, "foul"),
        (5, "out"),
        (6, "corner awarded"),
        (7, "tackle"),
        (8, "interception"),
        (9, "turnover"),
        (10, "save"),
        (11, "claim"),
        (12, "clearance"),
        (13, "miss"),
        (14, "post"),
        (15, "attempt saved"),
        (16, "goal"),
        (17, "card"),
        (18, "player off"),
        (19, "player on"),
        (20, "player retired"),
        (21, "player returns"),
        (22, "player becomes goalkeeper"),
        (23, "goalkeeper becomes player"),
        (24, "condition change"),
        (25, "official change"),
        (26, "unknown26"),
        (27, "start delay"),
        (28, "end delay"),
        (29, "unknown29"),
        (30, "end"),
        (31, "unknown31"),
        (32, "start"),
        (33, "unknown33"),
        (34, "team set up"),
        (35, "player changed position"),
        (36, "player changed jersey number"),
        (37, "collection end"),
        (38, "temp_goal"),
        (39, "temp_attempt"),
        (40, "formation change"),
        (41, "punch"),
        (42, "good skill"),
        (43, "deleted event"),
        (44, "aerial"),
        (45, "challenge"),
        (46, "unknown46"),
        (47, "rescinded card"),
        (48, "unknown46"),
        (49, "ball recovery"),
        (50, "dispossessed"),
        (51, "error"),
        (52, "keeper pick-up"),
        (53, "cross not claimed"),
        (54, "smother"),
        (55, "offside provoked"),
        (56, "shield ball opp"),
        (57, "foul throw in"),
        (58, "penalty faced"),
        (59, "keeper sweeper"),
        (60, "chance missed"),
        (61, "ball touch"),
        (62, "unknown62"),
        (63, "temp_save"),
        (64, "resume"),
        (65, "contentious referee decision"),
        (66, "possession data"),
        (67, "50/50"),
        (68, "referee drop ball"),
        (69, "failed to block"),
        (70, "injury time announcement"),
        (71, "coach setup"),
        (72, "caught offside"),
        (73, "other ball contact"),
        (74, "blocked pass"),
        (75, "delayed start"),
        (76, "early end"),
        (77, "player off pitch"),
        (78, "temp card"),
        (79, "coverage interruption"),
        (80, "drop of ball"),
        (81, "obstacle"),
        (83, "attempted tackle"),
        (84, "deleted after review"),
        (10000, "offside given"),  # Seems specific to WhoScored
    ],
    columns=["type_id", "type_name"],
)

# Load functions
def _get_end_x(qualifiers):
    try:
        # pass
        if 140 in qualifiers:
            return float(qualifiers[140])
        # blocked shot
        if 146 in qualifiers:
            return float(qualifiers[146])
        # passed the goal line
        if 102 in qualifiers:
            return float(100)
        return None
    except ValueError:
        return None

def _get_end_y(qualifiers):
    try:
        # pass
        if 141 in qualifiers:
            return float(qualifiers[141])
        # blocked shot
        if 147 in qualifiers:
            return float(qualifiers[147])
        # passed the goal line
        if 102 in qualifiers:
            return float(qualifiers[102])
        return None
    except ValueError:
        return None

def _get_xg(qualifiers):
    try:
        if 321 in qualifiers:
            return float(qualifiers[321])
    except ValueError:
        return 0        

def _get_xgot(qualifiers):
    try:
        if 322 in qualifiers:
            return float(qualifiers[322])
        return 0
    except ValueError:
        return 0

def _get_body_part(qualifiers):
    try:
        if 15 in qualifiers:
            return "head"
        if 20 in qualifiers:
            return "right foot"
        if 21 in qualifiers:
            return "other"
        if 72 in qualifiers:
            return "left foot"
    except ValueError:
        return "other"

def _get_pattern_of_play(qualifiers):
    try:
        if 23 in qualifiers:
            return "fast break"
        if 24 in qualifiers:
            return "free kick"
        if 25 in qualifiers:
            return "corner"
        if 26 in qualifiers:
            return "direct free kick"
        return "other"
    except ValueError:
        return "other"

def _get_shot(qualifiers):
    try:
        if 13 in qualifiers:
            return True
        if 14 in qualifiers:
            return True
        if 15 in qualifiers:
            return True
        if 16 in qualifiers:
            return True
        return False
    except ValueError:
        return False
    
def _get_goal(qualifiers):
    try:
        if 16 in qualifiers:
            return True
        return False
    except ValueError:
        return False