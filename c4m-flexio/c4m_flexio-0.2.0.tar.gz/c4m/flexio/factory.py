from math import floor, ceil
from collections import namedtuple
from typing import List, Dict, Generator, Iterable, Union, Optional, cast

from pdkmaster.typing import IntFloat
from pdkmaster import _util
from pdkmaster.technology import (
    property_ as _prp, mask as _msk, primitive as _prm, geometry as _geo,
)
from pdkmaster.design import circuit as _ckt, layout as _lay, library as _lbry

from . import _helpers as hlp


__all__ = ["IOSpecification", "IOFrameSpecification", "IOFactory"]


_MetalSpec = namedtuple(
    "_MetalSpec", (
        "prim",
        "minwidth_down", "minwidth4ext_down", "minwidth_up", "minwidth4ext_up",
        "minwidth_updown", "minwidth4ext_updown",
    ),
)


def _iterate_polygonbounds(*, polygon: _geo.MaskShape) -> Generator[
    _geo._Rectangular, None, None,
]:
    for shape in polygon.shape.pointsshapes:
        yield shape.bounds


class IOSpecification:
    def __init__(self, *,
        stdcelllib: _lbry.Library,
        nmos: _prm.MOSFET, pmos: _prm.MOSFET, ionmos: _prm.MOSFET, iopmos: _prm.MOSFET,
        cell_width: IntFloat, cell_height: IntFloat,
        ioring_maxwidth: IntFloat, ioring_space: IntFloat, ioring_spacetop: IntFloat,
        ioringvia_pitch: IntFloat, ioring_with_top: bool,
        pad_width: IntFloat, pad_height: IntFloat,
        padvia_pitch: Optional[IntFloat], padvia_corner_distance: IntFloat, padvia_metal_enclosure: IntFloat,
        metal_bigspace: IntFloat, topmetal_bigspace: IntFloat,
        clampnmos: Optional[_prm.MOSFET]=None,
        clampnmos_w: IntFloat, clampnmos_l: Optional[IntFloat]=None,
        clamppmos: Optional[_prm.MOSFET]=None,
        clamppmos_w: IntFloat, clamppmos_l: Optional[IntFloat]=None,
        clampfingers: int, clampfingers_analog: Optional[int], clampdrive: int,
        clampgate_gatecont_space: IntFloat, clampgate_sourcecont_space: IntFloat,
        clampgate_draincont_space: IntFloat,
        add_clampsourcetap: bool=False,
        clampsource_cont_tap_enclosure: Optional[Union[float, _prp.Enclosure]]=None,
        clampsource_cont_tap_space: Optional[IntFloat]=None,
        clampdrain_layer: Optional[_prm._DesignMaskPrimitive],
        clampgate_clampdrain_overlap: Optional[IntFloat], clampdrain_active_ext: Optional[IntFloat],
        clampdrain_gatecont_space: Optional[IntFloat],
        clampdrain_contcolumns: int, clampdrain_via1columns: int,
        nres: _prm.Resistor, pres: _prm.Resistor, ndiode: _prm.Diode, pdiode: _prm.Diode,
        secondres_width: IntFloat, secondres_length: IntFloat,
        secondres_active_space: IntFloat,
        corerow_height: IntFloat, corerow_nwell_height: IntFloat,
        iorow_height: IntFloat, iorow_nwell_height: IntFloat,
        nwell_minspace: Optional[IntFloat]=None, levelup_core_space: IntFloat,
        resvdd_prim: Optional[_prm.Resistor]=None, resvdd_w: Optional[IntFloat]=None,
        resvdd_lfinger: Optional[IntFloat]=None, resvdd_fingers: Optional[int]=None,
        resvdd_space: Optional[IntFloat]=None,
        capvdd_l: Optional[IntFloat]=None, capvdd_w: Optional[IntFloat]=None,
        capvdd_mosfet: Optional[_prm.MOSFET]=None, capvdd_fingers: Optional[int]=None,
        invvdd_n_l: Optional[IntFloat]=None, invvdd_n_w: Optional[IntFloat]=None,
        invvdd_n_mosfet: Optional[_prm.MOSFET]=None, invvdd_n_fingers: Optional[int]=None,
        invvdd_p_l: Optional[IntFloat]=None, invvdd_p_w: Optional[IntFloat]=None,
        invvdd_p_mosfet: Optional[_prm.MOSFET]=None, invvdd_p_fingers: Optional[int]=None,
    ):
        self.stdcelllib = stdcelllib

        self.iocell_width = _util.i2f(cell_width)
        self.iocell_height = _util.i2f(cell_height)

        self.ioring_maxwidth = _util.i2f(ioring_maxwidth)
        self.ioring_space = _util.i2f(ioring_space)
        self.ioring_spacetop = _util.i2f(ioring_spacetop)
        self.ioringvia_pitch = _util.i2f(ioringvia_pitch)
        self.ioring_with_top = ioring_with_top

        self.pad_width = _util.i2f(pad_width)
        self.pad_height = _util.i2f(pad_height)
        self.padvia_pitch = _util.i2f(padvia_pitch) if padvia_pitch is not None else None
        self.padvia_corner_distance = _util.i2f(padvia_corner_distance)
        self.padvia_metal_enclosure = _util.i2f(padvia_metal_enclosure)

        self.metal_bigspace = _util.i2f(metal_bigspace)
        self.topmetal_bigspace = _util.i2f(topmetal_bigspace)

        self.nmos = nmos
        self.pmos = pmos
        self.ionmos = ionmos
        self.iopmos = iopmos
        self.clampnmos = clampnmos if clampnmos is not None else ionmos
        self.clamppmos = clamppmos if clamppmos is not None else iopmos
        # TODO: Implement proper source implant for transistor
        self.clampnmos_w = _util.i2f(clampnmos_w)
        if clampnmos_l is not None:
            self.clampnmos_l = _util.i2f(clampnmos_l)
        else:
            self.clampnmos_l = self.clampnmos.computed.min_l
        self.clamppmos_w = _util.i2f(clamppmos_w)
        if clamppmos_l is not None:
            self.clamppmos_l = _util.i2f(clamppmos_l)
        else:
            self.clamppmos_l = self.clamppmos.computed.min_l
        self.clampcount = clampfingers
        self.clampdrive = clampdrive
        self.clampcount_analog = (
            clampfingers_analog if clampfingers_analog is not None
            else clampfingers
        )

        self.clampgate_gatecont_space = _util.i2f(clampgate_gatecont_space)
        self.clampgate_sourcecont_space = _util.i2f(clampgate_sourcecont_space)
        self.clampgate_draincont_space = _util.i2f(clampgate_draincont_space)

        if add_clampsourcetap:
            assert clampsource_cont_tap_enclosure is not None
            assert clampsource_cont_tap_space is not None
            if not isinstance(clampsource_cont_tap_enclosure, _prp.Enclosure):
                clampsource_cont_tap_enclosure = _prp.Enclosure(clampsource_cont_tap_enclosure)
            clampsource_cont_tap_space = _util.i2f(clampsource_cont_tap_space)
        self.add_clampsourcetap = add_clampsourcetap
        self.clampsource_cont_tap_enclosure = clampsource_cont_tap_enclosure
        self.clampsource_cont_tap_space = clampsource_cont_tap_space
        self.clamp_clampdrain = clampdrain_layer
        self.clampgate_clampdrain_overlap = _util.i2f(clampgate_clampdrain_overlap)
        self.clampdrain_active_ext = _util.i2f(clampdrain_active_ext)
        self.clampdrain_gatecont_space = _util.i2f(clampdrain_gatecont_space)
        self.clampdrain_contcolumns = clampdrain_contcolumns
        self.clampdrain_via1columns = clampdrain_via1columns

        self.nres = nres
        self.pres = pres
        self.ndiode = ndiode
        self.pdiode = pdiode
        self.secondres_width = _util.i2f(secondres_width)
        self.secondres_length = _util.i2f(secondres_length)
        self.secondres_active_space = _util.i2f(secondres_active_space)


        self.corerow_height = _util.i2f(corerow_height)
        self.corerow_nwell_height = _util.i2f(corerow_nwell_height)
        self.iorow_height = _util.i2f(iorow_height)
        self.iorow_nwell_height = _util.i2f(iorow_nwell_height)
        self.cells_height = self.corerow_height + self.iorow_height
        self.corerow_pwell_height = self.corerow_height - self.corerow_nwell_height
        self.iorow_pwell_height = self.iorow_height - self.iorow_nwell_height

        self.nwell_minspace = nwell_minspace

        self.levelup_core_space = _util.i2f(levelup_core_space)

        if resvdd_prim is None:
            assert (
                (resvdd_w is None) and (resvdd_lfinger is None)
                and (resvdd_fingers is None) and (resvdd_space is None)
                and (capvdd_l is None) and (capvdd_w is None)
                and (capvdd_mosfet is None) and (capvdd_fingers is None)
                and (invvdd_n_w is None) and (invvdd_n_l is None)
                and (invvdd_n_mosfet is None) and (invvdd_n_fingers is None)
                and (invvdd_p_w is None) and (invvdd_p_l is None)
                and (invvdd_p_mosfet is None) and (invvdd_p_fingers is None)
            )
        else:
            assert (
                (resvdd_w is not None) and (resvdd_lfinger is not None)
                and (resvdd_fingers is not None) and (resvdd_space is not None)
                and (capvdd_l is not None) and (capvdd_w is not None)
                and (capvdd_fingers is not None)
                and (invvdd_n_w is not None) and (invvdd_n_l is not None)
                and (invvdd_n_mosfet is not None) and (invvdd_n_fingers is not None)
                and (invvdd_p_w is not None) and (invvdd_p_l is not None)
                and (invvdd_p_mosfet is not None) and (invvdd_p_fingers is not None)
            )
            resvdd_w = _util.i2f(resvdd_w)
            resvdd_lfinger = _util.i2f(resvdd_lfinger)
            resvdd_space = _util.i2f(resvdd_space)
            capvdd_w = _util.i2f(capvdd_w)
            capvdd_l = _util.i2f(capvdd_l)
            if capvdd_mosfet is None:
                capvdd_mosfet = invvdd_n_mosfet
            invvdd_n_w = _util.i2f(invvdd_n_w)
            invvdd_n_l = _util.i2f(invvdd_n_l)
            invvdd_p_w = _util.i2f(invvdd_p_w)
            invvdd_p_l = _util.i2f(invvdd_p_l)
        self.resvdd_prim = resvdd_prim
        self.resvdd_w = resvdd_w
        self.resvdd_lfinger = resvdd_lfinger
        self.resvdd_fingers = resvdd_fingers
        self.resvdd_space = resvdd_space
        self.capvdd_l = capvdd_l
        self.capvdd_w = capvdd_w
        self.capvdd_mosfet = capvdd_mosfet
        self.capvdd_fingers = capvdd_fingers
        self.invvdd_n_l = invvdd_n_l
        self.invvdd_n_w = invvdd_n_w
        self.invvdd_n_mosfet = invvdd_n_mosfet
        self.invvdd_n_fingers = invvdd_n_fingers
        self.invvdd_p_l = invvdd_p_l
        self.invvdd_p_w = invvdd_p_w
        self.invvdd_p_mosfet = invvdd_p_mosfet
        self.invvdd_p_fingers = invvdd_p_fingers


class IOFrameSpecification:
    def __init__(self, *,
        pad_y: IntFloat,
        iovss_bottom: IntFloat, iovss_width: IntFloat,
        iovdd_bottom: IntFloat, iovdd_width: IntFloat,
        secondiovss_bottom: IntFloat, secondiovss_width: IntFloat,
        vddvss_bottom: IntFloat,
    ):
        self.pad_y = _util.i2f(pad_y)
        self.iovss_bottom = _util.i2f(iovss_bottom)
        self.iovss_width = _util.i2f(iovss_width)
        self.iovdd_bottom = _util.i2f(iovdd_bottom)
        self.iovdd_width = _util.i2f(iovdd_width)
        self.secondiovss_bottom = _util.i2f(secondiovss_bottom)
        self.secondiovss_width = _util.i2f(secondiovss_width)
        self.vddvss_bottom = _util.i2f(vddvss_bottom)


class _ComputedSpecs:
    def __init__(self, *,
        fab: "IOFactory",
        nmos: _prm.MOSFET, pmos: _prm.MOSFET, ionmos: _prm.MOSFET, iopmos: _prm.MOSFET,
    ):
        self.fab = fab
        spec = fab.spec
        tech = fab.tech

        # assert statements are used for unsupported technology configuration
        # TODO: Implement unsupported technology configurations

        assert nmos.well is None
        assert pmos.well is not None
        assert ionmos.well is None
        assert iopmos.well is not None
        assert pmos.well == iopmos.well

        prims = tech.primitives
        self.nmos = nmos
        self.pmos = pmos
        self.ionmos = ionmos
        self.iopmos = iopmos

        assert nmos.gate == pmos.gate
        assert ionmos.gate == iopmos.gate

        mosgate = nmos.gate
        iomosgate = ionmos.gate

        assert mosgate.oxide is None
        assert iomosgate.oxide is not None
        assert mosgate.active == iomosgate.active
        assert mosgate.poly == iomosgate.poly

        self.active = active = mosgate.active
        self.oxide = iomosgate.oxide
        self.poly = poly = mosgate.poly

        assert active.oxide is not None
        assert active.min_oxide_enclosure is not None
        assert active.min_substrate_enclosure is not None

        assert len(nmos.implant) == 1
        self.nimplant = nimplant = nmos.implant[0]
        nimplant_idx = active.implant.index(nimplant)
        nimplant_enc = active.min_implant_enclosure[nimplant_idx]
        assert len(pmos.implant) == 1
        self.pimplant = pimplant = pmos.implant[0]
        pimplant_idx = active.implant.index(pimplant)
        pimplant_enc = active.min_implant_enclosure[pimplant_idx]
        assert len(ionmos.implant) == 1
        self.ionimplant = ionimplant = ionmos.implant[0]
        ionimplant_idx = active.implant.index(ionimplant)
        ionimplant_enc = active.min_implant_enclosure[ionimplant_idx]
        assert len(iopmos.implant) == 1
        self.iopimplant = iopimplant = iopmos.implant[0]
        assert pimplant == iopimplant
        iopimplant_idx = active.implant.index(iopimplant)
        iopimplant_enc = active.min_implant_enclosure[iopimplant_idx]

        try:
            self.min_space_pimplant_active = tech.computed.min_space(pimplant, active)
        except AttributeError:
            self.min_space_pimplant_active = active.min_implant_enclosure[nimplant_idx].max()
        try:
            self.min_space_nimplant_active = tech.computed.min_space(nimplant, active)
        except AttributeError:
            self.min_space_nimplant_active = active.min_implant_enclosure[pimplant_idx].max()
        try:
            self.min_space_iopimplant_active = tech.computed.min_space(iopimplant, active)
        except AttributeError:
            self.min_space_iopimplant_active = active.min_implant_enclosure[ionimplant_idx].max()
        try:
            self.min_space_ionimplant_active = tech.computed.min_space(ionimplant, active)
        except AttributeError:
            self.min_space_ionimplant_active = active.min_implant_enclosure[iopimplant_idx].max()

        min_space_active_poly = tech.computed.min_space(poly, active)
        self.min_space_nmos_active = max((
            active.min_space,
            nmos.computed.min_polyactive_extension + min_space_active_poly,
            nmos.min_gateimplant_enclosure[0].max()
              + max(pimplant_enc.max(), self.min_space_pimplant_active),
        ))
        self.min_space_pmos_active = max((
            active.min_space,
            pmos.computed.min_polyactive_extension + min_space_active_poly,
            pmos.min_gateimplant_enclosure[0].max()
              + max(nimplant_enc.max(), self.min_space_nimplant_active),
        ))

        oxidx = active.oxide.index(iomosgate.oxide)
        try:
            self.min_oxactive_space = tech.computed.min_space(active.in_(iomosgate.oxide))
        except AttributeError:
            self.min_oxactive_space = active.min_space
        oxenc = iomosgate.min_gateoxide_enclosure
        if oxenc is None:
            oxenc = _prp.Enclosure(tech.grid)
        self.iogateoxide_enclosure = oxenc
        # TODO: add active oxide enclosure
        oxext = oxenc.second
        oxenc = active.min_oxide_enclosure[oxidx]
        if oxenc is None:
            oxenc = _prp.Enclosure(tech.grid)
        self.activeoxide_enclosure = oxenc
        oxext = max((oxext, oxenc.max()))
        min_space_iomosgate_active = (
            oxext + tech.computed.min_space(iomosgate.oxide, active)
        )
        self.min_space_ionmos_active = max((
            active.min_space,
            ionmos.computed.min_polyactive_extension + min_space_active_poly,
            ionmos.min_gateimplant_enclosure[0].max()
              + iopimplant_enc.max(),
            min_space_iomosgate_active,
        ))
        self.min_space_iopmos_active = max((
            active.min_space,
            iopmos.computed.min_polyactive_extension + min_space_active_poly,
            iopmos.min_gateimplant_enclosure[0].max()
              + ionimplant_enc.max(),
            min_space_iomosgate_active,
        ))

        self.vias = vias = tuple(prims.__iter_type__(_prm.Via))
        metals = tuple(filter(
            lambda m: not isinstance(m, _prm.MIMTop),
            prims.__iter_type__(_prm.MetalWire),
        ))
        assert all(metal.pin is not None for metal in metals), "Unsupported configuration"

        # Vias are sorted in the technology from bottom to top
        # so first via is the contact layer
        self.contact = contact = vias[0]
        assert (
            (active in contact.bottom) and (poly in contact.bottom)
            and (len(contact.top) == 1)
        ), "Unsupported configuration"

        actidx = contact.bottom.index(active)
        self.chact_enclosure = actenc = contact.min_bottom_enclosure[actidx]
        polyidx = contact.bottom.index(poly)
        self.chpoly_enclosure = polyenc = contact.min_bottom_enclosure[polyidx]
        self.chm1_enclosure = contact.min_top_enclosure[0]

        self.minwidth_activewithcontact = (
            contact.width + 2*actenc.min()
        )
        self.minwidth4ext_activewithcontact = (
            contact.width + 2*actenc.max()
        )

        self.minwidth_polywithcontact = (
            contact.width + 2*polyenc.min()
        )
        self.minwidth4ext_polywithcontact = (
            contact.width + 2*polyenc.max()
        )

        self.minnmos_contactgatepitch = (
            0.5*contact.width + nmos.computed.min_contactgate_space
            + 0.5*nmos.computed.min_l
        )
        self.minpmos_contactgatepitch = (
            0.5*contact.width + pmos.computed.min_contactgate_space
            + 0.5*pmos.computed.min_l
        )

        self.minionmos_contactgatepitch = (
            0.5*contact.width + ionmos.computed.min_contactgate_space
            + 0.5*ionmos.computed.min_l
        )
        self.miniopmos_contactgatepitch = (
            0.5*contact.width + iopmos.computed.min_contactgate_space
            + 0.5*iopmos.computed.min_l
        )

        self.nwell = nwell = pmos.well
        nwellidx = active.well.index(nwell)

        nactenc = active.min_substrate_enclosure.max()
        pactenc = active.min_well_enclosure[nwellidx].max()
        try:
            s = tech.computed.min_space(active, contact)
        except AttributeError:
            pass
        else:
            # Be sure that a poly contact can be put in between nmos and pmos
            if (nactenc + pactenc) < (contact.width + 2*s):
                # First make the two enclosures equal
                if pactenc < nactenc:
                    pactenc = nactenc
                else:
                    nactenc = pactenc
                # Then increase both if not enough yet
                if (nactenc + pactenc) < (contact.width + 2*s):
                    d = tech.on_grid(
                        0.5*((contact.width + 2*s) - (nactenc + pactenc)),
                        rounding="ceiling",
                    )
                    nactenc += d
                    pactenc += d
        self.activenwell_minspace = nactenc
        self.activenwell_minenclosure = pactenc

        nwellenc = active.min_well_enclosure[nwellidx].max()
        self.guardring_width = w = max(
            contact.width + contact.min_space,
            nwell.min_width - 2*nwellenc,
        )
        nwell_minspace = nwell.min_space
        if spec.nwell_minspace is not None:
            nwell_minspace = max(nwell_minspace, spec.nwell_minspace)
        s = max(
            pactenc + nactenc,
            0.5*(nwell_minspace + 2*pactenc - w), # Minimum NWELL spacing
        )
        self.guardring_space = 2*ceil(s/(2*tech.grid))*tech.grid
        self.guardring_pitch = self.guardring_width + self.guardring_space

        self.maxnmos_w = tech.on_grid(
            spec.corerow_pwell_height - (
                0.5*self.minwidth_activewithcontact
                + self.min_space_nmos_active + nactenc
            ),
            mult=2, rounding="floor",
        )
        self.maxnmos_y = tech.on_grid(
            spec.iorow_height + 0.5*self.minwidth_activewithcontact
            + self.min_space_nmos_active + 0.5*self.maxnmos_w,
        )
        self.maxnmos_activebottom = tech.on_grid(self.maxnmos_y - 0.5*self.maxnmos_w)
        self.maxnmos_activetop = tech.on_grid(self.maxnmos_y + 0.5*self.maxnmos_w)

        self.maxpmos_w = tech.on_grid(
            spec.corerow_nwell_height - (
                pactenc + self.min_space_pmos_active
                + 0.5*self.minwidth_activewithcontact
            ),
            mult=2, rounding="floor",
        )
        self.maxpmos_y = tech.on_grid(
            spec.iorow_height + spec.corerow_pwell_height
            + pactenc + 0.5*self.maxpmos_w,
        )
        self.maxpmos_activebottom = tech.on_grid(self.maxpmos_y - 0.5*self.maxpmos_w)
        self.maxpmos_activetop = tech.on_grid(self.maxpmos_y + 0.5*self.maxpmos_w)

        self.maxionmos_w = tech.on_grid(
            spec.iorow_pwell_height - (
                nactenc + self.min_space_ionmos_active
                + 0.5*self.minwidth_activewithcontact
            ),
            mult=2, rounding="floor",
        )
        self.maxionmos_y = tech.on_grid(
            spec.iorow_nwell_height + nactenc + 0.5*self.maxionmos_w,
        )
        self.maxionmos_activebottom = tech.on_grid(self.maxionmos_y - 0.5*self.maxionmos_w)
        self.maxionmos_activetop = tech.on_grid(self.maxionmos_y + 0.5*self.maxionmos_w)

        self.maxiopmos_w = tech.on_grid(
            spec.iorow_nwell_height - (
                0.5*self.minwidth_activewithcontact
                + self.min_space_iopmos_active + pactenc
            ),
            mult=2, rounding="floor",
        )
        self.maxiopmos_y = tech.on_grid(
            0.5*self.minwidth_activewithcontact + self.min_space_iopmos_active
            + 0.5*self.maxiopmos_w,
        )
        self.maxiopmos_activebottom = tech.on_grid(self.maxiopmos_y - 0.5*self.maxiopmos_w)
        self.maxiopmos_activetop = tech.on_grid(self.maxiopmos_y + 0.5*self.maxiopmos_w)

        self.io_oxidebottom = (
            0.5*self.minwidth_activewithcontact
            + tech.computed.min_space(iomosgate.oxide, active)
        )
        self.io_oxidetop = (
            spec.iorow_height
            - 0.5*self.minwidth_activewithcontact
            - tech.computed.min_space(iomosgate.oxide, active)
        )

        # Also get dimensions of io transistor in the core row
        self.maxionmoscore_w = tech.on_grid(
            spec.corerow_pwell_height - (
                nactenc + self.min_space_ionmos_active
                + 0.5*self.minwidth_activewithcontact
            ),
            mult=2, rounding="floor",
        )
        self.maxionmoscore_y = tech.on_grid(
            spec.iorow_height + 0.5*self.minwidth_activewithcontact
            + self.min_space_ionmos_active + 0.5*self.maxionmoscore_w,
        )
        self.maxionmoscore_activebottom = tech.on_grid(
            self.maxionmoscore_y - 0.5*self.maxionmoscore_w,
        )
        self.maxionmoscore_activetop = tech.on_grid(
            self.maxionmoscore_y + 0.5*self.maxionmoscore_w,
        )

        self.maxiopmoscore_w = tech.on_grid(
            spec.corerow_nwell_height - (
                0.5*self.minwidth_activewithcontact
                + self.min_space_iopmos_active + pactenc
            ),
            mult=2, rounding="floor",
        )
        self.maxiopmoscore_y = tech.on_grid(
            spec.iorow_height + spec.corerow_pwell_height
            + pactenc + 0.5*self.maxiopmoscore_w,
        )
        self.maxiopmoscore_activebottom = tech.on_grid(
            self.maxiopmoscore_y - 0.5*self.maxiopmoscore_w,
        )
        self.maxiopmoscore_activetop = tech.on_grid(
            self.maxiopmoscore_y + 0.5*self.maxiopmoscore_w,
        )

        for via in vias[1:]:
            assert all((
                (len(via.bottom) == 1) or isinstance(via.bottom[0], _prm.MetalWire),
                (len(via.top) == 1) or isinstance(via.top[0], _prm.MetalWire),
            )), "Unsupported configuration"

        def _metalspec(i):
            downvia = vias[i-1]
            downw = downvia.width
            downenc = downvia.min_top_enclosure[0]
            minwdown = downw + 2*downenc.min()
            minwextdown = downw + 2*downenc.max()
            try:
                upvia = vias[i+1]
            except:
                minwup = None
                minwextup = None
                minwupdown = minwdown
                minwextupdown = minwextdown
            else:
                upw = upvia.width
                upenc = upvia.min_bottom_enclosure[0]
                minwup = upw + 2*upenc.min()
                minwextup = upw + 2*upenc.max()
                minwupdown = max(minwdown, minwup)
                minwextupdown = max(minwextdown, minwextup)

            return _MetalSpec(
                metals[i-1],
                minwdown, minwextdown, minwup, minwextup, minwupdown, minwextupdown,
            )

        def _topmetalspec():
            via = vias[-1]
            w = via.width
            enc = via.min_bottom_enclosure[0]
            minwupdown = minwdown = w + 2*enc.min()
            minwextupdown = minwextdown = w + 2*enc.max()
            minwup = None
            minwextup = None
            return _MetalSpec(
                metals[len(vias) - 1],
                minwdown, minwextdown, minwup, minwextup, minwupdown, minwextupdown,
            )

        self.metal = {i: _metalspec(i) for i in range(1, len(vias))}
        self.metal[len(vias)] = _topmetalspec()

        pads = tuple(tech.primitives.__iter_type__(_prm.PadOpening))
        assert len(pads) == 1
        self.pad = pads[0]


