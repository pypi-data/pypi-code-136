# Copyright (c) 2022, Ora Lassila & So Many Aircraft
# All rights reserved.
#
# See LICENSE for licensing information
#
# This module implements some useful functionality for programming with RDFLib.
#

from rdflib import URIRef, BNode, Variable, Graph, RDF, ConjunctiveGraph
from rdflib.plugins.stores.sparqlstore import SPARQLUpdateStore
from rdfhelpers.templated import Templated, TemplatedQueryMixin
import re

# GLOSSARY
#
# This code uses certain terms or words in specific meanings:
# - "container" -- a composite object, an instance of any of the subclasses of rdfs:Container.
# - "context" -- something implemented as a named graph in the back-end.

# HELPFUL STUFF

# Make a new Graph instance from triples (an iterable)
def graphFrom(triples, add_to=None, graph_class=Graph, **kwargs):
    if add_to is None:
        add_to = graph_class(**kwargs)
    for triple in triples:
        add_to.add(triple)
    return add_to if len(add_to) > 0 else None

def expandQName(prefix, local_name, ns_mgr):
    ns = ns_mgr.store.namespace(prefix)
    if ns is not None:
        return str(ns) + local_name
    else:
        raise KeyError("Namespace prefix {} is not bound".format(prefix))

def URI(u):
    return u if isinstance(u, URIRef) or u is None else URIRef(u)

CBD_QUERY = '''
    SELECT ?s1 ?p1 ?o1 {
        {
            SELECT ?s1 ?p1 ?o1 {
                BIND($uri AS ?s1)
                ?s1 ?p1 ?o1
            }
        } UNION {
            SELECT ?s1 ?p1 ?o1 {
                BIND($uri AS ?s2)
                ?s2 ?p2 ?s1 . FILTER(ISBLANK(?s1))
                ?s1 ?p1 ?o1
            }
        } UNION {
            SELECT ?s1 ?p1 ?o1 {
                BIND($uri AS ?s3)
                ?s3 ?p3 ?s2 . FILTER(ISBLANK(?s2))
                ?s2 ?p2 ?s1 . FILTER(ISBLANK(?s1))
                ?s1 ?p1 ?o1
            }
        }
    }
'''
CBD_QUERY_WITH_CONTEXT = '''
    SELECT ?s1 ?p1 ?o1 {
        GRAPH $context {
            {
                SELECT ?s1 ?p1 ?o1 {
                    BIND($uri AS ?s1)
                    ?s1 ?p1 ?o1
                }
            } UNION {
                SELECT ?s1 ?p1 ?o1 {
                    BIND($uri AS ?s2)
                    ?s2 ?p2 ?s1 . FILTER(ISBLANK(?s1))
                    ?s1 ?p1 ?o1
                }
            } UNION {
                SELECT ?s1 ?p1 ?o1 {
                    BIND($uri AS ?s3)
                    ?s3 ?p3 ?s2 . FILTER(ISBLANK(?s2))
                    ?s2 ?p2 ?s1 . FILTER(ISBLANK(?s1))
                    ?s1 ?p1 ?o1
                }
            }
        }
    }
'''

def cbd(source, target, resource, context):
    # Does not support reified statements (yet)
    if not isinstance(source, Graph):
        # if context is None:
        #     raise NotImplementedError("CBD via SPARQL and no context")
        if target is None:
            target = Graph()
        return graphFrom(Templated.query(source,
                                         CBD_QUERY if context is None else CBD_QUERY_WITH_CONTEXT,
                                         context=context, uri=resource),
                         add_to=target)
    else:
        if target is None:
            target = source.__class__()
        subjects = list([resource])
        if isinstance(source, ConjunctiveGraph):
            def get_triples(s): return source.quads((s, None, None, context))
            if context is None and not isinstance(target, ConjunctiveGraph):
                raise ValueError("Target must be context-aware: %s".format(target))
        else:
            def get_triples(s): return source.triples((s, None, None))
        while subjects:
            subject = subjects.pop()
            for triple in get_triples(subject):
                target.add(triple)
                leaf = triple[2]
                if isinstance(leaf, BNode):
                    subjects.append(leaf)
        return target

CBD_ANALYSIS_QUERY = '''
    SELECT ?s ?p ?o {
        ?s ?p ?o .
        FILTER isBlank(?o)
        FILTER NOT EXISTS { ?o ?pp ?oo }
    }
'''

def cbdAnalysis(self, candidate_cbd):
    return candidate_cbd.query(self.CBD_ANALYSIS_QUERY)

# Helpful graph accessors

def getvalue(graph, node, predicate):
    return next(graph.objects(node, predicate), None)

def setvalue(graph, node, predicate, value):
    graph.remove((node, predicate, None))
    if value is not None:
        graph.add((node, predicate, value))

def addvalues(graph, node, predicates_and_values: dict):
    for predicate, value in predicates_and_values.items():
        graph.add((node, predicate, value))

def setvalues(graph, node, predicates_and_values: dict):
    for predicate, value in predicates_and_values.items():
        setvalue(graph, node, predicate, value)

def diff(graph1, graph2):
    return graph1 - graph2, graph2 - graph1

# CONTAINERS

LI_MATCH_PATTERN = re.compile(str(RDF) + "_([0-9]+)")
LI_CREATE_PATTERN = str(RDF) + "_{0}"

def isContainerItemPredicate(uri):
    match = LI_MATCH_PATTERN.match(uri)
    return int(match.group(1)) if match else None

def makeContainerItemPredicate(index):
    return LI_CREATE_PATTERN.format(index)

