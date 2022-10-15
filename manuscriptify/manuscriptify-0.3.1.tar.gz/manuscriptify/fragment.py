# manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Open source, MIT license: http://www.opensource.org/licenses/mit-license.php
"""
doc getter

"""
from manuscriptify.google_api.clients import Clients


class Fragment(list):

    def __init__(self, id_):
        """get the content fragment"""
        docs = Clients()['docs']
        doc = docs.documents().get(documentId=id_).execute()
        useful_stuff = ['paragraph']
        stuff = [{k:elem[k]}
                 for k in useful_stuff
                 for elem in doc['body']['content']
                 if k in elem]
        super().__init__(doc['body']['content'])