class _IOCellFrame:
    """Default cells for in IO cell framework"""
    def __init__(self, *,
        fab: "IOFactory", framespec: IOFrameSpecification,
    ):
        self.fab = fab
        spec = fab.spec
        self._pad = None # Only create pad first time it is accessed
        self.framespec = framespec

        l_gd = fab.get_cell("GateDecode").layout
        assert l_gd.boundary is not None
        gd_height = l_gd.boundary.top - l_gd.boundary.bottom
        self.cells_y = spec.iocell_height - gd_height

    @property
    def pad_y(self) -> float:
        return self.framespec.pad_y
    @property
    def iovss_bottom(self) -> float:
        return self.framespec.iovss_bottom
    @property
    def iovss_width(self) -> float:
        return self.framespec.iovss_width
    @property
    def iovdd_bottom(self) -> float:
        return self.framespec.iovdd_bottom
    @property
    def iovdd_width(self) -> float:
        return self.framespec.iovdd_width
    @property
    def secondiovss_bottom(self) -> float:
        return self.framespec.secondiovss_bottom
    @property
    def secondiovss_width(self) -> float:
        return self.framespec.secondiovss_width
    @property
    def vddvss_bottom(self) -> float:
        return self.framespec.vddvss_bottom

    @property
    def pad(self):
        if self._pad is None:
            fab = self.fab
            spec = fab.spec
            self._pad = fab.pad(width=spec.pad_width, height=spec.pad_height)
        return self._pad

    def add_track_nets(self, *, ckt: _ckt._Circuit) -> Dict[
        str, _ckt._CircuitNet,
    ]:
        nets = {
            net_name: ckt.new_net(name=net_name, external=True)
            for net_name in ("vss", "vdd", "iovss", "iovdd")
        }
        return nets

    def add_pad_inst(self, *, ckt: _ckt._Circuit, net: _ckt._CircuitNet):
        fab = self.fab
        spec = fab.spec

        c_pad = fab.pad(width=spec.pad_width, height=spec.pad_height)
        i_pad = ckt.instantiate(c_pad, name="pad")
        net.childports += i_pad.ports.pad

    def add_bulkconn_inst(self, *,
        ckt: _ckt._Circuit, width: float, connect_up: bool,
    ):
        fab = self.fab

        nets = ckt.nets

        bulkconn_cell = fab.bulkconn(width=width, connect_up=connect_up)
        inst = ckt.instantiate(bulkconn_cell, name="bulkconn")

        for net_name in ("vss", "vdd", "iovss", "iovdd"):
            nets[net_name].childports += inst.ports[net_name]

    def draw_tracks(self, *,
        ckt: _ckt._Circuit, layouter: _lay._CircuitLayouter,
        cell_width: Optional[float]=None,
    ):
        spec = self.fab.spec
        nets = ckt.nets

        if cell_width is None:
            cell_width = spec.iocell_width

        self.draw_track(
            layouter=layouter, net=nets.iovss, cell_width=cell_width,
            bottom=self.iovss_bottom, width=self.iovss_width,
        )
        self.draw_track(
            layouter=layouter, net=nets.iovdd, cell_width=cell_width,
            bottom=self.iovdd_bottom, width=self.iovdd_width,
        )
        self.draw_track(
            layouter=layouter, net=nets.iovss, cell_width=cell_width,
            bottom=self.secondiovss_bottom, width=self.secondiovss_width,
        )
        self.draw_duotrack(
            layouter=layouter, net1=nets.vss, net2=nets.vdd, cell_width=cell_width,
            track_bottom=self.vddvss_bottom, track_top=spec.iocell_height,
            space=spec.ioring_space,
        )

    def draw_corner_tracks(self, *,
        ckt: _ckt._Circuit, layouter: _lay._CircuitLayouter,
    ):
        spec = self.fab.spec
        nets = ckt.nets

        self.draw_corner_track(
            layouter=layouter, net=nets.iovss,
            bottom=self.iovss_bottom, width=self.iovss_width,
        )
        self.draw_corner_track(
            layouter=layouter, net=nets.iovdd,
            bottom=self.iovdd_bottom, width=self.iovdd_width,
        )
        self.draw_corner_track(
            layouter=layouter, net=nets.iovss,
            bottom=self.secondiovss_bottom, width=self.secondiovss_width,
        )
        self.draw_corner_duotrack(
            layouter=layouter, net1=nets.vss, net2=nets.vdd,
            track_bottom=self.vddvss_bottom, track_top=spec.iocell_height,
            space=spec.ioring_space,
        )

    def draw_track(self, *,
        layouter: _lay._CircuitLayouter, net: _ckt._CircuitNet, cell_width: float,
        bottom: float, width: float,
    ):
        fab = self.fab
        spec = fab.spec
        tech = fab.tech
        comp = fab.computed
        if spec.ioring_with_top:
            track_vias = comp.vias[3:]
        else:
            track_vias = comp.vias[3:-1]
        n_vias = len(track_vias)

        # Compute the subtracks dimensions
        maxw = spec.ioring_maxwidth
        space = spec.ioring_space
        if width <= maxw:
            n_tracks = 1
            segwidth = width
        else:
            maxp = maxw + space
            n_tracks = int((width - tech.grid - maxw)/(maxp)) + 2
            segwidth = tech.on_grid(
                (width - (n_tracks - 1)*space)/n_tracks,
                mult=2, rounding="floor",
            )
        pitch = segwidth + space
        subtracks_rects = tuple((
            *(
                _geo.Rect(
                    left=0.0, bottom=(bottom + i*pitch),
                    right=cell_width, top=(bottom + i*pitch + segwidth),
                ) for i in range(n_tracks - 1)
            ),
            _geo.Rect(
                left=0.0, bottom=(bottom + width - segwidth),
                right=cell_width, top=(bottom + width),
            ),
        ))
        topspace = spec.ioring_spacetop
        spacediff = (topspace - space)
        topsubtracks_rects = tuple(
            _geo.Rect.from_rect(
                rect=rect, bottom=(rect.bottom + 0.5*spacediff),
                top=(rect.top - 0.5*spacediff),
            ) for rect in subtracks_rects
        )

        for i, track_via in enumerate(track_vias):
            is_top = spec.ioring_with_top and (i == (len(track_vias) - 1))
            space = spec.ioringvia_pitch - track_via.width
            # Leave space at the border between vias
            segwidth = cell_width - 2*space
            for j, bot_rect in enumerate(subtracks_rects):
                if is_top:
                    top_rect = topsubtracks_rects[j]
                else:
                    top_rect = bot_rect
                if cell_width > 10*space: # Don't draw vias for small width
                    layouter.add_wire(
                        wire=track_via, net=net, space=space, origin=top_rect.center,
                        bottom_width=top_rect.width, bottom_height=top_rect.height,
                        bottom_enclosure=space,
                        top_width=top_rect.width, top_height=top_rect.height,
                        top_enclosure=space,
                    )
                metal = track_via.bottom[0]
                assert isinstance(metal, _prm.MetalWire) and (metal.pin is not None)
                pin = metal.pin[0]
                layouter.add_wire(net=net, wire=metal, pin=pin, shape=bot_rect)
                if i == (n_vias - 1):
                    metal = track_via.top[0]
                    assert isinstance(metal, _prm.MetalWire) and (metal.pin is not None)
                    pin = metal.pin[0]
                    layouter.add_wire(net=net, wire=metal, pin=pin, shape=top_rect)

    def draw_duotrack(self, *,
        layouter: _lay._CircuitLayouter, net1: _ckt._CircuitNet, net2: _ckt._CircuitNet,
        cell_width: float, track_bottom: float, track_top: float, space: float,
    ):
        fab = self.fab
        spec = fab.spec
        tech = fab.tech
        comp = fab.computed

        metal3 = comp.metal[3].prim
        via3 = comp.vias[3]
        metal4 = comp.metal[4].prim
        via4 = comp.vias[4]
        metal5 = comp.metal[5].prim

        height = track_top - track_bottom

        segheight = 0.5*(height - space)
        segheight = floor(segheight/tech.grid)*tech.grid

        bottom1 = track_bottom
        top1 = bottom1 + segheight
        top2 = track_top
        bottom2 = top2 - segheight

        rect1 = _geo.Rect(
            left=0.0, bottom=bottom1,
            right=cell_width, top=top1,
        )
        rect2 = _geo.Rect(
            left=-0.0, bottom=bottom2,
            right=cell_width, top=top2,
        )

        # metal3
        metal = metal3
        layouter.add_wire(net=net1, wire=metal, pin=metal.pin[0], shape=rect1)
        layouter.add_wire(net=net2, wire=metal, pin=metal.pin[0], shape=rect2)

        # metal5, rects are swapped !
        metal = metal5
        layouter.add_wire(net=net1, wire=metal, pin=metal.pin[0], shape=rect2)
        layouter.add_wire(net=net2, wire=metal, pin=metal.pin[0], shape=rect1)

        # metal4, reduced height
        viawidth = 0.5*(cell_width - 3*space)
        viawidth = floor(viawidth/tech.grid)*tech.grid
        viaheight = max(
            comp.metal[3].minwidth4ext_updown, comp.metal[4].minwidth4ext_updown,
        )

        top1b = top1 - 2*space
        bottom2b = bottom2 + 2*space

        metal = metal4
        rect1 = _geo.Rect(
            left=0.0, bottom=bottom1, right=cell_width, top=top1b,
        )
        rect2 = _geo.Rect(
            left=0.0, bottom=(bottom2 + 2*space), right=cell_width, top=top2,
        )

        layouter.add_wire(net=net1, wire=metal, pin=metal.pin[0], shape=rect2)
        layouter.add_wire(net=net2, wire=metal, pin=metal.pin[0], shape=rect1)

        if cell_width > 10*space: # Don't draw vias for small width
            l_via = layouter.add_wire(
                wire=via3, net=net1,
                x=tech.on_grid(.25*cell_width + 0.25*space),
                bottom_width=viawidth, top_width=viawidth,
                y=(top1 - 0.5*viaheight), bottom_height=viaheight, top_height=viaheight,
            )
            viam4_bounds = l_via.bounds(mask=metal4.mask)
            l_via = layouter.add_wire(
                wire=via3, net=net2,
                x=tech.on_grid(0.75*cell_width - 0.25*space),
                bottom_width=viawidth, top_width=viawidth,
                y=(bottom2 + 0.5*viaheight), bottom_height=viaheight, top_height=viaheight,
            )
            viam4_bounds2 = l_via.bounds(mask=metal4.mask)

            shape = _geo.Rect.from_rect(rect=viam4_bounds, top=(bottom2b + tech.grid))
            layouter.add_wire(net=net1, wire=metal, shape=shape)
            shape = _geo.Rect.from_rect(rect=viam4_bounds2, bottom=(top1b - tech.grid))
            layouter.add_wire(net=net2, wire=metal, shape=shape)

        # via4
        space = spec.ioringvia_pitch - via4.width
        if cell_width > 10*space: # Don't draw via for small width
            bottom_shape = _geo.Rect.from_rect(rect=rect2, bias=-space)
            layouter.add_wire(
                net=net1, wire=via4, space=space, bottom_shape=bottom_shape,
            )
            bottom_shape = _geo.Rect.from_rect(rect=rect1, bias=-space)
            layouter.add_wire(
                net=net2, wire=via4, space=space, bottom_shape=bottom_shape,
            )

    def _corner_segment(self, *, bottom: float, top: float) -> _geo.Polygon:
        fab = self.fab
        spec = fab.spec
        tech = fab.tech

        cell_height = spec.iocell_height
        sqrt2 = 2**0.5
        d_top = tech.on_grid((cell_height - top)/sqrt2)
        d_bottom = tech.on_grid(d_top + (top - bottom)/sqrt2)

        if d_top < _geo.epsilon:
            return _geo.Polygon.from_floats(points=(
                (0.0, bottom),
                (-d_bottom, bottom),
                (-(cell_height - bottom), cell_height - d_bottom),
                (-(cell_height - bottom), cell_height),
                (0.0, cell_height),
                (0.0, bottom),
            ))
        else:
            return _geo.Polygon.from_floats(points=(
                (0.0, bottom),
                (-d_bottom, bottom),
                (-(cell_height - bottom), cell_height - d_bottom),
                (-(cell_height - bottom), cell_height),
                (-(cell_height - top), cell_height),
                (-(cell_height - top), cell_height - d_top),
                (-d_top, top),
                (0.0, top),
                (0.0, bottom),
            ))

    def draw_corner_track(self, *,
        layouter: _lay._CircuitLayouter, net: _ckt._CircuitNet,
        bottom: float, width: float,
    ):
        fab = self.fab
        spec = fab.spec
        tech = fab.tech
        comp = fab.computed
        if spec.ioring_with_top:
            track_vias = comp.vias[3:]
        else:
            track_vias = comp.vias[3:-1]
        n_vias = len(track_vias)

        # Compute the subtracks dimensions
        maxw = spec.ioring_maxwidth
        space = spec.ioring_space
        if width <= maxw:
            n_tracks = 1
            segwidth = width
        else:
            maxp = maxw + space
            n_tracks = int((width - tech.grid - maxw)/(maxp)) + 2
            segwidth = tech.on_grid(
                (width - (n_tracks - 1)*space)/n_tracks,
                mult=2, rounding="floor",
            )
        pitch = segwidth + space
        subtracks_polys = tuple((
            *(
                self._corner_segment(
                    bottom=(bottom + i*pitch), top=(bottom + i*pitch + segwidth),
                ) for i in range(n_tracks - 1)
            ),
            self._corner_segment(
                bottom=(bottom + width - segwidth), top=(bottom + width),
            ),
        ))
        topspace = spec.ioring_spacetop
        spacediff = (topspace - space)
        topsubtracks_polys = tuple((
            *(
                self._corner_segment(
                    bottom=(bottom + i*pitch + 0.5*spacediff),
                    top=(bottom + i*pitch + segwidth - 0.5*spacediff),
                ) for i in range(n_tracks - 1)
            ),
            self._corner_segment(
                bottom=(bottom + width - segwidth + 0.5*spacediff),
                top=(bottom + width - 0.5*spacediff),
            ),
        ))

        for i, track_via in enumerate(track_vias):
            is_top = spec.ioring_with_top and (i == (len(track_vias) - 1))
            for j, bot_poly in enumerate(subtracks_polys):
                if is_top:
                    top_poly = topsubtracks_polys[j]
                else:
                    top_poly = bot_poly
                metal = track_via.bottom[0]
                assert isinstance(metal, _prm.MetalWire) and (metal.pin is not None)
                pin = metal.pin[0]
                layouter.add_wire(net=net, wire=metal, pin=pin, shape=bot_poly)
                if i == (n_vias - 1):
                    metal = track_via.top[0]
                    assert isinstance(metal, _prm.MetalWire) and (metal.pin is not None)
                    pin = metal.pin[0]
                    layouter.add_wire(net=net, wire=metal, pin=pin, shape=top_poly)

    def draw_corner_duotrack(self, *,
        layouter: _lay._CircuitLayouter, net1: _ckt._CircuitNet, net2: _ckt._CircuitNet,
        track_bottom: float, track_top: float, space: float,
    ):
        fab = self.fab
        spec = fab.spec
        tech = fab.tech
        comp = fab.computed

        metal3 = comp.metal[3].prim
        via3 = comp.vias[3]
        metal4 = comp.metal[4].prim
        via4 = comp.vias[4]
        metal5 = comp.metal[5].prim

        height = track_top - track_bottom

        segheight = 0.5*(height - space)
        segheight = floor(segheight/tech.grid)*tech.grid

        bottom1 = track_bottom
        top1 = bottom1 + segheight
        top2 = track_top
        bottom2 = top2 - segheight

        poly1 = self._corner_segment(bottom=bottom1, top=top1)
        poly2 = self._corner_segment(bottom=bottom2, top=top2)

        # metal3
        metal = metal3
        layouter.add_wire(net=net1, wire=metal, pin=metal.pin[0], shape=poly1)
        layouter.add_wire(net=net2, wire=metal, pin=metal.pin[0], shape=poly2)

        # metal5, rects are swapped !
        metal = metal5
        layouter.add_wire(net=net1, wire=metal, pin=metal.pin[0], shape=poly2)
        layouter.add_wire(net=net2, wire=metal, pin=metal.pin[0], shape=poly1)

        # metal4, reduced height
        top1b = top1 - 2*space
        bottom2b = bottom2 + 2*space

        metal = metal4
        poly1 = self._corner_segment(bottom=bottom1, top=top1b)
        poly2 = self._corner_segment(bottom=bottom2b, top=top2)

        layouter.add_wire(net=net1, wire=metal, pin=metal.pin[0], shape=poly2)
        layouter.add_wire(net=net2, wire=metal, pin=metal.pin[0], shape=poly1)

    def place_pad(self, *,
        layouter: _lay._CircuitLayouter, net: _ckt._CircuitNet,
    ) -> _lay._Layout:
        fab = self.fab
        spec = fab.spec
        comp = fab.computed
        frame = fab.frame

        ckt = layouter.circuit
        insts = ckt.instances

        topmetal = comp.metal[len(comp.vias)].prim
        pad = comp.pad

        x = 0.5*spec.iocell_width
        l_pad = layouter.place(insts.pad, x=x, y=frame.pad_y)
        pad_bounds = l_pad.bounds(mask=pad.mask)
        layouter.add_wire(net=net, wire=topmetal, pin=topmetal.pin[0], shape=pad_bounds)

        return l_pad

    def place_bulkconn(self, *, layouter: _lay._CircuitLayouter) -> _lay._Layout:
        ckt = layouter.circuit
        inst = ckt.instances.bulkconn

        return layouter.place(inst, x=0.0, y=self.cells_y)


class _FactoryCell(_lbry._Cell[_lbry.Library]):
    def __init__(self, *, fab: "IOFactory", name: str):
        self.fab = fab
        super().__init__(lib=fab.lib, name=name)


class _FactoryOnDemandCell(_lbry._OnDemandCell[_lbry.Library]):
    def __init__(self, *, fab: "IOFactory", name: str):
        self.fab = fab
        super().__init__(lib=fab.lib, name=name)


class _GuardRing(_FactoryCell):
    def __init__(self, *, name, fab, type_, width, height, fill_well, fill_implant):
        super().__init__(fab=fab, name=name)
        ckt = self.new_circuit()
        conn = ckt.new_net(name="conn", external=True)
        layouter = self.new_circuitlayouter()

        l = hlp.guardring(
            fab=fab, net=conn, type_=type_, width=width, height=height,
            fill_well=fill_well, fill_implant=fill_implant,
        )
        layouter.place(l, x=0.0, y=0.0)
        self.layout.boundary = l.boundary


class _Clamp(_FactoryCell):
    def __init__(self, *,
        name: str, fab: "IOFactory", type_: str, n_trans: int, n_drive: int,
    ):
        assert (
            (type_ in ("n", "p")) and (n_trans > 0) and (0 <= n_drive <= n_trans)
        ), "Internal error"
        spec = fab.spec
        tech = fab.tech
        comp = fab.computed

        nwell = comp.nwell
        cont = comp.contact
        metal1 = comp.metal[1].prim
        via1 = comp.vias[1]
        metal2 = comp.metal[2].prim
        via2 = comp.vias[2]

        super().__init__(fab=fab, name=name)

        ckt = self.new_circuit()
        layouter = self.new_circuitlayouter()
        layoutfab = layouter.fab

        iovss = ckt.new_net(name="iovss", external=True)
        iovdd = ckt.new_net(name="iovdd", external=True)
        source = iovss if type_ == "n" else iovdd
        notsource = iovdd if type_ == "n" else iovss
        pad = ckt.new_net(name="pad", external=True)

        gate_nets = tuple()
        gate: Optional[_ckt._CircuitNet] = None
        off: Optional[_ckt._CircuitNet] = None
        if n_drive > 0:
            gate = ckt.new_net(name="gate", external=True)
            gate_nets += n_drive*(gate,)
        if n_drive < n_trans:
            off = ckt.new_net(name="off", external=False)
            gate_nets += (n_trans - n_drive)*(off,)

        _l_clamp = hlp.clamp(
            fab=fab, ckt=ckt, type_=type_,
            source_net=source, drain_net=pad, gate_nets=gate_nets,
        )
        clampact_bounds = _l_clamp.bounds(mask=comp.active.mask)

        min_space_active_poly = tech.computed.min_space(comp.poly, comp.active)

        vspace = (
            spec.clampgate_gatecont_space + 0.5*cont.width + max(
                0.5*comp.minwidth_polywithcontact + min_space_active_poly,
                0.5*comp.metal[1].minwidth4ext_down + metal1.min_space,
            )
        )
        innerguardring_height = (
            (clampact_bounds.top - clampact_bounds.bottom) + 2*vspace
            + 2*comp.guardring_width
        )
        innerguardring_width = (spec.iocell_width - 2*comp.guardring_pitch)
        outerguardring_height = innerguardring_height + 2*comp.guardring_pitch

        c_outerring = fab.guardring(
            type_=type_, width=spec.iocell_width, height=outerguardring_height,
        )
        i_outerring = ckt.instantiate(c_outerring, name="OuterRing")
        notsource.childports += i_outerring.ports.conn
        c_innerring = fab.guardring(
            type_="p" if (type_ == "n") else "n",
            width=innerguardring_width, height=innerguardring_height,
            fill_well=(type_ == "p"), fill_implant=(not spec.add_clampsourcetap),
        )
        i_innerring = ckt.instantiate(c_innerring, name="InnerRing")
        source.childports += i_innerring.ports.conn

        # Place clamp, guard rings
        x = 0.5*spec.iocell_width
        y = 0.5*outerguardring_height
        layouter.place(i_outerring, x=x, y=y)
        layouter.place(i_innerring, x=x, y=y)
        l_clamp = layouter.place(_l_clamp, x=x, y=y)

        # Draw drain metal2 connections
        for ms in l_clamp.filter_polygons(net=pad, mask=metal1.mask, split=True):
            bounds = ms.shape.bounds
            l_via = layouter.add_wire(
                net=pad, wire=via1, x=bounds.center.x, columns=spec.clampdrain_via1columns,
                bottom_bottom=bounds.bottom, bottom_top=bounds.top,
            )
            viam2_bounds = l_via.bounds(mask=metal2.mask)

            shape = _geo.Rect.from_rect(
                rect=viam2_bounds, top=outerguardring_height,
            )
            layouter.add_wire(net=pad, wire=metal2, pin=metal2.pin[0], shape=shape)

        # Connect source to ring
        # Cache as polygons will be added during parsing
        for ms in l_clamp.filter_polygons(net=source, mask=metal1.mask, split=True):
            bounds = ms.shape.bounds
            x = bounds.center.x

            l_via = layouter.add_wire(
                net=source, wire=via1, x=x,
                bottom_bottom=bounds.bottom, bottom_top=bounds.top,
            )
            viam2_bounds = l_via.bounds(mask=metal2.mask)

            bottom = 0.5*outerguardring_height - 0.5*innerguardring_height
            top = bottom + comp.guardring_width
            layouter.add_wire(
                net=source, wire=via1, x=x,
                bottom_bottom=bottom, bottom_top=top,
            )
            top = 0.5*outerguardring_height + 0.5*innerguardring_height
            bottom = top - comp.guardring_width
            layouter.add_wire(
                net=source, wire=via1, x=x,
                bottom_bottom=bottom, bottom_top=top,
            )
            shape = _geo.Rect.from_rect(
                rect=viam2_bounds,
                bottom=0.0, top=outerguardring_height,
            )
            layouter.add_wire(net=source, wire=metal2, shape=shape)
            layouter.add_wire(
                net=source, wire=via2, x=x,
                bottom_bottom=0.0, bottom_top=outerguardring_height,
            )

        # Draw gate diode and connect the gates
        if n_drive > 0:
            assert gate is not None
            diode = spec.ndiode if type_ == "n" else spec.pdiode
            well_args = {} if type_ == "n" else {"well_net": iovdd, "bottom_well": nwell}
            l_ch = layoutfab.layout_primitive(
                prim=cont, portnets={"conn": gate}, **well_args, rows=2,
                bottom=diode.wire, bottom_implant=diode.implant,
            )
            chact_bounds = l_ch.bounds(mask=diode.wire.mask)
            dgate = ckt.instantiate(diode, name="DGATE",
                width=(chact_bounds.right - chact_bounds.left),
                height=(chact_bounds.top - chact_bounds.bottom),
            )
            an = dgate.ports.anode
            cath = dgate.ports.cathode
            gate.childports += an if type_ == "p" else cath
            source.childports += an if type_ == "n" else cath

            x = tech.on_grid(0.5*spec.iocell_width + 0.5*(
                clampact_bounds.left - 0.5*innerguardring_width + comp.guardring_width
            ))
            y = 0.5*outerguardring_height + clampact_bounds.top - chact_bounds.top
            l_ch = layouter.place(l_ch, x=x, y=y)
            layouter.place(dgate, x=x, y=y)

            chm1_bounds = l_ch.bounds(mask=metal1.mask)
            clampm1gate_bounds = l_clamp.bounds(mask=metal1.mask, net=gate)

            rect = _geo.Rect.from_rect(
                rect=chm1_bounds, top=clampm1gate_bounds.top,
            )
            layouter.add_wire(wire=metal1, net=gate, shape=rect)
            rect = _geo.Rect.from_rect(
                rect=clampm1gate_bounds, left=chm1_bounds.left,
                bottom=(clampm1gate_bounds.top - metal1.min_width),
            )
            layouter.add_wire(wire=metal1, net=gate, shape=rect)

            bottom = chm1_bounds.bottom
            top = clampm1gate_bounds.top
            l_via = layouter.add_wire(
                wire=via1, net=gate, x=x,
                bottom_bottom=bottom, bottom_top=top,
            )
            viam2_bounds = l_via.bounds(mask=metal2.mask)
            shape = _geo.Rect.from_rect(rect=viam2_bounds, top=outerguardring_height)
            layouter.add_wire(wire=metal2, net=gate, pin=metal2.pin[0], shape=shape)

        # Draw power off resistor and connect the gates
        if n_drive < n_trans:
            assert off is not None
            roff = ckt.instantiate(
                spec.nres if type_ == "n" else spec.pres, name="Roff",
                width=comp.minwidth4ext_polywithcontact,
                height=(clampact_bounds.top - clampact_bounds.bottom),
            )
            source.childports += roff.ports.port1
            off.childports += roff.ports.port2

            x = tech.on_grid(0.5*spec.iocell_width + 0.5*(
                clampact_bounds.right + 0.5*innerguardring_width - comp.guardring_width
            ))
            y = 0.5*outerguardring_height
            l_roff = layouter.place(roff, x=x, y=y)
            roffm1source_bounds = l_roff.bounds(mask=metal1.mask, net=source)
            roffm1off_bounds = l_roff.bounds(mask=metal1.mask, net=off)

            x = roffm1source_bounds.center.x
            y = roffm1source_bounds.center.y
            l_via = layouter.add_wire(
                wire=via1, net=source, x=x, y=y, columns=2,
            )
            viam2_bounds = l_via.bounds(mask=metal2.mask)
            y = comp.guardring_pitch + 0.5*comp.guardring_width
            l_via = layouter.add_wire(
                wire=via1, net=source, x=x, y=y, columns=2,
            )
            viam2_bounds2 = l_via.bounds(mask=metal2.mask)
            shape = _geo.Rect.from_rect(rect=viam2_bounds, bottom=viam2_bounds2.bottom)
            layouter.add_wire(wire=metal2, net=source, shape=shape)

            clampm1off_bounds = l_clamp.bounds(mask=metal1.mask, net=off)
            roffm1off_bounds = l_roff.bounds(mask=metal1.mask, net=off)

            rect = _geo.Rect.from_rect(
                rect=roffm1off_bounds, top=clampm1off_bounds.top,
            )
            layouter.add_wire(wire=metal1, net=off, shape=rect)
            shape = _geo.Rect.from_rect(
                rect=clampm1off_bounds, bottom=(clampm1off_bounds.top - metal1.min_width),
            )
            layouter.add_wire(wire=metal1, net=off, shape=shape)

        self.layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0,
            right=spec.iocell_width, top=outerguardring_height,
        )


class _Secondary(_FactoryCell):
    def __init__(self, *, fab: "IOFactory"):
        spec = fab.spec
        comp = fab.computed

        cont = comp.contact
        metal1 = comp.metal[1].prim
        via1 = comp.vias[1]
        metal2 = comp.metal[2].prim
        metal2pin = metal2.pin[0]

        super().__init__(fab=fab, name="SecondaryProtection")

        ckt = self.new_circuit()
        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        iovdd = ckt.new_net(name="iovdd", external=True)
        iovss = ckt.new_net(name="iovss", external=True)
        pad = ckt.new_net(name="pad", external=True)
        core = ckt.new_net(name="core", external=True)

        # Resistance
        r = ckt.instantiate(
            spec.nres, name="R",
            width=spec.secondres_width, height=spec.secondres_length,
        )
        pad.childports += r.ports.port1
        core.childports += r.ports.port2

        l_res = layouter.inst_layout(inst=r)
        respoly_bounds = l_res.bounds(mask=comp.poly.mask)
        res_width = respoly_bounds.right - respoly_bounds.left
        res_height = respoly_bounds.top - respoly_bounds.bottom

        guard_width = (
            res_width + 2*spec.secondres_active_space + 2*comp.guardring_width
        )
        guard_height = (
            res_height + 2*spec.secondres_active_space + 2*comp.guardring_width
        )
        l_guard = hlp.guardring(
            fab=fab, net=iovss, type_="p", width=guard_width, height=guard_height,
        )

        l_res = layouter.place(l_res, x=0.5*guard_width, y=0.5*guard_height)
        resm1pad_bounds = l_res.bounds(mask=metal1.mask, net=pad)
        resm1core_bounds = l_res.bounds(mask=metal1.mask, net=core)
        l_guard = layouter.place(l_guard, x=0.5*guard_width, y=0.5*guard_height)
        resm1guard_bounds = l_guard.bounds(mask=metal1.mask)

        # N diode
        dn_prim = spec.ndiode
        diode_height = (
            guard_height - 2*comp.guardring_width - 2*comp.min_space_nmos_active
        )
        l_ch = layouter.fab.layout_primitive(
            cont, portnets={"conn": core}, columns=2,
            bottom=dn_prim.wire, bottom_implant=dn_prim.implant,
            bottom_height=diode_height,
        )
        dnchact_bounds = l_ch.bounds(mask=comp.active.mask)
        diode_width = dnchact_bounds.right - dnchact_bounds.left
        dn = ckt.instantiate(
            dn_prim, name="DN", width=diode_width, height=diode_height,
        )
        core.childports += dn.ports.cathode
        iovss.childports += dn.ports.anode

        guard2_width = (
            diode_width + 2*comp.min_space_nmos_active + 2*comp.guardring_width
        )
        l_guard2 = hlp.guardring(
            fab=fab, net=iovss, type_="p", width=guard2_width, height=guard_height,
        )

        x = guard_width + comp.guardring_space + 0.5*guard2_width
        y = 0.5*guard_height
        l_dn_ch = layouter.place(l_ch, x=x, y=y)
        layouter.place(dn, x=x, y=y)
        l_guard2 = layouter.place(l_guard2, x=x, y=y)
        ndiom1guard_bounds = l_guard2.bounds(mask=metal1.mask)

        # connect guard rings
        # currently can't be done in metal1 as no shapes with two or more holes
        # in it are supported.
        _l_via = layouter.fab.layout_primitive(
            via1, portnets={"conn": iovss}, rows=3,
        )
        _m1_bounds = _l_via.bounds(mask=metal1.mask)
        y = (
            max(resm1guard_bounds.bottom, ndiom1guard_bounds.bottom)
            - _m1_bounds.bottom + 2*metal2.min_space
        )
        l = layouter.place(
            _l_via, x=(resm1guard_bounds.right - _m1_bounds.right), y=y,
        )
        m2_bounds1 = l.bounds(mask=metal2.mask)
        l = layouter.place(
            _l_via, x=(ndiom1guard_bounds.left - _m1_bounds.left), y=y,
        )
        m2_bounds2 = l.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(
            rect=m2_bounds1, right=m2_bounds2.right, top=m2_bounds2.top,
        )
        layouter.add_wire(net=iovss, wire=metal2, pin=metal2pin, shape=shape)

        # P diode
        dp_prim = spec.pdiode
        guard3_width = (
            guard_width + comp.guardring_space + guard2_width
        )
        diode2_width = (
            guard3_width - 2*comp.guardring_width - 2*comp.min_space_pmos_active
        )
        l_ch = layouter.fab.layout_primitive(
            cont, portnets={"conn": core}, rows=2,
            bottom=dp_prim.wire, bottom_implant=dp_prim.implant,
            bottom_width=diode2_width,
        )
        dpchact_bounds = l_ch.bounds(mask=comp.active.mask)
        diode2_height = dpchact_bounds.top - dpchact_bounds.bottom
        dp = ckt.instantiate(
            dp_prim, name="DP", width=diode2_width, height=diode2_height,
        )
        core.childports += dp.ports.anode
        iovdd.childports += dp.ports.cathode

        guard3_height = (
            diode2_height + 2*comp.min_space_pmos_active + 2*comp.guardring_width
        )
        l_guard3 = hlp.guardring(
            fab=fab, net=iovdd, type_="n", width=guard3_width, height=guard3_height,
            fill_well=True,
        )

        x = 0.5*guard3_width
        y = guard_height + comp.guardring_space + 0.5*guard3_height
        l_dp_ch = layouter.place(l_ch, x=x, y=y)
        layouter.place(dp, x=x, y=y)
        l_guard3 = layouter.place(l_guard3, x=x, y=y)

        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0,
            right=(guard_width + comp.guardring_space + guard2_width),
            top=(guard_height + comp.guardring_space + guard3_height),
        )

        # Draw interconnects
        w = resm1pad_bounds.right - resm1pad_bounds.left
        x = 0.5*(resm1pad_bounds.left + resm1pad_bounds.right)
        l_via = layouter.fab.layout_primitive(
            via1, portnets={"conn": pad}, bottom_width=w,
        )
        viam1_bounds = l_via.bounds(mask=metal1.mask)
        y = -viam1_bounds.top + resm1pad_bounds.top
        l_via = layouter.place(l_via, x=x, y=y)
        resm2pad_bounds = l_via.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=resm1pad_bounds, bottom=0.0)
        layouter.add_wire(wire=metal2, net=pad, pin=metal2.pin[0], shape=shape)

        dnm1_bounds = l_dn_ch.bounds(mask=metal1.mask)
        dpm1_bounds = l_dp_ch.bounds(mask=metal1.mask)

        w = resm1core_bounds.right - resm1core_bounds.left
        x = 0.5*(resm1core_bounds.left + resm1core_bounds.right)
        l_via = layouter.fab.layout_primitive(
            via1, portnets={"conn": core}, bottom_width=w
        )
        viam1_bounds = l_via.bounds(mask=metal1.mask)
        y = -viam1_bounds.bottom + resm1core_bounds.bottom
        layouter.place(l_via, x=x, y=y)
        shape = _geo.Rect.from_rect(rect=resm1core_bounds, top=dpm1_bounds.top)
        layouter.add_wire(wire=metal2, net=core, shape=shape)

        layouter.add_wire(wire=via1, net=core, bottom_shape=dnm1_bounds)
        layouter.add_wire(wire=metal2, net=core, shape=dpm1_bounds)

        layouter.add_wire(wire=via1, net=core, bottom_shape=dpm1_bounds)
        shape = _geo.Rect.from_rect(rect=dpm1_bounds, top=layout.boundary.top)
        layouter.add_wire(wire=metal2, net=core, pin=metal2.pin[0], shape=shape)


