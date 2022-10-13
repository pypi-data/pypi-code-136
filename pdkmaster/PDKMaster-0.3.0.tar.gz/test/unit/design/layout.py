# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest
from typing import cast

from pdkmaster.technology import (
    property_ as _prp, mask as _msk, net as _net, geometry as _geo, primitive as _prm,
)
from pdkmaster.design import layout as _lay, library as _lbry

from ..dummy import dummy_tech, dummy_cktfab, dummy_layoutfab, dummy_lib
prims = dummy_tech.primitives


class TestNet(_net.Net):
    # Non-abstract net class
    def __init__(self, name: str):
        super().__init__(name)


class LayoutTest(unittest.TestCase):
    def test__rect(self):

        self.assertEqual(
            _lay._rect(left=0.0, bottom=0.0, right=1.0, top=1.0, enclosure=1.0),
            _lay._rect(
                left=0.0, bottom=0.0, right=1.0, top=1.0,
                enclosure=_prp.Enclosure(1.0),
            ),
        )

    def test__via_array(self):
        left = 0.0
        bottom = 0.0
        width = 1.0
        pitch = 2.0

        via = _geo.Rect.from_size(width=width, height=width)
        point = _geo.Point(x=(left + 0.5*width), y=(bottom + 0.5*width))

        self.assertEqual(
            _lay._via_array(
                left=left, bottom=bottom, width=width, pitch=pitch, rows=1, columns=1,
            ),
            via + point,
        )
        self.assertEqual(
            _lay._via_array(
                left=left, bottom=bottom, width=width, pitch=pitch, rows=2, columns=2,
            ),
            _geo.ArrayShape(
                shape=via, offset0=point, rows=2, columns=2, pitch_x=pitch, pitch_y=pitch,
            ),
        )

    def test_maskshapessublayout(self):
        m1 = _msk.DesignMask(name="mask1", fill_space="no")
        m2 = _msk.DesignMask(name="mask2", fill_space="no")
        n1 = TestNet("net1")
        p = _geo.Point(x=3.0, y=-2.0)
        rot = _geo.Rotation.R90
        r1 = _geo.Rect(left=-3.0, bottom=-1.0, right=-1.0, top=1.0)
        r2 = _geo.Rect(left=1.0, bottom=-1.0, right=3.0, top=1.0)
        ms1 = _geo.MaskShape(mask=m1, shape=r1)
        ms2 = _geo.MaskShape(mask=m2, shape=r2)
        mssl1 = _lay.MaskShapesSubLayout(
            net=n1, shapes=_geo.MaskShapes(ms1),
        )
        mssl2 = _lay.MaskShapesSubLayout(
            net=None, shapes=_geo.MaskShapes(ms1),
        )
        mssl3 = _lay.MaskShapesSubLayout(
            net=n1, shapes=_geo.MaskShapes((ms1, ms2)),
        )
        mssl4 = mssl1.dup()
        mssl4.add_shape(shape=ms2)

        self.assertNotEqual(mssl1, "")
        self.assertNotEqual(mssl1, mssl2)
        with self.assertRaises(TypeError):
            hash(mssl1)
        self.assertNotEqual(mssl1, mssl4)
        self.assertEqual(mssl3, mssl4)
        # Get coverage for _hier_strs_, don't check output
        s = "\n".join(mssl1._hier_strs_)

        mssl5 = mssl3.moved(dxy=p)
        mssl4.move(dxy=p)

        self.assertNotEqual(mssl3, mssl5)
        self.assertEqual(mssl4, mssl5)

        mssl6 = mssl3.rotated(rotation=rot).moved(dxy=p)
        mssl7 = mssl3.dup()
        mssl7.rotate(rotation=rot)
        mssl7.move(dxy=p)

        self.assertEqual(mssl6, mssl7)

    def test__instancesublayout(self):
        cell = _lbry._Cell(lib=dummy_lib, name="cell")
        ckt = cell.new_circuit()

        inst = ckt.instantiate(dummy_lib.cells.cell1, name="libcell1")

        cell2 = _lbry._Cell(lib=dummy_lib, name="cell2")
        # Create empty layout for cell2
        cell2.new_circuit()
        cell2.new_circuitlayouter()

        cell3 = _lbry._Cell(lib=dummy_lib, name="cell3")
        ckt3 = cell3.new_circuit()

        inst2 = ckt3.instantiate(cell, name="cell")
        inst3 = ckt3.instantiate(cell2, name="cell2")

        dxy = _geo.Point(x=0.0, y=1.0)
        rot = _geo.Rotation.MX

        with self.assertRaises(ValueError):
            # No layout
            _lay._InstanceSubLayout(
                inst=inst2, origin=_geo.origin, layoutname=None, rotation=_geo.Rotation.R0,
            )
        with self.assertRaises(ValueError):
            # wrong layoutname
            _lay._InstanceSubLayout(
                inst=inst2, origin=_geo.origin, layoutname="error", rotation=_geo.Rotation.R0,
            )

        sl1 = _lay._InstanceSubLayout(
            inst=inst, origin=_geo.origin, layoutname=None, rotation=_geo.Rotation.R0,
        )
        sl2 = _lay._InstanceSubLayout(
            inst=inst3, origin=_geo.origin, layoutname=None, rotation=_geo.Rotation.R0,
        )
        sl3 = sl2.rotated(rotation=rot).moved(dxy=dxy)
        sl4 = sl2.moved(dxy=dxy).rotated(rotation=rot)

        # Code coverage
        tuple(sl1.polygons)

        self.assertIs(sl2.boundary, None)

        self.assertEqual(sl2.origin, _geo.origin)
        sl2.rotate(rotation=rot)
        sl2.move(dxy=dxy)
        self.assertEqual(sl2.origin, sl3.origin)
        self.assertEqual(sl2.origin*rot, sl4.origin)
        self.assertEqual(sl2.rotation, sl3.rotation)
        self.assertEqual(sl2.rotation, sl4.rotation)

        # Code coverage
        tuple(sl1._hier_strs_)

    def test_sublayouts(self):
        mask = prims.metal.mask

        r1 = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        r2 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))
        r3 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))

        ms1 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=r1))
        ms2 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=r2))
        ms3 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=r3))

        sl1 = _lay.MaskShapesSubLayout(net=None, shapes=ms1)
        sl2 = _lay.MaskShapesSubLayout(net=None, shapes=ms2)
        sl3 = _lay.MaskShapesSubLayout(net=None, shapes=ms3)

        with self.assertRaises(ValueError):
            # sublayouts for same net
            _lay.SubLayouts((sl1, sl2))

        sls = _lay.SubLayouts((sl1,))
        self.assertIs(sls._elem_type_, _lay._SubLayout)

        # Code coverage
        self.assertEqual(len(sls), 1)
        sls += sl2
        self.assertEqual(len(sls), 1)
        sls2 = sls.dup()

        sls3 = sls2 + sl3

    def test_add(self):
        mask = prims.metal.mask

        r1 = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        r2 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))
        r12 = _geo.Rect.from_floats(values=(0.0, 0.0, 2.0, 1.0))

        mps = _geo.MultiPartShape(fullshape=r12, parts=(r1, r2))

        ms1 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[0]))
        ms2 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[1]))

        sl1 = _lay.MaskShapesSubLayout(net=None, shapes=ms1)
        sl2 = _lay.MaskShapesSubLayout(net=None, shapes=ms2)

        lay = dummy_layoutfab.new_layout()
        lay += sl1
        lay += sl2

        lay2 = dummy_layoutfab.new_layout()
        lay2.add_shape(prim=prims.metal, net=None, shape=mps.parts[0])
        lay2.add_shape(prim=prims.metal, net=None, shape=mps.parts[1])

        for l, m in ((lay, "lay"), (lay2, "lay2")):
            self.assertEqual(len(l.sublayouts), 1)
            sl = cast(_lay.MaskShapesSubLayout, l.sublayouts[0])
            self.assertIsInstance(sl, _lay.MaskShapesSubLayout)
            self.assertIsNone(sl.net)
            self.assertEqual(len(sl.shapes), 1)
            ms = sl.shapes[0]
            s = cast(_geo.MultiShape, ms.shape)
            self.assertIsInstance(s, _geo.MultiShape)
            self.assertIn(mps.parts[0], s.shapes)
            self.assertIn(mps.parts[1], s.shapes)

    def test_move(self):
        mask = prims.metal.mask

        dxy = _geo.Point(x=0.0, y=1.0)

        r1 = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        r2 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))
        r12 = _geo.Rect.from_floats(values=(0.0, 0.0, 2.0, 1.0))

        mps = _geo.MultiPartShape(fullshape=r12, parts=(r1, r2))

        mss1 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[0]))
        mss2 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[1]))
        mus = _geo.MultiShape(shapes=(mps.parts[0], mps.parts[1]))
        mss3 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mus))

        sl1 = _lay.MaskShapesSubLayout(net=None, shapes=mss1)
        sl2 = _lay.MaskShapesSubLayout(net=None, shapes=mss2)
        sl3 = _lay.MaskShapesSubLayout(net=None, shapes=mss3)

        layout = dummy_layoutfab.new_layout(sublayouts=sl3)

        mps_moved = mps.moved(dxy=dxy)

        # Make different version of the layout with the same move
        layout2 = layout.moved(dxy=dxy)
        layout.move(dxy=dxy)
        layout3 = dummy_layoutfab.new_layout()
        layout3 += layout

        l = dummy_layoutfab.new_layout()
        l += sl1
        l += sl2
        layout4 = l.moved(dxy=dxy)

        def get_parts(l: _lay._Layout):
            for sl in l.sublayouts.__iter_type__(_lay.MaskShapesSubLayout):
                for ms in sl.shapes:
                    s = ms.shape
                    if isinstance(s, _geo.MultiPartShape._Part):
                        yield s
                    elif isinstance(s, _geo.MultiShape):
                        yield from filter(
                            lambda s2: isinstance(s2, _geo.MultiPartShape._Part),
                            s.shapes,
                        )

        # Check if all layouts conform
        for l, m in (
            (layout, "layout"), (layout2, "layout2"), (layout3, "layout3"), (layout4, "layout4"),
        ):
            parts = tuple(get_parts(l))
            self.assertEqual(len(parts), 2, msg=m)
            self.assertIn(mps_moved.parts[0], parts, msg=m)
            self.assertIn(mps_moved.parts[1], parts, msg=m)

    def test__layout(self):
        metalpin = dummy_tech.primitives.metalpin
        dxy = _geo.Point(x=0.0, y=1.0)
        rot = _geo.Rotation.MY

        ###

        cell3 = dummy_lib.cells.cell3

        ckt = cell3.circuit
        lay = cell3.layout

        i_net = ckt.nets.i

        # Code coverage
        lay2 = lay.dup()

        tuple(lay.net_polygons(net=i_net))
        tuple(lay.filter_polygons(net=i_net))
        tuple(lay.filter_polygons(net=i_net, mask=metalpin.mask))
        tuple(lay.filter_polygons(net=i_net, mask=metalpin.mask, split=True))

        with self.assertRaises(TypeError):
            lay.bounds(depth=1)
        lay.bounds(net=i_net)

        self.assertEqual(lay, lay)
        self.assertNotEqual(lay, "")

        lay.freeze()
        with self.assertRaises(ValueError):
            # Adding to frozen layout
            lay += lay

        with self.assertRaises(ValueError):
            # wrong primitive
            lay.add_primitive(_prm.Auxiliary(name="error"))

        bnd1 = lay2.boundary
        lay2.move(dxy=dxy)
        lay2.rotate(rotation=rot)
        self.assertEqual(lay2.boundary, rot*(bnd1 + dxy))

        lay._hier_str_

        # code coverage
        dummy_layoutfab.new_layout(sublayouts=lay.sublayouts[0])

        ###

        cell2 = dummy_lib.cells.cell2

        ckt = cell2.circuit
        lay = cell2.layout

        # TODO: supprt _InstanceSubLayout when net=None; see
        # https://gitlab.com/Chips4Makers/PDKMaster/-/issues/34
        with self.assertRaises(AssertionError):
            tuple(lay.filter_polygons(net=None, mask=metalpin.mask))

        ###

        cell4 = dummy_lib.cells.cell4 # no boundary

        lay = cell4.layout.dup()
        lay2 = lay.moved(dxy=dxy).rotated(rotation=rot)
        lay.move(dxy=dxy)

        self.assertIs(lay.boundary, None)


