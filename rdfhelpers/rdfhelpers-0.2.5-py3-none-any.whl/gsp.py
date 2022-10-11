# Copyright (c) 2022, Ora Lassila & So Many Aircraft
# All rights reserved.
#
# See LICENSE for licensing information
#
# This module implements experimental support of the SPARQL Graph Store HTTP Protocol
# for RDFLib. Not all method are implemented (yet)
#

import sys
import rdflib
import requests
import io

class GraphStoreClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get(self, context):
        response = requests.get(self.endpoint, {"graph": str(context)})
        if response.raise_for_status() is None:
            results = rdflib.Graph()
            results.parse(source=ResponseStream(response), format=responseContentType(response))
            return None if len(results) == 0 else results

    def put(self, context):
        raise NotImplementedError()

    def post(self, content):
        raise NotImplementedError()

    def delete(self, context):
        raise NotImplementedError()

    def head(self, context):
        raise NotImplementedError()


def responseContentType(response):
    ct = response.headers.get("Content-Type", None)
    if ct is None:
        return None
    else:
        i = ct.find(";")
        if i != -1:
            ct = ct[0:i]
    return ct

# ResponseStream adapted from https://gist.github.com/obskyr/b9d4b4223e7eaf4eedcd9defabb34f13
class ResponseStream(object):
    def __init__(self, response, chunk_size=64):
        self.stream = io.BytesIO()
        self.response = response
        self.iterator = response.iter_content(chunk_size)

    def load(self, target_pos):
        pos = self.stream.seek(0, io.SEEK_END)
        if target_pos is None:
            # load everything
            for chunk in self.iterator:
                self.stream.write(chunk)
        else:
            while pos < target_pos:
                try:
                    pos += self.stream.write(next(self.iterator))
                except StopIteration:
                    break

    def tell(self):
        return self.stream.tell()

    def read(self, size=None):
        pos = self.stream.tell()
        self.load(None if size is None else pos + size)
        self.stream.seek(pos)
        return self.stream.read(size)

    def seek(self, position, whence=io.SEEK_SET):
        if whence == io.SEEK_END:
            self.load(None)
        else:
            self.stream.seek(position, whence)

    def close(self):
        self.stream.close()
        self.response.close()

if __name__ == "__main__":
    client = GraphStoreClient("http://localhost:7200/repositories/omni-dev-2/rdf-graphs/service")
    OMNI = rdflib.Namespace("https://somanyaircraft.com/data/schemata/omni/1/core#")
    client.get(OMNI.Housekeeping).serialize(destination=sys.stdout.buffer)