class _RCClampResistor(_FactoryCell):
    def __init__(self, *, fab: "IOFactory"):
        # TODO: make3 more general; current only Sky130 compatibility
        super().__init__(fab=fab, name="RCClampResistor")

        spec = fab.spec

        res_prim = spec.resvdd_prim
        w = spec.resvdd_w
        l_finger = spec.resvdd_lfinger
        fingers = spec.resvdd_fingers
        space = spec.resvdd_space

        assert (
            (res_prim is not None) and (w is not None)
            and (l_finger is not None) and (fingers is not None)
            and (space is not None)
        )

        pitch = w + space

        wire = res_prim.wire
        assert len(res_prim.indicator) == 1
        indicator = res_prim.indicator[0]
        indicator_ext = res_prim.min_indicator_extension[0]
        contact = res_prim.contact
        contact_space = res_prim.min_contact_space
        assert (contact is not None) and (contact_space is not None)
        assert len(contact.top) == 1
        metal = contact.top[0]
        assert (
            isinstance(metal, _prm.MetalWire) and (metal.pin is not None)
            and (len(metal.pin) == 1)
        )
        metalpin = metal.pin[0]

        ckt = self.new_circuit()

        res = ckt.new_net(name="res", external=False)
        pin1 = ckt.new_net(name="pin1", external=True)
        pin2 = ckt.new_net(name="pin2", external=True)

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        # TODO: draw real resistor, currently just the wire is drawn
        coords1: List[_geo.Point] = []
        coords2: List[_geo.Point] = []

        _l = layouter.wire_layout(
            net=pin1, wire=contact, bottom=wire,
            bottom_height=w, bottom_enclosure="tall",
            top_enclosure="tall",
        )
        _ch_chbb = _l.bounds(mask=contact.mask)
        _ch_wirebb = _l.bounds(mask=wire.mask)
        x = min(
            -contact_space - _ch_chbb.right,
            -_ch_wirebb.right,
        )
        y = -_ch_wirebb.bottom
        l = layouter.place(_l, x=x, y=y)
        ch_wirebb = l.bounds(mask=wire.mask)
        ch_metalbb = l.bounds(mask=metal.mask)

        if ch_wirebb.right < -_geo.epsilon:
            shape = _geo.Rect.from_rect(rect=ch_wirebb, right=0.0)
            layouter.add_wire(net=pin1, wire=wire, shape=shape)
        layouter.add_wire(net=pin1, wire=metal, pin=metalpin, shape=ch_metalbb)

        coords1.extend((_geo.origin, _geo.Point(x=0.0, y=w)))
        coords2.append(_geo.origin)

        if fingers%2 != 0:
            raise NotImplementedError("Odd value for resvdd_fingers")
        for f in range(fingers//2):
            left = 2*f*pitch
            coords1.extend((
                _geo.Point(x=(left + space), y=w),
                _geo.Point(x=(left + space), y=l_finger),
                _geo.Point(x=(left + 2*pitch), y=l_finger),
                _geo.Point(x=(left + 2*pitch), y=w),
            ))
            coords2.extend((
                _geo.Point(x=(left + pitch), y=0.0),
                _geo.Point(x=(left + pitch), y=(l_finger - w)),
                _geo.Point(x=(left + pitch + space), y=(l_finger - w)),
                _geo.Point(x=(left + pitch + space), y=0.0),
            ))
        endp = coords1[-1]
        coords1[-1] = _geo.Point.from_point(point=endp, y=0.0)

        meander = _geo.Polygon(points=(*coords1, *reversed(coords2)))
        ms = _geo.MaskShape(mask=cast(_msk.DesignMask, wire.mask), shape=meander)
        layout.add_maskshape(net=res, maskshape=ms)
        ms = _geo.MaskShape(mask=cast(_msk.DesignMask, indicator.mask), shape=meander)
        layout.add_maskshape(net=None, maskshape=ms)

        _l = layouter.wire_layout(
            net=pin2, wire=contact, bottom=wire,
            bottom_height=w, bottom_enclosure="tall",
            top_enclosure="tall",
        )
        _ch_chbb = _l.bounds(mask=contact.mask)
        _ch_wirebb = _l.bounds(mask=wire.mask)
        x = fingers*pitch + max(
            contact_space - _ch_chbb.left,
            -ch_wirebb.left,
        )
        y = -_ch_wirebb.bottom
        l = layouter.place(_l, x=x, y=y)
        ch_wirebb = l.bounds(mask=wire.mask)
        ch_metalbb = l.bounds(mask=metal.mask)

        if ch_wirebb.left - _geo.epsilon > fingers*pitch:
            shape = _geo.Rect.from_rect(rect=ch_wirebb, left=fingers*pitch)
            layouter.add_wire(net=pin2, wire=wire, shape=shape)
        layouter.add_wire(net=pin2, wire=metal, pin=metalpin, shape=ch_metalbb)

        # boundary
        bb = _geo.Rect(
            left=0.0, bottom=0.0, right=meander.bounds.right, top=meander.bounds.top,
        )
        layouter.layout.boundary = bb


class _RCClampInverter(_FactoryCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="RCClampInverter")

        spec = fab.spec
        tech = fab.tech
        comp = fab.computed

        ninv_l = spec.invvdd_n_l
        ninv_w = spec.invvdd_n_w
        inv_nmos = spec.invvdd_n_mosfet
        n_fingers = spec.invvdd_n_fingers
        assert (
            (ninv_l is not None) and (ninv_w is not None)
            and (inv_nmos is not None) and (n_fingers is not None)
        )

        pinv_l = spec.invvdd_p_l
        pinv_w = spec.invvdd_p_w
        inv_pmos = spec.invvdd_p_mosfet
        p_fingers = spec.invvdd_p_fingers
        assert (
            (pinv_l is not None) and (pinv_w is not None)
            and (inv_pmos is not None) and (p_fingers is not None)
        )

        cap_l = spec.capvdd_l
        cap_w = spec.capvdd_w
        cap_mos = spec.capvdd_mosfet
        cap_fingers = spec.capvdd_fingers
        assert (
            (cap_l is not None) and (cap_w is not None)
            and (cap_mos is not None) and (cap_fingers is not None)
        )
        if cap_mos != inv_nmos:
            raise NotImplemented("Cap MOSFET != inverter nmos MOSFET")

        active = comp.active
        poly = comp.poly
        contact = comp.contact
        metal1 = comp.metal[1].prim
        metal1pin = metal1.pin[0]
        via1 = comp.vias[1]
        metal2 = comp.metal[2].prim
        metal2pin = metal2.pin[0]

        pclamp_cell = fab.clamp(type_="p", n_trans=spec.clampcount, n_drive=0)
        pclamp_lay = pclamp_cell.layout
        pclamp_actbb = pclamp_lay.bounds(mask=active.mask)

        ckt = self.new_circuit()
        supply = ckt.new_net(name="supply", external=True)
        ground = ckt.new_net(name="ground", external=True)
        in_ = ckt.new_net(name="in", external=True)
        out = ckt.new_net(name="out", external=True)

        layouter = self.new_circuitlayouter()

        actpitch = tech.computed.min_pitch(active, up=True)

        min_actpoly_space = tech.computed.min_space(active, poly)

        min_actch_space = None
        try:
            min_actch_space = tech.computed.min_space(active, contact)
        except ValueError:
            pass # Keep value at None

        # Outer ring with same dimensions as for the pclamp
        outerguardring_height = pclamp_actbb.height
        outerring_cell = fab.guardring(
            type_ = "p", width=spec.iocell_width, height=outerguardring_height,
        )
        inst = ckt.instantiate(outerring_cell, name="outerguard")
        ground.childports += inst.ports.conn
        x = 0.5*spec.iocell_width
        y = 0.5*outerguardring_height
        l = layouter.place(inst, x=x, y=y)
        outerguardring_m1bb = l.bounds(mask=metal1.mask)


        # Specs for cap mos and inverter nmos combined
        specs = []

        # inverter cap fingers
        for i in range(cap_fingers):
            inst = ckt.instantiate(cap_mos, name=f"capmos{i}", l=cap_l, w=cap_w)
            in_.childports += inst.ports.gate
            ground.childports += (
                inst.ports.sourcedrain1, inst.ports.sourcedrain2, inst.ports.bulk,
            )
            specs.append(_lay.MOSFETInstSpec(
                inst=inst, contact_left=contact, contact_right=contact,
            ))

        # inverter nmos fingers
        for i in range(n_fingers):
            inst = ckt.instantiate(inv_nmos, name=f"nmos{i}", l=ninv_l, w=ninv_w)
            in_.childports += inst.ports.gate
            ground.childports += inst.ports.bulk
            if i%2 == 0:
                ground.childports += inst.ports.sourcedrain1
                out.childports += inst.ports.sourcedrain2
            else:
                out.childports += inst.ports.sourcedrain1
                ground.childports += inst.ports.sourcedrain2
            specs.append(_lay.MOSFETInstSpec(
                inst=inst, contact_left=contact, contact_right=contact,
            ))

        _l = layouter.transistors_layout(trans_specs=specs)
        _actbb = _l.bounds()
        nmosguardring_height = _actbb.height + 8*actpitch
        nmosguardring_width = _actbb.width + 6*actpitch
        x = tech.on_grid(0.5*spec.iocell_width - _actbb.center.x)
        y = 0.5*_actbb.height + 10*actpitch
        nmos_lay = layouter.place(_l, x=x, y=y)
        nmos_actbb = nmos_lay.bounds(mask=active.mask)
        nmos_polybb = nmos_lay.bounds(mask=poly.mask)
        nmos_m1bb = nmos_lay.bounds(mask=metal1.mask)

        nmosguardring_cell = fab.guardring(
            type_="p", width=nmosguardring_width, height=nmosguardring_height,
            fill_implant=True,
        )
        inst = ckt.instantiate(nmosguardring_cell, name="nmosguardring")
        ground.childports += inst.ports.conn
        x = 0.5*spec.iocell_width
        l = layouter.place(inst, x=x, y=y)
        nmosguardring_actbb = l.bounds(mask=active.mask)
        nmosguardring_m1bb = l.bounds(mask=metal1.mask)

        # nmos guardring
        shape=_geo.Rect.from_rect(
            rect=nmosguardring_m1bb,
            top=nmosguardring_m1bb.bottom, bottom=outerguardring_m1bb.bottom,
        )
        layouter.add_wire(net=ground, wire=metal1, pin=metal1pin, shape=shape)

        # nmos ground connection
        for ms in nmos_lay.filter_polygons(
            net=ground, mask=metal1.mask, split=True, depth=1,
        ):
            bb = ms.shape.bounds
            shape = _geo.Rect.from_rect(rect=bb, top=nmosguardring_m1bb.top)
            layouter.add_wire(net=ground, wire=metal1, shape=shape)

        # nmos in connection
        w = nmos_polybb.width
        _l = layouter.wire_layout(
            net=in_, wire=contact, bottom=poly,
            bottom_width=w, bottom_enclosure="wide",
            top_width=w, top_enclosure="wide",
        )
        _ch_polybb = _l.bounds(mask=poly.mask)
        _ch_chbb = _l.bounds(mask=contact.mask)
        _ch_m1bb = _l.bounds(mask=metal1.mask)

        x = nmos_polybb.center.x
        y = min(
            nmos_actbb.bottom - min_actpoly_space - _ch_polybb.top,
            nmos_m1bb.bottom - metal1.min_space - _ch_m1bb.top,
        )
        if min_actch_space is not None:
            y = min(y, nmos_actbb.bottom - min_actch_space - _ch_chbb.top)
        l = layouter.place(_l, x=x, y=y)
        ch_polybb = l.bounds(mask=poly.mask)
        nmosinch_m1bb = l.bounds(mask=metal1.mask)

        for ms in nmos_lay.filter_polygons(net=in_, mask=poly.mask, split=True, depth=1):
            bb = ms.shape.bounds
            if bb.bottom - _geo.epsilon > ch_polybb.top:
                shape = _geo.Rect.from_rect(rect=bb, bottom=ch_polybb.bottom)
                layouter.add_wire(net=in_, wire=poly, shape=shape)

        _l = layouter.wire_layout(
            net=in_, wire=via1,
            bottom_width=w, bottom_enclosure="wide",
            top_width=w, top_enclosure="wide"
        )
        _via1_m1bb = _l.bounds(mask=metal1.mask)
        _via1_m2bb = _l.bounds(mask=metal2.mask)
        y = min(
            nmosinch_m1bb.top - _via1_m1bb.top,
            nmos_m1bb.bottom - metal1.min_space - _via1_m1bb.top,
            nmos_m1bb.bottom - 2*metal2.min_space - _via1_m2bb.top,
        )
        l = layouter.place(_l, x=x, y=y)
        nmosinvia1_m2bb = l.bounds(mask=metal2.mask)

        # nmos out connection
        nmosout_m2left = spec.iocell_width
        nmosout_m2right = 0.0
        for ms in nmos_lay.filter_polygons(
            net=out, mask=metal1.mask, split=True, depth=1,
        ):
            bb = ms.shape.bounds
            l = layouter.add_wire(
                net=out, wire=via1, x=bb.center.x,
                bottom_bottom=bb.bottom, bottom_top=bb.top, bottom_enclosure="tall",
                top_bottom=bb.bottom, top_top=bb.top, top_enclosure="tall",
            )
            m2bb = l.bounds(mask=metal2.mask)
            nmosout_m2left = min(nmosout_m2left, m2bb.left)
            nmosout_m2right = max(nmosout_m2right, m2bb.right)

        # inverter pmos fingers
        specs = []
        for i in range(p_fingers):
            inst = ckt.instantiate(inv_pmos, name=f"pmos{i}", l=pinv_l, w=pinv_w)
            in_.childports += inst.ports.gate
            supply.childports += inst.ports.bulk
            if i%2 == 0:
                supply.childports += inst.ports.sourcedrain1
                out.childports += inst.ports.sourcedrain2
            else:
                out.childports += inst.ports.sourcedrain1
                supply.childports += inst.ports.sourcedrain2
            specs.append(_lay.MOSFETInstSpec(
                inst=inst, contact_left=contact, contact_right=contact,
            ))

        _l = layouter.transistors_layout(trans_specs=specs)
        _actbb = _l.bounds(mask=active.mask)
        pmosguardring_height = _actbb.height + 8*actpitch
        pmosguardring_width = _actbb.width + 6*actpitch
        x = 0.5*spec.iocell_width - _actbb.center.x
        y = nmosguardring_actbb.top + 8*actpitch - _actbb.bottom
        pmos_lay = layouter.place(_l, x=x, y=y)
        pmos_actbb = pmos_lay.bounds(mask=active.mask)
        pmos_polybb = pmos_lay.bounds(mask=poly.mask)
        pmos_m1bb = pmos_lay.bounds(mask=metal1.mask)

        # pmos guardring
        pmosguardring_cell = fab.guardring(
            type_="n", width=pmosguardring_width, height=pmosguardring_height,
            fill_well=True, fill_implant=True,
        )
        inst = ckt.instantiate(pmosguardring_cell, name="pmosguardring")
        supply.childports += inst.ports.conn
        x = 0.5*spec.iocell_width
        l = layouter.place(inst, x=x, y=y)
        pmosguardring_m1bb = l.bounds(mask=metal1.mask)

        for ms in pmos_lay.filter_polygons(
            net=supply, mask=metal1.mask, split=True, depth=1,
        ):
            bb = ms.shape.bounds
            shape = _geo.Rect.from_rect(rect=bb, bottom=pmosguardring_m1bb.bottom)
            layouter.add_wire(net=supply, wire=metal1, shape=shape)

        shape = _geo.Rect.from_rect(
            rect=pmosguardring_m1bb,
            bottom=(pmosguardring_m1bb.top - comp.guardring_width),
        )
        layouter.add_wire(net=supply, wire=metal1, pin=metal1pin, shape=shape)

        # pmos in connection
        w = pmos_polybb.width
        _l = layouter.wire_layout(
            net=in_, wire=contact, bottom=poly,
            bottom_width=w, bottom_enclosure="wide",
            top_width=w, top_enclosure="wide",
        )
        _ch_polybb = _l.bounds(mask=poly.mask)
        _ch_chbb = _l.bounds(mask=contact.mask)
        _ch_m1bb = _l.bounds(mask=metal1.mask)

        x = pmos_polybb.center.x
        y = max(
            pmos_actbb.top + min_actpoly_space - _ch_polybb.bottom,
            pmos_m1bb.top + metal1.min_space - _ch_m1bb.bottom,
        )
        if min_actch_space is not None:
            y = max(y, pmos_actbb.top + min_actch_space - _ch_chbb.bottom)
        l = layouter.place(_l, x=x, y=y)
        ch_polybb = l.bounds(mask=poly.mask)
        pmosinch_m1bb = l.bounds(mask=metal1.mask)

        for ms in pmos_lay.filter_polygons(net=in_, mask=poly.mask, split=True, depth=1):
            bb = ms.shape.bounds
            if bb.top + _geo.epsilon < ch_polybb.bottom:
                shape = _geo.Rect.from_rect(rect=bb, top=ch_polybb.top)
                layouter.add_wire(net=in_, wire=poly, shape=shape)

        _l = layouter.wire_layout(
            net=in_, wire=via1,
            bottom_width=w, bottom_enclosure="wide",
            top_width=w, top_enclosure="wide",
        )
        _via1_m1bb = _l.bounds(mask=metal1.mask)
        _via1_m2bb = _l.bounds(mask=metal2.mask)
        y = max(
            pmosinch_m1bb.bottom - _via1_m1bb.bottom,
            pmos_m1bb.top + metal1.min_space - _via1_m1bb.bottom,
            pmos_m1bb.top + 2*metal2.min_space - _via1_m2bb.bottom,
        )
        l = layouter.place(_l, x=x, y=y)
        pmosinvia1_m2bb = l.bounds(mask=metal2.mask)

        # pmos out connection
        pmosout_m2left = spec.iocell_width
        pmosout_m2right = 0.0
        for ms in pmos_lay.filter_polygons(
            net=out, mask=metal1.mask, split=True, depth=1,
        ):
            bb = ms.shape.bounds
            l = layouter.add_wire(
                net=out, wire=via1, x=bb.center.x,
                bottom_bottom=bb.bottom, bottom_top=bb.top, bottom_enclosure="tall",
                top_bottom=bb.bottom, top_top=bb.top, top_enclosure="tall",
            )
            m2bb = l.bounds(mask=metal2.mask)
            pmosout_m2left = min(pmosout_m2left, m2bb.left)
            pmosout_m2right = max(pmosout_m2right, m2bb.right)

        assert nmosout_m2left > pmosout_m2left
        shape = _geo.Rect(
            left=pmosout_m2left, bottom=pmos_m1bb.bottom,
            right=max(nmosout_m2right, pmosout_m2right), top=pmos_m1bb.top,
        )
        layouter.add_wire(net=out, wire=metal2, shape=shape)
        shape = _geo.Rect(
            left=nmosout_m2left, bottom=nmos_m1bb.bottom,
            right=nmosout_m2right, top=pmos_m1bb.top,
        )
        layouter.add_wire(net=out, wire=metal2, pin=metal2pin, shape=shape)

        # in pin
        assert pmosinvia1_m2bb.left > nmosinvia1_m2bb.left
        shape = _geo.Rect.from_rect(rect=pmosinvia1_m2bb, left=nmosinvia1_m2bb.left)
        layouter.add_wire(net=in_, wire=metal2, shape=shape)
        shape = _geo.Rect(
            left=nmosinvia1_m2bb.left, bottom=nmosinvia1_m2bb.bottom,
            right=(pmosout_m2left - 3*metal2.min_space), top=pmosinvia1_m2bb.top,
        )
        layouter.add_wire(net=in_, wire=metal2, pin=metal2pin, shape=shape)

        # boundary
        layouter.layout.boundary = outerguardring_m1bb


class _Pad(_FactoryOnDemandCell):
    def __init__(self, *,
        name: str, fab: "IOFactory", width: float, height: float, start_via: int,
    ):
        super().__init__(fab=fab, name=name)

        self.width = width
        self.height = height
        self.start_via = start_via

    def _create_circuit(self):
        ckt = self.new_circuit()
        ckt.new_net(name="pad", external=True)

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        width = self.width
        height = self.height
        start_via = self.start_via

        comp = fab.computed
        pad = comp.pad
        topmetal = pad.bottom
        assert topmetal.pin is not None
        topmetalpin = topmetal.pin[0]

        pad_net = self.circuit.nets.pad
        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        enc = comp.pad.min_bottom_enclosure.max()
        metal_width = width + 2*enc
        metal_height = height + 2*enc

        metal_bounds = _geo.Rect.from_size(width=metal_width, height=metal_height)
        pad_bounds = _geo.Rect.from_size(width=width, height=height)

        # TODO: add support in layouter.add_wire for PadOpening
        layouter.add_wire(net=pad_net, wire=topmetal, pin=topmetalpin, shape=metal_bounds)
        layout.add_shape(prim=comp.pad, net=pad_net, shape=pad_bounds)

        if spec.padvia_pitch is None:
            top_via = comp.vias[-1]
            via_pitch = top_via.width + top_via.min_space
        else:
            via_pitch = spec.padvia_pitch

        for i, via in enumerate(comp.vias[start_via:]):
            l_via = hlp.diamondvia(
                fab=fab, net=pad_net, via=via,
                width=metal_width, height=metal_height,
                space=(via_pitch - via.width),
                enclosure=_prp.Enclosure(spec.padvia_metal_enclosure),
                center_via=((i%2) == 0), corner_distance=spec.padvia_corner_distance,
            )
            layouter.place(l_via, x=0.0, y=0.0)

        layout.boundary = metal_bounds


class _LevelUp(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="LevelUp")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        comp = fab.computed

        circuit = self.new_circuit()

        iopmos_lvlshift_w = max(
            spec.iopmos.computed.min_w, fab.computed.minwidth4ext_activewithcontact,
        )

        # Input inverter
        n_i_inv = circuit.instantiate(spec.nmos, name="n_i_inv", w=comp.maxnmos_w)
        p_i_inv = circuit.instantiate(spec.pmos, name="p_i_inv", w=comp.maxpmos_w)

        # Level shifter
        n_lvld_n = circuit.instantiate(
            spec.ionmos, name="n_lvld_n", w=comp.maxionmos_w,
            sd_width=0.5*spec.ionmos.computed.min_gate_space,
        )
        n_lvld = circuit.instantiate(
            spec.ionmos, name="n_lvld", w=comp.maxionmos_w,
            sd_width=0.5*spec.ionmos.computed.min_gate_space,
        )
        p_lvld_n = circuit.instantiate(
            spec.iopmos, name="p_lvld_n", w=iopmos_lvlshift_w,
            sd_width=0.5*spec.iopmos.computed.min_gate_space,
        )
        p_lvld = circuit.instantiate(
            spec.iopmos, name="p_lvld", w=iopmos_lvlshift_w,
            sd_width=0.5*spec.iopmos.computed.min_gate_space,
        )

        # Output inverter/driver
        n_lvld_n_inv = circuit.instantiate(
            spec.ionmos, name="n_lvld_n_inv", w=comp.maxionmos_w,
        )
        p_lvld_n_inv = circuit.instantiate(
            spec.iopmos, name="p_lvld_n_inv", w=comp.maxiopmos_w,
        )

        # Create the nets
        circuit.new_net(name="vdd", external=True, childports=(
            p_i_inv.ports.sourcedrain2, p_i_inv.ports.bulk,
        ))
        circuit.new_net(name="iovdd", external=True, childports=(
            p_lvld_n.ports.sourcedrain1, p_lvld_n.ports.bulk,
            p_lvld.ports.sourcedrain2, p_lvld.ports.bulk,
            p_lvld_n_inv.ports.sourcedrain1, p_lvld_n_inv.ports.bulk,
        ))
        circuit.new_net(name="vss", external=True, childports=(
            n_i_inv.ports.sourcedrain2, n_i_inv.ports.bulk,
            n_lvld_n.ports.sourcedrain1, n_lvld_n.ports.bulk,
            n_lvld.ports.sourcedrain2, n_lvld.ports.bulk,
            n_lvld_n_inv.ports.sourcedrain1, n_lvld_n_inv.ports.bulk,
        ))

        circuit.new_net(name="i", external=True, childports=(
            n_i_inv.ports.gate, p_i_inv.ports.gate,
            n_lvld_n.ports.gate,
        ))
        circuit.new_net(name="i_n", external=False, childports=(
            n_i_inv.ports.sourcedrain1, p_i_inv.ports.sourcedrain1,
            n_lvld.ports.gate,
        ))
        circuit.new_net(name="lvld", external=False, childports=(
            p_lvld_n.ports.gate,
            n_lvld.ports.sourcedrain1, p_lvld.ports.sourcedrain1,
        ))
        circuit.new_net(name="lvld_n", external=False, childports=(
            n_lvld_n.ports.sourcedrain2, p_lvld_n.ports.sourcedrain2,
            p_lvld.ports.gate,
            n_lvld_n_inv.ports.gate, p_lvld_n_inv.ports.gate,
        ))
        circuit.new_net(name="o", external=True, childports=(
            n_lvld_n_inv.ports.sourcedrain2, p_lvld_n_inv.ports.sourcedrain2,
        ))

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        tech = fab.tech
        comp = fab.computed

        circuit = self.circuit
        insts = circuit.instances
        nets = circuit.nets

        active = comp.active
        nimplant = comp.nimplant
        pimplant = comp.pimplant
        ionimplant = comp.ionimplant
        iopimplant = comp.iopimplant
        assert pimplant == iopimplant
        nwell = comp.nwell
        poly = comp.poly
        contact = comp.contact
        metal1 = cast(_prm.MetalWire, contact.top[0])
        assert metal1.pin is not None
        metal1pin = metal1.pin[0]
        via1 = comp.vias[1]
        metal2 = via1.top[0]
        assert isinstance(metal2, _prm.MetalWire)

        chm1_enc = contact.min_top_enclosure[0]
        chm1_wideenc = _prp.Enclosure((chm1_enc.max(), chm1_enc.min()))

        actox_enc = (
            comp.activeoxide_enclosure.max() if comp.activeoxide_enclosure is not None
            else comp.iogateoxide_enclosure.max()
        )

        iopmos_lvlshift_w = max(
            spec.iopmos.computed.min_w, comp.minwidth4ext_activewithcontact,
        )

        layouter = self.new_circuitlayouter()
        layout = self.layout
        active_left = 0.5*active.min_space

        if metal2.pin is not None:
            assert len(metal2.pin) == 1
            pin_args = {"pin": metal2.pin[0]}
        else:
            pin_args = {}

        min_actpoly_space = tech.computed.min_space(active, poly)
        try:
            min_actch_space = tech.computed.min_space(active, contact)
        except AttributeError:
            min_actch_space = None

        #
        # Core row
        #

        x = active_left + 0.5*comp.minwidth_activewithcontact
        bottom = comp.maxnmos_activebottom
        top = comp.maxnmos_activetop
        l = layouter.add_wire(
            net=nets.i_n, wire=contact, x=x, y=0.5*(bottom + top),
            bottom=active, bottom_implant=nimplant,
            bottom_height=(top - bottom),
        )
        chbounds_n = l.bounds(mask=metal1.mask)
        layouter.add_wire(
            net=nets.i_n, wire=active, implant=nimplant,
            x=x, width=comp.minwidth_activewithcontact,
            y=comp.maxnmos_y, height=comp.maxnmos_w,
        )
        bottom = comp.maxpmos_activebottom
        top = comp.maxpmos_activetop
        l = layouter.add_wire(
            net=nets.i_n, well_net=nets.vdd, wire=contact, x=x, y=0.5*(bottom + top),
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_height=(top - bottom),
        )
        chbounds_p = l.bounds(mask=metal1.mask)
        layouter.add_wire(
            net=nets.i_n, well_net=nets.vdd, wire=active, implant=pimplant, well=nwell,
            x=x, width=comp.minwidth_activewithcontact,
            y=comp.maxpmos_y, height=comp.maxpmos_w,
        )
        shape = _geo.Rect.from_rect(
            rect=chbounds_n, bottom=chbounds_n.top, top=chbounds_p.bottom,
        )
        layouter.add_wire(net=nets.i_n, wire=metal1, shape=shape)
        bottom_shape = _geo.Rect(
            bottom=chbounds_n.bottom, top=chbounds_p.top,
            right=chbounds_n.right, left=(chbounds_n.right - comp.metal[1].minwidth_up),
        )
        m2bounds = layouter.add_wire(
            net=nets.i_n, wire=via1, bottom_shape=bottom_shape,
        ).bounds(mask=metal2.mask)
        i_n_m2bounds = _geo.Rect.from_rect(rect=m2bounds, bottom=spec.iorow_height)
        layouter.add_wire(net=nets.i_n, wire=metal2, shape=i_n_m2bounds)

        x += max((
            comp.minnmos_contactgatepitch,
            comp.minpmos_contactgatepitch,
        ))
        l = layouter.place(insts.n_i_inv, x=x, y=comp.maxnmos_y)
        nimplbounds1 = l.bounds(mask=nimplant.mask)
        gatebounds_n = l.bounds(mask=poly.mask)
        l = layouter.place(insts.p_i_inv, x=x, y=comp.maxpmos_y)
        pimplbounds1 = l.bounds(mask=pimplant.mask)
        gatebounds_p = l.bounds(mask=poly.mask)

        shape = _geo.Rect(
            left=min(gatebounds_n.left, gatebounds_p.left), bottom=gatebounds_n.top,
            right=max(gatebounds_n.right, gatebounds_p.right), top=gatebounds_p.bottom,
        )
        polybounds = layouter.add_wire(
            net=nets.i, wire=poly, shape=shape,
        ).bounds(mask=poly.mask)
        x_pad = max(
            polybounds.left + 0.5*comp.minwidth4ext_polywithcontact,
            chbounds_n.right + metal1.min_space
            + 0.5*comp.metal[1].minwidth4ext_down,
        )
        l = layouter.add_wire(
            net=nets.i, wire=contact, bottom=poly, x=x_pad,
            y=tech.on_grid(0.5*(polybounds.bottom + polybounds.top)),
        )
        gatebounds = l.bounds(mask=metal1.mask)
        polybounds2 = l.bounds(mask=poly.mask)
        if polybounds2.left > polybounds.right:
            shape = _geo.Rect.from_rect(rect=polybounds2, left=polybounds.left)
            layouter.add_wire(net=nets.i, wire=poly, shape=shape)

        x += max((
            comp.minnmos_contactgatepitch,
            comp.minpmos_contactgatepitch,
        ))
        bottom = comp.maxnmos_activebottom
        top = min(comp.maxnmos_activetop, gatebounds.bottom - metal1.min_width)
        chbounds_n = layouter.add_wire(
            net=nets.vss, wire=contact, x=x, y=0.5*(bottom + top),
            bottom=active, bottom_implant=comp.nmos.implant[0],
            bottom_height=(top - bottom), top_height=(top - bottom),
        ).bounds(mask=metal1.mask)
        layouter.add_wire(
            net=nets.vss, wire=active, implant=nimplant,
            x=x, width=comp.minwidth_activewithcontact,
            y=comp.maxnmos_y, height=comp.maxnmos_w,
        )
        bottom = max(comp.maxpmos_activebottom, gatebounds.top + metal1.min_width)
        top = comp.maxpmos_activetop
        chbounds_p = layouter.add_wire(
            net=nets.vdd, wire=contact, x=x, y=0.5*(bottom + top),
            bottom=active, bottom_implant=comp.pmos.implant[0],
            bottom_height=(top - bottom), top_height=(top - bottom),
        ).bounds(mask=metal1.mask)
        layouter.add_wire(
            net=nets.vdd, well_net=nets.vdd, wire=active, implant=pimplant, well=nwell,
            x=x, width=comp.minwidth_activewithcontact,
            y=comp.maxpmos_y, height=comp.maxpmos_w,
        )

        shape = _geo.Rect.from_rect(
            rect=chbounds_n, bottom=spec.iorow_height, top=chbounds_n.bottom,
        )
        layouter.add_wire(net=nets.vss, wire=metal1, shape=shape)
        shape = _geo.Rect.from_rect(rect=chbounds_p, top=spec.cells_height)
        layouter.add_wire(net=nets.vdd, wire=metal1, shape=shape)

        x += comp.minwidth_activewithcontact + active.min_space
        bottom = comp.maxnmos_activebottom
        top = comp.maxnmos_activetop
        l = layouter.add_wire(
            net=nets.i, wire=contact, x=x, y=0.5*(bottom + top),
            bottom=active, bottom_implant=nimplant,
            bottom_height=(top - bottom),
        )
        chbounds_ndio = l.bounds(mask=metal1.mask)
        nimplbounds2 = l.bounds(mask=nimplant.mask)
        layouter.add_wire(
            net=nets.i, wire=active, implant=nimplant,
            x=x, width=comp.minwidth_activewithcontact,
            y=comp.maxnmos_y, height=comp.maxnmos_w,
        )
        bottom = comp.maxpmos_activebottom
        top = comp.maxpmos_activetop
        l = layouter.add_wire(
            net=nets.i, wire=contact, x=x, y=0.5*(bottom + top),
            bottom=active, bottom_implant=pimplant,
            bottom_height=(top - bottom),
        )
        chbounds_pdio = l.bounds(mask=metal1.mask)
        pimplbounds2 = l.bounds(mask=pimplant.mask)
        layouter.add_wire(
            net=nets.i, well_net=nets.vdd, wire=active, implant=pimplant, well=nwell,
            x=x, width=comp.minwidth_activewithcontact,
            y=comp.maxpmos_y, height=comp.maxpmos_w,
        )
        shape = _geo.Rect.from_rect(
            rect=chbounds_ndio, bottom=chbounds_ndio.top, top=chbounds_pdio.bottom,
        )
        layouter.add_wire(net=nets.i, wire=metal1, shape=shape)
        shape = _geo.Rect(
            left=gatebounds.left, bottom=(chbounds_n.top + metal1.min_width),
            right=chbounds_ndio.right, top=(chbounds_p.bottom - metal1.min_width),
        )
        layouter.add_wire(net=nets.i, wire=metal1, shape=shape)
        bottom = chbounds_ndio.bottom
        top = chbounds_pdio.top
        i_m2bounds = layouter.add_wire(
            net=nets.i, wire=via1, x=x, bottom_bottom=bottom, bottom_top=top,
        ).bounds(mask=metal2.mask)
        layouter.add_wire(net=nets.i, wire=metal2, **pin_args, shape=i_m2bounds)

        # Fill implants
        layouter.add_portless(prim=nimplant, shape=_geo.Rect.from_rect(
            rect=nimplbounds1, right=nimplbounds2.right,
        ))
        layouter.add_portless(prim=pimplant, shape=_geo.Rect.from_rect(
            rect=pimplbounds1, right=pimplbounds2.right,
        ))

        #
        # IO row
        #
        active_left = 0.5*comp.min_oxactive_space
        y_iopmos_lvlshift = comp.maxiopmos_y

        # Place left source-drain contacts
        _nch_lvld_lay = layouter.wire_layout(
            net=nets.lvld, wire=contact, bottom=active, bottom_implant=ionimplant,
            bottom_height=comp.maxionmos_w,
        )
        _nch_lvld_actbounds = _nch_lvld_lay.bounds(mask=active.mask)
        x = active_left - _nch_lvld_actbounds.left
        y = comp.maxionmos_y
        nch_lvld_lay = layouter.place(object_=_nch_lvld_lay, x=x, y=y)
        nch_lvld_chbounds = nch_lvld_lay.bounds(mask=contact.mask)
        nch_lvld_m1bounds = nch_lvld_lay.bounds(mask=metal1.mask)
        n_lvld_ionimplbounds = nch_lvld_lay.bounds(mask=ionimplant.mask)
        _pch_lvld_lay = layouter.wire_layout(
            net=nets.lvld, well_net=nets.iovdd, wire=contact,
            bottom=active, bottom_implant=iopimplant, bottom_well=nwell,
            bottom_height=iopmos_lvlshift_w,
        )
        _pch_lvld_actbounds = _pch_lvld_lay.bounds(mask=active.mask)
        x = active_left - _pch_lvld_actbounds.left
        y = y_iopmos_lvlshift
        pch_lvld_lay = layouter.place(object_=_pch_lvld_lay, x=x, y=y)
        pch_lvld_chbounds = pch_lvld_lay.bounds(mask=contact.mask)
        pch_lvld_m1bounds = pch_lvld_lay.bounds(mask=metal1.mask)
        pimpl_left = pch_lvld_lay.bounds(mask=iopimplant.mask).left
        p_lvld_iopimplbounds = pch_lvld_lay.bounds(mask=iopimplant.mask)
        pimpl_bottom = p_lvld_iopimplbounds.bottom
        pimpl_top = p_lvld_iopimplbounds.top
        lvld_m1_lay = layouter.add_wire(
            net=nets.lvld, wire=metal1, shape=_geo.Rect.from_rect(
                rect=nch_lvld_m1bounds, bottom=pch_lvld_m1bounds.bottom,
            ),
        )
        lvld_m1_bounds = lvld_m1_lay.bounds()

        poly_left = max(
            nch_lvld_chbounds.right + spec.ionmos.computed.min_contactgate_space,
            pch_lvld_chbounds.right + spec.iopmos.computed.min_contactgate_space,
        )

        # Place n_lvld and p_lvld, and compute pad y placements
        _n_lvld_lay = layouter.inst_layout(inst=insts.n_lvld)
        _n_lvld_polybounds = _n_lvld_lay.bounds(mask=poly.mask)
        x = poly_left - _n_lvld_polybounds.left
        y = comp.maxionmos_y
        n_lvld_lay = layouter.place(_n_lvld_lay, x=x, y=y)
        n_lvld_actbounds = n_lvld_lay.bounds(mask=active.mask)
        n_lvld_polybounds = n_lvld_lay.bounds(mask=poly.mask)
        _p_lvld_lay = layouter.inst_layout(inst=insts.p_lvld)
        _p_lvld_polybounds = _p_lvld_lay.bounds(mask=poly.mask)
        x = poly_left - _p_lvld_polybounds.left
        y = y_iopmos_lvlshift
        p_lvld_lay = layouter.place(_p_lvld_lay, x=x, y=y)
        p_lvld_actbounds = p_lvld_lay.bounds(mask=active.mask)
        p_lvld_polybounds = p_lvld_lay.bounds(mask=poly.mask)
        w = cast(_ckt._PrimitiveInstance, insts.p_lvld).params["w"]
        p_lvld_pad_bottom = (
            y_iopmos_lvlshift + 0.5*w
            + tech.computed.min_space(active, poly)
        )
        p_lvld_pad_top = (
            p_lvld_pad_bottom + comp.minwidth4ext_polywithcontact
        )
        p_lvld_n_pad_bottom = p_lvld_pad_top + poly.min_space
        p_lvld_n_pad_top = p_lvld_n_pad_bottom + comp.minwidth4ext_polywithcontact

        # Place mid source-drain contacts
        _lvlshift_chiovss_lay = layouter.wire_layout(
            net=nets.vss, wire=contact, bottom=active, bottom_implant=ionimplant,
            bottom_height=comp.maxionmos_w,
        )
        _lvlshift_chvss_chbounds = _lvlshift_chiovss_lay.bounds(mask=contact.mask)
        x = (
            n_lvld_polybounds.right + spec.ionmos.computed.min_contactgate_space
            - _lvlshift_chvss_chbounds.left
        )
        y = comp.maxionmos_y
        lvlshit_chiovss_lay = layouter.place(object_=_lvlshift_chiovss_lay, x=x, y=y)
        lvlshift_chiovss_chbounds = lvlshit_chiovss_lay.bounds(mask=contact.mask)
        lvlshift_chiovss_m1bounds = lvlshit_chiovss_lay.bounds(mask=metal1.mask)
        layouter.add_wire(
            net=nets.vss, wire=metal1, shape=_geo.Rect.from_rect(
                rect=lvlshift_chiovss_m1bounds, top=spec.iorow_height,
            ),
        )
        _lvlshift_chiovdd_lay = layouter.wire_layout(
            net=nets.iovdd, well_net=nets.iovdd, wire=contact, bottom_height=iopmos_lvlshift_w,
            bottom=active, bottom_implant=iopimplant, bottom_well=nwell,
            top_enclosure=chm1_wideenc,
        )
        _lvlshift_chiovdd_chbounds = _lvlshift_chiovdd_lay.bounds(mask=contact.mask)
        x = (
            p_lvld_polybounds.right + spec.iopmos.computed.min_contactgate_space
            - _lvlshift_chiovdd_chbounds.left
        )
        y = y_iopmos_lvlshift
        lvlshift_chiovdd_lay = layouter.place(object_=_lvlshift_chiovdd_lay, x=x, y=y)
        lvlshift_chiovdd_chbounds = lvlshift_chiovdd_lay.bounds(mask=contact.mask)
        lvlshift_chiovdd_m1bounds = lvlshift_chiovdd_lay.bounds(mask=metal1.mask)
        layouter.add_wire(
            net=nets.iovdd, wire=metal1, shape=_geo.Rect.from_rect(
                rect=lvlshift_chiovdd_m1bounds, bottom=0.0,
            ),
        )

        poly_left = max(
            lvlshift_chiovss_chbounds.right + spec.ionmos.computed.min_contactgate_space,
            lvlshift_chiovdd_chbounds.right + spec.iopmos.computed.min_contactgate_space,
        )

        # Place n_lvld_n and p_lvld_n
        _n_lvld_n_lay = layouter.inst_layout(inst=insts.n_lvld_n)
        _n_lvld_n_polybounds = _n_lvld_n_lay.bounds(mask=poly.mask)
        x = poly_left - _n_lvld_n_polybounds.left
        y = comp.maxionmos_y
        n_lvld_n_lay = layouter.place(object_=_n_lvld_lay, x=x, y=y)
        n_lvld_n_actbounds = n_lvld_n_lay.bounds(mask=active.mask)
        n_lvld_n_polybounds = n_lvld_n_lay.bounds(mask=poly.mask)
        _p_lvld_n_lay = layouter.inst_layout(inst=insts.p_lvld_n)
        _p_lvld_n_polybounds = _p_lvld_n_lay.bounds(mask=poly.mask)
        x = poly_left - _p_lvld_n_polybounds.left
        y = y_iopmos_lvlshift
        p_lvld_n_lay = layouter.place(object_=_p_lvld_n_lay, x=x, y=y)
        p_lvld_n_actbounds = p_lvld_n_lay.bounds(mask=active.mask)
        p_lvld_n_polybounds = p_lvld_n_lay.bounds(mask=poly.mask)

        # Place right source-drain contacts
        _nch_lvld_n_lay = layouter.wire_layout(
            net=nets.lvld_n, wire=contact, bottom_height=comp.maxionmos_w,
            bottom=active, bottom_implant=ionimplant,
        )
        _nch_lvld_n_chbounds = _nch_lvld_lay.bounds(mask=contact.mask)
        nch_lvld_n_x = (
            n_lvld_n_polybounds.right + spec.nmos.computed.min_contactgate_space
            - _nch_lvld_n_chbounds.left
        )
        nch_lvld_n_y = comp.maxionmos_y
        nch_lvld_n_lay = layouter.place(
            object_=_nch_lvld_n_lay, x=nch_lvld_n_x, y=nch_lvld_n_y,
        )
        nch_lvld_n_actbounds = nch_lvld_n_lay.bounds(mask=active.mask)
        nch_lvld_n_m1bounds = nch_lvld_n_lay.bounds(mask=metal1.mask)
        # assert nch_lvld_n_m1bounds.left >= (
        #     n_lvld_ppad_m1bounds.right + metal1.min_space
        # )
        _pch_lvld_n_lay = layouter.wire_layout(
            net=nets.lvld_n, well_net=nets.iovdd, wire=contact,
            bottom=active, bottom_implant=iopimplant, bottom_well=nwell,
            bottom_height=iopmos_lvlshift_w,
        )
        _pch_lvld_n_chbounds = _pch_lvld_n_lay.bounds(mask=contact.mask)
        pch_lvld_n_x = (
            p_lvld_n_polybounds.right + spec.pmos.computed.min_contactgate_space
            - _pch_lvld_n_chbounds.left
        )
        pch_lvld_n_y = y_iopmos_lvlshift
        pch_lvld_n_lay = layouter.place(
            object_=_pch_lvld_n_lay, x=pch_lvld_n_x, y=pch_lvld_n_y
        )
        pch_lvld_n_actbounds = pch_lvld_n_lay.bounds(mask=active.mask)
        pch_lvld_n_m1bounds = pch_lvld_n_lay.bounds(mask=metal1.mask)
        pimpl_right = l.bounds(mask=iopimplant.mask).right
        lvld_n_m1_lay = layouter.add_wire(
            net=nets.lvld_n, wire=metal1, shape=_geo.Rect.from_rect(
                rect=nch_lvld_n_m1bounds, bottom=pch_lvld_n_m1bounds.bottom,
            ),
        )
        lvld_n_m1_bounds = lvld_n_m1_lay.bounds()
        # Add manual implant rectangle
        layouter.add_portless(prim=iopimplant, shape=_geo.Rect(
            left=pimpl_left, bottom=pimpl_bottom,
            right=pimpl_right, top=pimpl_top,
        ))

        # Poly pads for nmoses of the level shifter
        _n_lvld_ppad_lay = layouter.wire_layout(
            net=nets.i_n, wire=contact, bottom=poly,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _n_lvld_ppad_polybounds = _n_lvld_ppad_lay.bounds(mask=poly.mask)
        _n_lvld_ppad_chbounds = _n_lvld_ppad_lay.bounds(mask=contact.mask)
        _n_lvld_ppad_m1bounds = _n_lvld_ppad_lay.bounds(mask=metal1.mask)
        _n_lvld_n_ppad_lay = layouter.wire_layout(
            net=nets.i_n, wire=contact, bottom=poly,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _n_lvld_n_ppad_polybounds = _n_lvld_n_ppad_lay.bounds(mask=poly.mask)
        _n_lvld_n_ppad_chbounds = _n_lvld_n_ppad_lay.bounds(mask=contact.mask)
        _n_lvld_n_ppad_m1bounds = _n_lvld_n_ppad_lay.bounds(mask=metal1.mask)

        n_lvld_ppad_x = max(
            n_lvld_polybounds.left - _n_lvld_ppad_polybounds.left,
            n_lvld_polybounds.right - _n_lvld_ppad_polybounds.right,
            lvld_m1_bounds.right + metal1.min_space - _n_lvld_ppad_m1bounds.left,
        )
        n_lvld_ppad_y = (
            n_lvld_actbounds.bottom - min_actpoly_space - _n_lvld_ppad_polybounds.top
        )
        if min_actch_space is not None:
            n_lvld_ppad_y = min(
                n_lvld_ppad_y,
                n_lvld_actbounds.bottom - min_actch_space - _n_lvld_ppad_chbounds.top,
            )
        n_lvld_n_ppad_x = min(
            n_lvld_n_polybounds.left - _n_lvld_n_ppad_polybounds.left,
            n_lvld_n_polybounds.right - _n_lvld_n_ppad_polybounds.right,
            lvld_n_m1_bounds.left - metal1.min_space - _n_lvld_n_ppad_m1bounds.right,
        )
        n_lvld_n_ppad_y = (
            n_lvld_n_actbounds.bottom - min_actpoly_space - _n_lvld_n_ppad_polybounds.top
        )
        if min_actch_space is not None:
            n_lvld_n_ppad_y = min(
                n_lvld_n_ppad_y,
                n_lvld_n_actbounds.bottom - min_actch_space - _n_lvld_n_ppad_chbounds.top,
            )

        n_lvld_ppad_lay = layouter.place(
            object_=_n_lvld_ppad_lay, x=n_lvld_ppad_x, y=n_lvld_ppad_y,
        )
        n_lvld_ppad_polybounds = n_lvld_ppad_lay.bounds(mask=poly.mask)
        n_lvld_ppad_m1bounds = n_lvld_ppad_lay.bounds(mask=metal1.mask)
        layouter.add_wire(net=nets.lvld, wire=poly, shape=_geo.Rect.from_rect(
            rect=n_lvld_polybounds, bottom=n_lvld_ppad_polybounds.bottom,
        ))
        n_lvld_n_ppad_lay = layouter.place(
            object_=_n_lvld_n_ppad_lay, x=n_lvld_n_ppad_x, y=n_lvld_n_ppad_y,
        )
        n_lvld_n_ppad_polybounds = n_lvld_n_ppad_lay.bounds(mask=poly.mask)
        n_lvld_n_ppad_m1bounds = n_lvld_n_ppad_lay.bounds(mask=metal1.mask)
        layouter.add_wire(net=nets.lvld_n, wire=poly, shape=_geo.Rect.from_rect(
            rect=n_lvld_n_polybounds, bottom=n_lvld_n_ppad_polybounds.bottom,
        ))

        # via1 pads on the poly pads
        # draw two vias to make sure metal1 area is big enough
        _n_lvld_via_lay = layouter.wire_layout(net=nets.i_n, wire=via1, rows=2)
        _n_lvld_via_m1bounds = _n_lvld_via_lay.bounds(mask=metal1.mask)
        n_lvld_via_x = n_lvld_ppad_m1bounds.left - _n_lvld_via_m1bounds.left
        n_lvld_via_y = n_lvld_ppad_m1bounds.top - _n_lvld_via_m1bounds.top
        n_lvld_via_lay = layouter.place(
            object_=_n_lvld_via_lay, x=n_lvld_via_x, y=n_lvld_via_y,
        )
        n_lvld_n_via_m2bounds = n_lvld_via_lay.bounds(mask=metal2.mask)
        layouter.add_wire(net=nets.i_n, wire=metal2, shape=_geo.Rect.from_rect(
            rect=i_n_m2bounds, bottom=n_lvld_n_via_m2bounds.bottom,
        ))
        layouter.add_wire(net=nets.i_n, wire=metal2, shape=_geo.Rect.from_rect(
            rect=n_lvld_n_via_m2bounds, left=i_n_m2bounds.left,
        ))
        _n_lvld_n_via_lay = layouter.wire_layout(net=nets.i, wire=via1, rows=2)
        _n_lvld_n_via_m1bounds = _n_lvld_n_via_lay.bounds(mask=metal1.mask)
        n_lvld_n_via_x = n_lvld_n_ppad_m1bounds.left - _n_lvld_n_via_m1bounds.left
        n_lvld_n_via_y = n_lvld_n_ppad_m1bounds.top - _n_lvld_n_via_m1bounds.top
        n_lvld_n_via_lay = layouter.place(
            object_=_n_lvld_n_via_lay, x=n_lvld_n_via_x, y=n_lvld_n_via_y,
        )
        n_lvld_n_via_m2bounds = n_lvld_n_via_lay.bounds(mask=metal2.mask)
        layouter.add_wire(net=nets.i, wire=metal2, shape=_geo.Rect.from_rect(
            rect=i_m2bounds, bottom=n_lvld_n_via_m2bounds.bottom,
        ))
        assert i_m2bounds.left <= n_lvld_n_via_m2bounds.right
        layouter.add_wire(net=nets.i, wire=metal2, shape=_geo.Rect.from_rect(
            rect=n_lvld_n_via_m2bounds, left=i_m2bounds.left,
        ))

        # Poly pads for the pmoses of the level shifter
        _p_lvld_ppad_lay = layouter.wire_layout(
            net=nets.lvld, wire=contact, bottom=poly,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _p_lvld_ppad_polybounds = _p_lvld_ppad_lay.bounds(mask=poly.mask)
        _p_lvld_ppad_chbounds = _p_lvld_ppad_lay.bounds(mask=contact.mask)
        _p_lvld_ppad_m1bounds = _p_lvld_ppad_lay.bounds(mask=metal1.mask)
        p_lvld_ppad_x = max(
            lvld_m1_bounds.right + metal1.min_space - _p_lvld_ppad_m1bounds.left,
            p_lvld_polybounds.left - _p_lvld_ppad_polybounds.left,
            p_lvld_polybounds.right - _p_lvld_ppad_polybounds.right,
        )
        p_lvld_ppad_y = max(
            p_lvld_actbounds.top + min_actpoly_space - _p_lvld_ppad_polybounds.bottom,
            lvlshift_chiovdd_m1bounds.top + metal1.min_space - _p_lvld_ppad_m1bounds.bottom,
        )
        if min_actch_space is not None:
            p_lvld_ppad_y = max(
                p_lvld_ppad_y,
                p_lvld_actbounds.top + min_actch_space - _p_lvld_ppad_chbounds.bottom
            )
        p_lvld_ppad_lay = layouter.place(
            object_=_p_lvld_ppad_lay, x=p_lvld_ppad_x, y=p_lvld_ppad_y,
        )
        p_lvld_ppad_polybounds = p_lvld_ppad_lay.bounds(mask=poly.mask)
        p_lvld_ppad_m1bounds = p_lvld_ppad_lay.bounds(mask=metal1.mask)
        layouter.add_wire(net=nets.lvld, wire=poly, shape=_geo.Rect.from_rect(
            rect=p_lvld_polybounds, top=p_lvld_ppad_polybounds.top,
        ))
        layouter.add_wire(net=nets.lvld_n, wire=metal1, shape=_geo.Rect.from_rect(
            rect=p_lvld_ppad_m1bounds, right=lvld_n_m1_bounds.right,
        ))

        _p_lvld_n_ppad_lay = layouter.wire_layout(
            net=nets.lvld_n, wire=contact, bottom=poly,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _p_lvld_n_ppad_polybounds = _p_lvld_n_ppad_lay.bounds(mask=poly.mask)
        _p_lvld_n_ppad_m1bounds = _p_lvld_n_ppad_lay.bounds(mask=metal1.mask)
        p_lvld_n_ppad_x = min(
            lvld_n_m1_bounds.left - metal1.min_space - _p_lvld_n_ppad_m1bounds.right,
            p_lvld_n_polybounds.left - _p_lvld_n_ppad_polybounds.left,
            p_lvld_n_polybounds.right - _p_lvld_n_ppad_polybounds.right,
        )
        p_lvld_n_ppad_y = (
            p_lvld_ppad_m1bounds.top + metal1.min_space - _p_lvld_n_ppad_m1bounds.bottom
        )
        p_lvld_n_ppad_lay = layouter.place(
            object_=_p_lvld_n_ppad_lay, x=p_lvld_n_ppad_x, y=p_lvld_n_ppad_y,
        )
        p_lvld_n_ppad_polybounds = p_lvld_n_ppad_lay.bounds(mask=poly.mask)
        p_lvld_n_ppad_m1bounds = p_lvld_n_ppad_lay.bounds(mask=metal1.mask)
        layouter.add_wire(net=nets.lvld, wire=poly, shape=_geo.Rect.from_rect(
            rect=p_lvld_n_polybounds, top=p_lvld_n_ppad_polybounds.top,
        ))
        layouter.add_wire(net=nets.lvld, wire=metal1, shape=_geo.Rect.from_rect(
            rect=p_lvld_n_ppad_m1bounds, left=lvld_m1_bounds.left,
        ))

        # Output buffer
        active_left = (
            max(nch_lvld_n_actbounds.right, pch_lvld_n_actbounds.right)
            + comp.min_oxactive_space
        )

        # Place left source-drain contacts
        _obuf_chiovss_lay = layouter.wire_layout(
            net=nets.vss, wire=contact, bottom_height=comp.maxionmos_w,
            bottom=active, bottom_implant=ionimplant,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _obuf_chiovss_actbounds = _obuf_chiovss_lay.bounds(mask=active.mask)
        obuf_chiovss_x = active_left - _obuf_chiovss_actbounds.left
        obuf_chiovss_y = comp.maxionmos_y
        obuf_chiovss_lay = layouter.place(
            object_=_obuf_chiovss_lay, x=obuf_chiovss_x, y=obuf_chiovss_y,
        )
        obuf_chiovss_chbounds = obuf_chiovss_lay.bounds(mask=contact.mask)
        obuf_chiovss_m1bounds = obuf_chiovss_lay.bounds(mask=metal1.mask)
        layouter.add_wire(net=nets.vss, wire=metal1, shape=_geo.Rect.from_rect(
            rect=obuf_chiovss_m1bounds, top=spec.iorow_height,
        ))
        _obuf_chiovdd_lay = layouter.wire_layout(
            net=nets.iovdd, well_net=nets.iovdd, wire=contact,
            bottom_height=comp.maxiopmos_w,
            bottom=active, bottom_implant=iopimplant, bottom_well=nwell,
        )
        _obuf_chiovdd_actbounds = _obuf_chiovdd_lay.bounds(mask=active.mask)
        obuf_chiovdd_x = active_left - _obuf_chiovdd_actbounds.left
        obuf_chiovdd_y = comp.maxiopmos_y
        obuf_chiovdd_lay = layouter.place(
            object_=_obuf_chiovdd_lay, x=obuf_chiovdd_x, y=obuf_chiovdd_y,
        )
        obuf_chiovdd_chbounds = obuf_chiovdd_lay.bounds(mask=contact.mask)
        obuf_chiovdd_m1bounds = obuf_chiovdd_lay.bounds(mask=metal1.mask)
        layouter.add_wire(net=nets.iovdd, wire=metal1, shape=_geo.Rect.from_rect(
            rect=obuf_chiovdd_m1bounds, bottom=0.0,
        ))

        poly_left = max(
            obuf_chiovss_chbounds.right + spec.ionmos.computed.min_contactgate_space,
            obuf_chiovdd_chbounds.right + spec.iopmos.computed.min_contactgate_space,
        )

        # Output buffer ionmos+iopmos
        x = obuf_chiovss_m1bounds.center.x + max(
            comp.minionmos_contactgatepitch,
            comp.miniopmos_contactgatepitch,
        )
        _n_obuf_lay = layouter.inst_layout(inst=insts.n_lvld_n_inv)
        _n_obuf_polybounds = _n_obuf_lay.bounds(mask=poly.mask)
        n_obuf_x = poly_left - _n_obuf_polybounds.left
        n_obuf_y = comp.maxionmos_y
        n_obuf_lay = layouter.place(
            object_=_n_obuf_lay, x=n_obuf_x, y=n_obuf_y
        )
        n_obuf_polybounds = n_obuf_lay.bounds(mask=poly.mask)
        n_obuf_nimplbounds = n_obuf_lay.bounds(mask=nimplant.mask)
        _p_obuf_lay = layouter.inst_layout(inst=insts.p_lvld_n_inv)
        _p_obuf_polybounds = _p_obuf_lay.bounds(mask=poly.mask)
        p_obuf_x = poly_left - _p_obuf_polybounds.left
        p_obuf_y = comp.maxiopmos_y
        p_obuf_lay = layouter.place(object_=_p_obuf_lay, x=p_obuf_x, y=p_obuf_y)
        p_obuf_polybounds = p_obuf_lay.bounds(mask=poly.mask)
        p_obuf_pimplbounds = p_obuf_lay.bounds(mask=pimplant.mask)
        layouter.add_wire(net=nets.lvld_n, wire=poly, shape=_geo.Rect.from_rect(
            rect=n_obuf_polybounds, bottom=p_obuf_polybounds.top,
        ))

        # poly pad
        _obuf_ppad_lay = layouter.wire_layout(
            net=nets.lvld_n, wire=contact, bottom=poly,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _obuf_ppad_polybounds = _obuf_ppad_lay.bounds(mask=poly.mask)
        obuf_ppad_x = min(
            n_obuf_polybounds.left - _obuf_ppad_polybounds.left,
            n_obuf_polybounds.right - _obuf_ppad_polybounds.right,
        )
        obuf_ppad_y = tech.on_grid(0.5*(n_obuf_polybounds.bottom + p_obuf_polybounds.top))
        obuf_ppad_lay = layouter.place(object_=_obuf_ppad_lay, x=obuf_ppad_x, y=obuf_ppad_y)
        obuf_ppad_m1bounds = obuf_ppad_lay.bounds(mask=metal1.mask)
        layouter.add_wire(net=nets.lvld_n, wire=metal1, shape=_geo.Rect.from_rect(
            rect=obuf_ppad_m1bounds, left=nch_lvld_n_m1bounds.left,
        ))

        # Place right source-drain contacts
        _nch_o_lay = layouter.wire_layout(
            net=nets.o, wire=contact, bottom_height=comp.maxionmos_w,
            bottom=active, bottom_implant=ionimplant,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _nch_o_chbounds = _nch_o_lay.bounds(mask=contact.mask)
        nch_o_x = (
            n_obuf_polybounds.right + spec.ionmos.computed.min_contactgate_space
            - _nch_o_chbounds.left
        )
        nch_o_y = comp.maxionmos_y
        nch_o_lay = layouter.place(object_=_nch_o_lay, x=nch_o_x, y=nch_o_y)
        nch_o_m1bounds = nch_o_lay.bounds(mask=metal1.mask)
        _pch_o_lay = layouter.wire_layout(
            net=nets.o, well_net=nets.iovdd, wire=contact, bottom_height=comp.maxiopmos_w,
            bottom=active, bottom_implant=iopimplant, bottom_well=nwell,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _pch_o_chbounds = _pch_o_lay.bounds(mask=contact.mask)
        pch_o_x = (
            p_obuf_polybounds.right + spec.iopmos.computed.min_contactgate_space
            - _pch_o_chbounds.left
        )
        pch_o_y = comp.maxiopmos_y
        pch_o_lay = layouter.place(object_=_pch_o_lay, x=pch_o_x, y=pch_o_y)
        pch_o_m1bounds = pch_o_lay.bounds(mask=metal1.mask)
        m1_o_lay = layouter.add_wire(net=nets.o, wire=metal1, shape=_geo.Rect.from_rect(
            rect=nch_o_m1bounds, bottom=pch_o_m1bounds.bottom,
        ))
        m1_o_bounds = m1_o_lay.bounds()
        _via1_o_lay = layouter.wire_layout(
            net=nets.o, wire=via1, bottom_height=m1_o_bounds.height
        )
        _via1_o_m1bounds = _via1_o_lay.bounds(mask=metal1.mask)
        via1_o_x = m1_o_bounds.left - _via1_o_m1bounds.left
        via1_o_y = m1_o_bounds.bottom - _via1_o_m1bounds.bottom
        via1_o_lay = layouter.place(object_=_via1_o_lay, x=via1_o_x, y=via1_o_y)
        via1_o_m2bounds = via1_o_lay.bounds(mask=metal2.mask)
        layouter.add_wire(net=nets.o, wire=metal2, **pin_args, shape=via1_o_m2bounds)

        cells_right = layout.bounds(mask=active.mask).right + 0.5*comp.min_oxactive_space

        # fill implants
        layouter.add_portless(
            prim=nimplant, shape=_geo.Rect(
                left=0.0, bottom=n_obuf_nimplbounds.bottom,
                right=cells_right, top=n_obuf_nimplbounds.top,
            ),
        )
        layouter.add_portless(
            prim=pimplant, shape=_geo.Rect(
                left=0.0, bottom=p_obuf_pimplbounds.bottom,
                right=cells_right, top=p_obuf_pimplbounds.top,
            ),
        )

        #
        # Set boundary
        #

        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=cells_right, top=spec.cells_height,
        )

        #
        # Well/bulk contacts
        #

        layouter.add_wire(
            net=nets.iovdd, wire=contact, well_net=nets.iovdd,
            bottom=active, bottom_implant=ionimplant, bottom_well=nwell,
            top_enclosure=comp.chm1_enclosure.wide(),
            x=0.5*cells_right, bottom_width=(cells_right - contact.min_space),
            y=0, bottom_height=comp.minwidth_activewithcontact,
            bottom_enclosure=comp.chact_enclosure.wide(),
        )
        l = layouter.add_wire(
            net=nets.iovdd, wire=active, implant=ionimplant,
            well_net=nets.iovdd, well=nwell,
            x=0.5*cells_right, width=cells_right,
            y=0, height=comp.minwidth_activewithcontact,
        )
        strap_iovdd_nwellbounds = l.bounds(mask=nwell.mask)
        shape = _geo.Rect.from_rect(
            rect=strap_iovdd_nwellbounds, top=spec.iorow_nwell_height,
        )
        layouter.add_wire(net=nets.iovdd, wire=nwell, shape=shape)
        layouter.add_wire(
            net=nets.iovdd, wire=metal1, pin=metal1pin,
            x=0.5*cells_right, width=cells_right,
            y=0, height=comp.metal[1].minwidth_updown,
        )

        layouter.add_wire(
            net=nets.vss, wire=contact, bottom=active,
            bottom_implant=pimplant, top_enclosure=comp.chm1_enclosure.wide(),
            x=0.5*cells_right, bottom_width=(cells_right - contact.min_space),
            y=spec.iorow_height, bottom_height=comp.minwidth_activewithcontact,
            bottom_enclosure=comp.chact_enclosure.wide(),
        )
        layouter.add_wire(
            net=nets.vss, wire=active, implant=pimplant,
            x=0.5*cells_right, width=cells_right,
            y=spec.iorow_height, height=comp.minwidth_activewithcontact,
        )
        layouter.add_wire(
            net=nets.vss, wire=metal1, pin=metal1pin,
            x=0.5*cells_right, width=cells_right,
            y=spec.iorow_height, height=comp.metal[1].minwidth_updown,
        )

        l = layouter.add_wire(
            net=nets.vdd, well_net=nets.vdd, wire=contact, bottom=active,
            bottom_implant=nimplant, bottom_well=nwell,
            top_enclosure=comp.chm1_enclosure.wide(),
            x=0.5*cells_right, bottom_width=(cells_right - contact.min_space),
            y=spec.cells_height, bottom_height=comp.minwidth_activewithcontact,
            bottom_enclosure=comp.chact_enclosure.wide(),
        )
        l = layouter.add_wire(
            net=nets.vdd, well_net=nets.vdd, wire=active,
            implant=nimplant, well=nwell,
            x=0.5*cells_right, width=cells_right,
            y=spec.cells_height, height=comp.minwidth_activewithcontact,
        )
        layouter.add_wire(
            net=nets.vdd, wire=metal1, pin=metal1pin,
            x=0.5*cells_right, width=cells_right,
            y=spec.cells_height, height=comp.metal[1].minwidth_updown,
        )
        strap_vdd_nwellbounds = l.bounds(mask=nwell.mask)
        shape = _geo.Rect.from_rect(
            rect=strap_vdd_nwellbounds,
            bottom=(spec.cells_height - spec.corerow_nwell_height),
        )
        layouter.add_wire(net=nets.vdd, wire=nwell, shape=shape)

        # Thick oxide
        assert comp.ionmos.gate.oxide is not None
        layouter.add_portless(prim=comp.ionmos.gate.oxide, shape=_geo.Rect(
            left=-actox_enc, bottom=comp.io_oxidebottom,
            right=(cells_right + actox_enc), top=comp.io_oxidetop,
        ))


class _LevelDown(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="LevelDown")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        comp = fab.computed

        circuit = self.new_circuit()

        # inverter with 5V gates
        n_hvinv = circuit.instantiate(
            spec.ionmos, name="n_hvinv", w=comp.maxionmoscore_w,
        )
        p_hvinv = circuit.instantiate(
            spec.iopmos, name="p_hvinv", w=comp.maxiopmoscore_w,
        )

        # second inverter, keep same w
        n_lvinv = circuit.instantiate(
            spec.nmos, name="n_lvinv", w=comp.maxnmos_w,
        )
        p_lvinv = circuit.instantiate(
            spec.pmos, name="p_lvinv", w=comp.maxpmos_w,
        )

        prot = circuit.instantiate(fab.get_cell("SecondaryProtection"), name="secondprot")

        # Create the nets
        circuit.new_net(name="vdd", external=True, childports=(
            p_hvinv.ports.sourcedrain1, p_hvinv.ports.bulk,
            p_lvinv.ports.sourcedrain2, p_lvinv.ports.bulk,
        ))
        circuit.new_net(name="vss", external=True, childports=(
            n_hvinv.ports.sourcedrain1, n_hvinv.ports.bulk,
            n_lvinv.ports.sourcedrain2, n_lvinv.ports.bulk,
        ))
        circuit.new_net(name="iovdd", external=True, childports=(
            prot.ports.iovdd,
        ))
        circuit.new_net(name="iovss", external=True, childports=(
            prot.ports.iovss,
        ))
        circuit.new_net(name="pad", external=True, childports=(
            prot.ports.pad,
        ))
        circuit.new_net(name="padres", external=False, childports=(
            prot.ports.core,
            n_hvinv.ports.gate, p_hvinv.ports.gate,
        ))
        circuit.new_net(name="padres_n", external=False, childports=(
            n_hvinv.ports.sourcedrain2, p_hvinv.ports.sourcedrain2,
            n_lvinv.ports.gate, p_lvinv.ports.gate,
        ))
        circuit.new_net(name="core", external=True, childports=(
            n_lvinv.ports.sourcedrain1, p_lvinv.ports.sourcedrain1,
        ))

    def _create_layout(self):
        fab = self.fab
        tech = fab.tech
        spec = fab.spec
        comp = fab.computed

        circuit = self.circuit
        insts = circuit.instances
        nets = circuit.nets

        active = comp.active
        nimplant = comp.nimplant
        ionimplant = comp.ionimplant
        pimplant = comp.pimplant
        oxide = comp.oxide
        nwell = comp.nwell
        poly = comp.poly
        metal1 = comp.metal[1].prim
        metal1pin = metal1.pin[0]
        metal2 = comp.metal[2].prim
        metal2pin = metal2.pin[0]

        contact = comp.contact
        chm1_enclosure = contact.min_top_enclosure[0]
        via1 = comp.vias[1]

        layouter = self.new_circuitlayouter()
        layout = self.layout

        left = 0.5*comp.active.min_space

        # Place instances
        #

        # transistors + contacts
        l = layouter.transistors_layout(trans_specs=(
            _lay.MOSFETInstSpec(
                inst=cast(_ckt._PrimitiveInstance, insts.n_lvinv),
                contact_left=contact, contact_right=contact,
            ),
        ))
        act_left = l.bounds(mask=active.mask).left
        l_n_lvinv = layouter.place(l, x=(left - act_left), y=comp.maxnmos_y)

        l = layouter.transistors_layout(trans_specs=(
            _lay.MOSFETInstSpec(
                inst=cast(_ckt._PrimitiveInstance, insts.p_lvinv),
                contact_left=contact, contact_right=contact,
            ),
        ))
        act_left = l.bounds(mask=active.mask).left
        l_p_lvinv = layouter.place(l, x=(left - act_left), y=comp.maxpmos_y)

        rect1 = l_n_lvinv.bounds(mask=active.mask)
        rect2 = l_p_lvinv.bounds(mask=active.mask)
        ox_left = (
            max(rect1.right, rect2.right)
            + tech.computed.min_space(oxide, active)
        )

        l = layouter.transistors_layout(trans_specs=(
            _lay.MOSFETInstSpec(
                inst=cast(_ckt._PrimitiveInstance, insts.n_hvinv),
                contact_left=contact, contact_right=contact,
            ),
        ))
        ox_left2 = l.bounds(mask=oxide.mask).left
        l_n_hvinv = layouter.place(l, x=(ox_left - ox_left2), y=comp.maxionmoscore_y)

        l = layouter.transistors_layout(trans_specs=(
            _lay.MOSFETInstSpec(
                inst=cast(_ckt._PrimitiveInstance, insts.p_hvinv),
                contact_left=contact, contact_right=contact,
            ),
        ))
        ox_left2 = l.bounds(mask=oxide.mask).left
        l_p_hvinv = layouter.place(l, x=(ox_left - ox_left2), y=comp.maxiopmoscore_y)

        # secondary protection
        l = layouter.inst_layout(inst=insts.secondprot)
        _actvdd_bounds = l.bounds(net=nets.iovdd, mask=active.mask)
        l_prot = layouter.place(
            l, x=0,
            y=(-_actvdd_bounds.top + 0.5*comp.minwidth_activewithcontact),
        )

        # Cell boundary
        #
        secprot = fab.get_cell("SecondaryProtection")
        assert secprot.layout.boundary is not None
        cell_width = tech.on_grid(
            max(
                layout.bounds(mask=active.mask).right + 0.5*active.min_space,
                secprot.layout.boundary.right,
            ),
            mult=2, rounding="ceiling",
        )
        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=cell_width, top=spec.cells_height,
        )
        x_mid = 0.5*cell_width

        # Connect nets
        #

        # core
        net = nets.core # Output of lv inverter
        rect1 = l_n_lvinv.bounds(mask=metal1.mask, net=net)
        rect2 = l_p_lvinv.bounds(mask=metal1.mask, net=net)
        layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=_geo.Rect(
            left=min(rect1.left, rect2.left), bottom=rect1.bottom,
            right=max(rect1.right, rect2.right), top=rect2.top,
        ))

        # pad
        net = nets.pad
        rect = l_prot.bounds(net=net, mask=metal2pin.mask)
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=rect)

        # padres
        net = nets.padres
        rect1 = l_n_hvinv.bounds(mask=poly.mask)
        rect2 = l_p_hvinv.bounds(mask=poly.mask)
        assert rect1.top < rect2.bottom
        layouter.add_wire(wire=poly, net=nets.padres, shape=_geo.Rect(
            left=min(rect1.left, rect2.left), bottom=rect1.top,
            right=max(rect1.right, rect2.right), top=rect2.bottom,
        ))
        l = layouter.wire_layout(
            net=net, wire=contact, bottom=poly, top_enclosure=chm1_enclosure.wide(),
        )
        rect3 = l.bounds(mask=poly.mask)
        x = max(rect1.right, rect2.right) - rect3.right
        y = tech.on_grid(0.5*(rect1.top + rect2.bottom))
        l_hv_ch = layouter.place(l, x=x, y=y)

        # y = y
        l = layouter.wire_layout(net=net, wire=via1)
        rect1 = l_hv_ch.bounds(mask=metal1.mask)
        rect2 = l.bounds(mask=metal1.mask)
        x = rect1.left - rect2.left
        l_hv_via1 = layouter.place(l, x=x, y=y)

        rect1 = l_hv_via1.bounds(mask=metal2.mask)
        rect2 = l_prot.bounds(net=net, mask=metal2pin.mask)
        assert rect1.left >= rect2.left
        l_m2_padres = layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
            rect=rect1, bottom=rect2.top,
        ))

        # padres_n
        net = nets.padres_n # Output of hv inverter
        rect1 = l_n_lvinv.bounds(mask=poly.mask)
        rect2 = l_p_lvinv.bounds(mask=poly.mask)
        assert rect1.top < rect2.bottom
        layouter.add_wire(wire=poly, net=nets.padres_n, shape=_geo.Rect(
            left=min(rect1.left, rect2.left), bottom=rect1.top,
            right=max(rect1.right, rect2.right), top=rect2.bottom,
        ))
        l = layouter.wire_layout(
            net=net, wire=contact, bottom=poly, top_enclosure=chm1_enclosure.wide(),
        )
        rect3 = l.bounds(mask=poly.mask)
        x = max(rect1.right, rect2.right) - rect3.left
        y = tech.on_grid(0.5*(rect1.top + rect2.bottom))
        l_lv_ch = layouter.place(object_=l, x=x, y=y)

        rect1 = l_lv_ch.bounds(mask=metal1.mask)
        l = layouter.wire_layout(net=net, wire=via1)
        rect2 = l.bounds(mask=metal1.mask)
        x = rect1.left - rect2.left
        # y = y
        l_lv_via1 = layouter.place(l, x=x, y=y)

        rect1 = l_n_hvinv.bounds(mask=metal1.mask, net=net)
        rect2 = l_p_hvinv.bounds(mask=metal1.mask, net=net)
        left = min(rect1.right, rect2.right)
        right = left + metal1.min_space
        bottom = rect1.bottom
        top = rect2.top
        l_hv_m1 = layouter.add_wire(net=net, wire=metal1, shape=_geo.Rect(
            left=left, bottom=bottom, right=right, top=top,
        ))

        m1rect1 = l_hv_m1.bounds(mask=metal1.mask)
        m2rect1 = l_lv_via1.bounds(mask=metal2.mask)
        m2rect2 = l_m2_padres.bounds(mask=metal2.mask)
        l = layouter.wire_layout(net=net, wire=via1)
        m1rect2 = l.bounds(mask=metal1.mask)
        m2rect3 = l.bounds(mask=metal2.mask)
        x = m1rect1.right - m1rect2.right
        y = (m2rect2.top + metal2.min_space) - m2rect3.bottom
        l_hv_via1 = layouter.place(l, x=x, y=y)
        m2rect3 = l_hv_via1.bounds(mask=metal2.mask)
        layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
            rect=m2rect1, top=m2rect3.top,
        ))
        layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
            rect=m2rect3, left=m2rect1.left,
        ))

        # vss
        net = nets.vss
        layouter.add_wire(
            net=net, wire=contact, bottom=active,
            bottom_implant=pimplant, top_enclosure=comp.chm1_enclosure.wide(),
            x=x_mid, bottom_width=(cell_width - contact.min_space),
            y=spec.iorow_height, bottom_height=comp.minwidth_activewithcontact,
            bottom_enclosure=comp.chact_enclosure.wide(),
        )
        layouter.add_wire(
            net=net, wire=active, implant=pimplant,
            x=x_mid, width=cell_width,
            y=spec.iorow_height, height=comp.minwidth_activewithcontact,
        )
        layouter.add_wire(
            net=net, wire=metal1, pin=metal1pin,
            x=x_mid, width=cell_width,
            y=spec.iorow_height, height=comp.metal[1].minwidth_updown,
        )

        rect1 = l_n_lvinv.bounds(net=net, mask=metal1.mask)
        rect2 = l_n_hvinv.bounds(net=net, mask=metal1.mask)
        layouter.add_wire(net=net, wire=metal1, shape=_geo.Rect(
            left=rect1.left, bottom=spec.iorow_height,
            right=rect2.right, top=min(rect1.top, rect2.top),
        ))

        # vdd
        net = nets.vdd
        l = layouter.add_wire(
            net=net, well_net=net, wire=contact, bottom=active,
            bottom_implant=nimplant, bottom_well=nwell,
            top_enclosure=comp.chm1_enclosure.wide(),
            x=x_mid, bottom_width=(cell_width - contact.min_space),
            y=spec.cells_height, bottom_height=comp.minwidth_activewithcontact,
            bottom_enclosure=comp.chact_enclosure.wide(),
        )
        l = layouter.add_wire(
            net=net, well_net=net, wire=active,
            implant=nimplant, well=nwell,
            x=x_mid, width=cell_width,
            y=spec.cells_height, height=comp.minwidth_activewithcontact,
        )
        layouter.add_wire(
            net=net, wire=metal1, pin=metal1pin,
            x=x_mid, width=cell_width,
            y=spec.cells_height, height=comp.metal[1].minwidth_updown,
        )
        strap_vdd_nwellbounds = l.bounds(mask=nwell.mask)
        shape = _geo.Rect.from_rect(
            rect=strap_vdd_nwellbounds,
            bottom=(spec.cells_height - spec.corerow_nwell_height),
        )
        layouter.add_wire(net=net, wire=nwell, shape=shape)

        rect1 = l_p_lvinv.bounds(net=net, mask=metal1.mask)
        rect2 = l_p_hvinv.bounds(net=net, mask=metal1.mask)
        layouter.add_wire(net=net, wire=metal1, shape=_geo.Rect(
            left=rect1.left, bottom=max(rect1.bottom, rect2.bottom),
            right=rect2.right, top=spec.cells_height,
        ))

        # iovss
        net = nets.iovss
        rect = l_prot.bounds(net=net, mask=metal2pin.mask)
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=rect)

        # iovdd
        layouter.add_wire(
            net=nets.iovdd, wire=metal1, pin=metal1pin,
            x=x_mid, width=cell_width,
            y=0, height=comp.metal[1].minwidth_updown,
        )

        # Netless polygons
        #

        # Join transistor implant layers
        n_lvinv_implbounds = l_n_lvinv.bounds(mask=nimplant.mask)
        n_hvinv_implbounds = l_n_hvinv.bounds(mask=nimplant.mask)
        shape = _geo.Rect.from_rect(rect=n_lvinv_implbounds, right=n_hvinv_implbounds.right)
        layouter.add_portless(prim=nimplant, shape=shape)

        p_lvinv_implbounds = l_p_lvinv.bounds(mask=pimplant.mask)
        p_hvinv_implbounds = l_p_hvinv.bounds(mask=pimplant.mask)
        shape = _geo.Rect.from_rect(rect=p_lvinv_implbounds, right=p_hvinv_implbounds.right)
        layouter.add_portless(prim=pimplant, shape=shape)

        # Join transistor oxide layer
        bounds = layout.bounds(mask=oxide.mask)
        layouter.add_portless(prim=oxide, shape=bounds)


