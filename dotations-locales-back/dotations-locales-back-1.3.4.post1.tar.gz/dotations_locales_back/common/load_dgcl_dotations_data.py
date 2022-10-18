from pandas import read_csv, concat
import os


"""Ensemble de fonctions permettant de mettre en forme les données contenant les montants des dotations.
Disponible ici : http://www.dotations-dgcl.interieur.gouv.fr/consultation/dotations_en_ligne.php
Les fichiers sont téléchargés puis mis au format csv et se trouvent dans le dossier /data du projet. 
"""


def load_dotation_data(path, dotation_name):
    """Renvoie un dataframe qui contient les données de la dotation passée en paramètre.
    Les données sont mises en forme pour faciliter leur utilisation dans le code.
    Paramètres :
        - path : chemin du fichier csv contenant les données de la dotation
        - dotation_name : nom de la dotation qui sera utilisé pour nommer la colonne du dataframe (utiliser les noms de variables openfisca)"""
    try:
        dotation_data = read_csv(
            path,
            delimiter=";",
            header=0,
            names=["commune", dotation_name],
            dtype={"commune": str, dotation_name: str},
        )
    except FileNotFoundError:
        print("file", path, "was not found")
        print("ls :", os.listdir("."))
        print("cwd :", os.getcwd())
        raise

    # On supprime les espaces qui représentent les milliers dans les montants.
    dotation_data[dotation_name] = dotation_data[dotation_name].str.replace(
        "\u202f", ""
    )
    dotation_data[dotation_name] = dotation_data[dotation_name].astype(float)

    # On sépare la première colonne en deux colonnes : code insee et nom de la commune
    dotation_data[["code_insee", "nom"]] = dotation_data["commune"].str.split(
        " - ", n=1, expand=True
    )
    dotation_data = dotation_data.filter(["code_insee", "nom", dotation_name], axis=1)
    return dotation_data


def concat_dotation_dfs(*dfs):
    """Fusionne tous les dataframes passées en entrée dans un dataframe global.
    Utilisé pour fusionner les données de toutes les dotations dans un seul dataframe.
    Calcule également le montant total de la dotation de solidarité rurale dans une colonne dédiée.
    Paramètre :
        - dfs : liste de dataframes à fusionner"""

    # On fusionne les donnés en prenant comme clé le code insee
    all_dotation = concat(
        [df.set_index("code_insee") for df in dfs], axis=1, join="outer"
    ).reset_index()

    # On enlève les colonnes "Communes" en trop
    all_dotation = all_dotation.loc[:, ~all_dotation.columns.duplicated()].copy()

    # On calcule la dotation de solidarité rurale totale
    if (
        "dsr_fraction_bourg_centre" in all_dotation.columns
        and "dsr_fraction_cible" in all_dotation.columns
        and "dsr_fraction_perequation" in all_dotation.columns
    ):
        all_dotation["dotation_solidarite_rurale"] = (
            all_dotation["dsr_fraction_bourg_centre"]
            + all_dotation["dsr_fraction_cible"]
            + all_dotation["dsr_fraction_perequation"]
        )
    return all_dotation


def merge_dotations_criteres(all_dotation, criteres):
    """Fusionne les données des dotations avec les données descritères.
    Cette fonction n'est utile que pendant la période où les montants sont publiés mais les critères ne le sont pas.
    Cela permet de fusionner les montants année N avec les critères année N-1 pour pouvoir exposer les données via API.
    Paramètres :
        - all_dotation : dataframe contenant les données de toutes les dotations année N
        - criteres : dataframe contenant les critères de la dotation année N-1 (df construite grâce à la fonction load_dgcl_data)"""
    # On garde que les colonnes qui nous intéressent, donc que les critères année N-1 et pas les montants
    criteres = criteres[
        [
            "code_insee",
            "population_dgf",
            "potentiel_financier_par_habitant",
            "longueur_voirie",
            "zone_de_montagne",
            "superficie",
            "population_enfants",
            "residences_secondaires",
            "places_caravanes_avant_majoration",
        ]
    ].copy()
    # On fusionne les données de la dotation avec les critères
    all_dotation = all_dotation.merge(criteres, on="code_insee", how="left")

    # On change les types pour les nouvelles colonnes qui ont été créées car sinon les types sont tous en float
    all_dotation["population_dgf"] = all_dotation["population_dgf"].astype("Int64")
    all_dotation["longueur_voirie"] = all_dotation["longueur_voirie"].astype("Int64")
    all_dotation["population_enfants"] = all_dotation["population_enfants"].astype(
        "Int64"
    )
    all_dotation["residences_secondaires"] = all_dotation[
        "residences_secondaires"
    ].astype("Int64")
    all_dotation["places_caravanes_avant_majoration"] = all_dotation[
        "places_caravanes_avant_majoration"
    ].astype("Int64")
    return all_dotation
