from __future__ import annotations
from fastapi import FastAPI, HTTPException
from typing import List, Dict, Union
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from dotations_locales_back.common.init_datas import init_dotations_data
from dotations_locales_back.common.search_commune import search_commune_by_code_insee
from dotations_locales_back.web_api.utils import (
    create_commune_response,
    create_simulation_response,
)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
)

(
    dotations_criteres_2020,
    dotations_criteres_2021,
    dotations_criteres_2022,
) = init_dotations_data()

dotations_criteres = {
    "2022": dotations_criteres_2022,
    "2021": dotations_criteres_2021,
    "2020": dotations_criteres_2020,
}

dotations_list = [
    "dotation_forfaitaire",
    "dsu_montant",
    "dotation_nationale_perequation",
    "dotation_solidarite_rurale",
]


@app.get("/")
async def root():
    return {
        "message": "Ceci est l'API de l'application Dotations Locales, pour voir la documentation ajoutez /docs sur votre URL",
        "api_version": "1.3.2",
    }


class CommuneRequest(BaseModel):
    code_insee: str


class ValeurCritere(BaseModel):
    valeur: Union[str, None] = None
    unite: Union[str, None] = None


class Montant(BaseModel):
    __root__: Union[float, None] = None


class ValeursCritereParAnnee(BaseModel):
    annees: List[Dict[str, ValeurCritere]]


class Dotation(BaseModel):
    annees: List[Dict[str, Montant]]
    criteres: Union[Dict[str, ValeursCritereParAnnee], None] = None
    sous_dotations: Union[List[Dict[str, Dotation]], None] = None


class Dotations(BaseModel):
    dotation_forfaitaire: Dotation
    dsu_montant: Dotation
    dotation_nationale_perequation: Dotation
    dotation_solidarite_rurale: Dotation


class Criteres(BaseModel):
    population_insee: ValeursCritereParAnnee
    potentiel_financier_par_habitant: ValeursCritereParAnnee
    longueur_voirie: ValeursCritereParAnnee
    zone_de_montagne: ValeursCritereParAnnee
    superficie: ValeursCritereParAnnee
    population_enfants: ValeursCritereParAnnee
    residences_secondaires: ValeursCritereParAnnee
    places_caravanes_apres_majoration: ValeursCritereParAnnee


class CommuneResponse(BaseModel):
    """
    Les éléments exacts de la réponse.
    Tout autre élément sera ignoré.
    """

    code_insee: str
    dotations: Dotations
    criteres_generaux: Criteres


@app.post("/commune/", response_model=CommuneResponse)
async def describe_commune(commune: CommuneRequest):
    communes_datas = {}
    commune_found = True
    for year in dotations_criteres.keys():
        commune_data = search_commune_by_code_insee(
            dotations_criteres.get(year), commune.code_insee
        )
        if not commune_data.empty:
            communes_datas.update({year: commune_data})
        else:
            commune_found = False
    if commune_found == False:
        raise HTTPException(status_code=404, detail="Commune non trouvée")
    else:
        response = create_commune_response(
            commune.code_insee, dotations_list, **communes_datas
        )

    return response


class CriteresSimulation(BaseModel):
    population_insee: int
    potentiel_financier_par_habitant: float
    longueur_voirie: int
    zone_de_montagne: bool
    superficie: int
    population_enfants: int
    residences_secondaires: int
    places_caravanes_apres_majoration: int


class SimulationRequest(BaseModel):
    code_insee: str
    periode_loi: str
    data: CriteresSimulation


@app.post("/simulation/", response_model=CommuneResponse)
async def commune_simulation(simulation_parameters: SimulationRequest):
    # scenario usager
    # de janvier à juillet de l'année N, on a la loi de N et les critères de N-1
    # de juillet à l'automne (PLF) de l'année N, on la loi de N et les critères de N
    # à l'automne (PLF) de l'année N+1, on a la loi estimée (PLF) de N+1 et les critères N

    # TODO renommer 'periode' sachant que période de la loi à appliquer lors de la simulation
    simulation_parameters_dict = simulation_parameters.dict()
    if simulation_parameters.periode_loi == "2022":
        commune_data_2022 = search_commune_by_code_insee(
            dotations_criteres_2022, simulation_parameters.code_insee
        )
        if commune_data_2022.empty:
            raise HTTPException(status_code=404, detail="Commune non trouvée")
        response = create_simulation_response(
            simulation_parameters.code_insee,
            simulation_parameters_dict["data"],
            dotations_criteres_2022,
            dotations_list,
            simulation_parameters.periode_loi,
        )
    elif simulation_parameters.periode_loi == "2021":
        commune_data_2021 = search_commune_by_code_insee(
            dotations_criteres_2022, simulation_parameters.code_insee
        )
        if commune_data_2021.empty:
            raise HTTPException(status_code=404, detail="Commune non trouvée")
        response = create_simulation_response(
            simulation_parameters.code_insee,
            simulation_parameters_dict["data"],
            dotations_criteres_2021,
            dotations_list,
            simulation_parameters.periode_loi,
        )

    else:
        raise HTTPException(
            status_code=400,
            detail="'periode' must be 2021 or 2022, others years are not supported",
        )

    # to do
    # - Ajouter étape d'initialisation modèle OF
    # - Ajouter les colonnes manquantes pour faire tourner le modèle OF
    # - Faire une fonction qui récupère les calculs OF pour les mettre dans le body de réponse
    return response
