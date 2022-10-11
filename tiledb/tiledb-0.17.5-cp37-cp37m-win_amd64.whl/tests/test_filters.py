import numpy as np
from numpy.testing import assert_array_equal, assert_allclose
import pytest
import warnings

import tiledb
from tiledb.tests.common import DiskTestCase


class TestFilterTest(DiskTestCase):
    def test_filter(self):
        gzip_filter = tiledb.GzipFilter(level=10)
        self.assertIsInstance(gzip_filter, tiledb.Filter)
        self.assertEqual(gzip_filter.level, 10)

        bw_filter = tiledb.BitWidthReductionFilter(window=10)
        self.assertIsInstance(bw_filter, tiledb.Filter)
        self.assertEqual(bw_filter.window, 10)

        filter_list = tiledb.FilterList([gzip_filter, bw_filter], chunksize=1024)
        self.assertEqual(filter_list.chunksize, 1024)
        self.assertEqual(len(filter_list), 2)
        self.assertEqual(filter_list[0].level, gzip_filter.level)
        self.assertEqual(filter_list[1].window, bw_filter.window)

        # test filter list iteration
        self.assertEqual(len(list(filter_list)), 2)

        # test `filters` kwarg accepts python list of filters
        tiledb.Attr("foo", dtype=np.int64, filters=[gzip_filter])
        tiledb.Attr("foo", dtype=np.int64, filters=(gzip_filter,))

        attr = tiledb.Attr("foo", dtype=np.int64, filters=filter_list)

        self.assertEqual(len(attr.filters), 2)
        self.assertEqual(attr.filters.chunksize, filter_list.chunksize)

    def test_filter_list(self):
        # should be constructible without a `filters` keyword arg set
        filter_list1 = tiledb.FilterList()
        filter_list1.append(tiledb.GzipFilter())
        self.assertEqual(len(filter_list1), 1)

        filter_list2 = [x for x in filter_list1]
        attr = tiledb.Attr(filters=filter_list2)
        self.assertEqual(len(attr.filters), 1)

    def test_all_filters(self):
        # test initialization
        filters = [
            tiledb.NoOpFilter(),
            tiledb.GzipFilter(),
            tiledb.ZstdFilter(),
            tiledb.LZ4Filter(),
            tiledb.RleFilter(),
            tiledb.Bzip2Filter(),
            tiledb.DoubleDeltaFilter(),
            tiledb.DictionaryFilter(),
            tiledb.BitWidthReductionFilter(),
            tiledb.BitShuffleFilter(),
            tiledb.ByteShuffleFilter(),
            tiledb.PositiveDeltaFilter(),
            tiledb.ChecksumSHA256Filter(),
            tiledb.ChecksumMD5Filter(),
            tiledb.FloatScaleFilter(),
        ]
        # make sure that repr works and round-trips correctly
        for f in filters:
            # some of these have attributes, so we just check the class name here
            self.assertTrue(type(f).__name__ in repr(f))

            tmp_globals = dict()
            setup = "from tiledb import *"
            exec(setup, tmp_globals)

            filter_repr = repr(f)
            new_filter = None
            try:
                new_filter = eval(filter_repr, tmp_globals)
            except Exception:
                warn_str = (
                    """Exception during FilterTest filter repr eval"""
                    + """, filter repr string was:\n"""
                    + """'''"""
                    + """\n{}\n'''""".format(filter_repr)
                )
                warnings.warn(warn_str)
                raise

            self.assertEqual(new_filter, f)

    def test_dictionary_encoding(self):
        path = self.path("test_dictionary_encoding")
        dom = tiledb.Domain(tiledb.Dim(name="row", domain=(0, 9), dtype=np.uint64))
        attr = tiledb.Attr(
            dtype="ascii",
            var=True,
            filters=tiledb.FilterList([tiledb.DictionaryFilter()]),
        )
        schema = tiledb.ArraySchema(domain=dom, attrs=[attr], sparse=True)
        tiledb.Array.create(path, schema)

        data = [b"x" * i for i in np.random.randint(1, 10, size=10)]

        with tiledb.open(path, "w") as A:
            A[np.arange(10)] = data

        with tiledb.open(path, "r") as A:
            assert_array_equal(A[:][""], data)

    @pytest.mark.parametrize("factor", [1, 0.5, 2])
    @pytest.mark.parametrize("offset", [0])
    @pytest.mark.parametrize("bytewidth", [1, 8])
    def test_float_scaling_filter(self, factor, offset, bytewidth):
        path = self.path("test_float_scaling_filter")
        dom = tiledb.Domain(tiledb.Dim(name="row", domain=(0, 9), dtype=np.uint64))

        filter = tiledb.FloatScaleFilter(factor, offset, bytewidth)

        attr = tiledb.Attr(dtype=np.float64, filters=tiledb.FilterList([filter]))
        schema = tiledb.ArraySchema(domain=dom, attrs=[attr], sparse=True)
        tiledb.Array.create(path, schema)

        data = np.random.rand(10)

        with tiledb.open(path, "w") as A:
            A[np.arange(10)] = data

        with tiledb.open(path, "r") as A:
            filter = A.schema.attr("").filters[0]
            assert filter.factor == factor
            assert filter.offset == offset
            assert filter.bytewidth == bytewidth

            # TODO compute the correct tolerance here
            assert_allclose(data, A[:][""], rtol=1, atol=1)