class _BulkConn(_FactoryOnDemandCell):
    def __init__(
        self, *, fab: "IOFactory", name: str,
        cell_width: float, connect_up: bool,
    ):
        super().__init__(fab=fab, name=name)

        self.cell_width = cell_width
        self.connect_up = connect_up

    def _create_circuit(self):
        ckt = self.new_circuit()

        ckt.new_net(name="vdd", external=True)
        ckt.new_net(name="vss", external=True)
        ckt.new_net(name="iovdd", external=True)
        ckt.new_net(name="iovss", external=True)

    def _create_layout(self):
        fab = self.fab
        tech = fab.tech
        spec = fab.spec
        comp = fab.computed
        frame = fab.frame

        cell_width = self.cell_width
        connect_up = self.connect_up

        nets = self.circuit.nets

        active = comp.active
        nimplant = comp.nimplant
        pimplant = comp.pimplant
        nwell = comp.nwell
        contact = comp.contact
        metal1 = comp.metal[1].prim
        metal1pin = metal1.pin[0]
        via1 = comp.vias[1]
        metal2 = comp.metal[2].prim
        via2 = comp.vias[2]
        metal3 = comp.metal[3].prim

        layouter = self.new_circuitlayouter()
        layout = self.layout

        c_leveldown = fab.get_cell("LevelDown")
        ports_leveldown = c_leveldown.circuit.ports
        _l_leveldown = c_leveldown.layout
        ldm1iovddpin_bounds = _l_leveldown.bounds(mask=metal1pin.mask, net=ports_leveldown.iovdd)
        ldm1vsspin_bounds = _l_leveldown.bounds(mask=metal1pin.mask, net=ports_leveldown.vss)
        ldm1vddpin_bounds = _l_leveldown.bounds(mask=metal1pin.mask, net=ports_leveldown.vdd)
        ldact_bounds = _l_leveldown.bounds(mask=active.mask)
        ldm1_bounds = _l_leveldown.bounds(mask=metal1.mask)

        c_pclamp = fab.clamp(type_="p", n_trans=spec.clampcount, n_drive=spec.clampdrive)
        _l_pclamp = c_pclamp.layout
        clact_bounds = _l_pclamp.bounds(mask=active.mask)
        clm1_bounds = _l_pclamp.bounds(mask=metal1.mask)
        clm3_bounds = _l_pclamp.bounds(mask=metal3.mask)

        # iovdd
        net = nets.iovdd
        _l_ch = layouter.fab.layout_primitive(
            prim=contact, portnets={"conn": net},
            bottom=active, bottom_implant=nimplant, bottom_well=nwell,
            columns=8, bottom_enclosure="wide", top_enclosure="wide",
        )
        _act_bounds = _l_ch.bounds(mask=active.mask)
        _nwell_bounds = _l_ch.bounds(mask=nwell.mask)
        y = ldm1iovddpin_bounds.center.y
        x = 0.5*cell_width
        layouter.add_wire(
            net=net, wire=active, implant=nimplant, well=nwell, well_net=net,
            x=x, width=cell_width, y=y, height=_act_bounds.height,
        )
        if _nwell_bounds.height < (nwell.min_width - 0.5*tech.grid):
            enc = _act_bounds.left - _nwell_bounds.left
            shape = _geo.Rect(
                left=-enc, bottom=(y - 0.5*nwell.min_width),
                right=(cell_width + enc),
                top=(y + 0.5*nwell.min_width),
            )
            layouter.add_wire(wire=nwell, net=net, shape=shape)
        if connect_up:
            x = -_act_bounds.left + contact.min_space
            layouter.place(_l_ch, x=x, y=y)
            x = cell_width - x
            layouter.place(_l_ch, x=x, y=y)

            x = 0.5*cell_width
            layouter.add_wire(
                net=net, wire=metal1, pin=metal1pin,
                x=x, width=cell_width, y=y, height=ldm1iovddpin_bounds.height,
            )

            _l_via = layouter.fab.layout_primitive(
                prim=via1, portnets={"conn": net}, columns=2,
            )
            _m2_bounds = _l_via.bounds(mask=metal2.mask)
            x = cell_width - _m2_bounds.right - metal2.min_space
            l = layouter.place(_l_via, x=x, y=y)
            m2_bounds1 = l.bounds(mask=metal2.mask)
            _l_via = layouter.fab.layout_primitive(
                prim=via2, portnets={"conn": net}, columns=2,
            )
            _m2_bounds = _l_via.bounds(mask=metal2.mask)
            y = frame.iovdd_bottom + clm3_bounds.top - _m2_bounds.top - frame.cells_y
            l = layouter.place(_l_via, x=x, y=y)
            m2_bounds2 = l.bounds(mask=metal2.mask)
            shape = _geo.Rect.from_rect(rect=m2_bounds2, top=m2_bounds1.top)
            layouter.add_wire(wire=metal2, net=net, shape=shape)

        # vss
        net = nets.vss
        _l_ch = layouter.fab.layout_primitive(
            prim=contact, portnets={"conn": net},
            bottom=active, bottom_implant=pimplant,
            columns=8, bottom_enclosure="wide", top_enclosure="wide",
        )
        _act_bounds = _l_ch.bounds(mask=active.mask)
        y = ldm1vsspin_bounds.center.y

        x = 0.5*cell_width
        layouter.add_wire(
            net=net, wire=active, implant=pimplant,
            x=x, width=cell_width, y=y, height=_act_bounds.height,
        )
        if connect_up:
            x = -_act_bounds.left + contact.min_space
            layouter.place(_l_ch, x=x, y=y)
            x = cell_width - _act_bounds.right - contact.min_space
            layouter.place(_l_ch, x=x, y=y)
            x = 0.5*cell_width
            layouter.add_wire(
                net=net, wire=metal1, pin=metal1pin,
                x=x, width=cell_width, y=y, height=ldm1vsspin_bounds.height,
            )
            _l_via = layouter.fab.layout_primitive(
                prim=via1, portnets={"conn": net}, columns=8,
            )
            _m2_bounds = _l_via.bounds(mask=metal2.mask)
            x = -_m2_bounds.left + metal2.min_space
            layouter.place(_l_via, x=x, y=y)
            x = cell_width -_m2_bounds.right - metal2.min_space
            layouter.place(_l_via, x=x, y=y)
            _l_via = layouter.fab.layout_primitive(
                prim=via2, portnets={"conn": net}, columns=8,
            )
            _m3_bounds = _l_via.bounds(mask=metal3.mask)
            x = -_m3_bounds.left + metal3.min_space
            layouter.place(_l_via, x=x, y=y)
            x = cell_width - x
            layouter.place(_l_via, x=x, y=y)

        # vdd
        net = nets.vdd
        _l_ch = layouter.fab.layout_primitive(
            prim=contact, portnets={"conn": net},
            bottom=active, bottom_implant=nimplant, bottom_well=nwell,
            columns=8, bottom_enclosure="wide", top_enclosure="wide",
        )
        _act_bounds = _l_ch.bounds(mask=active.mask)
        _nwell_bounds = _l_ch.bounds(mask=nwell.mask)
        y = ldm1vddpin_bounds.center.y

        x = 0.5*cell_width
        layouter.add_wire(
            net=net, wire=active, implant=nimplant, well=nwell, well_net=net,
            x=x, width=cell_width, y=y, height=_act_bounds.height,
        )
        if _nwell_bounds.height < (nwell.min_width - 0.5*tech.grid):
            enc = (_act_bounds.left - _nwell_bounds.left)
            shape = _geo.Rect(
                left=-enc, bottom=(y - 0.5*nwell.min_width),
                right=(cell_width + enc),
                top=(y + 0.5*nwell.min_width),
            )
            layouter.add_wire(wire=nwell, net=net, shape=shape)
        if connect_up:
            x = -_act_bounds.left + contact.min_space
            layouter.place(_l_ch, x=x, y=y)
            x = cell_width - _act_bounds.right- contact.min_space
            layouter.place(_l_ch, x=x, y=y)
            x = 0.5*cell_width
            layouter.add_wire(
                net=net, wire=metal1, pin=metal1pin,
                x=x, width=cell_width, y=y, height=ldm1vddpin_bounds.height,
            )
            _l_via = layouter.fab.layout_primitive(
                prim=via1, portnets={"conn": net}, columns=8,
            )
            _m2_bounds = _l_via.bounds(mask=metal2.mask)
            x = -_m2_bounds.left + metal2.min_space
            layouter.place(_l_via, x=x, y=y)
            x = cell_width -_m2_bounds.right - metal2.min_space
            layouter.place(_l_via, x=x, y=y)
            _l_via = layouter.fab.layout_primitive(
                prim=via2, portnets={"conn": net}, columns=8,
            )
            _m3_bounds = _l_via.bounds(mask=metal3.mask)
            x = -_m3_bounds.left + metal3.min_space
            layouter.place(_l_via, x=x, y=y)
            x = cell_width - x
            layouter.place(_l_via, x=x, y=y)

        # iovss
        net = nets.iovss
        left = 0.0
        right = cell_width
        act_bottom = frame.iovdd_bottom + clact_bounds.top - frame.cells_y
        m1_bottom = frame.iovdd_bottom + clm1_bounds.top - frame.cells_y
        act_top = ldact_bounds.bottom
        m1_top = ldm1_bounds.bottom

        shape = _geo.Rect(
            left=left, bottom=act_bottom, right=right, top=act_top,
        )
        layouter.add_wire(net=net, wire=active, implant=pimplant, shape=shape)
        if connect_up:
            bottom_shape = _geo.Rect(
                left=(left + contact.min_space),
                right=(right - contact.min_space),
                bottom=(act_bottom + contact.min_space),
                top=(act_top - contact.min_space),
            )
            xy = tech.on_grid(bottom_shape.center)
            w = tech.on_grid(bottom_shape.width, mult=2, rounding="floor")
            h = tech.on_grid(bottom_shape.height, mult=2, rounding="floor")
            layouter.add_wire(
                net=net, wire=contact, bottom=active, bottom_implant=pimplant,
                origin=xy, space=2*contact.min_space,
                bottom_width=w, bottom_height=h,
            )
            shape = _geo.Rect(
                left=left, bottom=m1_bottom, right=right, top=m1_top,
            )
            layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=shape)
            y = frame.secondiovss_bottom + 0.5*frame.secondiovss_width - frame.cells_y
            layouter.add_wire(
                net=net, wire=via1, x=4, bottom_width=5.0, y=y, bottom_height=10.0,
            )
            layouter.add_wire(
                net=net, wire=via1, x=(cell_width - 4.5), bottom_width=5.0,
                y=y, bottom_height=10.0,
            )
            layouter.add_wire(
                net=net, wire=via2, x=4, bottom_width=5.0, y=y, bottom_height=10.0,
            )
            layouter.add_wire(
                net=net, wire=via2, x=(cell_width - 4.5), bottom_width=5.0,
                y=y, bottom_height=10.0,
            )

        bb = layout.bounds()
        layout.boundary = _geo.Rect(
            left=0.0, bottom=bb.bottom, right=cell_width, top=bb.top,
        )


