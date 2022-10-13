from os.path import join

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
from typing import Callable, Tuple, List, Dict

from numpy import ndarray
from pandas import DataFrame

from aidev.blocks.data import Data
from aidev.blocks.optimization import (
    NSGA_III,
    ParticleSwarm,
    GeneticAlgorithm,
    NelderMeadSearch,
)
from aidev.blocks.postprocessing import Decision
from aidev.blocks.sampling import Latin, Random
from aidev.blocks.surrogates import (
    Kriging,
    NeuralNetwork,
    Polynomial,
    Spline,
    SupportVector,
)
from aidev.utilities.types import FeatureDefinition


class AiDev:
    def __init__(
        self,
        features: FeatureDefinition,
        simulator: Callable[..., List[float]],
        path: str,
    ):
        self.features = features
        self.simulator = simulator
        self.path = path

        self.data = DataFrame()
        self.datahandler = Data(
            features=self.features,
            simulator=self.simulator,
            db_name=join(self.path, "db.csv"),
        )

        self.sampling_strategy = "latin"
        self.n_samples = 50

        self.optimization_strategy = "global"
        self.global_optimizer = "PSO"
        self.popsize = 15
        self.local_iter = 500
        self.global_iter = 5

        self.surrogate_strategy = "polynomial"
        self.degree_fit = 1
        self.interaction_only = False
        self.fit_intercept = True
        self.kernel = "rbf"
        self.n_nodes = (16, 8)
        self.activation = "relu"
        self.n_epochs = 1000
        self.n_knots = 2

    def run(
        self,
        data: DataFrame = DataFrame(),
        sampling: bool = True,
        surrogate: bool = True,
        optimization: bool = True,
        # mail_at_completion=False
    ) -> DataFrame:
        if not data.empty:
            self.data = data.dropna().drop_duplicates()[
                self.features.pnames + self.features.tnames
            ]

        if sampling:
            doe = self._sampling()
            if not self.data.empty:
                self.data = self.datahandler.add(data=self.data, samples=doe)
            else:
                self.data = self.datahandler.generate(samples=doe)

            self.data.to_csv(join(self.path, "db.csv"), index=False, mode="w")

        if optimization:
            if surrogate:
                for _ in range(self.global_iter):
                    simulator_surrogate, performance = self._surrogate()
                    print(f"performance is: {round(performance[0],2)}")
                    results = self._optimization(simulator_surrogate)
                    x_results = results["x"]
                    self.data = self.datahandler.add(data=self.data, samples=x_results)  # type: ignore
            else:
                results = self._optimization(self.simulator, surrogate=surrogate)
                x_results = results["x_hist"]
                f_results = results["fmodel_hist"]
                if not self.data.empty:
                    self.data = self.datahandler.add(
                        data=self.data, samples=x_results, fval=f_results
                    )
                else:
                    self.data = self.datahandler.generate(
                        samples=x_results, fval=f_results
                    )

            self.data = (
                self._decision()
            )  # todo would be nice to perform decisions also after the sampling
            self.data.to_csv(join(self.path, "db.csv"), index=False, mode="w")

        return self.data

    def _sampling(self) -> ndarray:
        if self.sampling_strategy == "latin":
            doe = Latin(self.features)(n_samples=self.n_samples)
        else:
            doe = Random(self.features)(n_samples=self.n_samples)
        return doe

    def _surrogate(
        self,
    ) -> Tuple[Callable[..., List[float]], Tuple[float, float]]:

        if self.surrogate_strategy == "kriging":
            model, performance = Kriging(kernel=None)(self.data, self.features)
        elif self.surrogate_strategy == "supportvector":
            model, performance = SupportVector(
                kernel=self.kernel,
                degree_fit=self.degree_fit,
            )(self.data, self.features)
        elif self.surrogate_strategy == "neuralnetwork":
            model, performance = NeuralNetwork(
                n_nodes=self.n_nodes,
                activation=self.activation,
                n_epochs=self.n_epochs,
            )(self.data, self.features)
        elif self.surrogate_strategy == "spline":
            model, performance = Spline(
                n_knots=self.n_knots,
                degree_fit=self.degree_fit,
                fit_intercept=self.fit_intercept,
            )(self.data, self.features)
        else:
            model, performance = Polynomial(
                degree_fit=self.degree_fit,
                interaction_only=self.interaction_only,
                fit_intercept=self.fit_intercept,
            )(self.data, self.features)

        return model, performance

    def _optimization(
        self,
        objective: Callable[..., List[float]],
        surrogate: bool = True,
    ) -> Dict[str, list]:
        if len(self.features.targets) == 1:
            termination = (
                ("n_gen", self.local_iter)
                if surrogate
                else ("n_eval", self.global_iter)
            )
            if self.optimization_strategy == "local":
                results = NelderMeadSearch(
                    objective,
                    self.features,
                    popsize=self.popsize,
                )(termination=termination)
            else:
                if self.global_optimizer == "GA":
                    results = GeneticAlgorithm(
                        objective,
                        self.features,
                        popsize=self.popsize,
                    )(termination=termination)
                else:
                    results = ParticleSwarm(
                        objective,
                        self.features,
                        popsize=self.popsize,
                    )(termination=termination)
        else:
            termination = (
                ("n_gen", self.local_iter)
                if surrogate
                else ("n_eval", self.global_iter)
            )
            results = NSGA_III(objective, self.features, popsize=self.popsize)(
                termination=termination
            )
        return results

    def _decision(self, return_choices: int = 10) -> DataFrame:
        data = Decision(self.data, self.features).decide(
            self.data, return_choices=return_choices  # type: ignore
        )
        return data

    # @staticmethod
    # def _mail(content: str):
    #     with open("../../settings.json") as settings_file:
    #         settings = load(settings_file)
    #     message = MIMEMultipart()
    #     sender_address = settings["sender_address"]
    #     sender_psw = settings["sender_psw"]
    #     receiver_address = settings["receiver_address"]
    #
    #     message["From"] = sender_address
    #     message["To"] = receiver_address
    #     message["Subject"] = "Notification of AiDev process end."
    #     message.attach(MIMEText(content, "plain"))
    #
    #     session = smtplib.SMTP("smtp.gmail.com", 587)
    #     session.starttls()
    #     session.login(sender_address, sender_psw)
    #     text = message.as_string()
    #     session.sendmail(sender_address, receiver_address, text)
    #     session.quit()
