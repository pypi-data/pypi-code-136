#
# Copyright (c) 2015-2021 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_thesaurus.api.rest module

Thesaurus REST API module.
"""

import sys

from colander import MappingSchema, SchemaNode, SequenceSchema, String, drop
from cornice import Service
from cornice.validators import colander_querystring_validator
from hypatia.text import ParseError
from pyramid.httpexceptions import HTTPOk

from pyams_security.interfaces.base import VIEW_SYSTEM_PERMISSION
from pyams_security.rest import check_cors_origin, set_cors_headers
from pyams_thesaurus.interfaces import REST_EXTRACTS_GETTER_ROUTE, REST_TERMS_SEARCH_ROUTE


__docformat__ = 'restructuredtext'

from pyams_thesaurus import _
from pyams_thesaurus.interfaces.term import STATUS_ARCHIVED
from pyams_thesaurus.interfaces.thesaurus import IThesaurus, IThesaurusExtracts
from pyams_utils.list import unique
from pyams_utils.registry import query_utility


TEST_MODE = sys.argv[-1].endswith('/test')


#
# Thesaurus extracts getter services
#

class ThesaurusExtractsGetterSchema(MappingSchema):
    """Thesaurus extracts getter schema"""
    thesaurus_name = SchemaNode(String(),
                                description=_("Selected thesaurus name"))


class ThesaurusExtractResultSchema(MappingSchema):
    """Thesaurus extracts getter result schema"""


class ThesaurusExtractsResults(SequenceSchema):
    """Thesaurus extracts result schema"""
    result = ThesaurusExtractResultSchema()


class ThesaurusExtractsResultsSchema(MappingSchema):
    """Thesaurus extracts results schema"""
    results = ThesaurusExtractsResults(description=_("Results list"))


extracts_search_response = {
    HTTPOk.code: ThesaurusExtractsResultsSchema(description=_("Search results"))
}
if TEST_MODE:
    extracts_service_params = {}
else:
    extracts_service_params = {
        'response_schemas': extracts_search_response
    }


extracts_service = Service(name=REST_EXTRACTS_GETTER_ROUTE,
                           pyramid_route=REST_EXTRACTS_GETTER_ROUTE,
                           description="Thesaurus extracts management")


@extracts_service.options(validators=(check_cors_origin, set_cors_headers),
                          **extracts_service_params)
def extracts_options(request):  # pylint: disable=unused-argument
    """Extracts service OPTIONS handler"""
    return ''


@extracts_service.get(permission=VIEW_SYSTEM_PERMISSION,
                      schema=ThesaurusExtractsGetterSchema(),
                      validators=(check_cors_origin, colander_querystring_validator,
                                  set_cors_headers),
                      **extracts_service_params)
def get_extracts(request):
    """Get thesaurus extracts list"""
    if TEST_MODE:
        thesaurus_name = request.params.get('thesaurus_name')
    else:
        thesaurus_name = request.validated.get('thesaurus_name')
    if not thesaurus_name:
        return {}
    thesaurus = query_utility(IThesaurus, name=thesaurus_name)
    if thesaurus is None:
        return {}
    extracts = IThesaurusExtracts(thesaurus)
    return {
        'results': [
            {
                'id': extract.name,
                'text': extract.name
            }
            for extract in extracts.values()
        ]
    }


#
# Thesaurus terms search services
#

class ThesaurusTermsSearchQuerySchema(MappingSchema):
    """Thesaurus terms search schema"""
    thesaurus_name = SchemaNode(String(),
                                description=_("Selected thesaurus name"))
    extract_name = SchemaNode(String(),
                              description=_("Selected extract name"),
                              missing=drop)
    term = SchemaNode(String(),
                      description=_("Terms search string"))


class ThesaurusTermResultSchema(MappingSchema):
    """Thesaurus term result schema"""
    id = SchemaNode(String(),
                    description=_("Term ID"))
    text = SchemaNode(String(),
                      description=_("Term label"))


class ThesaurusSearchResults(SequenceSchema):
    """Thesaurus search results interface"""
    result = ThesaurusTermResultSchema()


class ThesaurusSearchResultsSchema(MappingSchema):
    """Thesaurus search results schema"""
    results = ThesaurusSearchResults(description=_("Results list"))


terms_search_response = {
    HTTPOk.code: ThesaurusSearchResultsSchema(description=_("Search results"))
}
if TEST_MODE:
    terms_service_params = {}
else:
    terms_service_params = {
        'response_schemas': terms_search_response
    }


terms_service = Service(name=REST_TERMS_SEARCH_ROUTE,
                        pyramid_route=REST_TERMS_SEARCH_ROUTE,
                        description="Thesaurus terms management")


@terms_service.options(validators=(check_cors_origin, set_cors_headers),
                       **terms_service_params)
def terms_options(request):  # pylint: disable=unused-argument
    """Terms service OPTIONS handler"""
    return ''


@terms_service.get(permission=VIEW_SYSTEM_PERMISSION,
                   schema=ThesaurusTermsSearchQuerySchema(),
                   validators=(check_cors_origin, colander_querystring_validator,
                               set_cors_headers),
                   **terms_service_params)
def get_terms(request):
    """Returns list of terms matching given query"""
    if TEST_MODE:
        thesaurus_name = request.params.get('thesaurus_name')
        extract_name = request.params.get('extract_name')
        query = request.params.get('term')
    else:
        thesaurus_name = request.validated.get('thesaurus_name')
        extract_name = request.validated.get('extract_name')
        query = request.validated.get('term')
    if not (thesaurus_name or query):
        return {}
    thesaurus = query_utility(IThesaurus, name=thesaurus_name)
    if thesaurus is None:
        return {}
    try:
        return {
            'results': [
                {
                    'id': term.label,
                    'text': term.label
                }
                for term in unique(thesaurus.find_terms(query, extract_name,
                                                        exact=True, stemmed=True))
                if term.status != STATUS_ARCHIVED
            ]
        }
    except ParseError:
        return []