class _GateLevelUp(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="GateLevelUp")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        stdcells = spec.stdcelllib.cells

        levelup = fab.get_cell("LevelUp")

        ckt = self.new_circuit()

        ngatelu = ckt.instantiate(levelup, name="ngate_levelup")
        pgatelu = ckt.instantiate(levelup, name="pgate_levelup")

        ckt.new_net(name="vdd", external=True, childports=(
            ngatelu.ports.vdd, pgatelu.ports.vdd,
        ))
        ckt.new_net(name="vss", external=True, childports=(
            ngatelu.ports.vss, pgatelu.ports.vss,
        ))
        ckt.new_net(name="iovdd", external=True, childports=(
            ngatelu.ports.iovdd, pgatelu.ports.iovdd,
        ))

        ckt.new_net(name="d", external=True, childports=(
            ngatelu.ports.i, pgatelu.ports.i,
        ))
        ckt.new_net(name="ngate", external=True, childports=(ngatelu.ports.o))
        ckt.new_net(name="pgate", external=True, childports=(pgatelu.ports.o))

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        stdcells = spec.stdcelllib.cells
        comp = fab.computed

        insts = self.circuit.instances
        nets = self.circuit.nets

        levelup = fab.get_cell("LevelUp")
        assert levelup.layout.boundary is not None

        via1 = comp.vias[1]
        metal1 = comp.metal[1].prim
        metal1pin = metal1.pin[0]
        metal2 = comp.metal[2].prim
        metal2pin = metal2.pin[0]
        metal2_pitch = comp.metal[2].minwidth4ext_updown + 2*metal2.min_space

        layouter = self.new_circuitlayouter()
        fab = layouter.fab
        layout = self.layout

        # Place the cells
        x_lu = 0.0
        y_lu = -levelup.layout.boundary.top - spec.levelup_core_space
        l_ngatelu = layouter.place(insts.ngate_levelup, x=x_lu, y=y_lu)
        ngatelu_d_m2pinbounds = l_ngatelu.bounds(mask=metal2pin.mask, net=nets.d)
        ngatelu_ngate_m2pinbounds = l_ngatelu.bounds(mask=metal2pin.mask, net=nets.ngate)
        ngatelu_bb = l_ngatelu.boundary
        assert ngatelu_bb is not None

        x_lu = ngatelu_bb.right
        l_pgatelu = layouter.place(insts.pgate_levelup, x=x_lu, y=y_lu)
        pgatelu_d_m2pinbounds = l_pgatelu.bounds(mask=metal2pin.mask, net=nets.d)
        pgatelu_pgate_m2pinbounds = l_pgatelu.bounds(mask=metal2pin.mask, net=nets.pgate)
        pgatelu_bb = l_pgatelu.boundary
        assert pgatelu_bb is not None

        # Set the boundary
        cell_bb = _geo.Rect.from_rect(rect=ngatelu_bb, right=pgatelu_bb.right)
        layout.boundary = cell_bb

        # Connect the nets
        # d
        net = nets.d

        shape = _geo.Rect.from_rect(rect=ngatelu_d_m2pinbounds, top=cell_bb.top)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(rect=pgatelu_d_m2pinbounds, top=cell_bb.top)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect(
            left=ngatelu_d_m2pinbounds.left, bottom=cell_bb.top,
            right=pgatelu_d_m2pinbounds.right, top=(cell_bb.top + 2*metal2.min_width),
        )
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

        # ngate
        net = nets.ngate
        layouter.add_wire(
            net=net, wire=metal2, pin=metal2pin, shape=ngatelu_ngate_m2pinbounds,
        )

        # pgate
        net = nets.pgate
        layouter.add_wire(
            net=net, wire=metal2, pin=metal2pin, shape=pgatelu_pgate_m2pinbounds,
        )

        # vss
        net = nets.vss
        m1pin_bounds = l_ngatelu.bounds(net=net, mask=metal1pin.mask)
        shape = _geo.Rect.from_rect(
            rect=m1pin_bounds, left=cell_bb.left, right=cell_bb.right,
        )
        layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=shape)

        # vdd
        net = nets.vdd
        m1pin_bounds = l_ngatelu.bounds(net=net, mask=metal1pin.mask)
        shape = _geo.Rect.from_rect(
            rect=m1pin_bounds, left=cell_bb.left, right=cell_bb.right,
        )
        layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=shape)

        # iovdd
        net = nets.iovdd
        m1pin_bounds = l_ngatelu.bounds(net=net, mask=metal1pin.mask)
        shape = _geo.Rect.from_rect(
            rect=m1pin_bounds, left=cell_bb.left, right=cell_bb.right,
        )
        layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=shape)


