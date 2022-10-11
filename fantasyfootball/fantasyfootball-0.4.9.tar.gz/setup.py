# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fantasyfootball']

package_data = \
{'': ['*'],
 'fantasyfootball': ['datasets/season/2015/*',
                     'datasets/season/2016/*',
                     'datasets/season/2017/*',
                     'datasets/season/2018/*',
                     'datasets/season/2019/*',
                     'datasets/season/2020/*',
                     'datasets/season/2021/*',
                     'datasets/season/2022/*']}

install_requires = \
['html5lib>=1.1,<2.0',
 'lxml>=4.7.1,<5.0.0',
 'openpyxl>=3.0.9,<4.0.0',
 'pandas-flavor>=0.2.0,<0.3.0',
 'pyjanitor>=0.22.0,<0.23.0',
 'requests>=2.27.1,<3.0.0',
 'sklearn>=0.0,<0.1']

extras_require = \
{':python_version >= "3.8" and python_version < "4.0"': ['pandas>=1.3.5,<2.0.0',
                                                         'scikit-learn>=1.0.2,<2.0.0']}

setup_kwargs = {
    'name': 'fantasyfootball',
    'version': '0.4.9',
    'description': 'A package for Fantasy Football data and analysis',
    'long_description': '\n![logo](https://github.com/thecodeforest/fantasyfootball/blob/main/docs/images/logo.png?raw=true)\n\n\n-----------------\n\n# Welcome to fantasyfootball\n![fantasyfootball](https://github.com/thecodeforest/fantasyfootball/actions/workflows/tests.yml/badge.svg)[![codecov](https://codecov.io/gh/thecodeforest/fantasyfootball/branch/main/graph/badge.svg?token=J2HY3ZOITH)](https://codecov.io/gh/thecodeforest/fantasyfootball)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![Documentation Status](https://readthedocs.org/projects/fantasyfootball/badge/?version=latest)](https://fantasyfootball.readthedocs.io/en/latest/?badge=latest)[![Python](https://img.shields.io/badge/Python-3.7%20%7C3.8%20%7C%203.9-blue)](https://badge.fury.io/py/fantasyfootball)[![PyPI version](https://badge.fury.io/py/fantasyfootball.svg)](https://badge.fury.io/py/fantasyfootball)[![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)\n\n\n\n**fantasyfootball** is a Python package that provides up-to-date game data, including player statistics, betting lines, injuries, defensive rankings, and game-day weather data. While many websites offer NFL game data, obtaining it in a format appropriate for analysis or inference requires either (1) a paid subscription or (2) manual weekly downloads with extensive data cleaning. **fantasy football** centralizes game data in a single location while ensuring it is up-to-date throughout the season.\n\nAdditionally, **fantasyfootball** streamlines the creation of features for in-season, player-level fantasy point projections. The resulting projections can then determine weekly roster decisions. Check out the [tutorial notebook](https://github.com/thecodeforest/fantasyfootball/blob/inference-example/examples/tutorial.ipynb) to get started! \n\n## Installation\n\n```bash\n$ pip install fantasyfootball\n```\n\n## Benchmarking\n\nThe **fantasyfootball** package provides football enthusiasts with the data and tools to create player point projections customized for their league\'s scoring system. Indeed, a simple comparison between (1) a "naive" projection, and (2) a subscription-based, "industry-grade" projection, revealed that accurate weekly player-level point projections are achievable with **fantasyfootball**. Across all player positions, **fantasyfootball** projections were, on average, 18% more accurate relative to the naive projection (5.6 pts vs. 4.6 pts), while the industry-grade projections were 4% more accurate than the **fantasyfootball** projections (4.6 pts vs. 4.4 pts). The figure below further disaggregates projection performance by player position. More details surrounding this analysis can be found in the [benchmarking notebook](https://github.com/thecodeforest/fantasyfootball/blob/main/examples/benchmarking.ipynb). \n\n![benchmark](https://github.com/thecodeforest/fantasyfootball/blob/main/docs/images/benchmark_performance_full.png?raw=true)\n\n## Quickstart\n\nLet\'s walk through an example to illustrate a core use-case of **fantasyfootball**: weekly roster decisions. Imagine it\'s Tuesday, Week 15 of the 2021 NFL regular season. Your somewhat mediocre team occupies 5th place in the league standings, one spot away from the coveted playoff threshold. It is a must-win week, and you are in the unenviable position of deciding who starts in the Flex roster spot. \nYou have three wide receivers available to start, Keenan Allen, Chris Godwin, or Tyler Lockett, and you want to estimate which player will score more points in Week 15. Accordingly, you use the data and feature engineering capabilities in **fantasyfootball** to create player-level point projections. The player with the highest point projection will be slotted into the Flex roster spot, propelling your team to fantasy victory!\n\nLet\'s start by importing several packages and reading all game data from the 2015-2021 seasons.\n\n```python\nfrom janitor import get_features_targets \nfrom sklearn.ensemble import RandomForestRegressor\n\nfrom fantasyfootball.data import FantasyData\nfrom fantasyfootball.features import FantasyFeatures\nfrom fantasyfootball.benchmarking import filter_to_prior_week\n\n# Instantiate FantasyData object for 2015-2021 seasons\nfantasy_data = FantasyData(season_year_start=2015, season_year_end=2021)\n```\nAt the time of writing this walkthrough, there are 45 fields available for each player-season-week. For more details on the data, see the [Datasets](#datasets) section below.\n\nNext, we\'ll create our outcome variable (y) that defines each player\'s total weekly fantasy points. Then, depending on your league\'s scoring rules, you can supply standard fantasy football scoring systems, including *yahoo*, *fanduel*, *draftkings*, or create your own *custom* configuration. In the current example, we\'ll assume you are part of a *yahoo* league with standard scoring.\n\n```python\nfantasy_data.create_fantasy_points_column(scoring_source="yahoo")\n```\n\nNow that we\'ve added our outcome variable, we\'ll extract the data and look at a few fields for Tyler Lockett over the past four weeks. Note that a subset of all fields appears below. \n\n```python\n# extract data from fantasy_data object\nfantasy_df = fantasy_data.data\n# filter to player-season-week in question\nlockty_df = fantasy_df.query("name==\'Tyler Lockett\' & season_year==2021 & 11<=week<=14")   \nprint(lockty_df)\n```\n\n| pid      |   week |   is_away |   receiving_rec |   receiving_td |   receiving_yds |   fanduel_salary |   ff_pts_yahoo |\n|:---------|-------:|----------:|----------------:|---------------:|----------------:|--------------------:|---------------:|\n| LockTy00 |     11 |         0 |               4 |              0 |             115 |                6000 |           13.5 |\n| LockTy00 |     12 |         1 |               3 |              0 |              96 |                6300 |           11.1 |\n| LockTy00 |     13 |         0 |               7 |              1 |              68 |                6500 |           16.3 |\n| LockTy00 |     14 |         1 |               5 |              1 |             142 |                6700 |           24.7 |\n\nWe\'ll create the feature set that will feed our predictive model in the following section. The first step is to filter to the most recently completed week for all wide receivers (WR). \n\n```python\n# extract the name of our outcome variable\ny = fantasy_df.columns[-1]\n# filter to all data prior to 2021, Week 15\nbacktest_df = fantasy_df.filter_to_prior_week(season_year=2021, week_number=14)\n# Instantiate FantasyFeatures object for all Wide Receivers\nfeatures = FantasyFeatures(backtest_df, position="WR", y=y)   \n```\n\nNow, we\'ll apply a few filters and transformations to prepare our data for modeling: \n\n* `filter_inactive_games` - Removes games where a player did not play, and therefore recorded zero points.\n\n* `filter_n_games_played_by_season` - Removes players who played only a few games in a season. Setting a threshold is necessary when creating lagged features (which happen to be some of the best predictors of future performance). Removing non-essential players, or those who play only one or two games in a season, also reduces noise and leads to more accurate models. \n\n* `create_future_week` - Adds leading indicators that we can use to make predictions for Week 15. Recall that, in the current example, we only have game data up to Week 14, so we need to create features for a future, unplayed game. For example, the over/under point projections combined with the point spread estimate how much each team will score. A high-scoring estimate would likely translate into more fantasy points for all players on a team. Another example is weather forecasts. An exceptionally windy game may favor a "run-centric" offense, leading to fewer passing/receiving plays and more rushing plays. Such an occurrence would benefit runnings backs while hurting wide receivers and quarterbacks. \nThe *is_future_week* field is also added during this step and allows an easy split between past and future data during the modeling process. \n \n* `add_coefficient_of_variation` - Adds a Coefficient of Variation (CV) for each player based on their past N games. CV shows how much scoring variability there is for each player on a week-to-week basis. While the CV will not serve as an input for predicting player performance in Week 15, it will help us to gauge the consistency of each player when deciding between multiple players. \n\n* `add_lag_feature` - Add lags of a specified length for lagging indicators, such as receptions, receiving yards, or rushing touchdowns from previous weeks. \n\n* `add_moving_avg_feature` - Add a moving average of a specified length for lagging indicators.\n\n* `create_ff_signature` - Executes all of the steps used to create "derived features," or features that we\'ve created using some transformation (e.g., a lag or moving average). \n\n```python\n\nfeatures.filter_inactive_games(status_column="is_active")\nfeatures.filter_n_games_played_by_season(min_games_played=1)\nfeatures.create_future_week()\nfeatures.add_coefficient_of_variation(n_week_window=16)\nfeatures.add_lag_feature(n_week_lag=1, lag_columns=y)\nfeatures.add_moving_avg_feature(n_week_window=4, window_columns=y)\nfeatures_signature_dict = features.create_ff_signature()\n```\n\nHaving created our feature set, we\'ll seperate our historical (training) data , denoted `hist_df`, from the future (testing), unplayed game data, denoted `future_df`, using the indicator added above during the `create_future_week` step. \n\n```python\nfeature_df = features_signature_dict.get("feature_df")\nhist_df = feature_df[feature_df["is_future_week"] == 0]\nfuture_df = feature_df[feature_df["is_future_week"] == 1]\n```\nFor the sake of simplicity, we\'ll leverage a small subset of raw, untransformed features from our original data, and combine these with the derived features we created in the previous step. \n\n```python\nderived_feature_names = features_signature_dict.get("pipeline_feature_names")\nraw_feature_names = ["avg_windspeed", "fanduel_salary"]\nall_features = derived_feature_names + raw_feature_names\n```\n\nLet\'s split between our train/hist and test/future data. \n```python\nX_hist, y_hist = hist_df[all_features + [y]].get_features_targets(y, all_features)\nX_future = future_df[all_features]\n```\n\nNow we can fit a simple model and make predictions for the upcoming week. \n\n```python\nrf = RandomForestRegressor(n_estimators=1000, max_depth=4, random_state=0)\nrf.fit(X_hist.values, y_hist.values)\ny_future = rf.predict(X_future.values).round(1)\n```\n\nBelow we\'ll assign our point predictions back to the `future_df` we created for Week 15 and filter to the three players in question.\n\n```python\nfuture_df = future_df.assign(**{f"{y}_pred": y_future})\nplayers = ["Chris Godwin", "Tyler Lockett", "Keenan Allen"]\nfuture_df[["name", "team", "opp", "week", "date", f"{y}_pred"]].query(\n    "name in @players"\n)\n```\n| name          | team   | opp   |   week | date       |   ff_pts_yahoo_pred |   cv |\n|:--------------|:-------|:------|-------:|:-----------|--------------------:|-----:|\n| Keenan Allen  | LAC    | KAN   |     15 | 2021-12-16 |                14.1 |   35 |\n| Chris Godwin  | TAM    | NOR   |     15 | 2021-12-19 |                11   |   49 |\n| Tyler Lockett | SEA    | LAR   |     15 | 2021-12-21 |                14   |   74 |\n\n\n\nKeenan Allen and Tyler Lockett are projected to score ~3 more points than Chris Godwin. And while Keenan Allen and Tyler Lockett have similar projections, over the past 16 games, Allen is much more consistent than Lockett. That is, we should put more faith in Allen\'s 14-point forecast relative to Lockett. When point projections are equivalent, CV can be a second input when deciding between two players. For example, if the goal is to score many points and win the week, a player with a large CV might be the better option, as they have a higher potential ceiling. In contrast, if the goal is to win, and the total points scored are less critical, then a more consistent player with a small CV is the better option. \n\n\n\n## Datasets\nThe package provides the following seven datasets by season: \n\n* **calendar** - The game schedule for the regular season. \n\n    * `date` - Date (yyyy-mm-dd) of the game\n    * `week` - The week of the season\n    * `team` - The three letter abbreviation of the team\n    * `opp` - The the letter abbreviation of the team\'s opponent\n    * `is_away` - Boolean indicator if the `team` is playing at the opponent\'s field (1 = away, 0 = home)\n    * `season_year` - The year of the season\n\n<br>\n\n* **players** - Each team\'s roster. Note that only Quarterbacks, Runningbacks, Wide Receivers, and Tight Ends are included. \n    * `name` - A player\'s first and last name\n    * `team` - The three letter abbreviation of the player\'s team\n    * `position` - The two letter abbreviation of the player\'s position\n    * `season_year` - The year of the season\n\n<br>    \n\n* **stats** - The aggregated game statistics for each player. \n    * `pid` - Unique identifier for each player. \n    * `name` - A player\'s first and last name \n    * `team` - The three letter abbreviation of the player\'s team\n    * `opp` - The three letter abbreviation of the players\'s weekly opponent \n    * `is_active` - Boolean indicator if the player is active for the game (1 = active, 0 = inactive)\n    * `date` - Date (yyyy-mm-dd) of the game\n    * `result` - The box score of the game, along with an indicator of the outcome (W or L)\n    * `is_away` - Boolean indicator if the game was played at the opponent\'s field (1 = away, 0 = home)\n    * `is_start` - Boolean indicator if the player started the game (1 = starter, 0 = bench)\n    * `age` - The age of the player in years\n    * `g_nbr` - The game number for the player. This differs from the week number, as it accounts for team buy weeks. \n    * `receiving_tgt` - The number of targets the player received\n    * `receiving_rec` - The total number of receptions\n    * `receiving_yds` - The total number of receiving yards\n    * `receiving_td` - The total number of receiving touchdowns\n    * `rushing_yds` - The total number or rushing yards\n    * `rushing_td` - The total number or rushing yards\n    * `rushing_att` - The total number of rushing attempts\n    * `receiving_td` - The total number of rushing touchdowns\n    * `passing_att` - The total number of passing attempts\n    * `passing_cmp` - The total number of completed passes\n    * `passing_yds` - The total number of passing yards\n    * `passing_td` - The total number of passing touchdowns\n    * `fumbles_fmb` - The total number of fumbles\n    * `passing_int` - The total number of passing interceptions\n    * `scoring_2pm` - The total number of 2-point conversions\n    * `punt_return_tds` - The total number punt return touchdowns\n    * `off_snaps_pct` - The percentage of offensive snaps the player played\n\n<br>\n\n* **salary** - The player salaries from DraftKings and FanDuel.\n    * `name` - A player\'s first and last name \n    * `position` - The two letter abbreviation of the player\'s position\n    * `season_year` - The year of the season\n    * `week` - The week of the season\n    * `fanduel_salary` - Fanduel player salary\n\n<br>\n\n* **weather** - The game-day weather conditions. Historical data are actual weather conditions, while  data collected prior to a game are based on weather forecasts. Weather data is updated daily throughout the season.\n    * `date` - Date (yyyy-mm-dd) of the game\n    * `team` - The three letter abbreviation of the team\n    * `opp` - The three letter abbreviation of the team\'s opponent\n    * `stadium_name` - Name of the stadium hosting the game. Updated as of 2020. \n    * `roof_type` - Indicates if stadium has dome, retractable roof, or is outdoor. \n    * `temperature` - Average daily temperature (f&deg;). Note that the `temperature` of dome/retractable roof stadiums are set to 75&deg;.\n    * `is_rain` - Boolean indicator if rain occurred or is expected (1 = yes, 0 = no)\n    * `is_snow` - Boolean indicator if snow occurred or is expected (1 = yes, 0 = no)\n    * `windspeed` - Average daily windspeed (mph)\n    * `is_outdoor` - Boolean indicator if stadium is outdoor (1 = is outdoor, 0 = retractable/dome). Note that for stadiums with a retractable roof, it is not possible to determine if roof was open during the game. \n    \n    \n\n\n\n<br>\n\n\n* **betting** - Offensive point projections that are derived from the opening over/under and point-spread. Opening point spreads are refreshed each week on Tuesday.\n\n    * `team` - The three letter abbreviation of team with the point projections\n    * `opp` - The three letter abbreviatino of the team\'s opponent\n    * `projected_off_pts` - The projected number of points for each team. For example, if the over/under for a game is 50, and one team is favored to win by 4 points, then the favored team is projected to score 27 points, while the underdog is projected to score 23 points. \n    * `date` - Date (yyyy-mm-dd) of the game\n    * `season_year` - The year of the season\n\n<br>\n\n* **defense** - The relative strength of each team\'s defense along rushing, passing, and receiving. Rankings are updated each week on Tuesday. \n\n    * `week` - The week of the season\n    * `opp` - The three letter team\'s abbreviation\n    * `rushing_def_rank` - Ordinal rank (1 = Best, 32 = Worst) of defensive strength against rushing offense. Combines total rushing yards and total rushing touchdowns to determine strength. The relative weight on each dimension is adjustable. \n    * `receiving_def_rank` - Ordinal rank (1 = Best, 32 = Worst) of defensive strength against receiving offense. Combines total receiving yards and total receiving touchdowns to determine strength. The relative weight on each dimension is adjustable. \n    * `passing_def_rank` - Ordinal rank (1 = Best, 32 = Worst) of defensive strength against passing offense. Combines total passing yards and total passing touchdowns to determine strength. The relative weight on each dimension is adjustable. \n    * `season_year` - The year of the season\n\n<br>\n\n* **injury** - The weekly injury reports for each team. Reports are updated the day before game day.\n\n    * `name` - A player\'s first and last name \n    * `team` - The three letter abbreviation of team with the point projections\n    * `position` - The two letter abbreviation of the player\'s position\n    * `season_year` - The year of the season\n    * `week` - The week of the season\n    * `injury_type` - The type of injury (e.g., Heel, Hamstring, Knee, Ankle)\n    * `has_dnp_tag` - A boolean indicator if the player received a DNP (did not practice) tag  at any point during the week leading up to the game (1) or (0) if not.\n    * `has_limited_tag` - A boolean indicator if the player received a Limited tag  at any point during the week leading up to the game (1) or (0) if not.\n    * `most_recent_injury_status` - The most recent status for a player prior to game-day (DNP, Limited, Full, no injury).\n    * `n_injured` - Indicates the number of injuries reported for a player. For example, "Shin, Ankle" indicates two injuries, or "Shoulder" indicates one injury.\n\n<br>\n\n* **draft** - The average draft position (ADP) of each player prior to the season. Positions are based on a standard 12 person draft. \n    * `avg_draft_position` - The average position a player was drafted across many pre-season mock drafts. Players drafted earlier are expected to score more points over a season than those drafted later. \n    * `name` - A player\'s first and last name \n    * `position` - The two letter abbreviation of the player\'s position\n    * `team` - The three letter abbreviation of team with the point projections    \n    \n    * `season_year` - The year of the season\n\n## Data Pipeline\n\nWhile the PyPi version of **fantasyfootball** is updated monthly, the GitHub version is updated every Thursday during the regular season (Sep 8 - Jan 8). New data is stored in [datasets](https://github.com/thecodeforest/fantasyfootball/tree/main/src/fantasyfootball/datasets/season) directory within the **fantasyfootball** package. If there is a difference between the data in Github and the installed version, creating a `FantasyData` object will download the new data. Note that differences in data persist when a session ends. Updating the installed version of **fantasyfooball** will correct this difference and is recommended at the end of each season. \n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`fantasyfootball` was created by Mark LeBoeuf. It is licensed under the terms of the MIT license.\n\n\n\n\n',
    'author': 'Mark LeBoeuf',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
