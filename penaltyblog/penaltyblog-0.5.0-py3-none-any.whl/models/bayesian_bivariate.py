import os

import aesara.tensor as tt
import numpy as np
import pandas as pd
import pymc as pm
from scipy.stats import poisson

from .football_probability_grid import FootballProbabilityGrid


class BayesianBivariateGoalModel:
    """Bayesian bivariate poisson model for predicting outcomes of football
    (soccer) matches.

    Methods
    -------
    fit()
        fits a Bayesian bivariate poisson model to the data to calculate the team strengths.
        Must be called before the model can be used to predict game outcomes

    predict(home_team, away_team, max_goals=15)
        predict the outcome of a football (soccer) game between the home_team and away_team

    get_params()
        Returns the fitted parameters from the model
    """

    def __init__(
        self,
        goals_home,
        goals_away,
        teams_home,
        teams_away,
        weights=1,
        n_jobs=None,
        draws=2500,
    ):
        """
        Parameters
        ----------
        goals_home : list
            A list or pd.Series of goals scored by the home_team
        goals_away : list
            A list or pd.Series of goals scored by the away_team
        teams_home : list
            A list or pd.Series of team_names for the home_team
        teams_away : list
            A list or pd.Series of team_names for the away_team
        weights : list
            A list or pd.Series of weights for the data,
            the lower the weight the less the match has on the output.
            A scalar value of 1 indicates equal weighting for each observation
        n_jobs : int or None
            Number of chains to run in parallel
        draws : int
            Number of samples to draw from the model
        """
        self.fixtures = pd.DataFrame([goals_home, goals_away, teams_home, teams_away]).T
        self.fixtures.columns = ["goals_home", "goals_away", "team_home", "team_away"]
        self.fixtures["goals_home"] = self.fixtures["goals_home"].astype(int)
        self.fixtures["goals_away"] = self.fixtures["goals_away"].astype(int)
        self.fixtures["weights"] = weights
        self.fixtures = self.fixtures.reset_index(drop=True)
        self.fixtures["weights"] = weights

        self.n_teams = len(self.fixtures["team_home"].unique())

        self.teams = (
            self.fixtures[["team_home"]]
            .drop_duplicates()
            .sort_values("team_home")
            .reset_index(drop=True)
            .assign(team_index=np.arange(self.n_teams))
            .rename(columns={"team_home": "team"})
        )

        self.fixtures = (
            self.fixtures.merge(
                self.teams,
                left_on="team_home",
                right_on="team",
                how="left",
            )
            .rename(columns={"team_index": "home_index"})
            .drop(["team"], axis=1)
            .merge(
                self.teams,
                left_on="team_away",
                right_on="team",
                how="left",
            )
            .rename(columns={"team_index": "away_index"})
            .drop(["team"], axis=1)
        )

        self.trace = None
        self.draws = draws
        self.params = dict()

        if n_jobs == -1 or n_jobs is None:
            self.n_jobs = os.cpu_count()
        elif n_jobs == 0:
            self.n_jobs = 1
        else:
            self.n_jobs = n_jobs

        self.fitted = False

    def __repr__(self):
        repr_str = ""
        repr_str += "Module: Penaltyblog"
        repr_str += "\n"
        repr_str += "\n"

        repr_str += "Model: Bayesian Random Intercept"
        repr_str += "\n"
        repr_str += "\n"

        repr_str += "Number of parameters: {0}".format(len(self.params))
        repr_str += "\n"

        repr_str += "{0: <20} {1:<20} {2:<20} {3:<20}".format(
            "Team", "Attack", "Defence", "rho"
        )
        repr_str += "\n"
        repr_str += "-" * 80
        repr_str += "\n"

        attack = [None] * self.n_teams
        defence = [None] * self.n_teams
        rho = [None] * self.n_teams
        team = self.teams["team"].tolist()

        for k, v in self.params.items():
            if "_" not in k:
                continue

            p = k.split("_")[0]
            t = k.split("_")[1]  # noqa
            if p == "attack":
                idx = self.teams.query("team == @t").iloc[0]["team_index"]
                attack[idx] = round(v, 3)
            elif p == "defence":
                idx = self.teams.query("team == @t").iloc[0]["team_index"]
                defence[idx] = round(v, 3)
            elif p == "rho":
                idx = self.teams.query("team == @t").iloc[0]["team_index"]
                rho[idx] = round(v, 3)
            else:
                continue

        for obj in zip(team, attack, defence, rho):
            repr_str += "{0:<20} {1:<20} {2:<20} {3:<20}".format(
                obj[0],
                obj[1],
                obj[2],
                obj[3],
            )
            repr_str += "\n"

        repr_str += "-" * 80
        repr_str += "\n"

        repr_str += "mu: {0}".format(round(self.params["mu"], 3))
        repr_str += "\n"
        repr_str += "eta: {0}".format(round(self.params["eta"], 3))
        repr_str += "\n"

        return repr_str

    def __str__(self):
        return self.__repr__()

    def fit(self):
        """
        Fits the model to the data and calculates the team strengths,
        home advantage and intercept. Should be called before `predict` can be used
        """
        goals_home_obs = self.fixtures["goals_home"].values
        goals_away_obs = self.fixtures["goals_away"].values

        home_team = self.fixtures["home_index"].values
        away_team = self.fixtures["away_index"].values

        weights = self.fixtures["weights"].values

        with pm.Model():
            # attack
            tau_att = pm.Gamma("tau_att", 1, 1)
            atts_star = pm.Normal("atts_star", mu=0, tau=tau_att, shape=self.n_teams)

            # defence
            tau_def = pm.Gamma("tau_def", 1, 1)
            def_star = pm.Normal("def_star", mu=0, tau=tau_def, shape=self.n_teams)

            # rho
            tau_rho = pm.Gamma("tau_rho", 1, 1)
            rho = pm.Normal("rho", mu=0, tau=tau_rho, shape=self.n_teams)

            # flat parameters
            mu = pm.Flat("mu")
            eta = pm.Flat("eta")

            # apply sum zero constraints
            atts = pm.Deterministic("atts", atts_star - tt.mean(atts_star))
            defs = pm.Deterministic("defs", def_star - tt.mean(def_star))

            # calulate theta
            lambda1 = tt.exp(mu + eta + atts[home_team] + defs[away_team])
            lambda2 = tt.exp(mu + atts[away_team] + defs[home_team])
            lambda3 = tt.exp(rho[away_team] + rho[away_team])

            # pm.Potential(
            #     "home_goals",
            #     weights * pm.Poisson.dist(mu=lambda1 + lambda3).logp(goals_home_obs),
            # )
            # pm.Potential(
            #     "away_goals",
            #     weights * pm.Poisson.dist(mu=lambda2 + lambda3).logp(goals_away_obs),
            # )

            # goal expectation
            pm.Potential(
                "home_goals",
                # weights * pm.Poisson.dist(mu=home_theta).logp(goals_home_obs),
                weights
                * pm.logp(pm.Poisson.dist(mu=lambda1 + lambda3), goals_home_obs),
            )
            pm.Potential(
                "away_goals",
                # weights * pm.Poisson.dist(mu=away_theta).logp(goals_away_obs),
                weights
                * pm.logp(pm.Poisson.dist(mu=lambda2 + lambda3), goals_away_obs),
            )
            self.trace = pm.sample(
                self.draws,
                tune=2000,
                cores=self.n_jobs,
                return_inferencedata=False,
                target_accept=0.95,
            )

        self.params["eta"] = np.mean(self.trace["eta"])
        self.params["mu"] = np.mean(self.trace["mu"])
        for idx, row in self.teams.iterrows():
            self.params["attack_" + row["team"]] = np.mean(
                [x[idx] for x in self.trace["atts"]]
            )
            self.params["defence_" + row["team"]] = np.mean(
                [x[idx] for x in self.trace["defs"]]
            )
            self.params["rho_" + row["team"]] = np.mean(
                [x[idx] for x in self.trace["rho"]]
            )

        self.fitted = True

    def predict(self, home_team, away_team, max_goals=15) -> FootballProbabilityGrid:
        """
        Predicts the probabilities of the different possible match outcomes

        Parameters
        ----------
        home_team : str
            The name of the home_team, must have been in the data the model was fitted on

        away_team : str
            The name of the away_team, must have been in the data the model was fitted on

        max_goals : int
            The maximum number of goals to calculate the probabilities over.
            Reducing this will improve performance slightly at the expensive of acuuracy

        Returns
        -------
        FootballProbabilityGrid
            A class providing access to a range of probabilites,
            such as 1x2, asian handicaps, over unders etc
        """
        if not self.fitted:
            raise ValueError(
                (
                    "Model's parameters have not been fit yet, please call the `fit()` "
                    "function before making any predictions"
                )
            )

        # check we have parameters for teams
        if home_team not in self.teams["team"].tolist():
            raise ValueError(
                (
                    "No parameters for home team - "
                    "please ensure the team was included in the training data"
                )
            )

        if away_team not in self.teams["team"].tolist():
            raise ValueError(
                (
                    "No parameters for away team - "
                    "please ensure the team was included in the training data"
                )
            )

        # get the parameters
        eta = self.params["eta"]
        mu = self.params["mu"]
        atts_home = self.params["attack_" + home_team]
        atts_away = self.params["attack_" + away_team]
        defs_home = self.params["defence_" + home_team]
        defs_away = self.params["defence_" + away_team]
        rho_home = self.params["rho_" + home_team]
        rho_away = self.params["rho_" + away_team]

        # calculate the goal vectors
        lambda1 = np.exp(mu + eta + atts_home + defs_away)
        lambda2 = np.exp(mu + atts_away + defs_home)
        lambda3 = np.exp(rho_home + rho_away)

        # calculate theta
        home_theta = lambda1 + lambda3
        away_theta = lambda2 + lambda3
        home_goals_vector = poisson(home_theta).pmf(np.arange(0, max_goals))
        away_goals_vector = poisson(away_theta).pmf(np.arange(0, max_goals))

        # get the probabilities for each possible score
        m = np.outer(home_goals_vector, away_goals_vector)

        probability_grid = FootballProbabilityGrid(m, home_theta, away_theta)
        return probability_grid

    def get_params(self) -> dict:
        """
        Provides access to the model's fitted parameters

        Returns
        -------
        dict
            A dict containing the model's parameters
        """
        if not self.fitted:
            raise ValueError(
                "Model's parameters have not been fit yet, please call the `fit()` function first"
            )

        return self.params
