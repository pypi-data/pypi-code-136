from typing import Union

from isodate import Duration
from Supplychain.Wrappers.simulator import CosmoEngine
from Supplychain.Generic.adx_and_file_writer import ADXAndFileWriter
import pandas as pd
from Supplychain.Generic.timer import Timer
from math import sqrt
from Supplychain.Wrappers.environment_variables import EnvironmentVariables
from Supplychain.Run.simulation import run_simple_simulation
import comets as co


def local_sensitivity_analysis(
    simulation_name: str,
    amqp_consumer_adress: Union[str, None] = None,
    parameter: str = "Transport Duration",  # type of variable on which the analysis is performed
    adx_writer: Union[ADXAndFileWriter, None] = None,
    variation: float = 0.5,  # variation value
    change: str = "relative",  # change mode
    local: bool = False,  # false to optionally send the results to adx ; true to return the results dataframe (useful for the test)
    simulator_path: str = "Simulation",
    saving_results: bool = False,
):  # give a different path is useful for the test

    with Timer("[Run Sensitivity]") as t:

        simulator = CosmoEngine.LoadSimulator(simulator_path)

        map_to_entities = {
            "Transport Duration": "TransportOperation",
            "Machine Opening Time": "Machine",
        }

        list_of_datapaths = get_list_of_datapaths(
            simulator_path, map_to_entities[parameter]
        )

        list_of_variables = create_variables(
            simulator_path, list_of_datapaths, change, variation
        )

        def encoder(parameters):
            """
            Encoder of the task on which the S.A will be performed. The encoder receives a parameter set where
            the attributes of type 'schedule' are separated (see function create_variables). The aim of this encoder is to
            re concatenate the schedules together. For example, if the encoder receives the following parameter set:
            {"transport_lyon": 2,
             "transport_paris__@__0": 1,
             "transport_paris__@__3": 2,
             "transport_paris__@__5": 4,}

            it will return :
            {'transport_lyon': 2,
             'transport_paris': {'0': 1, '3': 2, '5': 4}}
            Args:
                parameters : Parameter set with the value computed by the S.A algorithm where schedules are separated.
                Note that the keys of the parameter set are either a datatapth or a datapath + '__@__' + time_step.

            Returns:
                parameter_set : Parameter set with the value computed by the S.A algorithm where the schedules are re concatenated.
                Note that the keys of the parameter set are the datapath of the attributes.
            """
            parameter_set = {}
            for key, value in parameters.items():
                if "__@__" in key:  # check if it belongs to a group
                    if key not in parameter_set.keys():
                        parameter_set[key.split("__@__")[0]] = {
                            key.split("__@__")[-1]: value
                        }
                    else:
                        temp_dic = parameter_set[key.split("__@__")[0]].copy()
                        temp_dic[key.split("__@__")[-1]] = value
                        parameter_set[key.split("__@__")[0]] = temp_dic
                else:
                    parameter_set[key] = value
            return parameter_set

        used_probes = ["PerformanceIndicators"]

        class PerformanceConsumer:
            def __init__(self):
                self.data = {}

            def Consume(self, p_data):
                f = self.engine.PerformanceIndicatorsProbeOutput.Cast(p_data).GetFacts()
                for fact in f:
                    self.data = {
                        "OPEX": fact.GetOPEX().GetAsFloat(),
                        "Profit": fact.GetProfit().GetAsFloat(),
                        "AverageStockValue": fact.GetAverageStockValue().GetAsFloat(),
                        "ServiceLevelIndicator": fact.GetServiceLevelIndicator().GetAsFloat(),
                        "CO2Emissions": fact.GetCO2Emissions().GetAsFloat(),
                        "TotalDemand": fact.GetTotalDemand().GetAsFloat(),
                        "TotalServedQuantity": fact.GetTotalServedQuantity().GetAsFloat(),
                        "ServiceLevelSatisfaction": fact.GetTotalServedQuantity().GetAsFloat()
                        / fact.GetTotalDemand().GetAsFloat()
                        * 100,
                    }

        simulator_interface = co.CosmoInterface(
            simulator_path=simulator_path,
            custom_sim_engine=CosmoEngine,
            simulation_name=simulation_name,
            used_consumers=[],
            used_probes=used_probes,
            custom_consumers=[
                (PerformanceConsumer, "PerformanceConsumer", "PerformanceIndicators")
            ],
        )

        def get_outcomes(simulator_interface):
            data = simulator_interface.PerformanceConsumer.data
            return data

        simulationtask = co.ModelTask(
            modelinterface=simulator_interface,
            get_outcomes=get_outcomes,
            encode=encoder,
        )

        experiment = co.LocalSensitivityAnalysis(
            task=simulationtask, variables=list_of_variables, n_jobs=-2
        )

        t.display_message("Starting simulations")
        experiment.run()
        t.split("Ended simulations : {time_since_start}")

        results = reformat_results(
            experiment.results, simulation_name, change, variation, parameter
        )
        if saving_results:
            results.to_csv("Simulation/Output/SensitivityAnalysis.csv")

        # useful for tests
        if local:
            return results

        else:
            adx_writer.write_target_file(
                results.to_dict("records"),
                "LocalSensitivityAnalysis",
                EnvironmentVariables.simulation_id,
            )

            t.split("Sent stats to ADX : {time_since_last_split}")
            t.display_message("Running simple simulation to fill ADX")

            run_simple_simulation(
                simulation_name=simulation_name,
                amqp_consumer_adress=amqp_consumer_adress,
            )


