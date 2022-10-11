# encoding: utf-8

"""
Custom element classes for shape-related elements like ``<w:inline>``
"""

from . import parse_xml
from .ns import nsdecls
from .simpletypes import (
    ST_Coordinate, ST_DrawingElementId, ST_PositiveCoordinate,
    ST_RelationshipId, XsdString, XsdToken, XsdBoolean
)
from .xmlchemy import (
    BaseOxmlElement, OneAndOnlyOne, OptionalAttribute, RequiredAttribute,
    ZeroOrOne
)
from ..shared import lazyproperty, Emu


class CT_Blip(BaseOxmlElement):
    """
    ``<a:blip>`` element, specifies image source and adjustments such as
    alpha and tint.
    """
    embed = OptionalAttribute('r:embed', ST_RelationshipId)
    link = OptionalAttribute('r:link', ST_RelationshipId)


class CT_BlipFillProperties(BaseOxmlElement):
    """
    ``<pic:blipFill>`` element, specifies picture properties
    """
    blip = ZeroOrOne('a:blip', successors=(
        'a:srcRect', 'a:tile', 'a:stretch'
    ))


class CT_GraphicalObject(BaseOxmlElement):
    """
    ``<a:graphic>`` element, container for a DrawingML object
    """
    graphicData = OneAndOnlyOne('a:graphicData')

    @lazyproperty
    def pic(self):
        return self.graphicData.pic


class CT_GraphicalObjectData(BaseOxmlElement):
    """
    ``<a:graphicData>`` element, container for the XML of a DrawingML object
    """
    pic = ZeroOrOne('pic:pic')
    uri = RequiredAttribute('uri', XsdToken)


class CT_Inline(BaseOxmlElement):
    """
    ``<wp:inline>`` element, container for an inline shape.
    """
    extent = OneAndOnlyOne('wp:extent')
    docPr = OneAndOnlyOne('wp:docPr')
    graphic = OneAndOnlyOne('a:graphic')
    wrapNone = ZeroOrOne('wp:wrapNone')
    wrapSquare = ZeroOrOne('wp:wrapSquare')
    wrapThrough = ZeroOrOne('wp:wrapThrough')
    wrapTight = ZeroOrOne('wp:wrapTight')
    wrapTopAndBottom = ZeroOrOne('wp:wrapTopAndBottom')

    @property
    def pic(self):
        return self.graphic.pic

    @property
    def has_wrap(self):
        if self.wrapNone:
            return False
        if self.wrapSquare or self.wrapThrough or self.wrapTight or self.wrapTopAndBottom:
            return True
        return False


    @classmethod
    def new(cls, cx, cy, shape_id, pic):
        """
        Return a new ``<wp:inline>`` element populated with the values passed
        as parameters.
        """
        inline = parse_xml(cls._inline_xml())
        inline.extent.cx = cx
        inline.extent.cy = cy
        inline.docPr.id = shape_id
        inline.docPr.name = 'Picture %d' % shape_id
        inline.graphic.graphicData.uri = (
            'http://schemas.openxmlformats.org/drawingml/2006/picture'
        )
        inline.graphic.graphicData._insert_pic(pic)
        return inline

    @classmethod
    def new_pic_inline(cls, shape_id, rId, filename, cx, cy):
        """
        Return a new `wp:inline` element containing the `pic:pic` element
        specified by the argument values.
        """
        pic_id = 0  # Word doesn't seem to use this, but does not omit it
        pic = CT_Picture.new(pic_id, filename, rId, cx, cy)
        inline = cls.new(cx, cy, shape_id, pic)
        inline.graphic.graphicData._insert_pic(pic)
        return inline

    @classmethod
    def _inline_xml(cls):
        return (
                '<wp:inline %s>\n'
                '  <wp:extent cx="914400" cy="914400"/>\n'
                '  <wp:docPr id="666" name="unnamed"/>\n'
                '  <wp:cNvGraphicFramePr>\n'
                '    <a:graphicFrameLocks noChangeAspect="1"/>\n'
                '  </wp:cNvGraphicFramePr>\n'
                '  <a:graphic>\n'
                '    <a:graphicData uri="URI not set"/>\n'
                '  </a:graphic>\n'
                '</wp:inline>' % nsdecls('wp', 'a', 'pic', 'r')
        )


class CT_Drawing(BaseOxmlElement):
    """
    Used for ``w:drawing``
    """
    anchor = ZeroOrOne('wp:anchor')
    inline = ZeroOrOne('w:inline')

    @lazyproperty
    def child(self):
        if self.anchor is not None:
            return self.anchor
        return self.inline


