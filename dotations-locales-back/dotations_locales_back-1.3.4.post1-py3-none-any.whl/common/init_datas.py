# from .load_dgcl_dotations_data import (
#     load_dotation_data,
#     concat_dotation_dfs,
#     merge_dotations_criteres,
# )
from dotations_locales_back.common.load_dgcl_criteres_data import load_dgcl_data
from os import getcwd

from dotations_locales_back.common.mapping.criteres_dgcl_2020 import (
    filename_criteres_2020,
)
from dotations_locales_back.common.mapping.criteres_dgcl_2021 import (
    filename_criteres_2021,
)
from dotations_locales_back.common.mapping.criteres_dgcl_2022 import (
    filename_criteres_2022,
)

DATA_DIRECTORY = getcwd() + "/data/"

# DGCL dotations data

# DF_2022_PATH = DATA_DIRECTORY + "notification_dotations_forfaitaires_2022.csv"
# DSR_BC_2022_PATH = DATA_DIRECTORY + "notification_dotations_solidarite_rurale_bourg_centre_2022.csv"
# DSR_C_2022_PATH = DATA_DIRECTORY + "notification_dotations_solidarite_rurale_cible_2022.csv"
# DSR_P_2022_PATH = DATA_DIRECTORY + "notification_dotations_solidarite_rurale_perequation_2022.csv"
# DSU_2022_PATH = DATA_DIRECTORY + "notification_dotations_solidarite_urbaine_2022.csv"

# DGCL criteres data
CRITERES_2020_PATH = DATA_DIRECTORY + filename_criteres_2020
CRITERES_2021_PATH = DATA_DIRECTORY + filename_criteres_2021
CRITERES_2022_PATH = DATA_DIRECTORY + filename_criteres_2022

# On charge toutes les données des dotations 2022 et des critères 2021


def init_dotations_data():
    """Initialise les données des dotations et des critères.
    Retourne 2 dataframes contenant les données des dotations et des critères de répartition pour les années 2022 et 2021.
    """

    # # On charge les données des dotations brutes
    # df_2022 = load_dotation_data(DF_2022_PATH, "dotation_forfaitaire")
    # dsu_2022 = load_dotation_data(DSU_2022_PATH, "dsu_montant")
    # dsr_bp_2022 = load_dotation_data(DSR_BC_2022_PATH, "dsr_fraction_bourg_centre")
    # dsr_c_2022 = load_dotation_data(DSR_C_2022_PATH, "dsr_fraction_cible")
    # dsr_p_2022 = load_dotation_data(DSR_P_2022_PATH, "dsr_fraction_perequation")

    # # On fusionne toutes les données dans une seule DataFrame
    # all_dotations_2022 = concat_dotation_dfs(
    #     df_2022, dsu_2022, dsr_bp_2022, dsr_c_2022, dsr_p_2022
    # )

    # On charge les données des critères de repartiion
    dotations_criteres_2020 = load_dgcl_data(CRITERES_2020_PATH, 2020)
    dotations_criteres_2021 = load_dgcl_data(CRITERES_2021_PATH, 2021)
    dotations_criteres_2022 = load_dgcl_data(CRITERES_2022_PATH, 2022)

    #  On ajoute les critères de repartition 2021 à la DataFrame des dotations 2022 vu que les critères de repartition 2022 ne sont pas encore publiés
    # dotations_criteres_2022 = merge_dotations_criteres(
    #     all_dotations_2022, dotations_criteres_2021
    # )
    return dotations_criteres_2020, dotations_criteres_2021, dotations_criteres_2022
