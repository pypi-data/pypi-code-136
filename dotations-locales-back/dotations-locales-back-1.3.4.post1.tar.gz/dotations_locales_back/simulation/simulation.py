from os import getcwd
from pandas import read_csv

from openfisca_core.simulation_builder import SimulationBuilder
from openfisca_france_dotations_locales import (
    CountryTaxBenefitSystem as DotationsLocales,
)

from dotations_locales_back.simulation.load_dgcl_data import (
    adapt_dgcl_data,
    insert_dsu_garanties,
    insert_dsr_garanties_communes_nouvelles,
    get_last_year_dotations,
)

from dotations_locales_back.common.load_dgcl_criteres_data import load_dgcl_file

# étapes :
# data : injecter les données DGCL
# data : ajouter les colonnes manquantes aux données DGCL
# data : injecter la réforme des critères de l'usager
# loi : openfisca_france_dotations_locales (+ réforme au moment du PLF)
# data + loi : faire tourner la simulation sur ces données


# récupération des données brutes

DATA_DIRECTORY = getcwd() + "/data/"
CURRENT_YEAR = 2022

# DGCL data
DATA_2021_PATH = DATA_DIRECTORY + f"criteres_repartition_{CURRENT_YEAR-1}.csv"
DATA_2022_PATH = DATA_DIRECTORY + f"criteres_repartition_{CURRENT_YEAR}.csv"

# Garanties DSU estimées
# TODO vérifier si garanties 2021 calculées à la main (quand loi = PLF 2022)
# ou si garanties estimées pour 2022 sur la base des garanties 2021 (quand loi = PLF 2022)
GARANTIES_DSU_PATH = DATA_DIRECTORY + "garanties_dsu.csv"


# transformation des données brutes en DataFrame
# on complète par des associations entre colonnes des données DGCL@

dgcl_data_2021 = load_dgcl_file(DATA_2021_PATH)
# adapted_data_2021 = adapt_dgcl_data(dgcl_data_2021, "2021")

dgcl_data_2022 = load_dgcl_file(DATA_2022_PATH)
adapted_data_2022 = adapt_dgcl_data(dgcl_data_2022, "2022")

# ajout des garanties dsu toutes périodes (2019 -> 2022)
# insertion des garanties 2022 au titre de la DSU (non calculées explicitement dans OFDL)

fully_adapted_data_2022 = insert_dsu_garanties(
    adapted_data_2022, str(CURRENT_YEAR), GARANTIES_DSU_PATH
)

# insertion des garanties communes nouvelles au titre de la DSR (non calculées explicitement dans OFDL)
# TODO attention ! corriger ; par défaut, renvoie les garanties 2020 si l'année demandée > 2020
fully_adapted_data_2022 = insert_dsr_garanties_communes_nouvelles(
    fully_adapted_data_2022, str(CURRENT_YEAR)
)

results_2021_as_last_year = get_last_year_dotations(dgcl_data_2021, "2021")
data_2021_as_last_year = results_2021_as_last_year[
    [
        "Informations générales - Code INSEE de la commune",
        "dsu_montant_eligible",
        "dsr_montant_eligible_fraction_bourg_centre",
        "dsr_montant_eligible_fraction_perequation",
        "dsr_montant_hors_garanties_fraction_cible",
        "population_dgf_majoree",
        "dotation_forfaitaire",
    ]
]


# Initialisation du TBS
tbs = DotationsLocales()


def simulation_from_dgcl_csv(period, data, tbs, data_previous_year=None):
    # fonction importée de leximpact-server : dotations/simulation.py
    sb = SimulationBuilder()
    sb.create_entities(tbs)
    sb.declare_person_entity("commune", data.index)

    nombre_communes = len(data.index)
    etat_instance = sb.declare_entity("etat", ["france"])
    etat_communes = ["france"] * nombre_communes
    sb.join_with_persons(etat_instance, etat_communes, [None] * nombre_communes)

    simulation = sb.build(tbs)
    simulation.max_spiral_loops = 10

    for champ_openfisca in data.columns:
        if " " not in champ_openfisca:  # oui c'est comme ça que je checke
            # qu'une variable est openfisca ne me jugez pas
            simulation.set_input(
                champ_openfisca,
                period,
                data[champ_openfisca],
            )
    # data_previous_year est un dataframe dont toutes les colonnes
    # portent des noms de variables openfisca
    # et contiennent des valeurs de l'an dernier.
    if data_previous_year is not None:
        # on rassemble les informations de l'an dernier pour les communes
        # qui existent cette année (valeurs nouvelles communes à zéro)
        data = data.merge(
            data_previous_year,
            on="Informations générales - Code INSEE de la commune",
            how="left",
            suffixes=["_currentyear", ""],
        )
        for champ_openfisca in data_previous_year.columns:
            if " " not in champ_openfisca:  # oui c'est comme ça que je checke
                # qu'une variable est openfisca ne me jugez pas
                simulation.set_input(
                    champ_openfisca,
                    str(int(period) - 1),
                    data[champ_openfisca].fillna(0),
                )
    return simulation


