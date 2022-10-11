import multiprocessing
from typing import Union
from Supplychain.Wrappers.simulator import CosmoEngine
from Supplychain.Generic.adx_and_file_writer import ADXAndFileWriter
from Supplychain.Generic.timer import Timer
from Supplychain.Wrappers.environment_variables import EnvironmentVariables
from Supplychain.Run.simulation import run_simple_simulation
import comets as co


def uncertainty_analysis(
    simulation_name: str,
    simulation_path: str = "Simulation",
    amqp_consumer_adress: Union[str, None] = None,
    sample_size: int = 1000,
    batch_size: int = 100,
    adx_writer: Union[ADXAndFileWriter, None] = None,
    validation_folder: Union[str, None] = None,
):

    with Timer("[Run Uncertainty]") as t:
        if batch_size > sample_size:
            batch_size = sample_size

        processes_size = min(multiprocessing.cpu_count(), batch_size)

        used_probes = ["PerformanceIndicators", "Stocks"]
        used_consumers = ['PerformanceIndicatorsAMQP']

        class StockConsumer:
            def __init__(self):
                self.memory = list()

            def Consume(self, p_data):
                probe_output = self.engine.StocksProbeOutput.Cast(p_data)
                f = probe_output.GetFacts()
                timestep = int(
                    probe_output.GetProbeRunDimension().GetProbeOutputCounter()
                )
                for data in f:
                    fact = [
                        str(data.GetAttributeAsString("ID")),
                        timestep,
                        float(data.GetAttributeAsFloat64("Demand")),
                        float(data.GetAttributeAsFloat64("RemainingQuantity")),
                        float(data.GetAttributeAsFloat64("ServedQuantity")),
                        float(data.GetAttributeAsFloat64("UnservedQuantity")),
                    ]
                    self.memory.append(fact)

        simulator_interface = co.CosmoInterface(
            simulator_path=simulation_path,
            custom_sim_engine=CosmoEngine,
            simulation_name=simulation_name,
            amqp_consumer_address=amqp_consumer_adress,
            used_consumers=used_consumers,
            used_probes=used_probes,
            custom_consumers=[(StockConsumer, "LocalConsumer", "Stocks")],
        )
        # Getting the name of all the transport operations
        all_transports = get_transports(simulation_path)

        # Retrieving model information
        (
            max_time_step,
            distribution,
            actual_duration_schedule,
            list_of_transports,
            uncertainty_param_1,
            uncertainty_param_2,
            uncertainty_param_3,
            uncertainty_param_4,
        ) = model_info(simulator_interface, all_transports)

        distribution_params = get_distribution_parameter(distribution)

        # Extending the dictionaries above
        extended_actual_duration = extend_dic(
            actual_duration_schedule, max_time_step, list_of_transports
        )
        extended_param_1 = extend_dic(
            uncertainty_param_1, max_time_step, list_of_transports
        )
        extended_param_2 = extend_dic(
            uncertainty_param_2, max_time_step, list_of_transports
        )
        extended_param_3 = extend_dic(
            uncertainty_param_3, max_time_step, list_of_transports
        )
        extended_param_4 = extend_dic(
            uncertainty_param_4, max_time_step, list_of_transports
        )

        # The encoder takes a parameterset with the following format :
        # {'{Model} [..] Seed': 3251851028, 'T_@_0': 1.7504164949122698, 'T_@_1': 3.05256524351985, [...] 'T_@_10': 3.2371899035525793}
        # Except for the seed, the keys corresponds to: transport_name +_@_ + time_step
        # And returns a parameterset where the information for each transport's duration is transformed in one dictionary and updated as follows:
        # new_transport_duration = max(0, round(old_transport_duration + sample draw from the distribution))
        # {'Model [..] T::@ActualDurationSchedule': {'0': 5, '1': 6, [..] '10': 44}, '{Model}Model::{Attribute}Seed': 3209521878}
        def encoder(parameters):
            encoded_parameterset = {
                "{Model}Model::{Attribute}Seed": parameters[
                    "{Model}Model::{Attribute}Seed"
                ],
            }
            for transports in list_of_transports:
                ActualDurationSchedule = {}
                for i in range(len(extended_actual_duration[transports])):
                    ActualDurationSchedule[str(i)] = max(
                        0,
                        round(
                            extended_actual_duration[transports][i]
                            + parameters[f"{transports}_@_{i}"]
                        ),
                    )
                encoded_parameterset[
                    f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transports}::@ActualDurationSchedule"
                ] = ActualDurationSchedule
            return encoded_parameterset

        # Returns a parameter set with all the model's output. More precisely, the parameter set is the
        # the result of the concatenation of two parameter sets. The first one looks like this:
        # {'U__&@&__0': 5, 'U__&@&__1': 5, [...], 'U__&@&__10': 6}. The keys correspond to transport_name + __&@&__ +
        # time_step. The second parameter set looks like this:
        # {'A__&@&__ServedQuantity__&@&__0': 0.0, 'A__&@&__UnservedQuantity__&@&__0': 0.0}. The keys correspond to
        # stock + __&@&__ + category + time_step
        def get_outcomes(modelinterface):
            transport_duration = get_transport_duration(
                all_transports, modelinterface, max_time_step
            )
            transports_and_consumer = {
                **transport_duration,
                **transform_consumer_memory(modelinterface.LocalConsumer.memory),
            }

            return transports_and_consumer

        simulationtask = co.ModelTask(
            modelinterface=simulator_interface,
            encode=encoder,
            get_outcomes=get_outcomes,
        )

        # Creating the uncertainty analysis space
        space = creating_space(
            distribution,
            extended_param_1,
            extended_param_2,
            extended_param_3,
            extended_param_4,
            list_of_transports,
            distribution_params,
            max_time_step,
        )
        # adding the seed as an uncertain parameter
        space.append(
            {
                "name": "{Model}Model::{Attribute}Seed",
                "sampling": "seed_generator",
            }
        )
        experiment = co.UncertaintyAnalysis(
            task=simulationtask,
            sampling=space,
            stop_criteria={"max_evaluations": sample_size},
            analyzer=["standard", "quantiles"],
            n_jobs=processes_size,
        )

        t.display_message("Starting simulations")
        experiment.run()
        t.split("Ended simulations : {time_since_start}")
        # Separating the results data on the stock from the results data on transport's duration.
        transport_limiter = len(all_transports) * max_time_step
        df_probe_data = experiment.results["statistics"].iloc[transport_limiter:-1, :]
        df_probe_data.reset_index(inplace=True)
        df_transport_duration = experiment.results["statistics"].iloc[
            0:transport_limiter, :
        ]
        df_transport_duration.reset_index(inplace=True)

        # Transforming the data on both the stock and the transport duration
        df_stock_final = transform_stock_data(df_probe_data)
        df_transport_final = transform_transport_data(df_transport_duration)

        if validation_folder:
            # Saving the results
            df_stock_final.to_csv(str(validation_folder) + "/final_df_comets.csv")
            df_transport_final.to_csv(str(validation_folder) + "/df_transport.csv")

        if adx_writer is not None:
            adx_writer.write_target_file(
                df_stock_final.to_dict("records"), "StockUncertaintiesStatistics"
            )
            adx_writer.write_target_file(
                df_transport_final.to_dict("records"), "TransportUncertaintyStatistics"
            )
            t.split("Sent stats to ADX : {time_since_last_split}")
        t.display_message("Running simple simulation to fill ADX")
        # Put back log level to Info for final simulation
        # Reduce log level to Error during optimization
        logger = CosmoEngine.LoggerManager_GetInstance().GetLogger()
        logger.SetLogLevel(logger.eInfo)

        stop_uncertainty = {"Model::@ActivateUncertainties": "false"}

        run_simple_simulation(
            simulation_name=simulation_name,
            simulation_path=simulation_path,
            amqp_consumer_adress=amqp_consumer_adress,
            modifications=stop_uncertainty,
        )