class _GateDecode(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="GateDecode")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        stdcells = spec.stdcelllib.cells

        inv = stdcells.inv_x1
        nand = stdcells.nand2_x0
        nor = stdcells.nor2_x0
        levelup = fab.get_cell("LevelUp")

        ckt = self.new_circuit()

        oeinv = ckt.instantiate(inv, name="oe_inv")
        ngatenor = ckt.instantiate(nor, name="ngate_nor")
        ngatelu = ckt.instantiate(levelup, name="ngate_levelup")
        pgatenand = ckt.instantiate(nand, name="pgate_nand")
        pgatelu = ckt.instantiate(levelup, name="pgate_levelup")

        ckt.new_net(name="vdd", external=True, childports=(
            oeinv.ports.vdd, ngatenor.ports.vdd, ngatelu.ports.vdd,
            pgatenand.ports.vdd, pgatelu.ports.vdd,
        ))
        ckt.new_net(name="vss", external=True, childports=(
            oeinv.ports.vss, ngatenor.ports.vss, ngatelu.ports.vss,
            pgatenand.ports.vss, pgatelu.ports.vss,
        ))
        ckt.new_net(name="iovdd", external=True, childports=(
            ngatelu.ports.iovdd, pgatelu.ports.iovdd,
        ))

        ckt.new_net(name="d", external=True, childports=(
            ngatenor.ports.i0, pgatenand.ports.i0,
        ))
        ckt.new_net(name="de", external=True, childports=(
            oeinv.ports.i, pgatenand.ports.i1,
        ))
        ckt.new_net(name="de_n", external=False, childports=(
            oeinv.ports.nq, ngatenor.ports.i1,
        ))
        ckt.new_net(name="ngate_core", external=False, childports=(
            ngatenor.ports.nq, ngatelu.ports.i,
        ))
        ckt.new_net(name="ngate", external=True, childports=(ngatelu.ports.o))
        ckt.new_net(name="pgate_core", external=False, childports=(
            pgatenand.ports.nq, pgatelu.ports.i,
        ))
        ckt.new_net(name="pgate", external=True, childports=(pgatelu.ports.o))

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        stdcells = spec.stdcelllib.cells
        comp = fab.computed

        insts = self.circuit.instances
        nets = self.circuit.nets

        tie = stdcells.tie
        assert tie.layout.boundary is not None
        levelup = fab.get_cell("LevelUp")
        assert levelup.layout.boundary is not None
        via1 = comp.vias[1]
        metal1 = comp.metal[1].prim
        metal1pin = metal1.pin[0]
        metal2 = comp.metal[2].prim
        metal2pin = metal2.pin[0]
        metal2_pitch = comp.metal[2].minwidth4ext_updown + 2*metal2.min_space

        layouter = self.new_circuitlayouter()
        fab = layouter.fab
        layout = self.layout

        # Place the cells
        l_ngatenor = layouter.place(insts.ngate_nor, x=0.0, y=0.0)
        assert l_ngatenor.boundary is not None
        ngatenor_d_m1pinbounds = l_ngatenor.bounds(mask=metal1pin.mask, net=nets.d)
        ngatenor_ngatecore_m1pinbounds = l_ngatenor.bounds(
            mask=metal1pin.mask, net=nets.ngate_core,
        )
        ngatenor_den_m1pinbounds = l_ngatenor.bounds(mask=metal1pin.mask, net=nets.de_n)
        l_pgatenand = layouter.place(
            insts.pgate_nand, x=l_ngatenor.boundary.right, y=0.0,
        )
        assert l_pgatenand.boundary is not None
        pgatenand_d_m1pinbounds = l_pgatenand.bounds(mask=metal1pin.mask, net=nets.d)
        pgatenand_pgatecore_m1pinbounds = l_pgatenand.bounds(
            mask=metal1pin.mask, net=nets.pgate_core,
        )
        pgatenand_de_m1pinbounds = l_pgatenand.bounds(mask=metal1pin.mask, net=nets.de)
        l_oeinv = layouter.place(
            insts.oe_inv, x=l_pgatenand.boundary.right, y=0.0,
        )
        assert l_oeinv.boundary is not None
        oeinv_de_m1pinbounds = l_oeinv.bounds(mask=metal1pin.mask, net=nets.de)
        oeinv_den_m1pinbounds = l_oeinv.bounds(mask=metal1pin.mask, net=nets.de_n)

        y_lu = -levelup.layout.boundary.top - spec.levelup_core_space
        l_ngatelu = layouter.place(
            insts.ngate_levelup,
            x=tie.layout.boundary.right, y=y_lu,
        )
        ngatelu_ngatecore_m2pinbounds = l_ngatelu.bounds(mask=metal2pin.mask, net=nets.ngate_core)
        ngatelu_ngate_m2pinbounds = l_ngatelu.bounds(mask=metal2pin.mask, net=nets.ngate)
        assert l_ngatelu.boundary is not None
        l_pgatelu = layouter.place(
            insts.pgate_levelup, x=cast(_geo._Rectangular, l_ngatelu.boundary).right, y=y_lu
        )
        pgatelu_pgatecore_m2pinbounds = l_pgatelu.bounds(mask=metal2pin.mask, net=nets.pgate_core)
        pgatelu_pgate_m2pinbounds = l_pgatelu.bounds(mask=metal2pin.mask, net=nets.pgate)
        assert l_pgatelu.boundary is not None

        # Set the boundary
        cell_left = 0.0
        cell_bottom = l_pgatelu.boundary.bottom
        cell_right = max(l_oeinv.boundary.right, l_pgatelu.boundary.right)
        cell_top = l_oeinv.boundary.top
        layout.boundary = _geo.Rect(
            left=cell_left, bottom=cell_bottom, right=cell_right, top=cell_top,
        )

        # Connect the nets
        # de
        net = nets.de
        _l_via = layouter.wire_layout(
            net=net, wire=via1, bottom_enclosure="tall", top_enclosure="tall",
        )
        _m1bounds = _l_via.bounds(mask=metal1.mask)
        y = (
            min(pgatenand_de_m1pinbounds.top, oeinv_de_m1pinbounds.top)
            - _m1bounds.top
        )
        l_via_pgatenand_de = layouter.place(
            object_=_l_via, x=pgatenand_de_m1pinbounds.center.x, y=y,
        )
        via_pgatenand_de_m2bounds = l_via_pgatenand_de.bounds(mask=metal2.mask)
        l_via_oeinv_de = layouter.place(
            object_=_l_via, x=oeinv_de_m1pinbounds.center.x, y=y,
        )
        via_oeinv_de_m2bounds = l_via_oeinv_de.bounds(mask=metal2.mask)

        layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
            rect=via_pgatenand_de_m2bounds, right=via_oeinv_de_m2bounds.right,
        ))
        shape = _geo.Rect(
            left=via_pgatenand_de_m2bounds.left,
            bottom=via_pgatenand_de_m2bounds.bottom,
            right=via_pgatenand_de_m2bounds.left + comp.metal[2].minwidth4ext_updown,
            top=l_oeinv.boundary.top,
        )
        layouter.add_wire(net=net, wire=metal2, pin=metal2.pin[0], shape=shape)

        # d
        net = nets.d
        _l_via = layouter.wire_layout(
            net=net, wire=via1, bottom_enclosure="tall", top_enclosure="tall",
        )
        _m1bounds = _l_via.bounds(mask=metal1.mask)
        _m2bounds = _l_via.bounds(mask=metal2.mask)
        y = min(
            (
                min(via_pgatenand_de_m2bounds.bottom, via_oeinv_de_m2bounds.bottom)
                - metal2.min_space
                - _m2bounds.top
            ),
            (
                min(ngatenor_d_m1pinbounds.top, pgatenand_d_m1pinbounds.top)
                - _m1bounds.top
            ),
        )
        l_via_ngatenor_d = layouter.place(
            object_=_l_via, x=ngatenor_d_m1pinbounds.center.x, y=y,
        )
        via_ngatenor_d_m2bounds = l_via_ngatenor_d.bounds(mask=metal2.mask)
        l_via_pgatenand_d = layouter.place(
            object_=_l_via, x=pgatenand_d_m1pinbounds.center.x, y=y,
        )
        via_pgatenand_d_m2bounds = l_via_pgatenand_d.bounds(mask=metal2.mask)

        layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
            rect=via_ngatenor_d_m2bounds, right=via_pgatenand_d_m2bounds.right,
        ))
        shape = _geo.Rect(
            left=via_ngatenor_d_m2bounds.left,
            bottom=via_pgatenand_d_m2bounds.bottom,
            right=via_ngatenor_d_m2bounds.left + comp.metal[2].minwidth4ext_updown,
            top=l_oeinv.boundary.top,
        )
        layouter.add_wire(net=net, wire=metal2, pin=metal2.pin[0], shape=shape)

        # de_n
        net = nets.de_n
        _l_via = layouter.wire_layout(
            net=net, wire=via1, bottom_enclosure="tall", top_enclosure="tall",
        )
        _m1bounds = _l_via.bounds(mask=metal1.mask)
        _m2bounds = _l_via.bounds(mask=metal2.mask)
        y = min(
            (
                min(via_ngatenor_d_m2bounds.bottom, via_pgatenand_d_m2bounds.bottom)
                - metal2.min_space
                - _m2bounds.top
            ),
            (
                min(ngatenor_den_m1pinbounds.top, oeinv_den_m1pinbounds.top)
                - _m1bounds.top
            ),
        )
        l_via_ngatenor_den = layouter.place(
            object_=_l_via, x=ngatenor_den_m1pinbounds.center.x, y=y,
        )
        via_ngatenor_den_m2bounds = l_via_ngatenor_den.bounds(mask=metal2.mask)
        l_via_oeinv_den = layouter.place(
            object_=_l_via, x=oeinv_den_m1pinbounds.center.x, y=y,
        )
        via_oeinv_den_m2bounds = l_via_oeinv_den.bounds(mask=metal2.mask)

        layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
            rect=via_ngatenor_den_m2bounds, right=via_oeinv_den_m2bounds.right,
        ))

        # ngate_core
        net = nets.ngate_core
        _l_via = layouter.wire_layout(
            net=net, wire=via1, bottom_enclosure="tall", top_enclosure="tall",
        )
        _m1bounds = _l_via.bounds(mask=metal1.mask)
        _m2bounds = _l_via.bounds(mask=metal2.mask)
        x = ngatenor_ngatecore_m1pinbounds.left - _m1bounds.left
        y = ngatenor_ngatecore_m1pinbounds.bottom - _m1bounds.bottom
        l_via = layouter.place(object_=_l_via, x=x, y=y)
        m2bounds = l_via.bounds(mask=metal2.mask)
        layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
            rect=ngatelu_ngatecore_m2pinbounds, top=m2bounds.top,
        ))
        if m2bounds.left < ngatelu_ngatecore_m2pinbounds.left:
            layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
                rect=m2bounds, right=ngatelu_ngatecore_m2pinbounds.right,
            ))
        else:
            layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
                rect=m2bounds, left=ngatelu_ngatecore_m2pinbounds.left,
            ))

        # pgate_core
        net = nets.pgate_core
        _l_via = layouter.wire_layout(
            net=net, wire=via1, bottom_enclosure="tall", top_enclosure="tall",
        )
        _m1bounds = _l_via.bounds(mask=metal1.mask)
        _m2bounds = _l_via.bounds(mask=metal2.mask)
        x = pgatenand_pgatecore_m1pinbounds.left - _m1bounds.left
        y = pgatenand_pgatecore_m1pinbounds.bottom - _m1bounds.bottom
        l_via = layouter.place(object_=_l_via, x=x, y=y)
        m2bounds = l_via.bounds(mask=metal2.mask)
        layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
            rect=pgatelu_pgatecore_m2pinbounds, top=m2bounds.top,
        ))
        if m2bounds.left < pgatelu_pgatecore_m2pinbounds.left:
            layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
                rect=m2bounds, right=pgatelu_pgatecore_m2pinbounds.right,
            ))
        else:
            layouter.add_wire(net=net, wire=metal2, shape=_geo.Rect.from_rect(
                rect=m2bounds, left=pgatelu_pgatecore_m2pinbounds.left,
            ))

        # ngate
        net = nets.ngate
        layouter.add_wire(
            net=net, wire=metal2, pin=metal2pin, shape=ngatelu_ngate_m2pinbounds,
        )

        # pgate
        net = nets.pgate
        layouter.add_wire(
            net=net, wire=metal2, pin=metal2pin, shape=pgatelu_pgate_m2pinbounds,
        )

        # vss
        net = nets.vss
        lum1pin_bounds = l_pgatelu.bounds(mask=metal1pin.mask, net=net)
        invm1pin_bounds = l_oeinv.bounds(mask=metal1pin.mask, net=net)
        x = lum1pin_bounds.right - 0.5*comp.metal[1].minwidth4ext_up
        y = lum1pin_bounds.top
        l_via = layouter.add_wire(net=net, wire=via1, x=x, y=y)
        viam2_bounds1 = l_via.bounds(mask=metal2.mask)
        y = invm1pin_bounds.bottom + 0.5*comp.metal[1].minwidth4ext_up
        l_via = layouter.add_wire(net=net, wire=via1, x=x, y=y)
        viam2_bounds2 = l_via.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=viam2_bounds1, top=viam2_bounds2.top)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=invm1pin_bounds, left=cell_left, right=cell_right,
        )
        layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=shape)

        # vdd
        net = nets.vdd
        m1pin_bounds = l_oeinv.bounds(net=net, mask=metal1pin.mask)
        shape = _geo.Rect.from_rect(
            rect=m1pin_bounds, left=cell_left, right=cell_right,
        )
        layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=shape)
        x = cell_left + 0.5*comp.metal[1].minwidth4ext_up
        y = m1pin_bounds.bottom + 0.5*comp.metal[1].minwidth4ext_up
        l_via = layouter.add_wire(net=net, wire=via1, x=x, y=y)
        viam2_bounds1 = l_via.bounds(mask=metal2.mask)
        m1pin_bounds = l_ngatelu.bounds(net=net, mask=metal1pin.mask)
        y = m1pin_bounds.top - 0.5*comp.metal[1].minwidth4ext_up
        l_via = layouter.add_wire(net=net, wire=via1, x=x, y=y)
        viam2_bounds2 = l_via.bounds(mask=metal2.mask)
        viam1_bounds = l_via.bounds(mask=metal1.mask)
        shape = _geo.Rect.from_rect(rect=viam2_bounds1, bottom=viam2_bounds2.bottom)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(rect=m1pin_bounds, left=viam1_bounds.left)
        layouter.add_wire(net=net, wire=metal1, shape=shape)

        # iovdd
        net = nets.iovdd
        m1pin_bounds = l_ngatelu.bounds(net=net, mask=metal1pin.mask)
        shape = _geo.Rect.from_rect(rect=m1pin_bounds, left=cell_left, right=cell_right)
        layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=shape)


class _PadOut(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="IOPadOut")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        frame = fab.frame

        ckt = self.new_circuit()
        nets = ckt.nets

        frame.add_track_nets(ckt=ckt)
        vss = nets.vss
        vdd = nets.vdd
        iovss = nets.iovss
        iovdd = nets.iovdd

        ckt.new_net(name="d", external=True)
        pad = ckt.new_net(name="pad", external=True)

        ngate = ckt.new_net(name="ngate", external=False)
        pgate = ckt.new_net(name="pgate", external=False)

        frame.add_pad_inst(ckt=ckt, net=pad)

        c_nclamp = fab.clamp(type_="n", n_trans=spec.clampcount, n_drive=spec.clampdrive)
        i_nclamp = ckt.instantiate(c_nclamp, name="nclamp")
        pad.childports += i_nclamp.ports.pad
        iovdd.childports += i_nclamp.ports.iovdd
        iovss.childports += i_nclamp.ports.iovss
        ngate.childports += i_nclamp.ports.gate

        c_pclamp = fab.clamp(type_="p", n_trans=spec.clampcount, n_drive=spec.clampdrive)
        i_pclamp = ckt.instantiate(c_pclamp, name="pclamp")
        pad.childports += i_pclamp.ports.pad
        iovdd.childports += i_pclamp.ports.iovdd
        iovss.childports += i_pclamp.ports.iovss
        pgate.childports += i_pclamp.ports.gate

        frame.add_bulkconn_inst(ckt=ckt, width=spec.iocell_width, connect_up=True)

        i_gatelu = ckt.instantiate(fab.get_cell("GateLevelUp"), name="gatelu")
        for name in ("vss", "vdd", "iovdd", "d", "ngate", "pgate"):
            ckt.nets[name].childports += i_gatelu.ports[name]

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        tech = fab.tech
        frame = fab.frame
        comp = fab.computed

        metal = comp.metal
        metal1 = metal[1].prim
        metal2 = metal[2].prim
        metal2pin = metal2.pin[0]
        metal3 = metal[3].prim
        metal4 = metal[4].prim
        metal5 = metal[5].prim
        metal6 = metal[6].prim
        trackpinmasks = set(m.pin[0].mask for m in (
            metal3, metal4, metal5, metal6,
        ))
        via1 = comp.vias[1]

        def pinpolygons(polygons):
            return filter(lambda p: p.mask in trackpinmasks, polygons)

        ckt = self.circuit
        insts = ckt.instances
        nets = ckt.nets

        layouter = self.new_circuitlayouter()
        layout = self.layout
        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=spec.iocell_width, top=spec.iocell_height,
        )

        frame.draw_tracks(ckt=ckt, layouter=layouter)

        # PAD
        l_pad = frame.place_pad(layouter=layouter, net=nets.pad)
        padm2_bounds = l_pad.bounds(mask=metal2.mask)

        # iovss & iovdd
        l_nclamp = layouter.place(insts.nclamp, x=0.0, y=frame.iovss_bottom)
        for polygon in pinpolygons(l_nclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovss, maskshape=polygon)
        l_pclamp = layouter.place(insts.pclamp, x=0.0, y=frame.iovdd_bottom)
        for polygon in pinpolygons(l_pclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovdd, maskshape=polygon)

        # Connect clamps to pad
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_nclamp.net_polygons(net=nets.pad),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                shape = _geo.Rect.from_rect(rect=bounds, top=padm2_bounds.bottom)
                layouter.add_wire(wire=metal2, net=nets.pad, shape=shape)
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.pad),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                shape = _geo.Rect.from_rect(rect=bounds, bottom=padm2_bounds.top)
                layouter.add_wire(wire=metal2, net=nets.pad, shape=shape)

        # Draw guardring around pad and connect to iovdd track
        bottom = cast(_geo._Rectangular, l_nclamp.boundary).top
        top = cast(_geo._Rectangular, l_pclamp.boundary).bottom - comp.guardring_space
        _l_guardring = hlp.guardring(
            fab=fab, net=nets.iovss, type_="n",
            width=spec.iocell_width, height=(top - bottom),
        )
        l_guardring = layouter.place(
            _l_guardring, x=0.5*spec.iocell_width, y=0.5*(bottom + top),
        )
        guardringm1_bounds = l_guardring.bounds(mask=metal1.mask)
        viatop = guardringm1_bounds.top
        viabottom = viatop - comp.metal[2].minwidth4ext_updown
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.iovdd),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                top_shape = _geo.Rect.from_rect(
                    rect=bounds, bottom=viabottom, top=viatop,
                )
                l_via = layouter.add_wire(
                    net=nets.iovdd, wire=via1, top_shape=top_shape,
                )
                viam2_bounds = l_via.bounds(mask=metal2.mask)
                shape = _geo.Rect.from_rect(rect=bounds, bottom=viam2_bounds.bottom)
                layouter.add_wire(net=nets.iovdd, wire=metal2, shape=shape)

        # Bulk/well connection cell
        frame.place_bulkconn(layouter=layouter)

        # Gate levelup + interconnect
        _l_gatelu = layouter.inst_layout(inst=insts.gatelu)
        _gatelu_bb = _l_gatelu.boundary
        assert _gatelu_bb is not None
        dm2pin_bounds = _l_gatelu.bounds(net=nets.d, mask=metal2pin.mask)
        x = tech.on_grid(
            0.5*spec.iocell_width - 0.5*(dm2pin_bounds.left + dm2pin_bounds.right)
        )
        l_gatelu = layouter.place(
            _l_gatelu, x=x,
            y=(frame.cells_y - _gatelu_bb.bottom),
        )

        # d
        net = nets.d
        m2pin_bounds = l_gatelu.bounds(net=net, mask=metal2pin.mask)
        shape = _geo.Rect.from_rect(rect=m2pin_bounds, top=spec.iocell_height)
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

        net = nets.pgate
        m2pin_bounds1 = l_gatelu.bounds(net=net, mask=metal2pin.mask)
        m2pin_bounds2 = l_pclamp.bounds(net=net, mask=metal2pin.mask)
        m2_width = comp.metal[2].minwidth4ext_updown
        bottom = cast(_geo._Rectangular, l_pclamp.boundary).top + 2*metal2.min_space
        y = bottom + 0.5*m2_width
        shape = _geo.Rect.from_rect(
            rect=m2pin_bounds1, bottom=bottom, top=m2pin_bounds1.bottom,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        top = bottom + m2_width
        shape = _geo.Rect(
            left=m2pin_bounds2.left, bottom=bottom,
            right=m2pin_bounds1.right, top=top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=m2pin_bounds2, bottom=m2pin_bounds2.top, top=top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)

        net = nets.ngate
        m2pin_bounds1 = l_gatelu.bounds(net=net, mask=metal2pin.mask)
        m2pin_bounds2 = l_nclamp.bounds(net=net, mask=metal2pin.mask)
        y += m2_width + 2*metal2.min_space
        bottom = y - 0.5*m2_width
        top = y + 0.5*m2_width
        shape = _geo.Rect.from_rect(
            rect=m2pin_bounds1, bottom=bottom, top=m2pin_bounds1.bottom,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        left = 0.5*spec.metal_bigspace
        shape = _geo.Rect(
            left=left, bottom=bottom, right=m2pin_bounds1.right, top=top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        right = left + m2_width
        bottom = m2pin_bounds2.top - m2_width
        shape = _geo.Rect(left=left, bottom=bottom, right=right, top=top)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect(
            left=left, bottom=bottom, right=m2pin_bounds2.left, top=m2pin_bounds2.top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)


class _PadTriOut(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="IOPadTriOut")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        frame = fab.frame

        ckt = self.new_circuit()
        nets = ckt.nets

        frame.add_track_nets(ckt=ckt)
        vss = nets.vss
        vdd = nets.vdd
        iovss = nets.iovss
        iovdd = nets.iovdd

        ckt.new_net(name="d", external=True)
        ckt.new_net(name="de", external=True)
        pad = ckt.new_net(name="pad", external=True)

        ngate = ckt.new_net(name="ngate", external=False)
        pgate = ckt.new_net(name="pgate", external=False)

        frame.add_pad_inst(ckt=ckt, net=pad)

        c_nclamp = fab.clamp(type_="n", n_trans=spec.clampcount, n_drive=spec.clampdrive)
        i_nclamp = ckt.instantiate(c_nclamp, name="nclamp")
        pad.childports += i_nclamp.ports.pad
        iovdd.childports += i_nclamp.ports.iovdd
        iovss.childports += i_nclamp.ports.iovss
        ngate.childports += i_nclamp.ports.gate

        c_pclamp = fab.clamp(type_="p", n_trans=spec.clampcount, n_drive=spec.clampdrive)
        i_pclamp = ckt.instantiate(c_pclamp, name="pclamp")
        pad.childports += i_pclamp.ports.pad
        iovdd.childports += i_pclamp.ports.iovdd
        iovss.childports += i_pclamp.ports.iovss
        pgate.childports += i_pclamp.ports.gate

        frame.add_bulkconn_inst(ckt=ckt, width=spec.iocell_width, connect_up=True)

        i_gatedec = ckt.instantiate(fab.get_cell("GateDecode"), name="gatedec")
        for name in ("vss", "vdd", "iovdd", "d", "de", "ngate", "pgate"):
            ckt.nets[name].childports += i_gatedec.ports[name]

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        tech = fab.tech
        frame = fab.frame
        comp = fab.computed

        metal = comp.metal
        metal1 = metal[1].prim
        metal2 = metal[2].prim
        metal2pin = metal2.pin[0]
        metal3 = metal[3].prim
        metal4 = metal[4].prim
        metal5 = metal[5].prim
        metal6 = metal[6].prim
        trackpinmasks = set(m.pin[0].mask for m in (
            metal3, metal4, metal5, metal6,
        ))
        via1 = comp.vias[1]

        def pinpolygons(polygons):
            return filter(lambda p: p.mask in trackpinmasks, polygons)

        ckt = self.circuit
        insts = ckt.instances
        nets = ckt.nets

        layouter = self.new_circuitlayouter()
        layout = self.layout
        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=spec.iocell_width, top=spec.iocell_height,
        )

        frame.draw_tracks(ckt=ckt, layouter=layouter)

        # PAD
        l_pad = frame.place_pad(layouter=layouter, net=nets.pad)
        padm2_bounds = l_pad.bounds(mask=metal2.mask)

        # iovss & iovdd
        l_nclamp = layouter.place(insts.nclamp, x=0.0, y=frame.iovss_bottom)
        for polygon in pinpolygons(l_nclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovss, maskshape=polygon)
        l_pclamp = layouter.place(insts.pclamp, x=0.0, y=frame.iovdd_bottom)
        for polygon in pinpolygons(l_pclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovdd, maskshape=polygon)

        # Connect clamps to pad
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_nclamp.net_polygons(net=nets.pad),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                shape = _geo.Rect.from_rect(rect=bounds, top=padm2_bounds.bottom)
                layouter.add_wire(wire=metal2, net=nets.pad, shape=shape)
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.pad),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                shape = _geo.Rect.from_rect(rect=bounds, bottom=padm2_bounds.top)
                layouter.add_wire(wire=metal2, net=nets.pad, shape=shape)

        # Draw guardring around pad and connect to iovdd track
        bottom = cast(_geo._Rectangular, l_nclamp.boundary).top
        top = cast(_geo._Rectangular, l_pclamp.boundary).bottom - comp.guardring_space
        _l_guardring = hlp.guardring(
            fab=fab, net=nets.iovss, type_="n",
            width=spec.iocell_width, height=(top - bottom),
        )
        l_guardring = layouter.place(
            _l_guardring, x=0.5*spec.iocell_width, y=0.5*(bottom + top),
        )
        guardringm1_bounds = l_guardring.bounds(mask=metal1.mask)
        viatop = guardringm1_bounds.top
        viabottom = viatop - comp.metal[2].minwidth4ext_updown
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.iovdd),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                top_shape = _geo.Rect.from_rect(
                    rect=bounds, bottom=viabottom, top=viatop,
                )
                l_via = layouter.add_wire(
                    net=nets.iovdd, wire=via1, top_shape=top_shape,
                )
                viam2_bounds = l_via.bounds(mask=metal2.mask)
                shape = _geo.Rect.from_rect(rect=bounds, bottom=viam2_bounds.bottom)
                layouter.add_wire(net=nets.iovdd, wire=metal2, shape=shape)

        # Bulk/well connection cell
        frame.place_bulkconn(layouter=layouter)

        # Gate decoder + interconnect
        _l_gatedec = layouter.inst_layout(inst=insts.gatedec)
        dm2pin_bounds = _l_gatedec.bounds(net=nets.d, mask=metal2pin.mask)
        dem2pin_bounds = _l_gatedec.bounds(net=nets.de, mask=metal2pin.mask)
        x = tech.on_grid(
            0.5*spec.iocell_width - 0.5*(dm2pin_bounds.left + dem2pin_bounds.right)
        )
        l_gatedec = layouter.place(
            _l_gatedec, x=x,
            y=(frame.cells_y - cast(_geo._Rectangular, _l_gatedec.boundary).bottom),
        )

        # Bring pins to top
        for name in ("d", "de"):
            net = nets[name]
            m2pin_bounds = l_gatedec.bounds(net=net, mask=metal2pin.mask)
            layouter.add_wire(
                net=net, wire=metal2, pin=metal2pin, shape=m2pin_bounds,
            )

        net = nets.pgate
        m2pin_bounds1 = l_gatedec.bounds(net=net, mask=metal2pin.mask)
        m2pin_bounds2 = l_pclamp.bounds(net=net, mask=metal2pin.mask)
        m2_width = comp.metal[2].minwidth4ext_updown
        bottom = cast(_geo._Rectangular, l_pclamp.boundary).top + 2*metal2.min_space
        y = bottom + 0.5*m2_width
        shape = _geo.Rect.from_rect(
            rect=m2pin_bounds1, bottom=bottom, top=m2pin_bounds1.bottom,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        top = bottom + m2_width
        shape = _geo.Rect(
            left=m2pin_bounds2.left, bottom=bottom,
            right=m2pin_bounds1.right, top=top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=m2pin_bounds2, bottom=m2pin_bounds2.top, top=top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)

        net = nets.ngate
        m2pin_bounds1 = l_gatedec.bounds(net=net, mask=metal2pin.mask)
        m2pin_bounds2 = l_nclamp.bounds(net=net, mask=metal2pin.mask)
        y += m2_width + 2*metal2.min_space
        bottom = y - 0.5*m2_width
        top = y + 0.5*m2_width
        shape = _geo.Rect.from_rect(
            rect=m2pin_bounds1, bottom=bottom, top=m2pin_bounds1.bottom,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        left = 0.5*spec.metal_bigspace
        shape = _geo.Rect(
            left=left, bottom=bottom, right=m2pin_bounds1.right, top=top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        right = left + m2_width
        bottom = m2pin_bounds2.top - m2_width
        shape = _geo.Rect(left=left, bottom=bottom, right=right, top=top)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect(
            left=left, bottom=bottom, right=m2pin_bounds2.left, top=m2pin_bounds2.top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)


class _PadIn(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="IOPadIn")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        frame = fab.frame

        ckt = self.new_circuit()
        nets = ckt.nets

        frame.add_track_nets(ckt=ckt)
        vss = nets.vss
        vdd = nets.vdd
        iovss = nets.iovss
        iovdd = nets.iovdd

        s = ckt.new_net(name="s", external=True)
        pad = ckt.new_net(name="pad", external=True)

        frame.add_pad_inst(ckt=ckt, net=pad)

        c_nclamp = fab.clamp(type_="n", n_trans=spec.clampcount, n_drive=0)
        i_nclamp = ckt.instantiate(c_nclamp, name="nclamp")
        pad.childports += i_nclamp.ports.pad
        iovdd.childports += i_nclamp.ports.iovdd
        iovss.childports += i_nclamp.ports.iovss

        c_pclamp = fab.clamp(type_="p", n_trans=spec.clampcount, n_drive=0)
        i_pclamp = ckt.instantiate(c_pclamp, name="pclamp")
        pad.childports += i_pclamp.ports.pad
        iovdd.childports += i_pclamp.ports.iovdd
        iovss.childports += i_pclamp.ports.iovss

        frame.add_bulkconn_inst(ckt=ckt, width=spec.iocell_width, connect_up=True)

        i_leveldown = ckt.instantiate(fab.get_cell("LevelDown"), name="leveldown")
        for name in ("vss", "vdd", "iovss", "iovdd", "pad"):
            ckt.nets[name].childports += i_leveldown.ports[name]
        s.childports += i_leveldown.ports.core

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        frame = fab.frame
        comp = fab.computed

        metal = comp.metal
        metal1 = metal[1].prim
        metal1pin = metal1.pin[0]
        metal2 = metal[2].prim
        metal2pin = metal2.pin[0]
        metal3 = metal[3].prim
        metal4 = metal[4].prim
        metal5 = metal[5].prim
        metal6 = metal[6].prim
        trackpinmasks = set(m.pin[0].mask for m in (
            metal3, metal4, metal5, metal6,
        ))
        via1 = comp.vias[1]

        def pinpolygons(polygons):
            return filter(lambda p: p.mask in trackpinmasks, polygons)

        ckt = self.circuit
        insts = ckt.instances
        nets = ckt.nets

        layouter = self.new_circuitlayouter()
        layout = self.layout
        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=spec.iocell_width, top=spec.iocell_height,
        )

        frame.draw_tracks(ckt=ckt, layouter=layouter)

        # PAD
        l_pad = frame.place_pad(layouter=layouter, net=nets.pad)
        padm2_bounds = l_pad.bounds(mask=metal2.mask)

        # iovss & iovdd
        l_nclamp = layouter.place(insts.nclamp, x=0.0, y=frame.iovss_bottom)
        for polygon in pinpolygons(l_nclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovss, maskshape=polygon)
        l_pclamp = layouter.place(insts.pclamp, x=0.0, y=frame.iovdd_bottom)
        for polygon in pinpolygons(l_pclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovdd, maskshape=polygon)

        # Connect clamps to pad
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_nclamp.net_polygons(net=nets.pad),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                shape = _geo.Rect.from_rect(
                    rect=bounds, bottom=bounds.top, top=padm2_bounds.bottom,
                )
                layouter.add_wire(wire=metal2, net=nets.pad, shape=shape)
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.pad),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                shape = _geo.Rect.from_rect(
                    rect=bounds, bottom=padm2_bounds.top, top=bounds.bottom,
                )
                layouter.add_wire(wire=metal2, net=nets.pad, shape=shape)

        # Draw guardring around pad and connect to iovdd track
        bottom = cast(_geo._Rectangular, l_nclamp.boundary).top
        top = cast(_geo._Rectangular, l_pclamp.boundary).bottom - comp.guardring_space
        _l_guardring = hlp.guardring(
            fab=fab, net=nets.iovss, type_="n",
            width=spec.iocell_width, height=(top - bottom),
        )
        l_guardring = layouter.place(
            _l_guardring, x=0.5*spec.iocell_width, y=0.5*(bottom + top),
        )
        guardringm1_bounds = l_guardring.bounds(mask=metal1.mask)
        viatop = guardringm1_bounds.top
        viabottom = viatop - comp.metal[2].minwidth4ext_updown
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.iovdd),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                x = 0.5*(bounds.left + bounds.right)
                top_shape = _geo.Rect.from_rect(
                    rect=bounds, bottom=viabottom, top=viatop,
                )
                l_via = layouter.add_wire(
                    net=nets.iovdd, wire=via1, top_shape=top_shape,
                )
                viam2_bounds = l_via.bounds(mask=metal2.mask)
                shape = _geo.Rect.from_rect(rect=bounds, bottom=viam2_bounds.bottom)
                layouter.add_wire(net=nets.iovdd, wire=metal2, shape=shape)

        # Bulk/well connection cell
        frame.place_bulkconn(layouter=layouter)

        # LevelDown + interconnect
        _l_ld = layouter.inst_layout(inst=insts.leveldown)

        net = nets.s
        _m1pin_bounds = _l_ld.bounds(net=net, mask=metal1pin.mask)
        x = 0.5*spec.iocell_width - 0.5*(_m1pin_bounds.left + _m1pin_bounds.right)
        l_ld = layouter.place(_l_ld, x=x, y=frame.cells_y)
        m1pin_bounds = l_ld.bounds(net=net, mask=metal1pin.mask)
        _l_via1 = layouter.wire_layout(
            net=net, wire=via1, bottom_height=m1pin_bounds.height,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        _m1_bounds = _l_via1.bounds(mask=metal1.mask)
        x = m1pin_bounds.left - _m1_bounds.right
        y = m1pin_bounds.top - _m1_bounds.top
        l_via = layouter.place(object_=_l_via1, x=x, y=y)
        m2bounds = l_via.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=m2bounds, top=spec.iocell_height)
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

        net = nets.pad
        m2pin_bounds = l_ld.bounds(net=net, mask=metal2pin.mask)
        clamp_bounds = None
        for polygon in l_pclamp.filter_polygons(
            net=nets.pad, mask=metal2.mask, split=True,
        ):
            bounds = polygon.bounds
            if clamp_bounds is None:
                if bounds.left >= m2pin_bounds.left:
                    clamp_bounds = bounds
            else:
                if (
                    (bounds.left >= m2pin_bounds.left)
                    and (bounds.left < clamp_bounds.left)
                ):
                    clamp_bounds = bounds
        assert clamp_bounds is not None, "Internal error"
        m2_width = comp.metal[2].minwidth4ext_updown
        shape = _geo.Rect(
            left=m2pin_bounds.left, bottom=(m2pin_bounds.bottom - m2_width),
            right=(clamp_bounds.left + m2_width), top=m2pin_bounds.bottom,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=clamp_bounds, bottom=clamp_bounds.top, top=m2pin_bounds.bottom,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)


