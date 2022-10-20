#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Orchestrate Taxonomy Generation """


import pandas as pd
from pandas import DataFrame

from baseblock import BaseObject

from owl_builder.autorels.svc import FindImpliesRelationships
from owl_builder.autorels.svc import FindRequiresRelationships
from owl_builder.autorels.svc import GenerateRelationshipsTTL


class AutoRelsOrchestrator(BaseObject):
    """ Orchestrate Taxonomy Generation """

    def __init__(self):
        """ Change Log:

        Created:
            18-Jul-20922
            craigtrim@gmail.com
            *   https://github.com/craigtrim/buildolw/issues/4

        """
        BaseObject.__init__(self, __name__)

    def dataframe(self,
                  terms: list) -> DataFrame or None:

        master = []

        results = FindImpliesRelationships().process(terms)
        if results:
            [master.append(x) for x in results]

        results = FindRequiresRelationships().process(terms)
        if results:
            [master.append(x) for x in results]

        if not master:
            return None

        return pd.DataFrame(master)

    def ttl(self,
            df: DataFrame) -> list:
        return GenerateRelationshipsTTL().process(df)
