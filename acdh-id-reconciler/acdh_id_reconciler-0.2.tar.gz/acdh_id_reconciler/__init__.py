from SPARQLWrapper import SPARQLWrapper, JSON
from AcdhArcheAssets.uri_norm_rules import get_norm_id


ENDPOINT_URL = "https://query.wikidata.org/sparql"
USER_AGENT = "acdh-id-reconciler (https://www.oeaw.ac.at/acdh/acdh-ch-home)"


def gnd_to_geonames(gnd, user_agent=USER_AGENT):
    """
    """
    norm_id = get_norm_id(gnd)
    query = f"""SELECT ?wikidata ?gnd ?geonames
    WHERE
    {{
    ?wikidata wdt:P227 "{norm_id}".
    ?wikidata wdt:P227 ?gnd .
    ?wikidata wdt:P1566 ?geonames .
    }}"""
    sparql = SPARQLWrapper(ENDPOINT_URL, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    ids = {
        key: value['value'] for (key, value) in results["results"]["bindings"][0].items()
    }
    return ids