def replace_commune_simulation_criteres(
    code_comm, code_insee, simulation_criteres, data
):
    for critere in simulation_criteres.keys():
        data.loc[data[code_comm] == code_insee, critere] = simulation_criteres[critere]
    return data


def create_simulation_data(code_insee, simulation_criteres, real_data):
    simulation_data = real_data.copy()
    simulation_criteres_utiles = simulation_criteres.copy()
    simulation_criteres_utiles.pop("residences_secondaires")
    simulation_criteres_utiles.pop("places_caravanes_apres_majoration")
    simulation_data = replace_commune_simulation_criteres(
        "Informations générales - Code INSEE de la commune",
        code_insee,
        simulation_criteres_utiles,
        simulation_data,
    )
    return simulation_data


def calculate_dotations(simulation_data, dotations_criteres_data):
    simulation_2022 = simulation_from_dgcl_csv(
        CURRENT_YEAR,
        simulation_data,
        tbs,
        data_previous_year=data_2021_as_last_year,
    )

    dotation_forfaitaire = simulation_2022.calculate(
        "dotation_forfaitaire", CURRENT_YEAR
    )
    dsu_montant = simulation_2022.calculate("dsu_montant", CURRENT_YEAR)
    dsr_fraction_bourg_centre = simulation_2022.calculate(
        "dsr_fraction_bourg_centre", CURRENT_YEAR
    )
    dsr_fraction_perequation = simulation_2022.calculate(
        "dsr_fraction_perequation", CURRENT_YEAR
    )
    dsr_fraction_cible = simulation_2022.calculate("dsr_fraction_cible", CURRENT_YEAR)
    simulated_data = dotations_criteres_data.copy()
    simulated_data["dotation_forfaitaire"] = dotation_forfaitaire
    simulated_data["dsu_montant"] = dsu_montant
    simulated_data["dsr_fraction_bourg_centre"] = dsr_fraction_bourg_centre
    simulated_data["dsr_fraction_perequation"] = dsr_fraction_perequation
    simulated_data["dsr_fraction_cible"] = dsr_fraction_cible
    simulated_data["dotation_solidarite_rurale"] = (
        simulated_data["dsr_fraction_bourg_centre"]
        + simulated_data["dsr_fraction_perequation"]
        + simulated_data["dsr_fraction_cible"]
    )
    return simulated_data


def calcul_population_dgf(pop_insee, residences_secondaires, places_caravanes):
    return pop_insee + residences_secondaires + places_caravanes


def openfisca_simulation(code_insee, simulation_criteres, dotations_criteres_data):
    # On calcule la population dgf plus d'infos ici : https://www.cnis.fr/wp-content/uploads/2018/01/DC_2010_populations_legales_calcul_DGF.pdf
    simulation_criteres["population_dgf"] = calcul_population_dgf(
        simulation_criteres["population_insee"],
        simulation_criteres["residences_secondaires"],
        simulation_criteres["places_caravanes_apres_majoration"],
    )

    # On injecte les critères "simulés" dans la DF adaptée venant du tableau DGCL
    simulation_data = create_simulation_data(
        code_insee, simulation_criteres, fully_adapted_data_2022
    )

    # On calcule les dotations à partir du tableau dgcl contenant les données simulées
    simulated_data = calculate_dotations(simulation_data, dotations_criteres_data)

    # Pour la réponse, on réinjecte les critères simulés par l'utilisateur
    simulated_data = replace_commune_simulation_criteres(
        "code_insee", code_insee, simulation_criteres, simulated_data
    )
    return simulated_data
