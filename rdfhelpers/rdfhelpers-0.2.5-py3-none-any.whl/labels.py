# Copyright (c) 2022, Ora Lassila & So Many Aircraft
# All rights reserved.
#
# See LICENSE for licensing information
#
# This module implements some useful functionality for programming with RDFLib.
#

import collections
import itertools
from rdflib import URIRef, Literal
from rdfhelpers.templated import Templated

# LABEL CACHING
#
# Cache the values of rdfs:label (and sub-properties thereof) for faster access. Select
# either all vertices with a label (the default) or customize vertex selection.
class LabelCache:
    def __init__(self, db, label_query=None, selector=None, language="en", prepopulate=False):
        self.db = db
        self.label_query = label_query or self.LABELQUERY
        self.selector = selector or "?res ?p ?o"
        self.language = language
        self._labels = dict()
        self._search_index = collections.defaultdict(set)
        if prepopulate:
            self.repopulate()

    LABELQUERY = '''
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        SELECT ?r ?label {
            $selector
            BIND ($resource AS ?r)
            ?label_prop rdfs:subPropertyOf* rdfs:label
            OPTIONAL { $resource skos:prefLabel ?pref_label }
            OPTIONAL { $resource skos:altLabel ?alt_label }
            OPTIONAL { $resource ?label_prop ?real_label }
            OPTIONAL { $resource dc:title ?other_label }
            BIND (COALESCE(?pref_label, ?alt_label, ?real_label, ?other_label) AS ?label)
            FILTER ((str(lang(?label)) = "") || langMatches(lang(?label), "$language"))
        }
        $limit
    '''

    ALLLABELSQUERY = '''
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        SELECT DISTINCT ?label {
            $resource skos:prefLabel|skos:altLabel|dc:title|(rdfs:subPropertyOf*/rdfs:label) ?label
            BIND (IF(langMatches(lang(?label), "$language"), 0, 1) AS ?priority)
        }
        ORDER BY ?priority
    '''

    def getLabel(self, resource):
        if not isinstance(resource, URIRef):
            resource = URIRef(resource)
        label = self._labels.get(resource, None)
        if label:
            return label
        else:
            label = None
            for res, lb in Templated.query(self.db, self.label_query,
                                           resource=resource, selector=None, limit="LIMIT 1",
                                           language=self.language):
                label = lb
                self.updateSearchIndex(resource, label)
                break
            if label is None:
                label = self.makeQName(resource) or str(resource)
            return label

    def invalidateLabel(self, resource):
        self._labels[resource if isinstance(resource, URIRef) else URIRef(resource)] = None

    def repopulate(self):
        self._labels = {resource: label for resource, label
                        in Templated.query(self.db, self.label_query,
                                           resource="?res", selector=self.selector, limit=None,
                                           language=self.language)}
        self._search_index = collections.defaultdict(set)
        for resource, label in self._labels.items():
            self.updateSearchIndex(resource, label)

    def updateSearchIndex(self, resource, label):
        if label:
            for p in itertools.pairwise(label.upper()):
                self._search_index[p[0]+p[1]].add(resource)

    def findResources(self, substring):
        search_string = substring.upper()
        if len(substring) < 2:
            raise ValueError("Search string too short")
        if len(substring) == 2:
            return self._search_index[search_string]
        else:
            return [resource for resource in self.findResources(search_string[0:2])
                    if str(self.getLabel(resource)).upper().find(search_string) >= 0]

    def findResourcesForAutocomplete(self, substring):
        # this value can be "JSONified" (e.g., flask.json.jsonify)
        return [{"value": resource, "label": self.getLabel(resource)} for resource
                in self.findResources(substring)]

    def getAllLabels(self, resource, exclude_default_namespace=True):
        if not isinstance(resource, URIRef):
            resource = URIRef(resource)
        labels = [label for label, in Templated.query(self.db, self.ALLLABELSQUERY,
                                                      resource=resource, language=self.language)]
        qname = self.makeQName(resource)
        if qname == str(resource):
            return labels + [qname]
        elif exclude_default_namespace and qname.startswith(':'):
            return labels + [str(resource)]
        else:
            return labels + [qname, str(resource)]

    def makeQName(self, uri):
        try:
            return "{0}:{2}".format(*self.db.namespace_manager.compute_qname(uri))
        except ValueError:
            return str(uri)

# SKOS CONCEPT LABEL CACHING
#
# Similar to regular label caching, but the default selection of vertices includes only the
# concepts of a specified concept scheme. Also provides a mapping from labels to concepts.
class SKOSLabelCache(LabelCache):
    def __init__(self, db, scheme, selector=None):
        self._concepts = dict()
        selector = Templated.convert(selector or "?res skos:broader*/^skos:hasTopConcept $scheme",
                                     {"scheme": scheme})
        super().__init__(db, selector=selector)

    def invalidateLabel(self, resource):
        label = self.getLabel(resource)
        super().invalidateLabel(resource)
        self._concepts[label] = None

    def updateSearchIndex(self, resource, label):
        super().updateSearchIndex(resource, label)
        self._concepts[label] = resource

    def repopulate(self):
        self._concepts = dict()
        super().repopulate()

    def getConcept(self, label):
        return self._concepts.get(label if isinstance(label, Literal) else Literal(label), None)

    def listConcepts(self):
        return self._labels.keys()
