from django.test import TestCase

from server.models import TestDiff


class ModelDiffTestCase(TestCase):
    def setUp(self):
        self.obj = TestDiff(name="Foo")
        self.obj.save()

    def _no_change(self):
        self.assertEqual(self.obj.has_changed, False)
        self.assertEqual(list(self.obj.changed_fields), [])

    def test_no_change(self):
        self.assertEqual(self.obj.name, "Foo")
        self._no_change()

    def test_name_change(self):
        self.obj.name = "Bar"
        self.assertEqual(self.obj.name, "Bar")
        self.assertEqual(self.obj.has_changed, True)
        self.assertTrue("name" in self.obj.changed_fields)

        self.assertFalse(self.obj.recorded_name_change)
        self.obj.save()
        self.assertTrue(self.obj.recorded_name_change)
        self._no_change()

    def test_number_change(self):
        self.obj.number = 100
        self.assertEqual(self.obj.number, 100)
        self.assertEqual(self.obj.has_changed, True)
        self.assertTrue("number" in self.obj.changed_fields)

        self.obj.save()
        self._no_change()

    def test_initial(self):
        obj = TestDiff(name="Billy", number=1)
        obj.save()
        obj.number = 100

        self.assertEqual(obj.initial["number"], 1)

    def test_string_to_int(self):
        tm = TestDiff(name="Sally", number=1)
        tm.save()
        tm.number = "2"

        self.assertDictEqual(
            {"number": (1, 2)},
            tm._get_diff(),
        )

    def test_jsonfield_change(self):
        tm = TestDiff(a_json_field={"hi": "bye"})
        tm_2 = TestDiff(a_json_field={'beep': 'boop'})
        tm.save()
        tm_2.save()
        self.assertFalse(tm.has_changed)
        self.assertFalse(tm_2.has_changed)

        # Change a single field, should be marked as having changed
        tm.a_json_field['hi'] = 'OH YEAH!'

        # Ditto for setting a brand-new dict
        tm_2.a_json_field = {'beep': 'bloop'}

        self.assertTrue(tm.has_changed)
        self.assertTrue(tm_2.has_changed)

    def test_is_creation(self):
        tm = TestDiff.objects.create(name="New Thing")
        self.assertTrue(tm.is_creation)
        tm.save()
        self.assertFalse(tm.is_creation)

    def test_deferred_recursion_error(self):
        """
        Regression test: in some cases, deferring a field has caused infinite recursion
        """
        TestDiff.objects.create(name="sub", myself=self.obj)
        objects = TestDiff.objects.all().only("id")
        self.assertEqual(2, len(objects))