# Function to get the list of all the transports in the simulation
def get_transports(simulation_path):
    transports_list = []
    temporary_simulator = CosmoEngine.LoadSimulator(simulation_path)
    transports = temporary_simulator.get_entities_names_by_type(
        entity_type="TransportOperation"
    )
    temporary_simulator = None
    for keys in transports:
        transports_list.append(keys)
    return transports_list


def get_distribution_parameter(my_distribution):
    return co.DistributionRegistry.information[str(my_distribution)]["parameters"]


# Function to get the model information for each transports, such as the distribution used and
# Its parameters
def model_info(my_simulator, transports_names):
    my_simulator.initialize()
    actual_duration_schedule = {}
    list_of_transports = transports_names.copy()
    uncertainty_param_1 = {}
    uncertainty_param_2 = {}
    uncertainty_param_3 = {}
    uncertainty_param_4 = {}

    time_step_per_cycle = my_simulator.get_outputs(["Model::@TimeStepPerCycle"])[
        "Model::@TimeStepPerCycle"
    ]

    number_of_cycle = my_simulator.get_outputs(["Model::@NumberOfCycle"])[
        "Model::@NumberOfCycle"
    ]

    max_time_step = time_step_per_cycle * number_of_cycle

    distribution = my_simulator.get_outputs(
        ["Model::@TransportUncertaintiesProbabilityDistribution"]
    )["Model::@TransportUncertaintiesProbabilityDistribution"]

    for transport in transports_names:

        # If their is no ActualDuration in the TransportSchedules column of the dataset,
        # we use by default the attribute duration, in the Transport column of the dataset.
        if (
            my_simulator.get_outputs(
                [
                    f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@ActualDurationSchedule"
                ]
            )[
                f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@ActualDurationSchedule"
            ]
            == {}
        ):
            duration = my_simulator.get_outputs(
                [
                    f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@Duration"
                ]
            )[f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@Duration"]

            # Use a dict format so that the function "extended_dict" defined below can be applied
            actual_duration_schedule[transport] = {0: duration}
        else:
            actual_duration_schedule[transport] = my_simulator.get_outputs(
                [
                    f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@ActualDurationSchedule"
                ]
            )[
                f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@ActualDurationSchedule"
            ]

        uncertainty_param_1[transport] = my_simulator.get_outputs(
            [
                f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@TransportUncertaintiesParameter1"
            ]
        )[
            f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@TransportUncertaintiesParameter1"
        ]
        uncertainty_param_2[transport] = my_simulator.get_outputs(
            [
                f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@TransportUncertaintiesParameter2"
            ]
        )[
            f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@TransportUncertaintiesParameter2"
        ]
        uncertainty_param_3[transport] = my_simulator.get_outputs(
            [
                f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@TransportUncertaintiesParameter3"
            ]
        )[
            f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@TransportUncertaintiesParameter3"
        ]
        uncertainty_param_4[transport] = my_simulator.get_outputs(
            [
                f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@TransportUncertaintiesParameter4"
            ]
        )[
            f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@TransportUncertaintiesParameter4"
        ]
        # If the transport has no parameters, its transport duration will not be part of the uncertainty analysis
        if (
            uncertainty_param_1[transport] == uncertainty_param_2[transport]
            and uncertainty_param_1[transport] == {}
        ):
            list_of_transports.remove(transport)

    my_simulator.terminate()
    return (
        max_time_step,
        distribution,
        actual_duration_schedule,
        list_of_transports,
        uncertainty_param_1,
        uncertainty_param_2,
        uncertainty_param_3,
        uncertainty_param_4,
    )


# Function to extend dictionaries using transport schedules.
# the following dic: {0: 3, 6: 4, 7: 3, 8: 2, 9: 8, 10: 40}
# Becomes: {0: 3, 1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 4, 7: 3, 8: 2, 9: 8, 10: 40}
def extend_simple_dic(my_dic, number_of_iterations):
    if my_dic != {}:  # checking that the dic isn't empty
        extended_dic = {
            0: my_dic[0]
        }  # We assume that the uncertainty starts at the first time step
        for i in range(1, number_of_iterations):
            if i in my_dic:
                extended_dic[i] = my_dic[i]
            else:
                extended_dic[i] = extended_dic[i - 1]
    else:
        extended_dic = {}
    return extended_dic


# Function to extend dictionaries using transport schedules.
# For each transports, the following dic: {"transport name" : {0: 3, 6: 4, 7: 3, 8: 2, 9: 8, 10: 40}}
# Becomes: {"transport name" : {0: 3, 1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 4, 7: 3, 8: 2, 9: 8, 10: 40}}
def extend_dic(my_dic, number_of_iterations, transports_names):
    extended_dic = {}
    for transports in transports_names:
        extended_dic[transports] = extend_simple_dic(
            my_dic[transports], number_of_iterations
        )
    return extended_dic


# this function transforms supply chain's distribution parameters
# that don't match CoMETS format
def check_distrib_parameters(
    my_distribution, param1, param2, param3, param4, transports_names
):
    # In CoMETS the upper bound of the discreteuniform distribution is excluded.
    # However, in supply chain it is included. Therefore, we need to add 1 to the upper bound
    # so it matches CoMETS
    if my_distribution == "discreteuniform":
        for transport in transports_names:
            for keys in param2[transport].keys():
                param2[transport][keys] += 1

    # In CoMETS the two arguments of the uniform distribution are loc and scale
    # and the interval of the distribution is the following:  [loc, loc+scale]
    # However, in supply chain the two parameters of the uniform distribution are
    # [lower, upper]. Therefor, upper needs to be mapped to scale
    if my_distribution == "uniform":
        for transport in transports_names:
            for keys in param2[transport].keys():
                param2[transport][keys] = (
                    param2[transport][keys] - param1[transport][keys]
                )

    if my_distribution == "betabinom":
        for transport in transports_names:
            for keys in param1[transport].keys():
                param1[transport][keys] = round(param1[transport][keys])

    if my_distribution == "binomial":
        for transport in transports_names:
            for keys in param1[transport].keys():
                param1[transport][keys] = round(param1[transport][keys])

    if my_distribution == "hypergeom":
        for transport in transports_names:
            for keys in param1[transport].keys():
                param1[transport][keys] = round(param1[transport][keys])
                param2[transport][keys] = round(param2[transport][keys])
                param3[transport][keys] = round(param3[transport][keys])

    return [param1, param2, param3, param4]


# Function to create the uncertainty analysis space according to CoMETS format
# This function will create one variable for each time step of each transports
# distribution: name of the distribution used for the ua
# param1: values by transport by time step for the first parameter of the distribution
# param2: values by transport by time step for the second parameter of the distribution
# param3: values by transport by time step for the third parameter of the distribution
# param4: values by transport by time step for the fourth parameter of the distribution
# transports: list of all the uncertain transports names
# distribution_parameters: list of the parameters names required by CoMETS sampler for the given distribution
# number_of_time_steps: number of time step simulated
def creating_space(
    distribution, param1, param2, param3, param4, transports, distribution_parameters, number_of_time_steps
):
    sampling = []
    all_parameters = check_distrib_parameters(
        distribution, param1, param2, param3, param4, transports
    )
    for transport in transports:
        considered_parameters = [
            (position, parameter)
            for position, parameter in enumerate(distribution_parameters)
            if all_parameters[position][transport]
        ]
        for t in range(number_of_time_steps):
            parameters = {
                parameter: all_parameters[position][transport][t]
                for position, parameter in considered_parameters
            }
            sampling.append(
                {
                    "name": f"{transport}_@_{t}",
                    "sampling": distribution,
                    "parameters": parameters,
                }
            )
    return sampling


# Function that returns a parameterset with the transport duration for each transport at the end of the simulation
# The transport duration is separated for each time step. The output parameterset (for a simulation
# with 1 TransportOperation: U) will have the following format:
#    {Model[...]U::@ActualDurationSchedule__&@&__0': 10,
#          [...],
#     Model[...]U::@ActualDurationSchedule__&@&__10': 7}
def get_transport_duration(transports_names, modelinterface, max_time_step):
    transport_duration = {}
    transport_duration_transformed = {}
    for transport in transports_names:
        if (
            modelinterface.get_outputs(
                [
                    f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@ActualDurationSchedule"
                ]
            )[
                f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@ActualDurationSchedule"
            ]
            == {}
        ):
            duration = modelinterface.get_outputs(
                [
                    f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@Duration"
                ]
            )[f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@Duration"]
            # Use a dict format so that the function "extended_dict" defined below can be applied
            actual_duration_schedule = {0: duration}
        else:
            actual_duration_schedule = modelinterface.get_outputs(
                [
                    f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@ActualDurationSchedule"
                ]
            )[
                f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@ActualDurationSchedule"
            ]
        transport_duration[
            f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@ActualDurationSchedule"
        ] = extend_simple_dic(
            actual_duration_schedule,
            max_time_step,
        )
        time_step = 0
        for value in transport_duration[
            f"Model::{{Entity}}IndustrialNetwork::{{Entity}}{transport}::@ActualDurationSchedule"
        ].values():
            transport_duration_transformed[f"{transport}__&@&__{time_step}"] = value
            time_step += 1
    return transport_duration_transformed


# This function transform the consumer memory from a list of list to a list of
# ParameterSet. Note that each sublist in the initial format is transformed into
# a parameterset of 4 parameters : Demand, RemainingQuantity, ServedQuantity,UnservedQuantity
def transform_consumer_memory(transform_consumer_memory):
    dic_of_parameterset = {}
    for elements in transform_consumer_memory:
        dic_of_parameterset[
            str(elements[0] + "__&@&__" + "Demand" + "__&@&__" + str(elements[1]))
        ] = elements[2]
        dic_of_parameterset[
            str(
                elements[0]
                + "__&@&__"
                + "RemainingQuantity"
                + "__&@&__"
                + str(elements[1])
            )
        ] = elements[3]
        dic_of_parameterset[
            str(
                elements[0]
                + "__&@&__"
                + "ServedQuantity"
                + "__&@&__"
                + str(elements[1])
            )
        ] = elements[4]
        dic_of_parameterset[
            str(
                elements[0]
                + "__&@&__"
                + "UnservedQuantity"
                + "__&@&__"
                + str(elements[1])
            )
        ] = elements[5]
    return dic_of_parameterset


def transform_stock_data(data):
    # Splitting the first columns into 3 columns: TimeStep, StockId, Category
    # And adding the simulationRun
    temporary_df = data.copy()
    temporary_df.loc[:, "SimulationRun"] = EnvironmentVariables.simulation_id
    temporary_df[["StockId", "Category", "TimeStep"]] = temporary_df["index"].str.split(
        pat="__&@&__", expand=True
    )

    # Removing unused columns such as index, quantile 10 ...
    temporary_df = temporary_df.iloc[:, [1, 3, 5, 9, 14, 19, 23, 24, 25, 26, 27]]

    # Changing the columns' order and renaming them to match the adx table
    df_final = temporary_df[
        [
            "TimeStep",
            "SimulationRun",
            "StockId",
            "quantile 5%",
            "quantile 25%",
            "quantile 50%",
            "quantile 75%",
            "quantile 95%",
            "mean",
            "sem",
            "Category",
        ]
    ]

    df_final.rename(
        columns={
            "quantile 5%": "Percentile5",
            "quantile 25%": "Percentile25",
            "quantile 50%": "Percentile50",
            "quantile 75%": "Percentile75",
            "quantile 95%": "Percentile95",
            "mean": "Mean",
            "sem": "SE",
        },
        inplace=True,
    )
    return df_final


def transform_transport_data(data):

    # Adding the simulation run to the df
    temporary_df = data.copy()
    if not temporary_df.empty:
        temporary_df.loc[:, "SimulationRun"] = EnvironmentVariables.simulation_id
        # Splitting the first column into 2 columns: TransportOperation, TimeStep
        temporary_df[["TransportOperation", "TimeStep"]] = temporary_df["index"].str.split(
            pat="__&@&__", expand=True
        )
    else:
        temporary_df[["TransportOperation", "TimeStep"]] = None
    df_final = temporary_df.iloc[:, 1:]

    df_final.rename(
        columns={
            "confidence interval of the mean at 95%": "ConfidenceIntervalOfTheMeanAt95",
            "quantile 5%": "Percentile5",
            "quantile 10%": "Percentile10",
            "quantile 15%": "Percentile15",
            "quantile 20%": "Percentile20",
            "quantile 25%": "Percentile25",
            "quantile 30%": "Percentile30",
            "quantile 35%": "Percentile35",
            "quantile 40%": "Percentile40",
            "quantile 45%": "Percentile45",
            "quantile 50%": "Percentile50",
            "quantile 55%": "Percentile55",
            "quantile 60%": "Percentile60",
            "quantile 65%": "Percentile65",
            "quantile 70%": "Percentile70",
            "quantile 75%": "Percentile75",
            "quantile 80%": "Percentile80",
            "quantile 85%": "Percentile85",
            "quantile 90%": "Percentile90",
            "quantile 95%": "Percentile95",
        },
        inplace=True,
    )

    return df_final