class CT_Anchor(BaseOxmlElement):
    """
    Used for ``wp:anchor``
    """
    is_simplePos = RequiredAttribute('simplePos', XsdBoolean)
    positionH = ZeroOrOne('wp:positionH')
    positionV = ZeroOrOne('wp:positionV')
    simplePos = ZeroOrOne('wp:simplePos')
    graphic = OneAndOnlyOne('a:graphic')
    wrapNone = ZeroOrOne('wp:wrapNone')
    wrapSquare = ZeroOrOne('wp:wrapSquare')
    wrapThrough = ZeroOrOne('wp:wrapThrough')
    wrapTight = ZeroOrOne('wp:wrapTight')
    wrapTopAndBottom = ZeroOrOne('wp:wrapTopAndBottom')

    @lazyproperty
    def has_wrap(self):
        if self.wrapNone is not None:
            return False
        if self.wrapSquare is not None or self.wrapThrough is not None or \
                self.wrapTight is not None or self.wrapTopAndBottom is not None:
            return True
        return False

    @lazyproperty
    def is_wrapThrough(self):
        if self.wrapThrough is not None:
            return True
        return False

    @lazyproperty
    def pic(self):
        return self.graphic.pic


class CT_WrapNone(BaseOxmlElement):
    """
    Used for ``wp:wrapNone``
    """


class CT_WrapSquare(BaseOxmlElement):
    """
    Used for ``wp:wrapSquare``
    """


class CT_WrapThrough(BaseOxmlElement):
    """
    Used for ``wp:wrapThrough``
    """
    wrapText = OptionalAttribute('wrapText', XsdString)


class CT_WrapTight(BaseOxmlElement):
    """
    Used for ``wp:wrapTight``
    """


class CT_WrapTopAndBottom(BaseOxmlElement):
    """
    Used for ``wp:wrapTopAndBottom``
    """


class CT_PositionH(BaseOxmlElement):
    """
    Used for ``wp:positionH``
    """
    relativeFrom = RequiredAttribute('relativeFrom', XsdString)
    posOffset = ZeroOrOne('wp:posOffset')
    align = ZeroOrOne('wp:align')

    @property
    def value(self):
        return Emu(self.posOffset.text if self.posOffset is not None else 0)


class CT_PositionV(BaseOxmlElement):
    """
    Used for ``wp:positionV``
    """
    relativeFrom = RequiredAttribute('relativeFrom', XsdString)
    posOffset = ZeroOrOne('wp:posOffset')
    align = ZeroOrOne('wp:align')

    @property
    def value(self):
        return Emu(self.posOffset.text if self.posOffset is not None else 0)


class CT_NonVisualDrawingProps(BaseOxmlElement):
    """
    Used for ``<wp:docPr>`` element, and perhaps others. Specifies the id and
    name of a DrawingML drawing.
    """
    id = RequiredAttribute('id', ST_DrawingElementId)
    name = RequiredAttribute('name', XsdString)


class CT_NonVisualPictureProperties(BaseOxmlElement):
    """
    ``<pic:cNvPicPr>`` element, specifies picture locking and resize
    behaviors.
    """


class CT_Picture(BaseOxmlElement):
    """
    ``<pic:pic>`` element, a DrawingML picture
    """
    nvPicPr = OneAndOnlyOne('pic:nvPicPr')
    blipFill = OneAndOnlyOne('pic:blipFill')
    spPr = OneAndOnlyOne('pic:spPr')

    @lazyproperty
    def parent(self):
        return self.getparent().getparent().getparent()

    @lazyproperty
    def parent_off_x(self):
        if hasattr(self.parent, 'positionH') and self.parent.positionH is not None:
            return self.parent.positionH.value
        return Emu(0)

    @lazyproperty
    def parent_off_y(self):
        if hasattr(self.parent, 'positionV') and self.parent.positionV is not None:
            return self.parent.positionV.value
        return Emu(0)

    @classmethod
    def new(cls, pic_id, filename, rId, cx, cy):
        """
        Return a new ``<pic:pic>`` element populated with the minimal
        contents required to define a viable picture element, based on the
        values passed as parameters.
        """
        pic = parse_xml(cls._pic_xml())
        pic.nvPicPr.cNvPr.id = pic_id
        pic.nvPicPr.cNvPr.name = filename
        pic.blipFill.blip.embed = rId
        pic.spPr.cx = cx
        pic.spPr.cy = cy
        return pic

    @classmethod
    def _pic_xml(cls):
        return (
                '<pic:pic %s>\n'
                '  <pic:nvPicPr>\n'
                '    <pic:cNvPr id="666" name="unnamed"/>\n'
                '    <pic:cNvPicPr/>\n'
                '  </pic:nvPicPr>\n'
                '  <pic:blipFill>\n'
                '    <a:blip/>\n'
                '    <a:stretch>\n'
                '      <a:fillRect/>\n'
                '    </a:stretch>\n'
                '  </pic:blipFill>\n'
                '  <pic:spPr>\n'
                '    <a:xfrm>\n'
                '      <a:off x="0" y="0"/>\n'
                '      <a:ext cx="914400" cy="914400"/>\n'
                '    </a:xfrm>\n'
                '    <a:prstGeom prst="rect"/>\n'
                '  </pic:spPr>\n'
                '</pic:pic>' % nsdecls('pic', 'a', 'r')
        )


