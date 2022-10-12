import unittest

from import_definition import import_definition


class TestImportDefinition(unittest.TestCase):
    def setUp(self):
        pass

    def test_import_definition(self):
        imported = import_definition("define")
        self.assertTrue(hasattr(imported, "__call__"))

        # Import definition that doesn't exist.
        imported = import_definition("definetest")
        self.assertEqual(imported, None)

    def test_scope(self):
        imported = import_definition("define", namespace="metrics")
        self.assertEqual(imported, None)

        # import an object
        imported = import_definition("TestObj")
        self.assertTrue(hasattr(imported, "__init__"))

    def test_import_attr(self):
        imported = import_definition("TestObj")
        assert imported.static_func() == "static"
        assert imported().func() == "func"

    def test_import_dict(self):
        imported = import_definition("TestDict")
        assert imported["item"] == "item"

    def test_str(self):
        imported = import_definition("define")
        assert str(imported).startswith("<function define at ")

        imported = import_definition("define")
        assert repr(imported).startswith("<function define at ")