class _PadInOut(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="IOPadInOut")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        frame = fab.frame

        ckt = self.new_circuit()
        nets = ckt.nets

        frame.add_track_nets(ckt=ckt)
        vss = nets.vss
        vdd = nets.vdd
        iovss = nets.iovss
        iovdd = nets.iovdd

        s = ckt.new_net(name="s", external=True)
        ckt.new_net(name="d", external=True)
        ckt.new_net(name="de", external=True)
        pad = ckt.new_net(name="pad", external=True)

        ngate = ckt.new_net(name="ngate", external=False)
        pgate = ckt.new_net(name="pgate", external=False)

        frame.add_pad_inst(ckt=ckt, net=pad)

        c_nclamp = fab.clamp(type_="n", n_trans=spec.clampcount, n_drive=spec.clampdrive)
        i_nclamp = ckt.instantiate(c_nclamp, name="nclamp")
        pad.childports += i_nclamp.ports.pad
        iovdd.childports += i_nclamp.ports.iovdd
        iovss.childports += i_nclamp.ports.iovss
        ngate.childports += i_nclamp.ports.gate

        c_pclamp = fab.clamp(type_="p", n_trans=spec.clampcount, n_drive=spec.clampdrive)
        i_pclamp = ckt.instantiate(c_pclamp, name="pclamp")
        pad.childports += i_pclamp.ports.pad
        iovdd.childports += i_pclamp.ports.iovdd
        iovss.childports += i_pclamp.ports.iovss
        pgate.childports += i_pclamp.ports.gate

        frame.add_bulkconn_inst(ckt=ckt, width=spec.iocell_width, connect_up=True)

        i_gatedec = ckt.instantiate(fab.get_cell("GateDecode"), name="gatedec")
        for name in ("vss", "vdd", "iovdd", "d", "de", "ngate", "pgate"):
            ckt.nets[name].childports += i_gatedec.ports[name]

        i_leveldown = ckt.instantiate(fab.get_cell("LevelDown"), name="leveldown")
        for name in ("vss", "vdd", "iovss", "iovdd", "pad"):
            ckt.nets[name].childports += i_leveldown.ports[name]
        s.childports += i_leveldown.ports.core

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        tech = fab.tech
        frame = fab.frame
        comp = fab.computed

        metal = comp.metal
        metal1 = metal[1].prim
        metal1pin = metal1.pin[0]
        metal2 = metal[2].prim
        metal2pin = metal2.pin[0]
        metal3 = metal[3].prim
        metal4 = metal[4].prim
        metal5 = metal[5].prim
        metal6 = metal[6].prim
        trackpinmasks = set(m.pin[0].mask for m in (
            metal3, metal4, metal5, metal6,
        ))
        via1 = comp.vias[1]

        def pinpolygons(polygons):
            return filter(lambda p: p.mask in trackpinmasks, polygons)

        ckt = self.circuit
        insts = ckt.instances
        nets = ckt.nets

        layouter = self.new_circuitlayouter()
        layout = self.layout
        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=spec.iocell_width, top=spec.iocell_height,
        )

        frame.draw_tracks(ckt=ckt, layouter=layouter)

        # PAD
        l_pad = frame.place_pad(layouter=layouter, net=nets.pad)
        padm2_bounds = l_pad.bounds(mask=metal2.mask)

        # iovss & iovdd
        l_nclamp = layouter.place(insts.nclamp, x=0.0, y=frame.iovss_bottom)
        for polygon in pinpolygons(l_nclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovss, maskshape=polygon)
        l_pclamp = layouter.place(insts.pclamp, x=0.0, y=frame.iovdd_bottom)
        for polygon in pinpolygons(l_pclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovdd, maskshape=polygon)

        # Connect clamps to pad
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_nclamp.net_polygons(net=nets.pad),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                shape = _geo.Rect.from_rect(
                    rect=bounds, bottom=bounds.top, top=padm2_bounds.bottom,
                )
                layouter.add_wire(wire=metal2, net=nets.pad, shape=shape)
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.pad),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                shape = _geo.Rect.from_rect(
                    rect=bounds, bottom=padm2_bounds.top, top=bounds.bottom,
                )
                layouter.add_wire(wire=metal2, net=nets.pad, shape=shape)

        # Draw guardring around pad and connect to iovdd track
        bottom = cast(_geo._Rectangular, l_nclamp.boundary).top
        top = cast(_geo._Rectangular, l_pclamp.boundary).bottom - comp.guardring_space
        _l_guardring = hlp.guardring(
            fab=fab, net=nets.iovss, type_="n",
            width=spec.iocell_width, height=(top - bottom),
        )
        l_guardring = layouter.place(
            _l_guardring, x=0.5*spec.iocell_width, y=0.5*(bottom + top),
        )
        guardringm1_bounds = l_guardring.bounds(mask=metal1.mask)
        viatop = guardringm1_bounds.top
        viabottom = viatop - comp.metal[2].minwidth4ext_updown
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.iovdd),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                top_shape = _geo.Rect.from_rect(
                    rect=bounds, bottom=viabottom, top=viatop,
                )
                l_via = layouter.add_wire(
                    net=nets.iovdd, wire=via1, top_shape=top_shape,
                )
                viam2_bounds = l_via.bounds(mask=metal2.mask)
                shape = _geo.Rect.from_rect(rect=bounds, bottom=viam2_bounds.bottom)
                layouter.add_wire(net=nets.iovdd, wire=metal2, shape=shape)

        # Bulk/well connection cell
        frame.place_bulkconn(layouter=layouter)

        # Gate decoder + interconnect
        _l_gatedec = layouter.inst_layout(inst=insts.gatedec)
        dm2pin_bounds = _l_gatedec.bounds(net=nets.d, mask=metal2pin.mask)
        dem2pin_bounds = _l_gatedec.bounds(net=nets.de, mask=metal2pin.mask)
        x = tech.on_grid(
            0.25*spec.iocell_width - 0.5*(dm2pin_bounds.left + dem2pin_bounds.right),
        )
        l_gatedec = layouter.place(
            _l_gatedec, x=x,
            y=(frame.cells_y - cast(_geo._Rectangular, _l_gatedec.boundary).bottom),
        )

        # Bring pins to top
        for name in ("d", "de"):
            net = nets[name]
            m2pin_bounds = l_gatedec.bounds(net=net, mask=metal2pin.mask)
            layouter.add_wire(
                net=net, wire=metal2, pin=metal2pin, shape=m2pin_bounds,
            )

        net = nets.pgate
        m2pin_bounds1 = l_gatedec.bounds(net=net, mask=metal2pin.mask)
        m2pin_bounds2 = l_pclamp.bounds(net=net, mask=metal2pin.mask)
        m2_width = comp.metal[2].minwidth4ext_updown
        bottom = cast(_geo._Rectangular, l_pclamp.boundary).top + 2*metal2.min_space
        y = bottom + 0.5*m2_width
        shape = _geo.Rect.from_rect(
            rect=m2pin_bounds1, bottom=bottom, top=m2pin_bounds1.bottom,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        top = bottom + m2_width
        shape = _geo.Rect(
            left=m2pin_bounds2.left, bottom=bottom,
            right=m2pin_bounds1.right, top=top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=m2pin_bounds2, bottom=m2pin_bounds2.top, top=top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)

        net = nets.ngate
        m2pin_bounds1 = l_gatedec.bounds(net=net, mask=metal2pin.mask)
        m2pin_bounds2 = l_nclamp.bounds(net=net, mask=metal2pin.mask)
        y += m2_width + 2*metal2.min_space
        bottom = y - 0.5*m2_width
        top = y + 0.5*m2_width
        shape = _geo.Rect.from_rect(
            rect=m2pin_bounds1, bottom=bottom, top=m2pin_bounds1.bottom,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        left = 0.5*spec.metal_bigspace
        shape = _geo.Rect(
            left=left, bottom=bottom, right=m2pin_bounds1.right, top=top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        right = left + m2_width
        bottom = m2pin_bounds2.top - m2_width
        shape = _geo.Rect(left=left, bottom=bottom, right=right, top=top)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect(
            left=left, bottom=bottom, right=m2pin_bounds2.left, top=m2pin_bounds2.top,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)

        # LevelDown + interconnect
        _l_ld = layouter.inst_layout(inst=insts.leveldown)

        net = nets.s
        _m1pin_bounds = _l_ld.bounds(net=net, mask=metal1pin.mask)
        x = tech.on_grid(
            0.75*spec.iocell_width - 0.5*(_m1pin_bounds.left + _m1pin_bounds.right),
        )
        l_ld = layouter.place(_l_ld, x=x, y=frame.cells_y)
        m1pin_bounds = l_ld.bounds(net=net, mask=metal1pin.mask)
        _l_via1 = layouter.wire_layout(
            net=net, wire=via1, bottom_height=m1pin_bounds.height,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        _m1_bounds = _l_via1.bounds(mask=metal1.mask)
        x = m1pin_bounds.left - _m1_bounds.right
        y = m1pin_bounds.top - _m1_bounds.top
        l_via1 = layouter.place(object_=_l_via1, x=x, y=y)
        m2_bounds = l_via1.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=m2_bounds, top=spec.iocell_height)
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

        net = nets.pad
        m2pin_bounds = l_ld.bounds(net=net, mask=metal2pin.mask)
        clamp_bounds = None
        for polygon in l_pclamp.filter_polygons(
            net=nets.pad, mask=metal2.mask, split=True,
        ):
            bounds = polygon.bounds
            if clamp_bounds is None:
                if bounds.left >= m2pin_bounds.left:
                    clamp_bounds = bounds
            else:
                if (
                    (bounds.left >= m2pin_bounds.left)
                    and (bounds.left < clamp_bounds.left)
                ):
                    clamp_bounds = bounds
        assert clamp_bounds is not None, "Internal error"
        m2_width = comp.metal[2].minwidth4ext_updown
        shape = _geo.Rect(
            left=m2pin_bounds.left, bottom=(m2pin_bounds.bottom - m2_width),
            right=(clamp_bounds.left + m2_width), top=m2pin_bounds.bottom,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=clamp_bounds, bottom=clamp_bounds.top, top=m2pin_bounds.bottom,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)


class _PadAnalog(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="IOPadAnalog")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        frame = fab.frame

        ckt = self.new_circuit()
        nets = ckt.nets

        frame.add_track_nets(ckt=ckt)
        vss = nets.vss
        vdd = nets.vdd
        iovss = nets.iovss
        iovdd = nets.iovdd

        pad = ckt.new_net(name="pad", external=True)
        padres = ckt.new_net(name="padres", external=True)

        frame.add_pad_inst(ckt=ckt, net=pad)

        c_nclamp = fab.clamp(type_="n", n_trans=spec.clampcount_analog, n_drive=0)
        i_nclamp = ckt.instantiate(c_nclamp, name="nclamp")
        pad.childports += i_nclamp.ports.pad
        iovdd.childports += i_nclamp.ports.iovdd
        iovss.childports += i_nclamp.ports.iovss

        c_pclamp = fab.clamp(type_="p", n_trans=spec.clampcount_analog, n_drive=0)
        i_pclamp = ckt.instantiate(c_pclamp, name="pclamp")
        pad.childports += i_pclamp.ports.pad
        iovdd.childports += i_pclamp.ports.iovdd
        iovss.childports += i_pclamp.ports.iovss

        frame.add_bulkconn_inst(ckt=ckt, width=spec.iocell_width, connect_up=True)

        c_secondprot = fab.get_cell("SecondaryProtection")
        i_secondprot = ckt.instantiate(c_secondprot, name="secondprot")
        iovss.childports += i_secondprot.ports.iovss
        iovdd.childports += i_secondprot.ports.iovdd
        pad.childports += i_secondprot.ports.pad
        padres.childports += i_secondprot.ports.core

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        tech = fab.tech
        comp = fab.computed
        frame = fab.frame

        active = comp.active
        metal = comp.metal
        metal1 = metal[1].prim
        metal2 = metal[2].prim
        metal3 = metal[3].prim
        metal4 = metal[4].prim
        metal5 = metal[5].prim
        metal6 = metal[6].prim
        trackpinmasks = set(m.pin[0].mask for m in (
            metal3, metal4, metal5, metal6,
        ))
        via1 = comp.vias[1]
        via2 = comp.vias[2]

        def pinpolygons(polygons):
            return filter(lambda p: p.mask in trackpinmasks, polygons)

        ckt = self.circuit
        insts = ckt.instances
        nets = ckt.nets

        layouter = self.new_circuitlayouter()
        layout = self.layout
        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=spec.iocell_width, top=spec.iocell_height,
        )

        frame.draw_tracks(ckt=ckt, layouter=layouter)

        # PAD
        l_pad = frame.place_pad(layouter=layouter, net=nets.pad)
        padm2_bounds = l_pad.bounds(mask=metal2.mask)

        # iovss & iovdd
        l_nclamp = layouter.place(insts.nclamp, x=0.0, y=frame.iovss_bottom)
        for polygon in pinpolygons(l_nclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovss, maskshape=polygon)
        l_pclamp = layouter.place(insts.pclamp, x=0.0, y=frame.iovdd_bottom)
        for polygon in pinpolygons(l_pclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovdd, maskshape=polygon)

        # Connect clamps to pad
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_nclamp.net_polygons(net=nets.pad),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                shape = _geo.Rect.from_rect(rect=bounds, top=padm2_bounds.bottom)
                layouter.add_wire(wire=metal2, net=nets.pad, shape=shape)
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.pad),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                shape = _geo.Rect.from_rect(rect=bounds, bottom=padm2_bounds.top)
                layouter.add_wire(wire=metal2, net=nets.pad, shape=shape)

        # Draw guardring around pad and connect to iovdd track
        bottom = cast(_geo._Rectangular, l_nclamp.boundary).top
        top = cast(_geo._Rectangular, l_pclamp.boundary).bottom - comp.guardring_space
        _l_guardring = hlp.guardring(
            fab=fab, net=nets.iovss, type_="n",
            width=spec.iocell_width, height=(top - bottom),
        )
        l_guardring = layouter.place(
            _l_guardring, x=0.5*spec.iocell_width, y=0.5*(bottom + top),
        )
        guardringm1_bounds = l_guardring.bounds(mask=metal1.mask)
        viatop = guardringm1_bounds.top
        viabottom = viatop - comp.metal[2].minwidth4ext_updown
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.iovdd),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                x = 0.5*(bounds.left + bounds.right)
                top_shape = _geo.Rect.from_rect(
                    rect=bounds, bottom=viabottom, top=viatop,
                )
                l_via = layouter.add_wire(
                    net=nets.iovdd, wire=via1, top_shape=top_shape,
                )
                viam2_bounds = l_via.bounds(mask=metal2.mask)
                shape = _geo.Rect.from_rect(rect=bounds, bottom=viam2_bounds.bottom)
                layouter.add_wire(net=nets.iovdd, wire=metal2, shape=shape)

        # Bulk/well connection cell
        frame.place_bulkconn(layouter=layouter)

        # Place the secondary protection
        pclampact_bounds = l_pclamp.bounds(mask=comp.active.mask)
        # Search for pad pin closest to the middle of the cell
        x_clamppin = None
        pinmask = metal2.pin[0].mask
        hw = 0.5*spec.iocell_width
        clamppinm2_bounds: Optional[_geo.Rect] = None
        for polygon in filter(
            lambda p: p.mask == pinmask, l_pclamp.net_polygons(nets.pad),
        ):
            for bounds in _iterate_polygonbounds(polygon=polygon):
                x_p = bounds.center.x
                if (x_clamppin is None) or (x_p > x_clamppin):
                    x_clamppin = x_p
                    assert isinstance(bounds, _geo.Rect)
                    clamppinm2_bounds = bounds
        assert x_clamppin is not None
        assert clamppinm2_bounds is not None
        _l_secondprot = layouter.inst_layout(inst=insts.secondprot)
        _actvdd_bounds = _l_secondprot.bounds(net=nets.iovdd, mask=active.mask)
        y = frame.cells_y - _actvdd_bounds.bottom - 0.5*comp.minwidth_activewithcontact
        _protpadpin_bounds = _l_secondprot.bounds(mask=pinmask, net=nets.pad)
        x_protpadpin = 0.5*(_protpadpin_bounds.left + _protpadpin_bounds.right)
        # Center pins
        x = tech.on_grid(x_clamppin - x_protpadpin)
        l_secondprot = layouter.place(_l_secondprot, x=x, y=y)
        secondprotm2_bounds = l_secondprot.bounds(mask=metal2.mask)
        protpadpin_bounds = l_secondprot.bounds(mask=pinmask, net=nets.pad)
        protpadrespin_bounds = l_secondprot.bounds(mask=pinmask, net=nets.padres)

        # Connect pins of secondary protection
        shape = _geo.Rect.from_rect(
            rect=protpadpin_bounds, bottom=clamppinm2_bounds.top,
        )
        layouter.add_wire(wire=metal2, net=nets.pad, shape=shape)

        right = protpadrespin_bounds.right
        left = right - comp.metal[2].minwidth4ext_updown
        bottom = protpadrespin_bounds.top
        top = spec.iocell_height
        shape = _geo.Rect(left=left, bottom=bottom, right=right, top=top)
        layouter.add_wire(wire=metal2, pin=metal2.pin[0], net=nets.padres, shape=shape)

        # Connect pad pins
        left = spec.iocell_width
        right = 0.0
        for polygon in filter(
            lambda p: p.mask == pinmask, l_pclamp.net_polygons(nets.pad),
        ):
            for bounds in _iterate_polygonbounds(polygon=polygon):
                if bounds.right < x_clamppin:
                    shape = _geo.Rect.from_rect(rect=bounds, top=spec.iocell_height)
                    layouter.add_wire(net=nets.pad, wire=metal2, shape=shape)

                    left = min(left, bounds.left)
                    right = max(right, bounds.right)
        top = spec.iocell_height
        bottom = top - 5*metal2.min_width
        shape = _geo.Rect(left=left, bottom=bottom, right=right, top=top)
        layouter.add_wire(net=nets.pad, wire=metal2, pin=metal2.pin[0], shape=shape)


class _PadIOVss(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="IOPadIOVss")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        frame = fab.frame

        ckt = self.new_circuit()
        nets = ckt.nets

        frame.add_track_nets(ckt=ckt)
        vss = nets.vss
        vdd = nets.vdd
        iovss = nets.iovss
        iovdd = nets.iovdd

        frame.add_pad_inst(ckt=ckt, net=iovss)

        c_nclamp = fab.clamp(type_="n", n_trans=spec.clampcount, n_drive=0)
        i_nclamp = ckt.instantiate(c_nclamp, name="nclamp")
        iovdd.childports += i_nclamp.ports.iovdd
        iovss.childports += (i_nclamp.ports.pad, i_nclamp.ports.iovss)

        c_pclamp = fab.clamp(type_="p", n_trans=spec.clampcount, n_drive=0)
        i_pclamp = ckt.instantiate(c_pclamp, name="pclamp")
        iovdd.childports += i_pclamp.ports.iovdd
        iovss.childports += (i_pclamp.ports.pad, i_pclamp.ports.iovss)

        frame.add_bulkconn_inst(ckt=ckt, width=spec.iocell_width, connect_up=True)

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        comp = fab.computed
        frame = fab.frame

        metal = comp.metal
        metal1 = metal[1].prim
        metal2 = metal[2].prim
        metal3 = metal[3].prim
        metal4 = metal[4].prim
        metal5 = metal[5].prim
        metal6 = metal[6].prim
        metal2pin = metal2.pin[0]
        trackpinmasks = set(m.pin[0].mask for m in (
            metal3, metal4, metal5, metal6,
        ))
        via1 = comp.vias[1]
        via2 = comp.vias[2]

        def pinpolygons(polygons: Iterable[_geo.MaskShape]):
            return tuple(filter(lambda p: p.mask in trackpinmasks, polygons))

        ckt = self.circuit
        insts = ckt.instances
        nets = ckt.nets

        layouter = self.new_circuitlayouter()
        layout = self.layout
        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=spec.iocell_width, top=spec.iocell_height,
        )

        frame.draw_tracks(ckt=ckt, layouter=layouter)

        # PAD
        l_pad = frame.place_pad(layouter=layouter, net=nets.iovss)
        padm2_bounds = l_pad.bounds(mask=metal2.mask)

        # iovss & iovdd
        l_nclamp = layouter.place(insts.nclamp, x=0.0, y=frame.iovss_bottom)
        for polygon in pinpolygons(l_nclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovss, maskshape=polygon)
        l_pclamp = layouter.place(insts.pclamp, x=0.0, y=frame.iovdd_bottom)
        for polygon in pinpolygons(l_pclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovdd, maskshape=polygon)

        # Connect clamps to pad
        for polygon in l_nclamp.filter_polygons(
            net=nets.iovss, mask=metal2pin.mask, split=True,
        ):
            for metal in (metal2, metal3, metal4, metal5):
                shape = _geo.Rect.from_rect(
                    rect=polygon.bounds, top=padm2_bounds.bottom,
                )
                layouter.add_wire(wire=metal, net=nets.iovss, shape=shape)
        m3track_y = frame.secondiovss_bottom + 0.5*frame.secondiovss_width
        m3track_top = frame.secondiovss_bottom + frame.secondiovss_width
        m3track_height = frame.secondiovss_width
        for polygon in l_pclamp.filter_polygons(
            net=nets.iovss, mask=metal2pin.mask, split=True,
        ):
            bounds = polygon.bounds
            layouter.add_wire(
                wire=metal2, net=nets.iovss, shape=_geo.Rect.from_rect(
                    rect=bounds, bottom=padm2_bounds.top, top=m3track_top,
                ),
            )
            _l_via2 = layouter.wire_layout(
                wire=via2, net=nets.iovss,
                bottom_width=bounds.width, bottom_height=m3track_height,
            )
            layouter.place(_l_via2, x=bounds.center.x, y=m3track_y)

        # Draw guardring around pad and connect to iovdd track
        bottom = cast(_geo._Rectangular, l_nclamp.boundary).top
        top = cast(_geo._Rectangular, l_pclamp.boundary).bottom - comp.guardring_space
        _l_guardring = hlp.guardring(
            fab=fab, net=nets.iovss, type_="n",
            width=spec.iocell_width, height=(top - bottom),
        )
        l_guardring = layouter.place(
            _l_guardring, x=0.5*spec.iocell_width, y=0.5*(bottom + top),
        )
        guardringm1_bounds = l_guardring.bounds(mask=metal1.mask)
        viatop = guardringm1_bounds.top
        viabottom = viatop - comp.metal[2].minwidth4ext_updown
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.iovdd),
        ):
            # Iterate over bounds of individual shapes
            for bounds in _iterate_polygonbounds(polygon=polygon):
                x = 0.5*(bounds.left + bounds.right)
                top_shape = _geo.Rect.from_rect(
                    rect=bounds, bottom=viabottom, top=viatop,
                )
                l_via = layouter.add_wire(
                    net=nets.iovdd, wire=via1, top_shape=top_shape,
                )
                viam2_bounds = l_via.bounds(mask=metal2.mask)
                shape = _geo.Rect.from_rect(rect=bounds, bottom=viam2_bounds.bottom)
                layouter.add_wire(net=nets.iovdd, wire=metal2, shape=shape)

        # Bulk/well connection cell
        frame.place_bulkconn(layouter=layouter)