class CT_PictureNonVisual(BaseOxmlElement):
    """
    ``<pic:nvPicPr>`` element, non-visual picture properties
    """
    cNvPr = OneAndOnlyOne('pic:cNvPr')


class CT_Point2D(BaseOxmlElement):
    """
    Used for ``<a:off>`` element, and perhaps others. Specifies an x, y
    coordinate (point).
    """
    x = RequiredAttribute('x', ST_Coordinate)
    y = RequiredAttribute('y', ST_Coordinate)


class CT_PositiveSize2D(BaseOxmlElement):
    """
    Used for ``<wp:extent>`` element, and perhaps others later. Specifies the
    size of a DrawingML drawing.
    """
    cx = RequiredAttribute('cx', ST_PositiveCoordinate)
    cy = RequiredAttribute('cy', ST_PositiveCoordinate)


class CT_PresetGeometry2D(BaseOxmlElement):
    """
    ``<a:prstGeom>`` element, specifies an preset autoshape geometry, such
    as ``rect``.
    """


class CT_RelativeRect(BaseOxmlElement):
    """
    ``<a:fillRect>`` element, specifying picture should fill containing
    rectangle shape.
    """


class CT_ShapeProperties(BaseOxmlElement):
    """
    ``<pic:spPr>`` element, specifies size and shape of picture container.
    """
    xfrm = ZeroOrOne('a:xfrm', successors=(
        'a:custGeom', 'a:prstGeom', 'a:ln', 'a:effectLst', 'a:effectDag',
        'a:scene3d', 'a:sp3d', 'a:extLst'
    ))

    @property
    def cx(self):
        """
        Shape width as an instance of Emu, or None if not present.
        """
        xfrm = self.xfrm
        if xfrm is None:
            return None
        return xfrm.cx

    @cx.setter
    def cx(self, value):
        xfrm = self.get_or_add_xfrm()
        xfrm.cx = value

    @property
    def cy(self):
        """
        Shape height as an instance of Emu, or None if not present.
        """
        xfrm = self.xfrm
        if xfrm is None:
            return None
        return xfrm.cy

    @cy.setter
    def cy(self, value):
        xfrm = self.get_or_add_xfrm()
        xfrm.cy = value

    @property
    def ox(self):
        xfrm = self.xfrm
        if xfrm is None:
            return Emu(0)
        return xfrm.ox

    @property
    def oy(self):
        xfrm = self.xfrm
        if xfrm is None:
            return Emu(0)
        return xfrm.oy


class CT_StretchInfoProperties(BaseOxmlElement):
    """
    ``<a:stretch>`` element, specifies how picture should fill its containing
    shape.
    """


class CT_Transform2D(BaseOxmlElement):
    """
    ``<a:xfrm>`` element, specifies size and shape of picture container.
    """
    off = ZeroOrOne('a:off', successors=('a:ext',))
    ext = ZeroOrOne('a:ext', successors=())

    @property
    def cx(self):
        ext = self.ext
        if ext is None:
            return None
        return ext.cx

    @cx.setter
    def cx(self, value):
        ext = self.get_or_add_ext()
        ext.cx = value

    @property
    def cy(self):
        ext = self.ext
        if ext is None:
            return None
        return ext.cy

    @cy.setter
    def cy(self, value):
        ext = self.get_or_add_ext()
        ext.cy = value

    @property
    def ox(self):
        off = self.off
        if off is None:
            return Emu(0)
        return off.x

    @property
    def oy(self):
        off = self.off
        if off is None:
            return Emu(0)
        return off.y