def getContainerStatements(graph, source, predicate):
    containers = list(graph.objects(URI(source), predicate))
    n = len(containers)
    if n == 1:
        return sorted([statement for statement in graph.triples((containers[0], None, None))
                       if isContainerItemPredicate(statement[1])],
                      key=lambda tr: tr[1])
    elif n == 0:
        return None
    else:
        raise ValueError("Expected only one value for {0}".format(predicate))

def getContainerItems(graph, node, predicate):
    statements = getContainerStatements(graph, node, predicate)
    return [statement[2] for statement in statements] if statements else None

def setContainerItems(graph, node, predicate, values, newtype=RDF.Seq):
    # Having to write code like this is a clear indication that triples are the wrong
    # abstraction for graphs, way too low level. Just sayin'.
    if values:
        statements = getContainerStatements(graph, node, predicate)
        if statements:
            container = statements[0][0]
            for statement in statements:
                graph.remove(statement)
        else:
            container = BNode()
            graph.add((node, predicate, container))
            graph.add((container, RDF.type, newtype))
        i = 1
        for value in values:
            graph.add((container, URIRef(makeContainerItemPredicate(i)), value))
            i += 1
    else:
        container = getvalue(graph, node, predicate)
        if container:
            graph.remove((node, predicate, container))
            graph.remove((container, None, None))

# FOCUSED GRAPH
#
# Instances of FocusedGraph have a specified "focus node".

def ntriples(graph, destination=None):
    result = graph.serialize(destination=destination, format="nt", encoding="utf-8")
    return result.decode("utf-8") if destination is None else None

class FocusedGraph(Graph):
    def __init__(self, focus=None, source=None, focus_class=None, **kwargs):
        super().__init__(**kwargs)
        if source:
            self.parse(source)
        self._focus = focus or self.findFocus(focus_class=focus_class, **kwargs)

    @property
    def focus(self):
        return self._focus

    def findFocus(self, focus_class=None, **kwargs):
        if focus_class:
            focus = next(self.triples((None, RDF.type, focus_class)), None)
            if focus:
                return focus[0]
        raise ValueError("No focus found")

    def getvalue(self, predicate):
        return getvalue(self, self._focus, predicate)

    def setvalue(self, predicate, value):
        setvalue(self, self._focus, predicate, value)

# CBD GRAPH

class CBDGraph(FocusedGraph):
    def __init__(self, focus, data, context=None, **kwargs):
        super().__init__(focus=focus, **kwargs)
        self.data = data
        self.context = context
        cbd(data, self, focus, context)

    FLUSHUPDATE = '''
        DELETE DATA { $remove_stuff };
        INSERT DATA { $add_stuff }
    '''
    FLUSHUPDATE_WITH_CONTEXT = '''
        DELETE DATA { GRAPH $context { $remove_stuff } };
        INSERT DATA { GRAPH $context { $add_stuff } }
    '''

    def flush(self):
        context = self.context
        additions, retractions = diff(self, cbd(self, None, self.focus, context))
        if len(additions) > 0 or len(retractions) > 0:
            Templated.update(self.data,
                             self.FLUSHUPDATE if context is None else self.FLUSHUPDATE_WITH_CONTEXT,
                             context=context,
                             add_stuff=ntriples(additions), remove_stuff=ntriples(retractions))

# SPARQL REPOSITORY

class SPARQLRepository(TemplatedQueryMixin, SPARQLUpdateStore):
    def __init__(self, query_endpoint=None, update_endpoint=None, **kwargs):
        super().__init__(query_endpoint=query_endpoint,
                         update_endpoint=update_endpoint or query_endpoint,
                         **kwargs)

    # Why do I get a complaint about this? SPARQLUpdateStore is not an abstract class...
    def triples_choices(self, _, context=None):
        pass

# JOURNALED GRAPH
#
# Instances of JournaledGraph keep a list of modifications (additions and deletions) and are
# capable of "flushing" these modifications to a backing store with a SPARQL endpoint.

class JournaledGraph(Graph):
    def __init__(self, store: SPARQLUpdateStore = None, **kwargs):
        super().__init__(**kwargs)
        self._journal = list()
        self._store = store

    def add(self, triple):
        super().add(triple)
        self._journal.append(("add", triple))
        return self

    def remove(self, triple):
        super().remove(triple)
        self._journal.append(("remove_all" if triple[2] is None else "remove", triple))
        return self

    def addN(self, quads):
        raise NotImplementedError()

    def flush(self, context=None):
        if self._store is None:
            raise ValueError("{g} has no store, but flush() called".format(g=self))
        if len(self._journal) > 0:
            if context is None:
                add_update = "INSERT DATA { $stuff }"
                remove_update = "DELETE DATA { $stuff }"
                remove_all_update = "DELETE WHERE { $stuff }"
            else:
                add_update = "INSERT DATA { GRAPH $context { $stuff } }"
                remove_update = "DELETE DATA { GRAPH $context { $stuff } }"
                remove_all_update = "DELETE WHERE { GRAPH $context { $stuff } }"
            mods = list()
            case = self._journal[0][0]
            current_mods = Graph()
            for new_case, triple in self._journal:
                if new_case != case:
                    mods.append((case, current_mods))
                    case = new_case
                    current_mods = Graph()
                current_mods.add(triple)
            mods.append((case, current_mods))
            updates = list()
            for case, triples in mods:
                if case == "add" or case == "remove":
                    updates.append(Templated.convert(add_update if case == "add" else remove_update,
                                                     {"stuff": ntriples(triples),
                                                      "context": context}))
                else:
                    for triple in triples:
                        g = graphFrom(list((triple[0], triple[1], Variable("x"))))
                        updates.append(Templated.convert(remove_all_update,
                                                         {"stuff": ntriples(g),
                                                          "context": context}))
            self._store.update(";".join(updates))
            self._journal = list()