class _PadIOVdd(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="IOPadIOVdd")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        frame = fab.frame

        ckt = self.new_circuit()
        nets = ckt.nets

        frame.add_track_nets(ckt=ckt)
        iovss = nets.iovss
        iovdd = nets.iovdd

        frame.add_pad_inst(ckt=ckt, net=iovdd)

        if spec.invvdd_n_mosfet is None:
            # Just put a n&p clamp without drive
            c_nclamp = fab.clamp(type_="n", n_trans=spec.clampcount, n_drive=0)
            i_nclamp = ckt.instantiate(c_nclamp, name="nclamp")
            iovdd.childports += (i_nclamp.ports.pad, i_nclamp.ports.iovdd)
            iovss.childports += i_nclamp.ports.iovss

            c_pclamp = fab.clamp(type_="p", n_trans=spec.clampcount, n_drive=0)
            i_pclamp = ckt.instantiate(c_pclamp, name="pclamp")
            iovdd.childports += (i_pclamp.ports.pad, i_pclamp.ports.iovdd)
            iovss.childports += i_pclamp.ports.iovss
        else:
            # Add RC active clamp
            c_nclamp = fab.clamp(
                type_="n", n_trans=spec.clampcount, n_drive=spec.clampcount,
            )
            i_nclamp = ckt.instantiate(c_nclamp, name="nclamp")
            iovdd.childports += (i_nclamp.ports.pad, i_nclamp.ports.iovdd)
            iovss.childports += i_nclamp.ports.iovss

            c_res = fab.get_cell("RCClampResistor")
            i_res = ckt.instantiate(c_res, name="rcres")
            iovdd.childports += i_res.ports.pin1

            c_inv = fab.get_cell("RCClampInverter")
            i_inv = ckt.instantiate(c_inv, name="rcinv")
            iovss.childports += i_inv.ports.ground
            iovdd.childports += i_inv.ports.supply

            ckt.new_net(name="iovdd_res", external=False, childports=(
                i_res.ports.pin2, i_inv.ports["in"],
            ))
            ckt.new_net(name="ngate", external=False, childports=(
                i_inv.ports.out, i_nclamp.ports.gate,
            ))

        frame.add_bulkconn_inst(ckt=ckt, width=spec.iocell_width, connect_up=True)

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        comp = fab.computed
        frame = fab.frame

        metal = comp.metal
        metal1 = metal[1].prim
        metal1pin = metal1.pin[0]
        metal2 = metal[2].prim
        metal3 = metal[3].prim
        metal4 = metal[4].prim
        metal5 = metal[5].prim
        metal6 = metal[6].prim
        metal2pin = metal2.pin[0]
        trackpinmasks = set(m.pin[0].mask for m in (
            metal3, metal4, metal5, metal6,
        ))
        via1 = comp.vias[1]
        via2 = comp.vias[2]

        def pinpolygons(polygons):
            return filter(lambda p: p.mask in trackpinmasks, polygons)

        ckt = self.circuit
        insts = ckt.instances
        nets = ckt.nets

        layouter = self.new_circuitlayouter()
        layout = self.layout
        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=spec.iocell_width, top=spec.iocell_height,
        )

        frame.draw_tracks(ckt=ckt, layouter=layouter)

        # PAD
        l_pad = frame.place_pad(layouter=layouter, net=nets.iovdd)
        padm2_bounds = l_pad.bounds(mask=metal2.mask)
        padm3_bounds = l_pad.bounds(mask=metal3.mask)

        # Draw guardring around pad and connect to iovdd track
        bottom = frame.iovss_bottom + frame.iovss_width
        top = frame.iovdd_bottom - comp.guardring_space
        _l = hlp.guardring(
            fab=fab, net=nets.iovss, type_="n",
            width=spec.iocell_width, height=(top - bottom),
        )
        l = layouter.place(_l, x=0.5*spec.iocell_width, y=0.5*(bottom + top))
        padguardring_m1bb = l.bounds(mask=metal1.mask)

        # Place nclamp + connect to pad + pad guard ring
        l_nclamp = layouter.place(insts.nclamp, x=0.0, y=frame.iovss_bottom)
        for polygon in l_nclamp.filter_polygons(
            net=nets.iovdd, mask=metal2pin.mask, split=True,
        ):
            shape = _geo.Rect.from_rect(rect=polygon.bounds, top=padm2_bounds.bottom)
            layouter.add_wire(wire=metal2, net=nets.iovdd, shape=shape)

            y = frame.iovss_bottom + frame.iovss_width
            layouter.add_wire(
                net=nets.iovdd, wire=via1, y=y,
                bottom_left=shape.left, bottom_right=shape.right, bottom_enclosure="tall",
                top_left=shape.left, top_right=shape.right, top_enclosure="tall",
            )

        if spec.invvdd_n_mosfet is None:
            # Place pclamp + connect to iovdd track
            l_pclamp = layouter.place(insts.pclamp, x=0.0, y=frame.iovdd_bottom)
            for polygon in l_pclamp.filter_polygons(
                net=nets.iovdd, mask=metal2pin.mask, split=True,
            ):
                shape = _geo.Rect.from_rect(rect=polygon.bounds, bottom=padm2_bounds.top)
                for metal in (metal2, metal3, metal4, metal5):
                    layouter.add_wire(wire=metal, net=nets.iovdd, shape=shape)
        else:
            # Place the RC clamp subblocks
            l_rcinv = layouter.place(
                insts.rcinv, x=spec.iocell_width, y=frame.iovdd_bottom,
                rotation=_geo.Rotation.MY,
            )
            # RC inverter replaces the pclamp
            l_pclamp = l_rcinv
            _l = layouter.inst_layout(inst=insts.rcres, rotation=_geo.Rotation.MX)
            _bb = _l.boundary
            assert _bb is not None
            o = padm2_bounds.center - _bb.center
            l_rcres = layouter.place(_l, origin=o)

            # Connect pad to iovdd track
            net = nets.iovdd
            width = spec.ioring_maxwidth
            space = 3*spec.ioring_space # Draw rectangular openings
            pitch = width + space
            fingers = floor((padm3_bounds.width - width)/pitch) + 1
            bottom = padm3_bounds.top
            top = frame.iovdd_bottom + frame.iovdd_width
            for n in range(fingers-1):
                left = padm3_bounds.left + n*pitch
                right = left + width
                shape = _geo.Rect(left=left, bottom=bottom, right=right, top=top)
                for metal in (metal3, metal4, metal5):
                    layouter.add_wire(net=net, wire=metal, shape=shape)
            right = padm3_bounds.right
            left = right - width
            shape = _geo.Rect(left=left, bottom=bottom, right=right, top=top)
            for metal in (metal3, metal4, metal5):
                layouter.add_wire(net=net, wire=metal, shape=shape)

            # Connect supply of inv to iovdd track
            net = nets.iovdd
            m1pinbb = l_rcinv.bounds(mask=metal1pin.mask, net=net, depth=1)

            w = m1pinbb.width
            _l = layouter.wire_layout(
                net=net, wire=via1,
                bottom_width=w, bottom_enclosure="tall",
                top_width=w, top_enclosure="tall",
            )
            _m1bb = _l.bounds(mask=metal1.mask)
            x = m1pinbb.center.x
            y = m1pinbb.bottom - _m1bb.bottom
            layouter.place(_l, x=x, y=y)
            layouter.add_wire(
                net=net, wire=via2, x=x, y=y,
                bottom_width=w, bottom_enclosure="tall",
                top_width=w, top_enclosure="tall",
            )

            # Connect pin1 of rcres
            m1pinbb = l_rcres.bounds(mask=metal1pin.mask, net=nets.iovdd, depth=1)

            _l = layouter.wire_layout(
                net=nets.iovdd, wire=via1, columns=2,
                bottom_enclosure="tall", top_enclosure="tall",
            )
            _m1bb = _l.bounds(mask=metal1.mask)
            x = m1pinbb.right - _m1bb.right
            y = m1pinbb.center.y
            l = layouter.place(_l, x=x, y=y)
            m2bb = l.bounds(mask=metal2.mask)

            _l = layouter.wire_layout(
                net=nets.iovdd, wire=via2, columns=2,
                bottom_enclosure="tall", top_enclosure="tall",
            )
            _m2bb = _l.bounds(mask=metal2.mask)
            x = m2bb.right - _m2bb.right
            layouter.place(_l, x=x, y=y)

            # Connect res output to inv input
            net = nets.iovdd_res
            res_m1pinbb = l_rcres.bounds(mask=metal1pin.mask, net=net, depth=1)
            inv_m2pinbb = l_rcinv.bounds(mask=metal2pin.mask, net=net, depth=1)

            w = inv_m2pinbb.right - res_m1pinbb.left
            _l = layouter.wire_layout(
                net=net, wire=via1,
                bottom_width=w, bottom_enclosure="tall",
                top_width=w, top_enclosure="tall",
            )
            _via1_m1bb = _l.bounds(mask=metal1.mask)
            x = res_m1pinbb.left - _via1_m1bb.left
            y = (
                padguardring_m1bb.top - comp.guardring_width - 2*metal1.min_space
                - _via1_m1bb.top
            )
            l = layouter.place(_l, x=x, y=y)
            via1_m1bb = l.bounds(mask=metal1.mask)
            via1_m2bb = l.bounds(mask=metal2.mask)
            shape = _geo.Rect.from_rect(rect=res_m1pinbb, top=via1_m1bb.top)
            layouter.add_wire(net=net, wire=metal1, shape=shape)
            shape = _geo.Rect.from_rect(
                rect=inv_m2pinbb,
                bottom=via1_m2bb.bottom, left=max(inv_m2pinbb.left, via1_m2bb.left),
            )
            layouter.add_wire(net=net, wire=metal2, shape=shape)

            # Connect inv output to gate of nclamp
            net = nets.ngate
            inv_m2pinbb = l_rcinv.bounds(mask=metal2pin.mask, net=net, depth=1)
            nclamp_m2pinbb = l_nclamp.bounds(mask=metal2pin.mask, net=net, depth=1)

            left = 2*metal2.min_space
            shape = _geo.Rect.from_rect(rect=inv_m2pinbb, left=left)
            layouter.add_wire(net=net, wire=metal2, shape=shape)
            shape = _geo.Rect.from_rect(rect=nclamp_m2pinbb, left=left)
            layouter.add_wire(net=net, wire=metal2, shape=shape)
            shape = _geo.Rect(
                left=left, bottom=nclamp_m2pinbb.bottom,
                right=(left + 2*metal2.min_width), top=inv_m2pinbb.top,
            )
            layouter.add_wire(net=net, wire=metal2, shape=shape)

        # Bulk/well connection cell
        frame.place_bulkconn(layouter=layouter)


class _PadVss(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="IOPadVss")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        frame = fab.frame

        ckt = self.new_circuit()
        nets = ckt.nets

        frame.add_track_nets(ckt=ckt)
        vss = nets.vss
        vdd = nets.vdd
        iovss = nets.iovss
        iovdd = nets.iovdd

        frame.add_pad_inst(ckt=ckt, net=vss)

        c_nclamp = fab.clamp(type_="n", n_trans=spec.clampcount, n_drive=0)
        i_nclamp = ckt.instantiate(c_nclamp, name="nclamp")
        vss.childports += i_nclamp.ports.pad
        iovdd.childports += i_nclamp.ports.iovdd
        iovss.childports += i_nclamp.ports.iovss

        c_pclamp = fab.clamp(type_="p", n_trans=spec.clampcount, n_drive=0)
        i_pclamp = ckt.instantiate(c_pclamp, name="pclamp")
        vss.childports += i_pclamp.ports.pad
        iovdd.childports += i_pclamp.ports.iovdd
        iovss.childports += i_pclamp.ports.iovss

        frame.add_bulkconn_inst(ckt=ckt, width=spec.iocell_width, connect_up=True)

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        comp = fab.computed
        frame = fab.frame

        metal = comp.metal
        metal1 = metal[1].prim
        metal2 = metal[2].prim
        metal3 = metal[3].prim
        metal4 = metal[4].prim
        metal5 = metal[5].prim
        metal6 = metal[6].prim
        metal2pin = metal2.pin[0]
        trackpinmasks = set(m.pin[0].mask for m in (
            metal3, metal4, metal5, metal6,
        ))
        via1 = comp.vias[1]
        via2 = comp.vias[2]

        def pinpolygons(polygons):
            return filter(lambda p: p.mask in trackpinmasks, polygons)

        ckt = self.circuit
        insts = ckt.instances
        nets = ckt.nets

        layouter = self.new_circuitlayouter()
        layout = self.layout
        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=spec.iocell_width, top=spec.iocell_height,
        )

        frame.draw_tracks(ckt=ckt, layouter=layouter)
        vssm3track_bounds = layout.bounds(mask=metal3.mask, net=nets.vss, depth=0)

        # PAD
        l_pad = frame.place_pad(layouter=layouter, net=nets.vss)
        padm2_bounds = l_pad.bounds(mask=metal2.mask)

        # iovss & iovdd
        l_nclamp = layouter.place(insts.nclamp, x=0.0, y=frame.iovss_bottom)
        for polygon in pinpolygons(l_nclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovss, maskshape=polygon)
        l_pclamp = layouter.place(insts.pclamp, x=0.0, y=frame.iovdd_bottom)
        for polygon in pinpolygons(l_pclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovdd, maskshape=polygon)

        # Connect clamps to pad
        for polygon in l_nclamp.filter_polygons(
            net=nets.vss, mask=metal2pin.mask, split=True,
        ):
            shape = _geo.Rect.from_rect(rect=polygon.bounds, top=padm2_bounds.bottom)
            layouter.add_wire(wire=metal2, net=nets.vss, shape=shape)
        for polygon in l_pclamp.filter_polygons(
            net=nets.vss, mask=metal2pin.mask, split=True,
        ):
            bounds = polygon.bounds
            layouter.add_wire(wire=metal2, net=nets.vss, shape=_geo.Rect.from_rect(
                rect=bounds, bottom=padm2_bounds.top, top=vssm3track_bounds.top,
            ))
            _l_via2 = layouter.wire_layout(
                wire=via2, net=nets.vss,
                bottom_width=bounds.width, bottom_height=vssm3track_bounds.height,
            )
            layouter.place(_l_via2, x=bounds.center.x, y=vssm3track_bounds.center.y)

        # Draw guardring around pad and connect to iovdd track
        bottom = cast(_geo._Rectangular, l_nclamp.boundary).top
        top = cast(_geo._Rectangular, l_pclamp.boundary).bottom - comp.guardring_space
        _l_guardring = hlp.guardring(
            fab=fab, net=nets.iovss, type_="n",
            width=spec.iocell_width, height=(top - bottom),
        )
        l_guardring = layouter.place(
            _l_guardring, x=0.5*spec.iocell_width, y=0.5*(bottom + top),
        )
        guardringm1_bounds = l_guardring.bounds(mask=metal1.mask)
        viatop = guardringm1_bounds.top
        viabottom = viatop - comp.metal[2].minwidth4ext_updown
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.iovdd),
        ):
            for bounds in _iterate_polygonbounds(polygon=polygon):
                x = 0.5*(bounds.left + bounds.right)
                _l_via = layouter.wire_layout(
                    net=nets.iovdd, wire=via1,
                    top_width=bounds.width, top_height=(viatop - viabottom),
                )
                l_via = layouter.place(_l_via, x=bounds.center.x, y=0.5*(viabottom + viatop))
                viam2_bounds = l_via.bounds(mask=metal2.mask)
                layouter.add_wire(net=nets.iovdd, wire=metal2, shape=_geo.Rect.from_rect(
                    rect=bounds, bottom=viam2_bounds.bottom,
                ))

        # Bulk/well connection cell
        frame.place_bulkconn(layouter=layouter)


class _PadVdd(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="IOPadVdd")

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        frame = fab.frame

        ckt = self.new_circuit()
        nets = ckt.nets

        frame.add_track_nets(ckt=ckt)
        vss = nets.vss
        vdd = nets.vdd
        iovss = nets.iovss
        iovdd = nets.iovdd

        frame.add_pad_inst(ckt=ckt, net=vdd)

        c_nclamp = fab.clamp(type_="n", n_trans=spec.clampcount, n_drive=0)
        i_nclamp = ckt.instantiate(c_nclamp, name="nclamp")
        vdd.childports += i_nclamp.ports.pad
        iovdd.childports += i_nclamp.ports.iovdd
        iovss.childports += i_nclamp.ports.iovss

        c_pclamp = fab.clamp(type_="p", n_trans=spec.clampcount, n_drive=0)
        i_pclamp = ckt.instantiate(c_pclamp, name="pclamp")
        vdd.childports += i_pclamp.ports.pad
        iovdd.childports += i_pclamp.ports.iovdd
        iovss.childports += i_pclamp.ports.iovss

        frame.add_bulkconn_inst(ckt=ckt, width=spec.iocell_width, connect_up=True)

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        comp = fab.computed
        frame = fab.frame

        metal = comp.metal
        metal1 = metal[1].prim
        metal2 = metal[2].prim
        metal3 = metal[3].prim
        metal4 = metal[4].prim
        metal5 = metal[5].prim
        metal6 = metal[6].prim
        metal2pin = metal2.pin[0]
        trackpinmasks = set(m.pin[0].mask for m in (
            metal3, metal4, metal5, metal6,
        ))
        via1 = comp.vias[1]
        via2 = comp.vias[2]

        def pinpolygons(polygons):
            return filter(lambda p: p.mask in trackpinmasks, polygons)

        ckt = self.circuit
        insts = ckt.instances
        nets = ckt.nets

        layouter = self.new_circuitlayouter()
        layout = self.layout
        layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=spec.iocell_width, top=spec.iocell_height,
        )

        frame.draw_tracks(ckt=ckt, layouter=layouter)
        vddm3track_bounds = layout.bounds(mask=metal3.mask, net=nets.vdd, depth=0)

        # PAD
        l_pad = frame.place_pad(layouter=layouter, net=nets.vdd)
        padm2_bounds = l_pad.bounds(mask=metal2.mask)

        # iovss & iovdd
        l_nclamp = layouter.place(insts.nclamp, x=0.0, y=frame.iovss_bottom)
        for polygon in pinpolygons(l_nclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovss, maskshape=polygon)
        l_pclamp = layouter.place(insts.pclamp, x=0.0, y=frame.iovdd_bottom)
        for polygon in pinpolygons(l_pclamp.polygons):
            assert isinstance(polygon, _geo.MaskShape)
            layout.add_maskshape(net=nets.iovdd, maskshape=polygon)

        # Connect clamps to pad
        for polygon in l_nclamp.filter_polygons(
            net=nets.vdd, mask=metal2pin.mask, split=True,
        ):
            bounds = polygon.bounds
            layouter.add_wire(wire=metal2, net=nets.vdd, shape=_geo.Rect.from_rect(
                rect=bounds, top=padm2_bounds.bottom,
            ))
        for polygon in l_pclamp.filter_polygons(
            net=nets.vdd, mask=metal2pin.mask, split=True,
        ):
            bounds = polygon.bounds
            layouter.add_wire(wire=metal2, net=nets.vdd, shape=_geo.Rect.from_rect(
                rect=bounds, bottom=padm2_bounds.top, top=vddm3track_bounds.top,
            ))
            _l_via2 = layouter.wire_layout(
                wire=via2, net=nets.vdd,
                bottom_width=bounds.width, bottom_height=vddm3track_bounds.height,
            )
            layouter.place(_l_via2, x=bounds.center.x, y=vddm3track_bounds.center.y)

        # Draw guardring around pad and connect to iovdd track
        bottom = cast(_geo._Rectangular, l_nclamp.boundary).top
        top = cast(_geo._Rectangular, l_pclamp.boundary).bottom - comp.guardring_space
        _l_guardring = hlp.guardring(
            fab=fab, net=nets.iovss, type_="n",
            width=spec.iocell_width, height=(top - bottom),
        )
        l_guardring = layouter.place(
            _l_guardring, x=0.5*spec.iocell_width, y=0.5*(bottom + top),
        )
        guardringm1_bounds = l_guardring.bounds(mask=metal1.mask)
        viatop = guardringm1_bounds.top
        viabottom = viatop - comp.metal[2].minwidth4ext_updown
        for polygon in filter(
            lambda p: p.mask == metal2.mask,
            l_pclamp.net_polygons(net=nets.iovdd),
        ):
            for bounds in _iterate_polygonbounds(polygon=polygon):
                _l_via = layouter.wire_layout(
                    net=nets.iovdd, wire=via1,
                    top_width=bounds.width, top_height=(viatop - viabottom),
                )
                l_via = layouter.place(_l_via, x=bounds.center.x, y=0.5*(viabottom + viatop))
                viam2_bounds = l_via.bounds(mask=metal2.mask)
                layouter.add_wire(net=nets.iovdd, wire=metal2, shape=_geo.Rect.from_rect(
                    rect=bounds, bottom=viam2_bounds.bottom,
                ))

        # Bulk/well connection cell
        frame.place_bulkconn(layouter=layouter)


class _Filler(_FactoryCell):
    def __init__(self, *,
        fab: "IOFactory", name: str, cell_width: float,
    ):
        super().__init__(fab=fab, name=name)

        frame = fab.frame
        spec = fab.spec

        ckt = self.new_circuit()
        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        frame.add_track_nets(ckt=ckt)
        frame.add_bulkconn_inst(ckt=ckt, width=cell_width, connect_up=False)

        frame.draw_tracks(ckt=ckt, layouter=layouter, cell_width=cell_width)
        frame.place_bulkconn(layouter=layouter)

        # Boundary
        bb = _geo.Rect(
            left=0.0, bottom=0.0, right=cell_width, top=spec.iocell_height,
        )
        layout.boundary = bb


class _Corner(_FactoryCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="Corner")

        frame = fab.frame
        spec = fab.spec

        ckt = self.new_circuit()
        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        frame.add_track_nets(ckt=ckt)
        frame.draw_corner_tracks(ckt=ckt, layouter=layouter)

        # Boundary
        bb = _geo.Rect(
            left=-spec.iocell_height, bottom=0.0, right=0.0, top=spec.iocell_height,
        )
        layout.boundary = bb


class _Gallery(_FactoryOnDemandCell):
    def __init__(self, *, fab: "IOFactory"):
        super().__init__(fab=fab, name="Gallery")

    cells = (
        "IOPadVss", "IOPadVdd", "IOPadIn", "IOPadOut", "IOPadTriOut", "IOPadInOut",
        "IOPadIOVss", "IOPadIOVdd", "IOPadAnalog",
    )
    cells_l = tuple(cell.lower() for cell in cells)

    def _create_circuit(self):
        fab = self.fab
        ckt = self.new_circuit()
        insts = ckt.instances

        for cell in self.cells:
            ckt.instantiate(fab.get_cell(cell), name=cell.lower())

        # vss and iovss are connected by the substrate
        # make only vss in Gallery so it is LVS clean.
        for net in ("vdd", "vss", "iovdd"):
            ports = tuple(insts[cell].ports[net] for cell in self.cells_l)
            if net == "vss":
                ports += tuple(insts[cell].ports["iovss"] for cell in self.cells_l)
            ckt.new_net(name=net, external=True, childports=ports)

        ckt.new_net(name="in_s", external=True, childports=(
            insts.iopadin.ports.s,
        ))
        ckt.new_net(name="in_pad", external=True, childports=(
            insts.iopadin.ports.pad,
        ))
        ckt.new_net(name="out_d", external=True, childports=(
            insts.iopadout.ports.d,
        ))
        ckt.new_net(name="out_pad", external=True, childports=(
            insts.iopadout.ports.pad,
        ))
        ckt.new_net(name="triout_d", external=True, childports=(
            insts.iopadtriout.ports.d,
        ))
        ckt.new_net(name="triout_de", external=True, childports=(
            insts.iopadtriout.ports.de,
        ))
        ckt.new_net(name="triout_pad", external=True, childports=(
            insts.iopadtriout.ports.pad,
        ))
        ckt.new_net(name="io_s", external=True, childports=(
            insts.iopadinout.ports.s,
        ))
        ckt.new_net(name="io_d", external=True, childports=(
            insts.iopadinout.ports.d,
        ))
        ckt.new_net(name="io_de", external=True, childports=(
            insts.iopadinout.ports.de,
        ))
        ckt.new_net(name="io_pad", external=True, childports=(
            insts.iopadinout.ports.pad,
        ))
        ckt.new_net(name="ana_out", external=True, childports=(
            insts.iopadanalog.ports.pad,
        ))
        ckt.new_net(name="ana_outres", external=True, childports=(
            insts.iopadanalog.ports.padres,
        ))

    def _create_layout(self):
        ckt = self.circuit
        insts = ckt.instances
        layouter = self.new_circuitlayouter()

        x = 0.0
        y = 0.0

        l: Optional[_lay._Layout] = None
        for cell in self.cells_l:
            l = layouter.place(insts[cell], x=x, y=y)
            x = cast(_geo._Rectangular, l.boundary).right
        assert l is not None

        self.layout.boundary = _geo.Rect(
            left=0.0, bottom=0.0, right=cast(_geo._Rectangular, l.boundary).right,
            top=cast(_geo._Rectangular, l.boundary).top,
        )


class IOFactory:
    def __init__(self, *,
        lib: _lbry.Library, spec: IOSpecification, framespec:IOFrameSpecification,
    ):
        self.lib = lib
        self.spec = spec

        self.computed = _ComputedSpecs(
            fab=self, nmos=spec.nmos, pmos=spec.pmos, ionmos=spec.ionmos, iopmos=spec.iopmos,
        )
        self.frame = _IOCellFrame(fab=self, framespec=framespec)

    @property
    def tech(self):
        return self.lib.tech
    @property
    def layoutfab(self):
        return self.lib.layoutfab
    @property
    def cktfab(self):
        return self.lib.cktfab

    def guardring(self, *, type_, width, height, fill_well=False, fill_implant=False):
        s = "GuardRing_{}{}W{}H{}{}".format(
            type_.upper(),
            round(width/self.tech.grid),
            round(height/self.tech.grid),
            "T" if fill_well else "F",
            "T" if fill_implant else "F",
        )

        try:
            return self.lib.cells[s]
        except KeyError:
            cell = _GuardRing(
                name=s, fab=self, type_=type_, width=width, height=height,
                fill_well=fill_well, fill_implant=fill_implant,
            )
            self.lib.cells += cell
            return cell

    def pad(self, *, width: IntFloat, height: IntFloat):
        s = "Pad_{}W{}H".format(
            round(width/self.tech.grid),
            round(height/self.tech.grid),
        )

        try:
            return self.lib.cells[s]
        except KeyError:
            cell = _Pad(
                name=s, fab=self, width=_util.i2f(width), height=_util.i2f(height),
                start_via=2,
            )
            self.lib.cells += cell
            return cell

    def bulkconn(self, *, width: IntFloat, connect_up: bool):
        s = f"BulkConn_{round(width/self.tech.grid)}W{'' if connect_up else 'No'}Up"

        try:
            return self.lib.cells[s]
        except KeyError:
            cell = _BulkConn(
                name=s, fab=self, cell_width=_util.i2f(width), connect_up=connect_up,
            )
            self.lib.cells += cell
            return cell

    def clamp(self, *, type_: str, n_trans: int, n_drive: int):
        s = "Clamp_{}{}N{}D".format(
            type_.upper(),
            n_trans,
            n_drive,
        )

        try:
            return self.lib.cells[s]
        except KeyError:
            cell = _Clamp(
                name=s, type_=type_, fab=self, n_trans=n_trans, n_drive=n_drive,
            )
            self.lib.cells += cell
            return cell

    def filler(self, *, cell_width: IntFloat):
        tech = self.tech
        s = f"Filler{round(cell_width/tech.grid)}"

        try:
            return self.lib.cells[s]
        except KeyError:
            cell = _Filler(name=s, fab=self, cell_width=_util.i2f(cell_width))
            self.lib.cells += cell
            return cell

    def get_cell(self, name) -> _lbry._Cell:
        try:
            return self.lib.cells[name]
        except KeyError:
            lookup = {
                "SecondaryProtection": _Secondary,
                "RCClampResistor": _RCClampResistor,
                "RCClampInverter": _RCClampInverter,
                "LevelUp": _LevelUp,
                "LevelDown": _LevelDown,
                "GateLevelUp": _GateLevelUp,
                "GateDecode": _GateDecode,
                "IOPadIn": _PadIn,
                "IOPadOut": _PadOut,
                "IOPadTriOut": _PadTriOut,
                "IOPadInOut": _PadInOut,
                "IOPadVdd": _PadVdd,
                "IOPadVss": _PadVss,
                "IOPadIOVdd": _PadIOVdd,
                "IOPadIOVss": _PadIOVss,
                "IOPadAnalog": _PadAnalog,
                "Corner": _Corner,
                "Gallery": _Gallery,
            }
            cell = lookup[name](fab=self)
            self.lib.cells += cell
            return cell
