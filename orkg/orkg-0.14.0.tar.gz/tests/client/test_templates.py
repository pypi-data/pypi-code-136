from unittest import TestCase
from orkg import ORKG


class TestTemplates(TestCase):
    """
    Some test scenarios might need to be adjusted to the content of the running ORKG instance
    """
    orkg = ORKG(host="https://sandbox.orkg.org")

    def test_materialize(self):
        self.orkg.templates.materialize_templates(templates=['R199091', 'R199040'], verbose=False)
        self.assertTrue(True)

    def test_df_template(self):
        from pandas import DataFrame as df
        lst = ['this', 'is', 'fancy']
        lst2 = [4, 2, 5]
        param = df(list(zip(lst, lst2)), columns=['word', 'length'])
        self.orkg.templates.materialize_template(template_id='R199091')
        self.orkg.templates.test_df(label="what!", dataset=(param, 'Fancy Table'), uses_library="pyORKG").pretty_print(format='json-ld')
        self.assertTrue(True)


