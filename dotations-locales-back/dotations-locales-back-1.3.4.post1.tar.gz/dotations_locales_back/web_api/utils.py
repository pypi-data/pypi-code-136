from dotations_locales_back.common.mapping.dotation_forfaitaire import *
from dotations_locales_back.common.mapping.dotation_solidarite_urbaine import *
from dotations_locales_back.common.mapping.dotation_nationale_perequation import *
from dotations_locales_back.common.mapping.dotation_solidarite_rurale import *
from dotations_locales_back.common.mapping.criteres_generaux import (
    unites_criteres_generaux,
)
from dotations_locales_back.common.search_commune import search_commune_by_code_insee

from dotations_locales_back.simulation.simulation import openfisca_simulation


def create_commune_criteres_structure(unites_criteres, **communes_datas):
    """Permet de créer un dictionnaire des critères nécessaire pour créer le body de réponse de l'endpoint /commune.
    Convertit aussi les données brutes venant du tableau DGCL au format attendu en sortie.
    Paramètres :
     - unites_criteres : dictionnaire listant les critères et leur unité
     - commune_data_2021 : Dataframe contenant les données 2021 de la commune appelée
     - commune_data_2022 : Dataframe contenant les données 2022 de la commune appelée"""
    criteres = {}
    for critere in unites_criteres.keys():
        year_list = []
        # Si le critères est un booléen, on remplace par Oui ou par Non.
        if unites_criteres[critere] == "boolean":
            unit = None
            for year in communes_datas:
                value = "Oui" if communes_datas.get(year)[critere].iloc[0] else "Non"
                year_list.append({year: {"valeur": value, "unite": unit}})

        # Pour tous les autres critères, on convertit seuelement en string la valeur
        else:
            unit = unites_criteres[critere]
            for year in communes_datas:
                value = str(communes_datas.get(year)[critere].iloc[0])
                year_list.append({year: {"valeur": value, "unite": unit}})
        criteres[critere] = {"annees": year_list}

    return criteres


def create_dotation_structure(dotation, **communes_datas):
    """Permet de créer un dictionnaire contenant le détail d'une dotation nécessaire pour créer le body de réponse de l'endpoint /commune.
    Paramètres :
     - dotation : Le nom de la dotation à traiter
     - commune_data_2021 : Dataframe contenant les données 2021 de la commune appelée
     - commune_data_2022 : Dataframe contenant les données 2022 de la commune appelée"""
    year_list = []
    for year in communes_datas:
        year_list.append({year: communes_datas.get(year)[dotation].iloc[0]})
    dot = {
        "annees": year_list,
    }
    unites_criteres = eval(dotation + "_unites_criteres")
    if len(unites_criteres.keys()) != 0:
        dot["criteres"] = create_commune_criteres_structure(
            unites_criteres, **communes_datas
        )
    return dot


def create_commune_dotations_structure(dotations_list, **communes_datas):
    """Permet de créer un dictionnaire contenant toutes les dotations nécessaire pour créer le body de réponse de l'endpoint /commune.
    Paramètres :
     - dotations_list : Liste des dotations à servir en réponse
     - commune_data_2021 : Dataframe contenant les données 2021 de la commune appelée
     - commune_data_2022 : Dataframe contenant les données 2022 de la commune appelée"""
    dotations = {}
    for dotation in dotations_list:
        dotations[dotation] = create_dotation_structure(dotation, **communes_datas)
        sous_dotations = eval(dotation + "_sous_dotations")
        if len(sous_dotations) != 0:
            dotations[dotation]["sous_dotations"] = []
            for sous_dotation in sous_dotations:
                dotations[dotation]["sous_dotations"].append(
                    {
                        sous_dotation: create_dotation_structure(
                            sous_dotation, **communes_datas
                        ),
                    }
                )
    return dotations


def create_commune_response(code_insee, dotations_list, **communes_datas):
    """Permet de créer la réponse de l'endpoint /commune.
    Paramètres :
     - code_insee : Code INSEE de la commune passé en paramètre de l'appel
     - dotations_list : Liste des dotations à servir en réponse
     - commune_data_2021 : Dataframe contenant les données 2021 de la commune appelée
     - commune_data_2022 : Dataframe contenant les données 2022 de la commune appelée"""
    response = {
        "code_insee": code_insee,
        "dotations": create_commune_dotations_structure(
            dotations_list, **communes_datas
        ),
        "criteres_generaux": create_commune_criteres_structure(
            unites_criteres_generaux, **communes_datas
        ),
    }

    return response


def create_simulation_response(
    code_insee, simulation_parameters, dotations_criteres, dotations_list, periode
):
    simulation = openfisca_simulation(
        code_insee,
        simulation_parameters,
        dotations_criteres,
    )
    simulated_data = search_commune_by_code_insee(simulation, code_insee)
    commune_data = search_commune_by_code_insee(dotations_criteres, code_insee)
    communes_datas = {
        "simulation": simulated_data,
        "2022": commune_data,
    }
    response = create_commune_response(code_insee, dotations_list, **communes_datas)
    return response
