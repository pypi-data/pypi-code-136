filename_criteres_2021 = "criteres_repartition_2021.csv"

infos_generales_2021 = {
    "Informations générales - Code INSEE de la commune": "code_insee",
    "Informations générales - Nom de la commune": "nom",
    "Informations générales - Population DGF de l'année N": "population_dgf",
    "Informations générales - Population INSEE de l'année N": "population_insee",
    "Potentiel fiscal et financier des communes - Potentiel financier": "potentiel_financier",
    "Potentiel fiscal et financier des communes - Potentiel financier par habitant": "potentiel_financier_par_habitant",
    "Informations générales - Strate démographique de l'année N": "strate_demographique",
    "Effort fiscal - Effort fiscal": "effort_fiscal",
    "Potentiel fiscal et financier des communes - Potentiel fiscal 4 taxes": "potentiel_fiscal",
    "Dotation de solidarité rurale - Péréquation - Longueur de voirie en mètres": "longueur_voirie",  # OF
    "Dotation de solidarité rurale - Péréquation - Commune située en zone de montagne": "zone_de_montagne",
    "Informations générales - Superficie de l'année N": "superficie",
    "Dotation de solidarité rurale - Péréquation - Population 3 à 16 ans": "population_enfants",
    "Informations générales - Résidences secondaires de l'année N": "residences_secondaires",  # attention n'est pas un nom de variable openfisca
    "Informations générales - Places de caravanes de l'année N après majoration": "places_caravanes_apres_majoration",  # attention n'est pas un nom de variable openfisca
}

montants_dotations_2021 = {
    "Dotation forfaitaire - Dotation forfaitaire notifiée N": "dotation_forfaitaire",
    "Dotation de solidarité urbaine - Montant total réparti": "dsu_montant",
    "Dotation nationale de péréquation - DNP totale": "dotation_nationale_perequation",
    "Dotation de solidarité rurale Bourg-centre - Montant global réparti": "dsr_fraction_bourg_centre",
    "Dotation de solidarité rurale - Péréquation - Montant global réparti (après garantie CN)": "dsr_fraction_perequation",
    "Dotation de solidarité rurale - Cible - Montant global réparti": "dsr_fraction_cible",
}

criteres_2021 = {
    "Dotation forfaitaire - Recettes réelles de fonctionnement des communes N-2 pour l'année N": "recettes_reelles_fonctionnement",  # OF
    "Dotation forfaitaire - Population DGF majorée de l'année N": "population_dgf_majoree",  # OF
    "Dotation de solidarité urbaine - Nombre de logements TH de la commune": "nombre_logements",  # OF
    "Dotation de solidarité urbaine - Nombre de logements sociaux de la commune": "nombre_logements_sociaux",  # OF
    "Dotation de solidarité urbaine - Nombre de bénéficiaires des aides au logement de la commune": "nombre_beneficiaires_aides_au_logement",  # OF
    "Dotation de solidarité urbaine - Revenu imposable des habitants de la commune": "revenu_total",  # OF
    "Dotation de solidarité urbaine - Population QPV": "population_qpv",  # OF
    "Dotation de solidarité urbaine - Population ZFU": "population_zfu",  # OF
    "Dotation de solidarité rurale Bourg-centre - Pourcentage de la population communale dans le canton d'appartenance en 2014": "part_population_canton",  # OF
    "Dotation de solidarité rurale Bourg-centre - Population DGF des communes de l'agglomération": "population_dgf_agglomeration",  # OF
    "Dotation de solidarité rurale Bourg-centre - Population départementale de référence de l'agglomération": "population_dgf_departement_agglomeration",  # OF
    "Dotation de solidarité rurale Bourg-centre - Appartenance à une agglomération avec le chef-lieu de département": "chef_lieu_departement_dans_agglomeration",  # OF
    "Dotation de solidarité rurale Bourg-centre - Bureaux centralisateurs": "bureau_centralisateur",  # OF
    "Dotation de solidarité rurale Bourg-centre - Chef-lieu d'arrondissement au 31 décembre 2014": "chef_lieu_arrondissement",  # OF
    "Dotation de solidarité rurale - Bourg-centre - Commune située en ZRR": "zrr",  # OF
    "Dotation de solidarité rurale - Péréquation - Commune située en zone de montagne": "zone_de_montagne",  # OF
    "Dotation de solidarité rurale - Péréquation - Commune insulaire": "insulaire",  # OF
    "Dotation de solidarité rurale - Péréquation - Population 3 à 16 ans": "population_enfants",  # OF
    "Dotation de solidarité rurale - Péréquation - Longueur de voirie en mètres": "longueur_voirie",  # OF
}

