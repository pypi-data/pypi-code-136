# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
from textwrap import dedent
import unittest

from pdkmaster import _util
from pdkmaster.technology import (
    property_ as _prp, mask as _msk, edge as _edg, geometry as _geo
)
from pdkmaster.io import klayout as _kl

from ...dummy import dummy_tech, dummy_gdslayers, dummy_lib, empty_tech

import pya


class FileExportTest(unittest.TestCase):
    def test_maskconverter(self):
        from pdkmaster.technology.wafer_ import wafer
        from pdkmaster.io.klayout.export import _MaskConverter

        mc = _MaskConverter(tech=dummy_tech)

        mask = _msk.DesignMask(name="layer0", fill_space="no")
        alias = mask.alias("0layer:s1.s2")
        mask2 = _msk.DesignMask(name="layer1", fill_space="no")

        self.assertEqual(mc(mask), "layer0")
        self.assertEqual(mc(alias), "_0layer__s1_s2")
        self.assertEqual(mc(_msk.Join((mask, mask2))), "(layer0+layer1)")
        self.assertEqual(mc(_msk.Intersect((mask, mask2))), "(layer0&layer1)")
        self.assertEqual(mc(mask.remove(mask2)), "(layer0-layer1)")
        self.assertEqual(mc(wafer), "extent.sized(1.0)")

    def test_waferempty(self):
        from pdkmaster.technology.wafer_ import wafer
        from pdkmaster.io.klayout.export import _MaskConverter

        mc = _MaskConverter(tech=empty_tech)
        self.assertEqual(mc(wafer), "extent")

    def test_edgeconverter(self):
        from pdkmaster.io.klayout import export
        # _edge_conv needs _mask_conv to be initialized
        export._mask_conv = export._MaskConverter(tech=dummy_tech)

        ec = export._edge_conv

        mask = _msk.DesignMask(name="mask", fill_space="no")
        edge = _edg.MaskEdge(mask)
        mask2 = _msk.DesignMask(name="mask2", fill_space="no")
        edge2 = _edg.MaskEdge(mask2)

        interact1 = edge.interact_with(mask2)
        interact2 = edge.interact_with(edge2)

        self.assertEqual(ec(edge), "mask.edges")
        self.assertEqual(ec(interact1), "mask.edges.interacting(mask2)")
        self.assertEqual(ec(interact2), "mask.edges.interacting(mask2.edges)")
        self.assertEqual(ec(_edg.Join((edge, edge2))), "(mask.edges+mask2.edges)")
        self.assertEqual(ec(_edg.Join((edge, mask2))), "(mask.edges+mask2)")
        self.assertEqual(ec(_edg.Intersect((edge, edge2))), "(mask.edges&mask2.edges)")
        self.assertEqual(ec(_edg.Intersect((edge, mask2))), "(mask.edges&mask2)")

        export._mask_conv = None

    def test_stralias(self):
        from pdkmaster.io.klayout import export
        export._mask_conv = export._MaskConverter(tech=dummy_tech)

        mask = _msk.DesignMask(name="mask", fill_space="no")
        alias = mask.alias("alias")
        self.assertEqual(export._str_alias(alias), "alias = mask\n")

        export._mask_conv = None

    def test_ruleconverter(self):
        from pdkmaster.io.klayout import export
        # _edge_conv needs _mask_conv to be initialized
        export._mask_conv = export._MaskConverter(tech=dummy_tech)

        rc = export._rule_conv

        mask = _msk.DesignMask(name="mask", fill_space="no")
        alias = mask.alias("alias")
        edge = _edg.MaskEdge(mask)
        mask2 = _msk.DesignMask(name="mask2", fill_space="no")

        self.assertEqual(
            rc(mask.area >= 0.1),
            dedent("""
                # mask.area >= 0.1
                mask.with_area(nil, 0.1).output(
                    "mask area", "mask minimum area: 0.1µm"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(mask.density >= 0.25),
            dedent("""
                # mask.density >= 0.25
                mask_mindens = polygon_layer
                dens_check(mask_mindens, mask, 0.25, 1)
                mask_mindens.output(
                    "mask density", "mask minimum density: 25%"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(mask.density <= 0.80, allow_unimplented=True),
            dedent("""
                # mask.density <= 0.8
                # Not supported
            """[1:]),
        )
        self.assertEqual(
            rc(alias.space >= 1.0, allow_unimplented=True),
            dedent("""
                # alias.space >= 1.0
                alias.space(1.0).output(
                    "alias space", "alias minimum space: 1.0µm"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(edge.length >= 0.5),
            dedent("""
                # edge(mask).length >= 0.5
                mask.edges.with_length(nil, 0.5).output(
                    "mask.edges length",
                    "Minimum length of mask.edges: 0.5µm"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(_msk.Spacing(mask, mask2) >= 1.0),
            dedent("""
                # space(mask,mask2) >= 1.0
                mask.separation(mask2, 1.0, square).output(
                    "mask:mask2 spacing",
                    "Minimum spacing between mask and mask2: 1.0µm"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(_msk.OverlapWidth(mask, mask2) >= 0.5),
            dedent("""
                # overlapwidth(mask,mask2) >= 0.5
                (mask&mask2).width(0.5).output(
                    "mask:mask2 overlap width",
                    "Minimum overlap widht of mask and mask2: 0.5µm"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(mask.extend_over(mask2) >= 0.1),
            dedent("""
                # mask.extend_over(mask2) >= 0.1
                extend_check(mask2, mask, 0.1).output(
                    "mask:mask2 extension",
                    "Minimum extension of mask of mask2: 0.1µm"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(mask.enclosed_by(mask2) >= 0.1),
            dedent("""
                # mask.enclosed_by(mask2) >= Enclosure(0.1)
                mask2.enclosing(mask, 0.1).output(
                    "mask2:mask enclosure",
                    "Minimum enclosure of mask2 around mask: 0.1µm"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(edge.enclosed_by(mask2) >= 0.1),
            dedent("""
                # edge(mask).enclosed_by(mask2) >= 0.1
                mask2.edges.enclosing(mask.edges, 0.1).output(
                    "mask2.edges:mask.edges enclosure",
                    "Minimum enclosure of mask2.edges around mask.edges: 0.1µm"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(mask.enclosed_by(mask2) >= _prp.Enclosure((0.2, 0.1))),
            dedent("""
                # mask.enclosed_by(mask2) >= Enclosure((0.2,0.1))
                oppenc_check(mask, mask2, 0.1, 0.2).output(
                    "mask2:mask asymmetric enclosure",
                    "Minimum enclosure of mask2 around mask: 0.1µm minimum, 0.2µm opposite"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(_msk.Spacing(mask.parts_with(mask.width >= 3.0), mask) >= 0.8),
            dedent("""
                # space(mask.parts_with(mask.width >= 3.0),mask) >= 0.8
                space4width_check(mask, 3.0, 0.8).output(
                    "mask table spacing",
                    "Minimum mask spacing for 3.0µm width: 0.8µm"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(_msk.Spacing(mask, mask.parts_with(mask.width >= 3.0)) >= 0.8),
            dedent("""
                # space(mask,mask.parts_with(mask.width >= 3.0)) >= 0.8
                space4width_check(mask, 3.0, 0.8).output(
                    "mask table spacing",
                    "Minimum mask spacing for 3.0µm width: 0.8µm"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(mask.width == 0.5),
            dedent("""
                # mask.width == 0.5
                width_check(mask, 0.5).output(
                    "mask width", "mask width: 0.5µm"
                )
            """[1:]),
        )
        self.assertEqual(
            rc(mask.area == 0.0),
            dedent("""
                # mask.area == 0.0
                mask.output("mask empty")
            """[1:]),
        )
        with self.assertRaises(ValueError):
            rc(mask.area == 1.0)
        self.assertEqual(
            rc(edge.length == 0.0),
            dedent("""
                # edge(mask).length == 0.0
                mask.edges.output("mask.edges empty")
            """[1:]),
        )
        with self.assertRaises(ValueError):
            rc(edge.length == 0.1)
        self.assertEqual(
            rc(alias),
            dedent("""
                # mask.alias(alias)
                alias = mask
            """[1:]),
        )
        self.assertEqual(
            rc(_msk.Connect(mask, mask2)),
            dedent("""
                # connect(mask,mask2)
                connect(mask, mask2)
            """[1:]),
        )

        export._mask_conv = None

    def test_shapeexporter(self):
        from pdkmaster.io.klayout.export import _ShapeExporter

        se = _ShapeExporter(export_fullshape=False)

        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=1.0, bottom=0.0, right=2.0, top=1.0)
        rect12 = _geo.Rect(left=0.0, bottom=0.0, right=2.0, top=1.0)
        shapes = (rect1, rect2)
        rs = _geo.RepeatedShape(
            shape=rect1, n=2, n_dxy=_geo.Point(x=0.0, y=2.0), offset0=_geo.origin,
        )
        ms1 = _geo.MultiShape(shapes=shapes)
        ms2 = _geo.MultiShape(shapes=(*shapes, rs))
        mps = _geo.MultiPartShape(fullshape=rect12, parts=shapes)
        part0 = mps.parts[0]
        part1 = mps.parts[1]
        rmps = _geo.RepeatedShape(
            shape=mps, n=3, n_dxy=_geo.Point(x=0.0, y=10.0), offset0=_geo.origin,
        )

        rr = _geo.RectRing(outer_bound=rect1, rect_width=0.3, min_rect_space=0.3)

        self.assertEqual(
            se(_geo.Point(x=0.0, y=0.0)),
            pya.DPoint(0.0, 0.0),
        )
        self.assertEqual(
            se(_geo.Line(point1=_geo.Point(x=0.0, y=0.0), point2=_geo.Point(x=0.0, y=1.0))),
            pya.DPath((pya.DPoint(0.0, 0.0), pya.DPoint(0.0, 1.0)), 0.0),
        )
        points = (
            (0.0, 0.0), (0.0, 2.0), (2.0, 2.0), (2.0, 1.0), (1.0, 1.0), (1.0, 0.0), (0.0, 0.0),
        )
        self.assertEqual(
            se(_geo.Polygon.from_floats(points=points)),
            pya.DSimplePolygon(tuple(pya.DPoint(x, y) for x, y in points[:-1])),
        )
        self.assertEqual(se(rect1), pya.DBox(0.0, 0.0, 1.0, 1.0))
        self.assertEqual(set(se(ms1)), set(se(shape) for shape in shapes))
        self.assertEqual(set(se(ms2)), set(se(shape) for shape in ms2.pointsshapes))

        self.assertEqual(
            set(se(rmps)),
            set(se(ps) for ps in rmps.pointsshapes),
        )

        self.assertEqual(se(mps), se(mps.fullshape))
        self.assertEqual(se(part0), se(part0.partshape))

        se2 = _ShapeExporter(export_fullshape=True)
        self.assertEqual(se2(part0), se2(mps.fullshape))
        self.assertIsNone(se2(part1))

        self.assertEqual(set(se(rr)), set(se(shape) for shape in rr.pointsshapes))

    def test_tech(self):
        # We just generate the code to get the code coverage.
        # Correctness of out is assumed to be checked with lower level unit tests
        # on the Exporter classes and higher level test using gds files etc.
        _kl.FileExporter(tech=dummy_tech, gds_layers=dummy_gdslayers)()


class Export2DBTest(unittest.TestCase):
    # We don't foresee special unit test for _LayoutExporter class
    # All test of that class to be done through export2db unit tests
    rect_geo = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
    rect_kl = pya.DBox(0.0, 0.0, 1.0, 1.0)

    def test_error(self):
        with self.assertRaises(TypeError):
            _kl.export2db(3, gds_layers=dummy_gdslayers)

    def test_rect(self):
        rect_conv = _kl.export2db(self.rect_geo)
        self.assertEqual(rect_conv, self.rect_kl)

        with self.assertRaises(AssertionError):
            _kl.export2db(self.rect_geo, gds_layers=dummy_gdslayers)

    def test_maskshapes(self):
        # This mainly runs code to get coverage but does not extensive test of correctness
        # of results. This is assumed to be done with lower level unit tests.
        mask = _util.first(dummy_tech.designmasks)

        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=2.0, bottom=0.0, right=3.0, top=1.0)

        ms = _geo.MultiShape(shapes=(rect1, rect2))

        msr1 = _geo.MaskShape(mask=mask, shape=rect1)
        msr2 = _geo.MaskShape(mask=mask, shape=ms)

        with self.assertRaises(AssertionError):
            _kl.export2db(msr1)
        kllay = _kl.export2db(msr1, gds_layers=dummy_gdslayers)
        self.assertIsInstance(kllay, pya.Layout)
        kllay = _kl.export2db(msr2, gds_layers=dummy_gdslayers)
        self.assertIsInstance(kllay, pya.Layout)

    def test_cells_library(self):
        # This mainly runs code to get coverage but does not extensive test of correctness
        # of results. This is assumed to be done with lower level unit tests.
        _kl.export2db(
            dummy_lib.cells.cell1, gds_layers=dummy_gdslayers, add_pin_label=True, merge=True,
        )

        with self.assertRaises(AssertionError):
            _kl.export2db(dummy_lib, gds_layers=dummy_gdslayers, cell_name="test")
        _kl.export2db(dummy_lib, gds_layers=dummy_gdslayers, add_pin_label=True, merge=True)
