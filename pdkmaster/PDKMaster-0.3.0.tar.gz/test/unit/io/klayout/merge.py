# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster import _util
from pdkmaster.technology import geometry as _geo
from pdkmaster.design import layout as _lay
from pdkmaster.io import klayout as _kl
from pdkmaster.io.klayout import merge_ as _klmrg

from ...dummy import MyNet, dummy_tech, dummy_cktfab, dummy_layoutfab
prims = dummy_tech.primitives


class SupportTest(unittest.TestCase):
    def test_importexport(self):
        import pya

        rect = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        polygon = _geo.Polygon.from_floats(points=(
            (0.0, 0.0), (0.0, 1.0), (1.0, 1.0), (1.0, 2.0),
            (2.0, 2.0), (2.0, 0.0), (0.0, 0.0),
        ))
        eps = _geo.epsilon
        box = pya.Box(0, 0, round(1.0/eps), round(1.0/eps))

        self.assertEqual(_klmrg._import_regionshape(_klmrg._export_polygon(rect)), rect)
        self.assertEqual(_klmrg._import_polygon(box), rect)
        self.assertEqual(_klmrg._import_regionshape(_klmrg._export_polygon(polygon)), polygon)


class MPSDictTest(unittest.TestCase):
    def test_in(self):
        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=1.0, bottom=0.0, right=2.0, top=1.0)
        rect3 = _geo.Rect(left=2.0, bottom=0.0, right=3.0, top=1.0)
        rect12 = _geo.Rect(left=0.0, bottom=0.0, right=2.0, top=1.0)
        rect123 = _geo.Rect(left=0.0, bottom=0.0, right=3.0, top=1.0)

        mps12 = _geo.MultiPartShape(fullshape=rect12, parts=(rect1, rect2))
        mps123 = _geo.MultiPartShape(fullshape=rect123, parts=(rect1, rect2, rect3))

        d = _klmrg._MPSDict(merger=_klmrg._ShapeMerger())
        e = d[mps12]

        self.assertIsInstance(e, _klmrg._MPSDictElem)
        self.assertEqual(e.mps_orig, mps12)
        self.assertEqual(len(e.partregions), 2)
        self.assertTrue(mps12 in d)
        self.assertFalse(mps123 in d)

    def test_merge_with(self):
        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=1.0, bottom=0.0, right=2.0, top=1.0)
        rect3 = _geo.Rect(left=2.0, bottom=0.0, right=3.0, top=1.0)
        rect4 = _geo.Rect(left=3.0, bottom=0.0, right=4.0, top=1.0)
        rect12 = _geo.Rect(left=0.0, bottom=0.0, right=2.0, top=1.0)
        rect34 = _geo.Rect(left=2.0, bottom=0.0, right=4.0, top=1.0)
        rect1234 = _geo.Rect(left=0.0, bottom=0.0, right=4.0, top=1.0)

        mps12 = _geo.MultiPartShape(fullshape=rect12, parts=(rect1, rect2))
        mps34 = _geo.MultiPartShape(fullshape=rect34, parts=(rect3, rect4))
        mps1234 = _geo.MultiPartShape(fullshape=rect1234, parts=(rect1, rect2, rect3, rect4))

        d =_klmrg._MPSDict()

        elem1 = d[mps12]
        elem2 = d[mps34]

        ref1 = _klmrg._PartRef(elem=elem1, idx=0)
        ref2 = _klmrg._PartRef(elem=elem1, idx=1)
        ref3 = _klmrg._PartRef(elem=elem2, idx=0)
        ref4 = _klmrg._PartRef(elem=elem2, idx=1)

        off1 = elem1.merge_with(elem1)
        off2 = elem1.merge_with(elem2)

        part1 = ref1.deref()
        part2 = ref2.deref()
        part3 = ref3.deref()
        part4 = ref4.deref()

        self.assertEqual(off1, 0)
        self.assertEqual(off2, 2)
        self.assertIsInstance(part1, _geo.MultiPartShape._Part)
        self.assertEqual(part1.partshape, rect1)
        self.assertEqual(part1.multipartshape, mps1234)
        self.assertIsInstance(part2, _geo.MultiPartShape._Part)
        self.assertEqual(part2.partshape, rect2)
        self.assertEqual(part2.multipartshape, mps1234)
        self.assertIsInstance(part3, _geo.MultiPartShape._Part)
        self.assertEqual(part3.partshape, rect3)
        self.assertEqual(part3.multipartshape, mps1234)
        self.assertIsInstance(part4, _geo.MultiPartShape._Part)
        self.assertEqual(part4.partshape, rect4)
        self.assertEqual(part4.multipartshape, mps1234)