variables_openfisca_presentes_fichier_2021 = {
    "bureau_centralisateur": "Dotation de solidarité rurale Bourg-centre - Bureaux centralisateurs",
    "chef_lieu_arrondissement": "Dotation de solidarité rurale Bourg-centre - Chef-lieu d'arrondissement au 31 décembre 2014",
    "chef_lieu_de_canton": "Dotation de solidarité rurale Bourg-centre - Code commune chef-lieu de canton au 1er janvier 2014",
    "chef_lieu_departement_dans_agglomeration": "Dotation de solidarité rurale Bourg-centre - Appartenance à une agglomération avec le chef-lieu de département",
    "part_population_canton": "Dotation de solidarité rurale Bourg-centre - Pourcentage de la population communale dans le canton d'appartenance en 2014",
    "population_dgf": "Informations générales - Population DGF de l'année N",
    "population_dgf_agglomeration": "Dotation de solidarité rurale Bourg-centre - Population DGF des communes de l'agglomération",
    "population_dgf_departement_agglomeration": "Dotation de solidarité rurale Bourg-centre - Population départementale de référence de l'agglomération",
    "population_insee": "Informations générales - Population INSEE de l'année N",
    "potentiel_financier": "Potentiel fiscal et financier des communes - Potentiel financier",
    "potentiel_financier_par_habitant": "Potentiel fiscal et financier des communes - Potentiel financier par habitant",
    "revenu_total": "Dotation de solidarité urbaine - Revenu imposable des habitants de la commune",
    "strate_demographique": "Informations générales - Strate démographique de l'année N",
    "zrr": "Dotation de solidarité rurale - Bourg-centre - Commune située en ZRR",
    "effort_fiscal": "Effort fiscal - Effort fiscal",
    "longueur_voirie": "Dotation de solidarité rurale - Péréquation - Longueur de voirie en mètres",
    "zone_de_montagne": "Dotation de solidarité rurale - Péréquation - Commune située en zone de montagne",
    "insulaire": "Dotation de solidarité rurale - Péréquation - Commune insulaire",
    "superficie": "Informations générales - Superficie de l'année N",
    "population_enfants": "Dotation de solidarité rurale - Péréquation - Population 3 à 16 ans",
    "nombre_logements": "Dotation de solidarité urbaine - Nombre de logements TH de la commune",
    "nombre_logements_sociaux": "Dotation de solidarité urbaine - Nombre de logements sociaux de la commune",
    "nombre_beneficiaires_aides_au_logement": "Dotation de solidarité urbaine - Nombre de bénéficiaires des aides au logement de la commune",
    "population_qpv": "Dotation de solidarité urbaine - Population QPV",
    "population_zfu": "Dotation de solidarité urbaine - Population ZFU",
    "population_dgf_majoree": "Dotation forfaitaire - Population DGF majorée de l'année N",
    "recettes_reelles_fonctionnement": "Dotation forfaitaire - Recettes réelles de fonctionnement des communes N-2 pour l'année N",
    "potentiel_fiscal": "Potentiel fiscal et financier des communes - Potentiel fiscal 4 taxes",
}

colonnes_utiles_2021 = {
    "actual_indice_synthetique": "Dotation de solidarité rurale - Cible - IS DSR Cible",
    "pot_fin_strate": "Potentiel fiscal et financier des communes - Potentiel financier moyen par habitant de la strate",
    "chef_lieu_de_canton_dgcl": "Dotation de solidarité rurale Bourg-centre - Code commune chef-lieu de canton au 1er janvier 2014",
    "rang_indice_synthetique": "Dotation de solidarité rurale - Cible - Rang DSR Cible",
    "montant_commune_eligible": "Dotation de solidarité rurale Bourg-centre - Montant de la commune éligible",
    "part_pfi": "Dotation de solidarité rurale - Péréquation - Part Pfi (avant garantie CN)",
}


