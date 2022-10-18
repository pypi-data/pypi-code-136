filename_criteres_2020 = "criteres_repartition_2020.csv"

infos_generales_2020 = {
    "Informations générales - Code INSEE de la commune": "code_insee",
    "Informations générales - Nom de la commune": "nom",
    "Informations générales - Population DGF de l'année N'": "population_dgf",
    "Informations générales - Population INSEE de l'année N ": "population_insee",
    "Potentiel fiscal et financier des communes - Potentiel financier": "potentiel_financier",
    "Potentiel fiscal et financier des communes - Potentiel financier par habitant": "potentiel_financier_par_habitant",
    "Informations générales - Strate démographique de l'année N": "strate_demographique",
    "Effort fiscal - Effort fiscal": "effort_fiscal",
    "Potentiel fiscal et financier des communes - Potentiel fiscal 4 taxes": "potentiel_fiscal",
    "Dotation de solidarité rurale - Péréquation - Longueur de voirie en mètres": "longueur_voirie",  # OF
    "Dotation de solidarité rurale - Péréquation - Commune située en zone de montagne": "zone_de_montagne",
    "Informations générales - Superficie année N": "superficie",
    "Dotation de solidarité rurale - Péréquation - Population 3 à 16 ans": "population_enfants",
    "Informations générales - Résidences secondaires de l'année N": "residences_secondaires",  # attention n'est pas un nom de variable openfisca
    "Informations générales - Places de caravanes de l'année N après majoration": "places_caravanes_apres_majoration",  # attention n'est pas un nom de variable openfisca
}

montants_dotations_2020 = {
    "Dotation forfaitaire - Dotation forfaitaire notifiée N": "dotation_forfaitaire",
    "Dotation de solidarité urbaine - Montant total réparti": "dsu_montant",
    "Dotation nationale de péréquation - DNP totale": "dotation_nationale_perequation",
    "Dotation de solidarité rurale Bourg-centre - Montant global réparti": "dsr_fraction_bourg_centre",
    "Dotation de solidarité rurale - Péréquation - Montant global réparti (après garantie CN)": "dsr_fraction_perequation",
    "Dotation de solidarité rurale - Cible - Montant global réparti": "dsr_fraction_cible",
}

criteres_2020 = {
    "Dotation forfaitaire - Recettes réelles de fonctionnement des communes N-2 pour l'année N": "recettes_reelles_fonctionnement",  # OF
    "Dotation forfaitaire - Population DGF major?e": "population_dgf_majoree",  # OF
    "Dotation de solidarité urbaine - Nombre de logements TH de la commune": "nombre_logements",  # OF
    "Dotation de solidarité urbaine - Nombre de logements sociaux de la commune": "nombre_logements_sociaux",  # OF
    "Dotation de solidarité urbaine - Nombre de bénéficiaires des aides au logement de la commune": "nombre_beneficiaires_aides_au_logement",  # OF
    "Dotation de solidarité urbaine - Revenu imposable des habitants de la commune": "revenu_total",  # OF
    "Dotation de solidarité urbaine - Population QPV": "population_qpv",  # OF
    "Dotation de solidarité urbaine - Population ZFU": "population_zfu",  # OF
    "Dotation de solidarité rurale Bourg-centre - Pourcentage de la population communale dans le canton": "part_population_canton",  # OF
    "Dotation de solidarité rurale Bourg-centre - Population DGF des communes de l'agglomération": "population_dgf_agglomeration",  # OF
    "Dotation de solidarité rurale Bourg-centre - Population départementale de référence de l'agglomération": "population_dgf_departement_agglomeration",  # OF
    "Dotation de solidarité rurale Bourg-centre - Chef-lieu de département agglo": "chef_lieu_departement_dans_agglomeration",  # OF
    "Dotation de solidarité rurale Bourg-centre - Bureaux centralisateurs": "bureau_centralisateur",  # OF
    "Dotation de solidarité rurale Bourg-centre - Chef-lieu d'arrondissement au 31 décembre 2014": "chef_lieu_arrondissement",  # OF
    "Dotation de solidarité rurale - Bourg-centre - Commune située en ZRR": "zrr",  # OF
    "Dotation de solidarité rurale - Péréquation - Commune située en zone de montagne": "zone_de_montagne",  # OF
    "Dotation de solidarité rurale - Péréquation - Commune insulaire": "insulaire",  # OF
    "Dotation de solidarité rurale - Péréquation - Population 3 à 16 ans": "population_enfants",  # OF
    "Dotation de solidarité rurale - Péréquation - Longueur de voirie en mètres": "longueur_voirie",  # OF
}

columns_to_keep_2020 = {
    **infos_generales_2020,
    **montants_dotations_2020,
    **criteres_2020,
}
