dotation_solidarite_rurale_unites_criteres = {}

dotation_solidarite_rurale_sous_dotations = [
    "dsr_fraction_bourg_centre",
    "dsr_fraction_perequation",
    "dsr_fraction_cible",
]

dsr_fraction_bourg_centre_unites_criteres = {
    "population_dgf": None,
    "population_dgf_agglomeration": None,
    "part_population_canton": "%",
    "potentiel_financier": "€",
    "potentiel_financier_par_habitant": "€",
    "effort_fiscal": "€",
    "bureau_centralisateur": "boolean",
    "chef_lieu_arrondissement": "boolean",
    "chef_lieu_departement_dans_agglomeration": "boolean",
    "zrr": "boolean",
}

dsr_fraction_perequation_unites_criteres = {
    "population_dgf": None,
    "population_enfants": None,
    "potentiel_financier_par_habitant": "€",
    "effort_fiscal": "€",
    "superficie": "ha",
    "longueur_voirie": "m",
    "zone_de_montagne": "boolean",
    "insulaire": "boolean",
}

dsr_fraction_cible_unites_criteres = {
    "population_dgf": None,
    "population_insee": None,
    "population_enfants": None,
    "revenu_total": "€",
    "potentiel_financier_par_habitant": "€",
    "superficie": "ha",
    "longueur_voirie": "m",
}