variables_calculees_presentes_2021 = {
    "Dotation de solidarité rurale - Péréquation - Part Pfi (avant garantie CN)": "dsr_fraction_perequation_part_potentiel_financier_par_habitant",
    "Dotation de solidarité rurale - Péréquation - Part VOIRIE (avant garantie CN)": "dsr_fraction_perequation_part_longueur_voirie",
    "Dotation de solidarité rurale - Péréquation - Part ENFANTS (avant garantie CN)": "dsr_fraction_perequation_part_enfants",
    "Dotation de solidarité rurale - Péréquation - Part Pfi/hectare (avant garantie CN)": "dsr_fraction_perequation_part_potentiel_financier_par_hectare",
    "Dotation de solidarité rurale - Cible - Indice synthétique": "indice_synthetique_dsr_cible",
    "Dotation de solidarité rurale - Cible - Rang DSR Cible": "rang_indice_synthetique_dsr_cible",
    "Dotation de solidarité rurale - Cible - Part Pfi (avant garantie CN)": "dsr_fraction_cible_part_potentiel_financier_par_habitant",
    "Dotation de solidarité rurale - Cible - Part VOIRIE (avant garantie CN)": "dsr_fraction_cible_part_longueur_voirie",
    "Dotation de solidarité rurale - Cible - Part ENFANTS (avant garantie CN)": "dsr_fraction_cible_part_enfants",
    "Dotation de solidarité rurale - Cible - Part Pfi/hectare (Pfis) (avant garantie CN)": "dsr_fraction_cible_part_potentiel_financier_par_hectare",
    "Dotation de solidarité rurale Bourg-centre - Montant de la commune éligible": "dsr_montant_eligible_fraction_bourg_centre",
    "Dotation de solidarité urbaine - Valeur de l'indice synthétique de classement de la commune à la DSU": "indice_synthetique_dsu",
    "Dotation de solidarité urbaine - Rang de classement à la DSU des communes mét de plus de 10000 habitants": "rang_indice_synthetique_dsu_seuil_haut",
    "Dotation de solidarité urbaine - Rang de classement à la DSU des communes mét de 5000 à 9999 habitants": "rang_indice_synthetique_dsu_seuil_bas",
    "Dotation de solidarité urbaine - Montant de la garantie effectivement appliquée à la commune": "dsu_montant_garantie_non_eligible",
    "Dotation de solidarité urbaine - Montant attribution spontanée DSU": "dsu_part_spontanee",
    "Dotation de solidarité urbaine - Montant progression de la DSU": "dsu_part_augmentation",
    "Dotation de solidarité urbaine - Montant total réparti": "dsu_montant",
    "Dotation de solidarité rurale Bourg-centre - Montant global réparti": "dsr_fraction_bourg_centre",
    "Dotation de solidarité rurale - Péréquation - Montant global réparti (après garantie CN)": "dsr_fraction_perequation",
    "Dotation de solidarité rurale - Cible - Montant global réparti": "dsr_fraction_cible",
    "Dotation forfaitaire - Dotation forfaitaire notifiée N": "dotation_forfaitaire",
    "Dotation forfaitaire - Part dynamique de la population des communes": "df_evolution_part_dynamique",
    "Dotation forfaitaire - Montant de l'écrêtement": "df_montant_ecretement",
}


variables_calculees_an_dernier_2021 = {
    "Dotation de solidarité rurale Bourg-centre - Montant de la commune éligible": "dsr_montant_eligible_fraction_bourg_centre",
    "Dotation de solidarité urbaine - Montant attribution spontanée DSU": "dsu_part_spontanee",
    "Dotation de solidarité urbaine - Montant progression de la DSU": "dsu_part_augmentation",
    "Dotation de solidarité urbaine - Montant total réparti": "dsu_montant",
    "Dotation de solidarité rurale - Cible - Part Pfi": "dsr_fraction_cible_part_potentiel_financier_par_habitant",
    "Dotation de solidarité rurale - Cible - Part VOIRIE": "dsr_fraction_cible_part_longueur_voirie",
    "Dotation de solidarité rurale - Cible - Part ENFANTS": "dsr_fraction_cible_part_enfants",
    "Dotation de solidarité rurale - Cible - Part Pfi/hectare (Pfis)": "dsr_fraction_cible_part_potentiel_financier_par_hectare",
    "Dotation de solidarité rurale - Péréquation - Part Pfi (avant garantie CN)": "dsr_fraction_perequation_part_potentiel_financier_par_habitant",
    "Dotation de solidarité rurale - Péréquation - Part VOIRIE (avant garantie CN)": "dsr_fraction_perequation_part_longueur_voirie",
    "Dotation de solidarité rurale - Péréquation - Part ENFANTS (avant garantie CN)": "dsr_fraction_perequation_part_enfants",
    "Dotation de solidarité rurale - Péréquation - Part Pfi/hectare (avant garantie CN)": "dsr_fraction_perequation_part_potentiel_financier_par_hectare",
    "Dotation de solidarité rurale Bourg-centre - Montant global réparti": "dsr_fraction_bourg_centre",
    "Dotation de solidarité rurale - Péréquation - Montant global réparti (après garantie CN)": "dsr_fraction_perequation",
    "Dotation de solidarité rurale - Cible - Montant global réparti": "dsr_fraction_cible",
    "Dotation forfaitaire - Dotation forfaitaire notifiée N": "dotation_forfaitaire",
    "Dotation forfaitaire - Population DGF majorée de l'année N": "population_dgf_majoree",
}


columns_to_keep_2021 = {
    **infos_generales_2021,
    **montants_dotations_2021,
    **criteres_2021,
}
