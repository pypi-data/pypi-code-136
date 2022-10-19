import unittest
import io

from tabletools import table_cat


class TestTableCat(unittest.TestCase):
    def test_parser(self):
        parser = table_cat.parse_args(['foo', '-z'])
        self.assertEqual(parser.tables, ['foo'])
        self.assertTrue(parser.gunzip)

        parser = table_cat.parse_args(['foo', 'bar', '-z'])
        self.assertEqual(parser.tables, ['foo', 'bar'])
        self.assertTrue(parser.gunzip)

        parser = table_cat.parse_args(['foo', 'bar'])
        self.assertEqual(parser.tables, ['foo', 'bar'])
        self.assertFalse(parser.gunzip)

    def test_cat_tables(self):
        tables = [
                io.StringIO('A\tB\n0\t0\n0\t0\n'),
                io.StringIO('A\tB\n1\t1\n1\t1\n')]
        expected = 'A\tB\n0\t0\n0\t0\n1\t1\n1\t1\n'

        out = io.StringIO()
        err = table_cat.cat_tables(tables, False, out)
        out.seek(0)
        self.assertTrue(err is None)
        self.assertEqual(out.read(), expected)

        tables_bad_headers = [
                io.StringIO('A\tB\n0\t0\n0\t0\n'),
                io.StringIO('A\tC\n1\t1\n1\t1\n')]
        expected = ''

        out = io.StringIO()
        err = table_cat.cat_tables(tables_bad_headers, False, out)
        out.seek(0)
        self.assertTrue(err is not None)
        self.assertEqual(out.read(), expected)

        # TODO: Test gzipped input


if __name__ == '__main__':
    unittest.main()
