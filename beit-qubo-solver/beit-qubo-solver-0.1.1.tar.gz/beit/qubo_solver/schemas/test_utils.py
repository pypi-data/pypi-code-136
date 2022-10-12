import json
import unittest

from beit.runfiles import runfiles
from jsonschema import validate, ValidationError

def JSONSchemaTest(schema_path) -> type:

    class JSONSchemaTest(unittest.TestCase):

        RUNFILES = runfiles.Create()
        schema = json.load(open(RUNFILES.Rlocation(schema_path)))
        metaschema = json.load(open(RUNFILES.Rlocation("json_schema/file/metaschema.json")))
        metaschema["additionalProperties"] = False

        @classmethod
        def setUpClass(cls):
            """
            Checks whether the schema is a valid AWS-flavoured schema.
            If not, no other tests are run.
            """
            validate(cls.schema, schema=cls.metaschema)

        def assertCorrect(self, tested_json):
            validate(tested_json, schema=self.schema)
    
        def assertIncorrect(self, tested_json):
            with self.assertRaises(ValidationError):
                validate(tested_json, schema=self.schema)
    
    return JSONSchemaTest