def get_list_of_datapaths(simulator_path, entity_type):
    """
    Function to automatically retrieve the list of datapath on which the S.A will be performed, based on the entity type
    specified by the user.

    Args:
        simulator_path : path to the simulator
        entity_type : type of the entities on which the S.A will be performed
    Returns:
        list: list of datapaths on which the S.A will be used
    """

    # Retrieve the name of all the entities whose type corresponds to the one selected by the user
    list_of_datapaths = []
    sim1 = CosmoEngine.LoadSimulator(simulator_path)
    list_of_entities = sorted(
        transport.GetName()
        for transport in sim1.GetModel().FindEntitiesByType(entity_type)
    )

    sim2 = co.CosmoInterface(simulator_path)
    sim2.initialize()
    datapaths = sim2.get_datapaths()
    sim2.terminate()

    # For Transport Operation we retrieve the attribute ActualDurationSchedule. If it doesn't exist or
    # is an empty dict we take Duration instead
    if entity_type == "TransportOperation":
        for entity in list_of_entities:
            try:
                datapath = list(
                    filter(
                        lambda x: str("{Entity}" + entity + "::@ActualDurationSchedule")
                        in x,
                        datapaths,
                    )
                )[0]
                if (
                    sim1.FindAttribute(datapath).Get() == {}
                ):  # Check that the attribute isn't an empty dict.
                    raise IndexError  # If it is, we use the attribute Duration instead.
                else:
                    list_of_datapaths.append(datapath)

            except IndexError:
                list_of_datapaths.append(
                    list(
                        filter(
                            lambda x: str("{Entity}" + entity + "::@Duration") in x,
                            datapaths,
                        )
                    )[0]
                )
    # For Machine entities we retrieve the attribute OpeningTimeSchedule
    elif entity_type == "Machine":
        for entity in list_of_entities:
            list_of_datapaths.append(
                list(
                    filter(
                        lambda x: str("{Entity}" + entity + "::@OpeningTimeSchedule")
                        in x,
                        datapaths,
                    )
                )[0]
            )
    return list_of_datapaths


def create_variables(simulator_path, datapaths, change, variation):
    """
    Function to create the list of variables to perform the S.A based on a list of datapaths.
    Each datapath corresponds to an attribute in the model. If the attribute is of type "schedule":
    i.e {'time_step_0': value on time step 0, [...], 'time_step_k': value on time step k}
    the function will create more than one variable per datapath. More precisely n variables all belonging to
    the same group will be created, where n corresponds to the number of items in the dic. For example,
    the following attribute : {'0': 3, '2': 4, '7':2} will lead to the creation of the following variables:
    {"name": datapath__@__0,
     "type": int),
     "reference": 3,
     "variation": variation,
     "change": change,
     "group": datapath,
                }
    {"name": datapath__@__2,
     "type": int),
     "reference": 4,
     "variation": variation,
     "change": change,
     "group": datapath,
                }
    {"name": datapath__@__7,
     "type": int),
     "reference": 2,
     "variation": variation,
     "change": change,
     "group": datapath,
                }

    Args:
        simulator_path : path to the simulator
        datapaths : list containing the datapaths that need to be mapped to a variable
        change : change mode of the S.A
        variation : variation of the variable for the S.A

    Returns
        list_of_variables : list of dic where each dic is a variable according to the
        definition of a variable in CoMETs' sensitivity analysis

    """
    sim = CosmoEngine.LoadSimulator(simulator_path)
    list_of_variables = []
    for elements in datapaths:
        reference = sim.FindAttribute(elements).Get()

        if type(reference) == dict:
            for key in reference:
                variable = {
                    "name": str(elements + "__@__" + str(key)),
                    "type": get_type(reference[key]),
                    "reference": reference[key],
                    "variation": variation,
                    "change": change,
                    "group": elements,
                }
                list_of_variables.append(variable)

        else:
            variable = {
                "name": elements,
                "type": get_type(reference),
                "reference": reference,
                "variation": variation,
                "change": change,
            }
            list_of_variables.append(variable)

    return list_of_variables


def get_type(value):
    """
    Function to return the value's type. Instead of returning "<class 'int'>" the function returns 'int'.
    Similarly, for float, instead of <class 'float'>" the function returns 'float'
    """

    if type(value) == type(2):
        return "int"
    elif type(value) == type(0.2):
        return "float"


def reformat_results(row_results, simulation_name, change, variation, parameter):
    """
    Function to reformat the S.A results to be compatible with the adx table.

    """
    df = row_results.reset_index()
    df["SimulationRun"] = EnvironmentVariables.simulation_id
    df["ScenarioName"] = simulation_name
    df["SensitivityParameters"] = parameter + "   " + str(variation) + "   " + change
    if (
        "Group" not in df.columns
    ):  # if there is no 'Group' column, creates one where the name of the groups correspond to the ID.
        df.insert(1, "Group", df["Name"])
    df["Name"] = df["Name"].apply(
        lambda name: (
            name.removeprefix("Model::{Entity}IndustrialNetwork::{Entity}").split("::@", 1)[0]
            + (
                f".{name.rsplit('__@__', 1)[1]}"
                if "__@__" in name
                else ""
            )
        )
    )

    df = df.rename(
        columns={
            "Output": "KPI",
            "Name": "ID",
            "ReferenceOutputValue": "ReferenceKPI",
            "NewOutputValue": "NewKPI",
            "Difference": "Gap",
        }
    )
    if type(df["ReferenceInputValue"][0]) == dict:
        for i in range(len(df.index)):
            df["ReferenceInputValue"][i] = df["ReferenceInputValue"][i][0]
            df["NewInputValue"][i] = df["NewInputValue"][i][0]

    return df
