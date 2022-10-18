def search_commune_by_code_insee(data, code_insee):
    """Renvoie la commune correspondant au code insee passé en paramètre.
    Ne renvoie rien si la commune n'existe pas.
    Paramètres :
        - data : dataframe contenant les données des dotations
        - code_insee : code insee de la commune à rechercher"""
    try:
        commune = data.loc[data["code_insee"] == code_insee]
    except:
        commune = None
    return commune