class PrimitiveLayouterTest(unittest.TestCase):
    def test__primitivelayouter(self):
        layouter = _lay._PrimitiveLayouter(fab=dummy_layoutfab)

        enc = _prp.Enclosure(0.2)
        enc2 = _prp.Enclosure(1.0)
        rect = _geo.Rect.from_size(width=1.0, height=1.0)
        rect_enc = _geo.Rect.from_rect(rect=rect, bias=enc)
        rect_enc2 = _geo.Rect.from_rect(rect=rect, bias=enc2)

        with self.assertRaises(NotImplementedError):
            layouter(prims.anything_goes)

        with self.assertRaises(NotImplementedError):
            # Marker without width/height
            layouter(prims.metalpin)

        lay = layouter(prims.metalpin, width=1.0, height=1.0)
        self.assertEqual(len(lay.sublayouts), 1)
        sl = lay.sublayouts[0]
        self.assertIs(sl.net, None)
        self.assertEqual(len(sl.shapes), 1)
        ms = sl.shapes[0]
        self.assertEqual(
            ms,
            _geo.MaskShape(mask=prims.metalpin.mask, shape=rect),
        )

        # _WidthSpaceConductor without portnets
        lay = layouter(prims.metal, width=1.0, height=1.0)
        self.assertEqual(len(lay.sublayouts), 1)
        sl = lay.sublayouts[0]
        self.assertIs(sl.net, prims.metal.ports.conn)
        self.assertEqual(len(sl.shapes), 1)
        ms = sl.shapes[0]
        self.assertEqual(
            ms,
            _geo.MaskShape(mask=prims.metal.mask, shape=rect),
        )

        # WaferWire without well
        lay = layouter(
            prims.active, width=1.0, height=1.0,
            implant=prims.nplus, implant_enclosure=enc,
        )
        self.assertEqual(
            lay.sublayouts,
            _lay.SubLayouts((
                _lay.MaskShapesSubLayout(
                    net=prims.active.ports.conn,
                    shapes=_geo.MaskShapes(_geo.MaskShape(
                        mask=prims.active.mask, shape=rect,
                    ))
                ),
                _lay.MaskShapesSubLayout(
                    net=None,
                    shapes=_geo.MaskShapes(_geo.MaskShape(
                        mask=prims.nplus.mask, shape=rect_enc,
                    ))
                ),
            )),
        )

        # WaferWire with well and oxide
        lay = layouter(
            prims.active, width=1.0, height=1.0,
            implant=prims.nplus, implant_enclosure=enc,
            oxide=prims.hvox, oxide_enclosure=enc,
            well=prims.nwell, well_enclosure=enc2,
            well_net=prims.active.ports.conn,
        )
        self.assertEqual(
            lay.sublayouts,
            _lay.SubLayouts((
                _lay.MaskShapesSubLayout(
                    net=prims.active.ports.conn,
                    shapes=_geo.MaskShapes((
                        _geo.MaskShape(mask=prims.active.mask, shape=rect),
                        _geo.MaskShape(mask=prims.nwell.mask, shape=rect_enc2),
                    ))
                ),
                _lay.MaskShapesSubLayout(
                    net=None,
                    shapes=_geo.MaskShapes((
                        _geo.MaskShape(mask=prims.nplus.mask, shape=rect_enc),
                        _geo.MaskShape(mask=prims.hvox.mask, shape=rect_enc),
                    ))
                ),
            )),
        )

        # WaferWire with well but no well_net
        with self.assertRaises(TypeError):
            lay = layouter(
                prims.active, width=1.0, height=1.0,
                implant=prims.nplus, implant_enclosure=_prp.Enclosure(0.2),
                well=prims.nwell, well_enclosure=_prp.Enclosure(1.0),
            )

        # MIMTop
        with self.assertRaises(ValueError):
            layouter(prims.MIMTop)

        # Via with bottom/top_enclosure as value
        lay = layouter(
            prims.via, space=0.35, rows=1, columns=1,
            bottom=prims.metal, bottom_enclosure=enc,
            bottom_width=None, bottom_height=None,
            top=prims.metal2, top_enclosure=enc,
            top_width=None, top_height=None,
        )
        viarect = _geo.Rect.from_size(width=prims.via.width, height=prims.via.width)
        mrect = _geo.Rect.from_rect(rect=viarect, bias=enc)
        mwidth = mrect.bounds.width
        self.assertEqual(
            lay.sublayouts,
            _lay.SubLayouts((
                _lay.MaskShapesSubLayout(
                    net=prims.via.ports.conn,
                    shapes=_geo.MaskShapes((
                        _geo.MaskShape(mask=prims.via.mask, shape=viarect),
                        _geo.MaskShape(mask=prims.metal.mask, shape=mrect),
                        _geo.MaskShape(mask=prims.metal2.mask, shape=mrect),
                    ))
                )
            ))
        )

        self.assertEqual(
            layouter(
                prims.via, space=0.35, rows=None, columns=1,
                bottom=prims.metal, bottom_enclosure=enc,
                bottom_width=None, bottom_height=mwidth,
                top=prims.metal2, top_enclosure=enc,
                top_width=None, top_height=mwidth,
            ),
            layouter(
                prims.via, space=0.35, rows=1, columns=None,
                bottom=prims.metal, bottom_enclosure=enc,
                bottom_width=mwidth, bottom_height=None,
                top=prims.metal2, top_enclosure=enc,
                top_width=mwidth, top_height=None,
            ),
        )

        # Code coverage for bottom_width/bottom_height/top_width/top_width None/float
        # combinations
        layouter(
            prims.via, space=0.35, rows=None, columns=1,
            bottom=prims.metal, bottom_enclosure=enc,
            bottom_width=None, bottom_height=None,
            top=prims.metal2, top_enclosure=enc,
            top_width=None, top_height=mwidth,
        )
        layouter(
            prims.via, space=0.35, rows=None, columns=1,
            bottom=prims.metal, bottom_enclosure=enc,
            bottom_width=None, bottom_height=mwidth,
            top=prims.metal2, top_enclosure=enc,
            top_width=None, top_height=None,
        )
        layouter(
            prims.via, space=0.35, rows=1, columns=None,
            bottom=prims.metal, bottom_enclosure=enc,
            bottom_width=None, bottom_height=None,
            top=prims.metal2, top_enclosure=enc,
            top_width=mwidth, top_height=None,
        )
        layouter(
            prims.via, space=0.35, rows=1, columns=None,
            bottom=prims.metal, bottom_enclosure=enc,
            bottom_width=mwidth, bottom_height=None,
            top=prims.metal2, top_enclosure=enc,
            top_width=None, top_height=None,
        )

        # Via with bottom/top_enclosure as str
        # enclosures are symmetric so "wide" and "tall" should give same layout
        self.assertEqual(
            layouter(
                prims.via, space=0.35, rows=1, columns=1,
                bottom=prims.metal, bottom_enclosure="wide",
                bottom_width=None, bottom_height=None,
                top=prims.metal2, top_enclosure="wide",
                top_width=None, top_height=None,
            ),
            layouter(
                prims.via, space=0.35, rows=1, columns=1,
                bottom=prims.metal, bottom_enclosure="tall",
                bottom_width=None, bottom_height=None,
                top=prims.metal2, top_enclosure="tall",
                top_width=None, top_height=None,
            ),
        )

        # Via with wrong portnets
        with self.assertRaises(ValueError):
            lay = layouter(prims.via, portnets={"error": prims.via.ports.conn})

        # Via with WaferWire as bottom
        # code coverage for
        # bottom_(implant|implante_enclosre|oxide|oxide_enclosure|well|well_enclosure)
        layouter(
            prims.contact, space=0.35, rows=1, columns=1,
            bottom=prims.active, bottom_enclosure=enc,
            bottom_width=None, bottom_height=None,
            bottom_implant=prims.pplus, bottom_implant_enclosure=enc,
            bottom_oxide=prims.hvox, bottom_oxide_enclosure=enc,
            bottom_well=prims.nwell, well_net=prims.active.ports.conn,
            bottom_well_enclosure=enc,
            top=prims.metal, top_enclosure=enc,
            top_width=None, top_height=None,
        )
        layouter(
            prims.contact, space=0.35, rows=1, columns=1,
            bottom=prims.active, bottom_enclosure=enc,
            bottom_width=None, bottom_height=None,
            bottom_implant=prims.nplus, bottom_implant_enclosure=enc,
            bottom_oxide=prims.hvox, bottom_oxide_enclosure=None,
            bottom_well=prims.nwell, well_net=prims.contact.ports.conn,
            bottom_well_enclosure=enc,
            top=prims.metal, top_enclosure=enc,
            top_width=None, top_height=None,
        )
        # bottom_well not given
        with self.assertRaises(TypeError):
            layouter(
                prims.contact, space=0.35, rows=1, columns=1,
                bottom=prims.active, bottom_enclosure=enc,
                bottom_width=None, bottom_height=None,
                bottom_implant=prims.pplus, bottom_implant_enclosure=enc,
                bottom_oxide=prims.hvox, bottom_oxide_enclosure=enc,
                bottom_well=prims.nwell, well_net=None,
                bottom_well_enclosure=enc,
                top=prims.metal, top_enclosure=enc,
                top_width=None, top_height=None,
            )
        # bottom_well type is bottom_implant type but net is different
        with self.assertRaises(ValueError):
            layouter(
                prims.contact, space=0.35, rows=1, columns=1,
                bottom=prims.active, bottom_enclosure=enc,
                bottom_width=None, bottom_height=None,
                bottom_implant=prims.nplus, bottom_implant_enclosure=enc,
                bottom_oxide=prims.hvox, bottom_oxide_enclosure=None,
                bottom_well=prims.nwell, well_net=prims.poly.ports.conn,
                bottom_well_enclosure=enc,
                top=prims.metal, top_enclosure=enc,
                top_width=None, top_height=None,
            )
        # bottom_well type == implant type; same well
        lay = layouter(
            prims.contact, space=0.35, rows=1, columns=1,
            bottom=prims.active, bottom_enclosure=enc,
            bottom_width=None, bottom_height=None,
            bottom_implant=prims.nplus, bottom_implant_enclosure=enc,
            bottom_oxide=prims.hvox, bottom_oxide_enclosure=None,
            bottom_well=prims.nwell,
            bottom_well_enclosure=enc,
            top=prims.metal, top_enclosure=enc,
            top_width=None, top_height=None,
        )
        self.assertEqual(len(lay.sublayouts), 2)

        # DeppWell
        with self.assertRaises(NotImplementedError):
            layouter(prims.deepwell)

        # Resistor
        # resistor without contact layer
        with self.assertRaises(NotImplementedError):
            layouter(prims.metal2res)
        self.assertEqual(
            layouter(prims.resistor, width=1.0, height=1.0),
            layouter(
                prims.resistor, portnets={
                    "port1": prims.resistor.ports.port1,
                    "port2": prims.resistor.ports.port2,
                },
                width=1.0, height=1.0,
            ),
        )
        # wrong ports
        with self.assertRaises(ValueError):
            layouter(prims.resistor, portnets={}, width=1.0, height=1.0),

        # MIMCapacitor
        self.assertEqual(
            layouter(
                prims.MIMCap, width=1.0, height=1.0, bottom_connect_up=True,
            ),
            layouter(
                prims.MIMCap, portnets={
                    "top": prims.MIMCap.ports.top,
                    "bottom": prims.MIMCap.ports.bottom,
                },
                width=1.0, height=1.0, bottom_connect_up=True,
            ),
        )
        # code coverage for bottom_connect_up == False
        layouter(
            prims.MIMCap, width=1.0, height=1.0, bottom_connect_up=False,
        )
        # wrong ports
        with self.assertRaises(ValueError):
            layouter(
                prims.MIMCap, portnets={}, width=1.0, height=1.0,
                bottom_connect_up=True,
            )

        # Diode
        self.assertEqual(
            layouter(prims.ndiode),
            layouter(prims.ndiode, portnets={
                "anode": prims.ndiode.ports.anode,
                "cathode": prims.ndiode.ports.cathode,
            }),
        )
        self.assertNotEqual(layouter(prims.ndiode), layouter(prims.pdiode))
        # wrong portnets
        with self.assertRaises(ValueError):
            layouter(prims.ndiode, portnets={})

        # MOSFET
        self.assertNotEqual(
            layouter(
                prims.nmos, l=0.3, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
            layouter(
                prims.nmos, l=0.4, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
        )
        self.assertNotEqual(
            layouter(
                prims.nmos, l=0.3, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
            layouter(
                prims.pmos, l=0.3, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
        )
        self.assertNotEqual(
            layouter(
                prims.hvnmos, l=0.3, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
            layouter(
                prims.hvnmos, l=0.4, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
        )
        self.assertNotEqual(
            layouter(
                prims.esdnmos, l=0.3, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
            layouter(
                prims.esdnmos, l=0.4, w=0.3,
                activeimplant_enclosure=enc, gateimplant_enclosures=(enc,),
                sd_width=0.3,
            ),
        )

        # Bipolar
        # not implmented
        with self.assertRaises(NotImplementedError):
            layouter(prims.npn)

class CircuitLayouterTest(unittest.TestCase):
    def test_addwire(self):
        # MetalWire
        wire = prims.metal

        ckt = dummy_cktfab.new_circuit(name="test")
        net = ckt.new_net(name="net", external=False)

        shape = _geo.Rect(left=1.0, bottom=-1.0, right=2.0, top=1.0)

        layouter = dummy_layoutfab.new_circuitlayouter(circuit=ckt, boundary=None)
        layouter.add_wire(net=net, wire=wire, shape=shape)

        layout = dummy_layoutfab.new_layout()
        layout.add_shape(net=net, prim=wire, shape=shape)

        self.assertEqual(layouter.layout, layout)

        # Via
        wire = prims.contact
        bottom = prims.poly

        ckt = dummy_cktfab.new_circuit(name="test")
        net = ckt.new_net(name="net", external=False)

        p = _geo.Point(x=-2.0, y=3.0)

        layouter = dummy_layoutfab.new_circuitlayouter(circuit=ckt, boundary=None)
        layouter.add_wire(net=net, wire=wire, origin=p, bottom=bottom)

        layout = dummy_layoutfab.new_layout()
        layout.add_primitive(portnets={"conn": net}, prim=wire, x=p.x, y=p.y, bottom=bottom)

        self.assertEqual(layouter.layout, layout)

    def test_place_layout_1(self):
        # Place layout with two parts from a _MultiPartShape
        mask = prims.metal.mask

        ckt = dummy_cktfab.new_circuit(name="ckt")
        net = ckt.new_net(name="net", external=False)
        net2 = ckt.new_net(name="net2", external=False)
        layouter = dummy_layoutfab.new_circuitlayouter(circuit=ckt, boundary=None)

        r1 = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        r2 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))
        r12 = _geo.Rect.from_floats(values=(0.0, 0.0, 2.0, 1.0))

        mps = _geo.MultiPartShape(fullshape=r12, parts=(r1, r2))

        ms1 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[0]))
        ms2 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[1]))

        sl1 = _lay.MaskShapesSubLayout(net=net, shapes=ms1)
        sl2 = _lay.MaskShapesSubLayout(net=net2, shapes=ms2)

        lay = dummy_layoutfab.new_layout()
        lay += sl1
        lay += sl2
        layouter.place(lay, origin=_geo.origin)

        def get_parts(l: _lay._Layout):
            for sl in l.sublayouts.__iter_type__(_lay.MaskShapesSubLayout):
                for ms in sl.shapes:
                    s = ms.shape
                    if isinstance(s, _geo.MultiPartShape._Part):
                        yield s
                    elif isinstance(s, _geo.MultiShape):
                        yield from filter(
                            lambda s2: isinstance(s2, _geo.MultiPartShape._Part),
                            s.shapes,
                        )
        parts = tuple(get_parts(layouter.layout))

        self.assertEqual(len(parts), 2)
        self.assertIn(mps.parts[0], parts)
        self.assertIn(mps.parts[1], parts)

    def test_place_layout_2(self):
        # Place layout with two parts from a _MultiPartShape
        # Difference to test_place_layout_1 is that here the two parts
        # are put on the same net.
        mask = prims.metal.mask

        ckt = dummy_cktfab.new_circuit(name="ckt")
        net = ckt.new_net(name="net", external=False)
        layouter = dummy_layoutfab.new_circuitlayouter(circuit=ckt, boundary=None)

        r1 = _geo.Rect.from_floats(values=(0.0, 0.0, 1.0, 1.0))
        r2 = _geo.Rect.from_floats(values=(1.0, 0.0, 2.0, 1.0))
        r12 = _geo.Rect.from_floats(values=(0.0, 0.0, 2.0, 1.0))

        mps = _geo.MultiPartShape(fullshape=r12, parts=(r1, r2))

        ms1 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[0]))
        ms2 = _geo.MaskShapes(_geo.MaskShape(mask=mask, shape=mps.parts[1]))

        sl1 = _lay.MaskShapesSubLayout(net=net, shapes=ms1)
        sl2 = _lay.MaskShapesSubLayout(net=net, shapes=ms2)

        lay = dummy_layoutfab.new_layout()
        lay += sl1
        lay += sl2
        layouter.place(lay, origin=_geo.origin)

        def get_parts(l: _lay._Layout):
            for sl in l.sublayouts.__iter_type__(_lay.MaskShapesSubLayout):
                for ms in sl.shapes:
                    s = ms.shape
                    if isinstance(s, _geo.MultiPartShape._Part):
                        yield s
                    elif isinstance(s, _geo.MultiShape):
                        yield from filter(
                            lambda s2: isinstance(s2, _geo.MultiPartShape._Part),
                            s.shapes,
                        )
        parts = tuple(get_parts(layouter.layout))

        self.assertEqual(len(parts), 2)
        self.assertIn(mps.parts[0], parts)
        self.assertIn(mps.parts[1], parts)