class ShapeMergerTest(unittest.TestCase):
    def test_part_overlap(self):
        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=0.5, bottom=0.0, right=2.0, top=1.0)
        rect3 = _geo.Rect(left=2.0, bottom=0.0, right=3.0, top=1.0)
        rect12 = _geo.Rect(left=0.0, bottom=0.0, right=2.0, top=1.0)
        rect13 = _geo.Rect(left=0.0, bottom=0.0, right=3.0, top=1.0)
        mps1 = _geo.MultiPartShape(fullshape=rect12, parts=(rect1, rect2))
        mps2 = _geo.MultiPartShape(fullshape=rect13, parts=(rect1, rect3))

        # Overlapping parts
        with self.assertRaises(ValueError):
            with _klmrg._ShapeMerger() as merger:
                merger.mps_lookup[mps1]
        # Mismatch fullshape and parts
        with self.assertRaises(ValueError):
            with _klmrg._ShapeMerger() as merger:
                merger.mps_lookup[mps2]

    def test_part_poly(self):
        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=1.0, bottom=0.0, right=2.0, top=1.0)
        rect3 = _geo.Rect(left=2.0, bottom=0.0, right=3.0, top=1.0)
        rect12 = _geo.Rect(left=0.0, bottom=0.0, right=2.0, top=1.0)
        rect23 = _geo.Rect(left=1.0, bottom=0.0, right=3.0, top=1.0)
        rect123 =  _geo.Rect(left=0.0, bottom=0.0, right=3.0, top=1.0)

        mps12 = _geo.MultiPartShape(fullshape=rect12, parts=(rect1, rect2))
        mps123 = _geo.MultiPartShape(fullshape=rect123, parts=(rect1, rect23))

        merged = _klmrg._ShapeMerger()((
            mps12.parts[0],
            _geo.MultiShape(shapes=(mps12.parts[1], rect3)),
        ))

        self.assertEqual(len(merged), 2)

        part0 = merged[0].deref()
        part1 = merged[1].deref()

        self.assertIsInstance(part0, _geo.MultiPartShape._Part)
        self.assertIsInstance(part1, _geo.MultiPartShape._Part)

        self.assertEqual(part0.partshape, rect1)
        self.assertEqual(part1.partshape, rect23)
        self.assertEqual(part0.multipartshape, mps123)
        self.assertEqual(part0.multipartshape, part1.multipartshape)

    def test_parts(self):
        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=1.0, bottom=0.0, right=2.0, top=1.0)
        rect3 = _geo.Rect(left=2.0, bottom=0.0, right=3.0, top=1.0)
        rect12 = _geo.Rect(left=0.0, bottom=0.0, right=2.0, top=1.0)
        rect23 = _geo.Rect(left=1.0, bottom=0.0, right=3.0, top=1.0)
        rect123 = _geo.Rect(left=0.0, bottom=0.0, right=3.0, top=1.0)

        mps1 = _geo.MultiPartShape(fullshape=rect12, parts=(rect1, rect2))
        mps2 = _geo.MultiPartShape(fullshape=rect23, parts=(rect2, rect3))
        mps3 = _geo.MultiPartShape(fullshape=rect123, parts=(rect1, rect2, rect3))

        merged = _klmrg._ShapeMerger()((
            mps1.parts[0],
            _geo.MultiShape(shapes=(mps1.parts[1], mps2.parts[0])),
            mps2.parts[1],
        ))

        part0 = merged[0].deref()
        part1 = merged[1].deref()
        part2 = merged[2].deref()

        self.assertIsInstance(part0, _geo.MultiPartShape._Part)
        self.assertIsInstance(part1, _geo.MultiPartShape._Part)
        self.assertIsInstance(part2, _geo.MultiPartShape._Part)
        self.assertEqual(part0.partshape, rect1)
        self.assertEqual(part1.partshape, rect2)
        self.assertEqual(part2.partshape, rect3)
        self.assertEqual(part0.multipartshape, mps3)
        self.assertEqual(part0.multipartshape, part1.multipartshape)
        self.assertEqual(part0.multipartshape, part2.multipartshape)

    def test_parts_2(self):
        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=1.0, bottom=0.0, right=2.0, top=1.0)
        rect3 = _geo.Rect(left=2.0, bottom=0.0, right=3.0, top=1.0)
        rect4 = _geo.Rect(left=3.0, bottom=0.0, right=4.0, top=1.0)
        rect5 = _geo.Rect(left=4.0, bottom=0.0, right=5.0, top=1.0)
        rect6 = _geo.Rect(left=5.0, bottom=0.0, right=6.0, top=1.0)
        rect7 = _geo.Rect(left=6.0, bottom=0.0, right=7.0, top=1.0)
        rect8 = _geo.Rect(left=7.0, bottom=0.0, right=8.0, top=1.0)

        rect12 = _geo.Rect(left=0.0, bottom=0.0, right=2.0, top=1.0)
        rect23 = _geo.Rect(left=1.0, bottom=0.0, right=3.0, top=1.0)
        rect34 = _geo.Rect(left=2.0, bottom=0.0, right=4.0, top=1.0)
        rect45 = _geo.Rect(left=3.0, bottom=0.0, right=5.0, top=1.0)
        rect56 = _geo.Rect(left=4.0, bottom=0.0, right=6.0, top=1.0)
        rect67 = _geo.Rect(left=5.0, bottom=0.0, right=7.0, top=1.0)
        rect78 = _geo.Rect(left=6.0, bottom=0.0, right=8.0, top=1.0)
        rect1_8 = _geo.Rect(left=0.0, bottom=0.0, right=8.0, top=1.0)

        mps23 = _geo.MultiPartShape(fullshape=rect23, parts=(rect2, rect3))
        mps45 = _geo.MultiPartShape(fullshape=rect45, parts=(rect4, rect5))
        mps67 = _geo.MultiPartShape(fullshape=rect67, parts=(rect6, rect7))
        mps1_8 = _geo.MultiPartShape(
            fullshape=rect1_8, parts=(rect12, rect34, rect56, rect78)
        )

        merged = _klmrg._ShapeMerger()((
            _geo.MultiShape(shapes=(rect1, mps23.parts[0])),
            _geo.MultiShape(shapes=(mps23.parts[1], mps45.parts[0])),
            _geo.MultiShape(shapes=(mps45.parts[1], mps67.parts[0])),
            _geo.MultiShape(shapes=(mps67.parts[1], rect8)),
        ))

        for i, partref in enumerate(merged):
            part = partref.deref()
            msg = f"part{i}"
            self.assertIsInstance(part, _geo.MultiPartShape._Part, msg=msg)
            self.assertEqual(part.multipartshape, mps1_8, msg=msg)
            self.assertEqual(part.partshape, mps1_8.parts[i].partshape, msg=msg)

    def test_part_rect(self):
        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=1.0, bottom=0.0, right=2.0, top=1.0)
        rect3 = _geo.Rect(left=2.0, bottom=0.0, right=3.0, top=1.0)
        rect4 = _geo.Rect(left=2.5, bottom=0.0, right=4.0, top=1.0)
        rect12 = _geo.Rect(left=0.0, bottom=0.0, right=2.0, top=1.0)
        rect23 = _geo.Rect(left=1.0, bottom=0.0, right=3.0, top=1.0)
        rect34 = _geo.Rect(left=2.0, bottom=0.0, right=4.0, top=1.0)
        rect1234 = _geo.Rect(left=1.0, bottom=0.0, right=3.0, top=1.0)

        mps1 = _geo.MultiPartShape(fullshape=rect23, parts=(rect2, rect3))
        mps2 = _geo.MultiPartShape(fullshape=rect1234, parts=(rect12, rect34))

        merged = _klmrg._ShapeMerger()((
            _geo.MultiShape(shapes=(rect1, mps1.parts[0])),
            _geo.MultiShape(shapes=(mps1.parts[1], rect4)),
        ))

        part0 = merged[0].deref()
        part1 = merged[1].deref()

        self.assertIsInstance(part0, _geo.MultiPartShape._Part)
        self.assertIsInstance(part1, _geo.MultiPartShape._Part)
        self.assertEqual(part0.multipartshape, mps2)
        self.assertEqual(part0.multipartshape, part1.multipartshape)

    def test_part_rect_2(self):
        rect1_1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect1_2 = _geo.Rect(left=1.0, bottom=0.0, right=2.0, top=1.0)
        rect1_3 = _geo.Rect(left=2.0, bottom=0.0, right=3.0, top=1.0)
        rect1_123 = _geo.Rect(left=0.0, bottom=0.0, right=3.0, top=1.0)

        rect2_1 = _geo.Rect(left=0.0, bottom=2.0, right=1.0, top=3.0)
        rect2_2 = _geo.Rect(left=1.0, bottom=2.0, right=2.0, top=3.0)
        rect2_3 = _geo.Rect(left=2.0, bottom=2.0, right=3.0, top=3.0)
        rect2_123 = _geo.Rect(left=0.0, bottom=2.0, right=3.0, top=3.0)

        rect12_1 = _geo.Rect(left=-1, bottom=0.0, right=0.5, top=3.0)
        rect12_2 = _geo.Rect(left=2.5, bottom=0.0, right=4, top=3.0)

        poly12_1 = _geo.Polygon.from_floats(points=(
            (-1.0, 0.0), (-1.0, 3.0), (1.0, 3.0), (1.0, 2.0),
            (0.5, 2.0), (0.5, 1.0), (1.0, 1.0), (1.0, 0.0), (-1.0, 0.0),
        ))
        poly12_2 = _geo.Polygon.from_floats(points=(
            (2.0, 0.0), (2.0, 1.0), (2.5, 1.0), (2.5, 2.0), (2.0, 2.0), (2.0, 3.0),
            (4.0, 3.0), (4.0, 0.0), (2.0, 0.0),
        ))

        poly12_12 = _geo.Polygon.from_floats(points=(
            (-1.0, 0.0), (-1.0, 2.0), (0.5, 2.0), (0.5, 1.0), (2.5, 1.0), (2.5, 2.0),
            (-1.0, 2.0), (-1.0, 3.0), (4.0, 3.0), (4.0, 0.0), (-1.0, 0.0),
        ))

        mps1 = _geo.MultiPartShape(fullshape=rect1_123, parts=(rect1_1, rect1_2, rect1_3))
        mps2 = _geo.MultiPartShape(fullshape=rect2_123, parts=(rect2_1, rect2_2, rect2_3))
        mps12 = _geo.MultiPartShape(fullshape=poly12_12, parts=(
            poly12_1, rect1_2, rect2_2, poly12_2
        ))

        shapes = (
            _geo.MultiShape(shapes=(rect12_1, mps1.parts[0], mps2.parts[0])),
            _geo.MultiShape(shapes=(mps1.parts[1], mps2.parts[1])),
            _geo.MultiShape(shapes=(rect12_2, mps1.parts[2], mps2.parts[2])),
        )

        (part0ref, ms1, part2ref) = _klmrg._ShapeMerger()(shapes)
        part0 = part0ref.deref()
        part2 = part2ref.deref()
        (part1_0, part1_1) = ms1.deref().shapes

        self.assertIsInstance(part0, _geo.MultiPartShape._Part)
        self.assertIsInstance(part1_0, _geo.MultiPartShape._Part)
        self.assertIsInstance(part1_1, _geo.MultiPartShape._Part)
        self.assertIsInstance(part2, _geo.MultiPartShape._Part)
        self.assertEqual(part0.multipartshape, mps12)
        self.assertEqual(part0.multipartshape, part1_0.multipartshape)
        self.assertEqual(part0.multipartshape, part1_1.multipartshape)
        self.assertEqual(part0.multipartshape, part2.multipartshape)


