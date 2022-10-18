import pandas
from pathlib import Path
from pandas.api.types import is_string_dtype
from os import listdir, getcwd

from dotations_locales_back.common.mapping.criteres_dgcl_2020 import (
    columns_to_keep_2020,
)
from dotations_locales_back.common.mapping.criteres_dgcl_2021 import (
    columns_to_keep_2021,
)
from dotations_locales_back.common.mapping.criteres_dgcl_2022 import (
    columns_to_keep_2022,
)

"""Ensemble de fonctions permettant de mettre en forme les données contenant les critères de repartition des dotations.
Disponible ici : http://www.dotations-dgcl.interieur.gouv.fr/consultation/criteres_repartition.php
Les fichiers sont téléchargés puis mis au format csv et se trouvent dans le dossier /data du projet. 
"""

code_insee = "Informations générales - Code INSEE de la commune"


def load_dgcl_file(path="/data/criteres_repartition_2021.csv"):
    try:
        print(f"Loading {Path(path).resolve()}")
        data = pandas.read_csv(path, decimal=",", dtype={code_insee: str})
    except FileNotFoundError:
        print("file", path, "was not found")
        print("ls :", listdir("."))
        print("cwd :", getcwd())
        raise
    return data


def delete_unecessary_columns(data, columns_to_keep):
    """Supprime les colonnes inutiles de la dataframe pour l'API du MVP"""
    data = data[list(columns_to_keep.keys())]
    return data


def rename_columns(data, columns_to_rename):
    """Renome les colonnes de data avec les noms de variables openfisca
    La table de renommage est fixée dans ce fichier python
    Arguments :
    - data : dataframe contenant les données de la DGCL
    """

    data.rename(
        columns={
            old_name: new_name for old_name, new_name in columns_to_rename.items()
        },
        inplace=True,
    )
    return data


def dsr_calculation(data):
    """Permet de calculer la dotation de solidarité rurale pour chaque commune.
    Arguments :
    - data : dataframe contenant les données de la DGCL avec colonnes nommées avec les noms de variables openfisca
    Retourne :
    - data : la même dataframe avec une colonne en plus contenant le montant de la DSR
    """
    data["dotation_solidarite_rurale"] = (
        data["dsr_fraction_bourg_centre"]
        + data["dsr_fraction_perequation"]
        + data["dsr_fraction_cible"]
    )
    return data


def convert_cols_to_real_bool(data):
    """Convertit les colonnes contenant des "OUI" ou "NON" en vrai booléens "True" ou "False"
    La liste des colonnes est fixée "en dur" dans la fonction
    Arguments :
    - data : dataframe contenant les données de la DGCL avec colonnes nommées avec les noms de variables openfisca
    Retourne :
    - data : la même dataframe avec des colonnes contenant des vrais booléens"""
    columns_list_to_convert = [
        "zone_de_montagne",
        "insulaire",
        "zrr",
        "bureau_centralisateur",
        "chef_lieu_arrondissement",
        "chef_lieu_departement_dans_agglomeration",
    ]
    for col in columns_list_to_convert:
        if is_string_dtype(data[col]):
            data[col] = data[col].str.contains(pat="oui", case=False)
        else:
            data[col] = data[col].astype(bool)
    return data


def convert_cols_types(data):
    """Convertit le types de certaines colonnes contenant des données aux types mixtes.
    On remplace aussi les valeurs "nd" qui, à priori signifie "Non défini", par la valeur 0.
    La liste des colonnes est fixée "en dur" dans la fonction
    Arguments :
    - data : dataframe contenant les données de la DGCL avec colonnes nommées avec les noms de variables openfisca
    Retourne :
    - data : la même dataframe avec les types des colonnes convertis"""
    columns_list_to_convert = [
        "population_enfants",
        "longueur_voirie",
        "part_population_canton",
    ]
    for col in columns_list_to_convert:
        data[col] = data[col].replace("nd", 0)
    data["population_enfants"] = data["population_enfants"].astype(int)
    data["longueur_voirie"] = data["longueur_voirie"].astype(float)
    data["part_population_canton"] = data["part_population_canton"].astype(float)
    return data


def load_dgcl_data(path, year):
    data = load_dgcl_file(path)
    if year == 2022:
        data = delete_unecessary_columns(data, columns_to_keep_2022)
        data = rename_columns(data, columns_to_keep_2022)
        data = convert_cols_types(data)
    elif year == 2021:
        data = delete_unecessary_columns(data, columns_to_keep_2021)
        data = rename_columns(data, columns_to_keep_2021)
    elif year == 2020:
        data = delete_unecessary_columns(data, columns_to_keep_2020)
        data = rename_columns(data, columns_to_keep_2020)
    else:
        raise ValueError(
            "Year must be 2020, 2021 or 2022, others years are not supported"
        )
    data = dsr_calculation(data)
    data = convert_cols_to_real_bool(data)
    return data
