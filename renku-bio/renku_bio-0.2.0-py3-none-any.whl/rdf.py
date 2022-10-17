"""Helper functions to interact with the project's rdf graph containing
Renku metadata"""
import json
from typing import Any, Dict, Optional

from rdflib import Graph, URIRef
from rdflib.namespace import Namespace
from renku.command.graph import export_graph_command

from renkubio.utils import nest_dict_items

schema = Namespace("http://schema.org/")
bio = Namespace("http://bioschemas.org/")

NS_DICT = {
    "prov": "http://www.w3.org/ns/prov#",
    "oa": "http://www.w3.org/ns/oa#",
    "schema": "http://schema.org/",
    "renku": "https://swissdatasciencecenter.github.io/renku-ontology#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "bio": "http://bioschemas.org/",
}


def load_graph() -> Graph:
    """Load the Renku project RDF graph of the current working directory."""
    # Ideally use RDFGraph(), but unable due to client init bug

    result = export_graph_command().build().execute()
    graph = result.output.as_rdflib_graph()
    for k, v in NS_DICT.items():
        graph.bind(k, v)

    return graph


def get_sample_uri(sample_name: str, graph: Graph) -> Optional[URIRef]:
    """Return the URI corresponding to input biosample name in the renku project graph."""
    res = graph.query(
        f"""
        SELECT *
        WHERE {{
            ?sample schema:name "{sample_name}" ;
                    a           bio:BioSample .
        }}""",
        initNs=NS_DICT,
    )
    try:
        sample_id = res.serialize(format="csv").splitlines()[1].decode()
        sample_id = URIRef(sample_id)
    except IndexError:
        sample_id = None
    return sample_id


def extract_biosample_meta(sample_uri: URIRef, graph: Graph) -> Dict[str, Any]:
    """Extract user-relevant biosample metadata into a human-readable dictionary"""
    ordered_fields = [
        "name",
        "description",
        "common_name",
        "scientific_name",
        "parent_taxon",
        "taxon_rank",
        "sex",
        "age",
        "control",
        "collector",
        "location_name",
        "latitude",
        "longitude",
        "url",
    ]

    # Get the URI of each nested object in the biosample
    taxon_uri = graph.value(sample_uri, bio.taxonomicRange)
    org_uri = graph.value(sample_uri, bio.collector)
    loc_uri = graph.value(sample_uri, bio.locationCreated)

    # Get the sample name (mandatory), and all other available
    # properties (optional)
    query = f"""
    SELECT ?{' ?'.join(ordered_fields)}
    WHERE {{
                    <{sample_uri}> schema:name         ?name .
        OPTIONAL {{ <{sample_uri}> schema:gender       ?sex  ; }}
        OPTIONAL {{ <{sample_uri}> schema:description  ?description ; }}
        OPTIONAL {{ <{sample_uri}> schema:url          ?url ; }}
        OPTIONAL {{ <{sample_uri}> bio:isControl       ?control  .  }}
        OPTIONAL {{ <{sample_uri}> bio:samplingAge     ?age  .  }}
        OPTIONAL {{ <{loc_uri}>    schema:name         ?location_name . }}
        OPTIONAL {{ <{loc_uri}>    schema:latitude     ?latitude ;
                                   schema:longitude    ?longitude .
        }}
        OPTIONAL {{ <{org_uri}>    schema:name         ?collector . }}
        OPTIONAL {{ <{taxon_uri}>  schema:name         ?common_name . }}
        OPTIONAL {{ <{taxon_uri}>  bio:scientificName  ?scientific_name ;
                                   bio:parentTaxon     ?parent_taxon ;
                                   bio:taxonRank       ?taxon_rank   .
        }}
    }}
    """
    res = graph.query(query, initNs=NS_DICT).serialize(format="json").decode()
    # Only keep field: value pairs, discarding datatypes and other information
    meta_dict = json.loads(res)["results"]["bindings"][0]
    values_dict = {
        field: meta_dict[field]["value"]
        for field in ordered_fields
        if field in meta_dict
    }
    # Nest properties belonging to objects in biosample
    taxon_properties = set(
        ("scientific_name", "common_name", "parent_taxon", "taxon_rank")
    )
    if set(meta_dict) & taxon_properties:
        nest_dict_items(
            values_dict,
            taxon_properties,
            "taxon",
        )

    location_properties = set(("location_name", "latitude", "longitude"))
    if set(meta_dict) & location_properties:
        nest_dict_items(values_dict, location_properties, "location_created")

    return values_dict


def get_sample_table(graph: Graph) -> str:
    res = graph.query(
        """
    SELECT ?name ?taxon
    WHERE {
        ?sampleid   a                  bio:BioSample ;
                    schema:name        ?name .
        OPTIONAL {
        ?sampleid   bio:taxonomicRange ?taxid .
        ?taxid      schema:name        ?taxon .
        }
    }
    """,
        initNs=NS_DICT,
    )
    return res.serialize(format="csv").decode()
