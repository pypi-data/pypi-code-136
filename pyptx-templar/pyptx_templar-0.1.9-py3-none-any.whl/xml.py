"""
Contains an helper method to directly edit the xml
representation of the Presentation.
"""

from pptx.oxml.xmlchemy import OxmlElement


# https://github.com/scanny/python-pptx/issues/71
# https://groups.google.com/g/python-pptx/c/UTkdemIZICw
def SubElement(parent, tagname, before=(), **kwargs):
    """
    Adds the given tag, with attributes given in `kwargs`,
    inside `parent`, and as late as possible,
    but before all elements of tag in `before`.

    Returns the added element.
    """
    element = OxmlElement(tagname)
    element.attrib.update(kwargs)
    if before:
        parent.insert_element_before(element, *before)
    else:
        parent.append(element)
    return element