class MergeTest(unittest.TestCase):
    def test_type(self):
        with self.assertRaises(TypeError):
            _kl.merge(1)
        with self.assertRaises(TypeError):
            _kl.merge((1,))

    def test_mutable(self):
        # Mutable objects are not hashable
        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=1.0, bottom=0.0, right=2.0, top=1.0)
        rect12 = _geo.Rect(left=0.0, bottom=0.0, right=2.0, top=1.0)
        mps1 = _geo.MultiPartShape(fullshape=rect12, parts=(rect1, rect2))
        d = _klmrg._MPSDict()
        elem = _klmrg._MPSDictElem(mps=mps1, mpsdict=d)
        elem.init_elemmps()

        with self.assertRaises(TypeError):
            hash(d)
        with self.assertRaises(TypeError):
            hash(elem)
        with self.assertRaises(TypeError):
            hash(elem.elemmps)

    def test_zeroarea(self):
        p1 = _geo.Point(x=0.0, y=0.0)
        p2 = _geo.Point(x=1.0, y=1.0)
        l1 = _geo.Line(point1=p1, point2=p2)
        ms1 = _geo.MultiShape(shapes=(p1, l1))

        self.assertEqual(_kl.merge(p1), p1)

        merged = _kl.merge(ms1)
        self.assertIsInstance(merged, _geo.MultiShape)
        self.assertEqual(merged, ms1)

    def test_rect(self):
        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=0.0, bottom=1.0, right=1.0, top=2.0)
        rect3 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=2.0)
        ms1 = _geo.MultiShape(shapes=(rect1, rect2))

        self.assertEqual(_kl.merge(rect1), rect1)
        self.assertEqual(_kl.merge(ms1), rect3)

    def test_rect_polygon(self):
        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        polygon1 = _geo.Polygon.from_floats(points=(
            (1.0, 0.0), (1.0, 1.0), (2.0, 1.0), (2.0, 2.0),
            (3.0, 2.0), (3.0, 0.0), (1.0, 0.0),
        ))
        polygon2 = _geo.Polygon.from_floats(points=(
            (0.0, 0.0), (0.0, 1.0), (2.0, 1.0), (2.0, 2.0),
            (3.0, 2.0), (3.0, 0.0), (0.0, 0.0),
        ))

        ms = _geo.MultiShape(shapes=(rect1, polygon1))

        shape = _kl.merge(ms)

        self.assertEqual(shape, polygon2)

    def test_maskshape(self):
        mask = _util.first(dummy_tech.designmasks)

        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        poly2 = _geo.Polygon.from_floats(points=(
            (1.0, 0.0), (1.0, 1.0), (2.0, 1.0), (2.0, 2.0), (3.0, 2.0), (3.0, 0.0),
            (1.0, 0.0),
        ))
        poly12 = _geo.Polygon.from_floats(points=(
            (0.0, 0.0), (0.0, 1.0), (2.0, 1.0), (2.0, 2.0), (3.0, 2.0), (3.0, 0.0),
            (0.0, 0.0),
        ))
        mps1 = _geo.MultiPartShape(fullshape=poly12, parts=(rect1, poly2))
        ms1 = _geo.MaskShape(mask=mask, shape=rect1)
        ms2 = _geo.MaskShape(mask=mask, shape=mps1.parts[0])

        self.assertEqual(_kl.merge(ms1), ms1)
        self.assertEqual(_kl.merge(ms2), ms2)

    def test_maskshapes(self):
        mask = _util.first(dummy_tech.designmasks)

        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        rect2 = _geo.Rect(left=2.0, bottom=0.0, right=3.0, top=1.0)
        ms1 = _geo.MaskShape(mask=mask, shape=rect1)
        ms2 = _geo.MaskShape(mask=mask, shape=rect2)
        mss1 = _geo.MaskShapes((ms1, ms2))

        self.assertEqual(_kl.merge(mss1), mss1)

    def test_layout(self):
        metal = prims.metal
        fab = _lay.LayoutFactory(tech=dummy_tech)

        net1 = MyNet(name="net1")
        rect1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        layout1 = fab.new_layout()
        layout1.add_shape(prim=metal, net=net1, shape=rect1)

        layout1_merged = _kl.merge(layout1)
        self.assertEqual(layout1_merged, layout1)

    def test_layout_multishapeparts(self):
        active = prims.active

        r1 = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        r2 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))
        r12 = _geo.Rect.from_floats(values=(0.0, 0.0, 2.0, 1.0))
        r3 = _geo.Rect.from_floats(values=(2.0, 0.0, 3.0, 1.0))
        r4 = _geo.Rect.from_floats(values=(3.0, 0.0, 4.0, 1.0))
        r234 = _geo.Rect.from_floats(values=(1.0, 0.0, 4.0, 1.0))
        r5 = _geo.Rect.from_floats(values=(4.0, 0.0, 5.0, 1.0))
        r45 = _geo.Rect.from_floats(values=(3.0, 0.0, 5.0, 1.0))
        r6 = _geo.Rect.from_floats(values=(5.0, 0.0, 6.0, 1.0))
        r7 = _geo.Rect.from_floats(values=(6.0, 0.0, 7.0, 1.0))
        r567 = _geo.Rect.from_floats(values=(4.0, 0.0, 7.0, 1.0))
        r8 = _geo.Rect.from_floats(values=(7.0, 0.0, 8.0, 1.0))
        r78 = _geo.Rect.from_floats(values=(6.0, 0.0, 8.0, 1.0))
        r1_8 = _geo.Rect.from_floats(values=(0.0, 0.0, 8.0, 1.0))

        mps234 = _geo.MultiPartShape(fullshape=r234, parts=(r2, r3, r4))
        mps567 = _geo.MultiPartShape(fullshape=r567, parts=(r5, r6, r7))

        ckt = dummy_cktfab.new_circuit(name="ckt")
        layouter = dummy_layoutfab.new_circuitlayouter(circuit=ckt, boundary=None)
        layout = layouter.layout

        net1 = ckt.new_net(name="net1", external=False)
        net2 = ckt.new_net(name="net2", external=False)
        net3 = ckt.new_net(name="net3", external=False)

        layout.add_shape(prim=active, net=net1, shape=r1)
        layout.add_shape(prim=active, net=net1, shape=mps234.parts[0])
        layout.add_shape(prim=active, net=None, shape=mps234.parts[1])
        layout.add_shape(prim=active, net=net2, shape=mps234.parts[2])
        layout.add_shape(prim=active, net=net2, shape=mps567.parts[0])
        layout.add_shape(prim=active, net=None, shape=mps567.parts[1])
        layout.add_shape(prim=active, net=net3, shape=mps567.parts[2])
        layout.add_shape(prim=active, net=net3, shape=r8)

        # print("test_layout_multishapepart:merge()")
        lay_m = _kl.merge(layouter.layout)
        # print("done")

        for sl in lay_m.sublayouts:
            self.assertIsInstance(sl, _lay.MaskShapesSubLayout)
            self.assertEqual(len(sl.shapes), 1)
            ms = sl.shapes[0]
            self.assertEqual(ms.mask, active.mask)
            if sl.net is None:
                self.assertIsInstance(ms.shape, _geo.MultiShape)
                self.assertTrue(all(
                    s.partshape in (r3, r6) for s in ms.shape.shapes
                ))
                self.assertTrue(all(
                    s.multipartshape.fullshape == r1_8 for s in ms.shape.shapes
                ))
            else:
                self.assertIsInstance(ms.shape, _geo.MultiPartShape._Part)
                # print(ms.shape.multipartshape.fullshape)
                self.assertEqual(ms.shape.multipartshape.fullshape, r1_8)
                if sl.net == net1:
                    self.assertEqual(ms.shape.partshape, r12)
                elif sl.net == net2:
                    self.assertEqual(ms.shape.partshape, r45)
                elif sl.net == net3:
                    self.assertEqual(ms.shape.partshape, r78)
                else:
                    assert False

    def test_library(self):
        from ...dummy import dummy_lib

        # Coverage of the library merge code
        _kl.merge(dummy_lib)
