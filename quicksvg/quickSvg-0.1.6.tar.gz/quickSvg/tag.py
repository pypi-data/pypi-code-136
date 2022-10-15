# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tag.py
   Description :
   Author :       liaozhaoyan
   date：          2022/10/12
-------------------------------------------------
   Change Activity:
                   2022/10/12:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

from six import with_metaclass

xmlQuot = {
    '&': "&amp;",
    '<': "&gt;",
    '>': "&lt;",
    '"': "&quot;",
    "'": "&apos;",
}


def escape(text):
    for k, v in xmlQuot.items():
        text = text.replace(k, v)
    return text


def identifier(text):
    return "".join(filter(lambda x: x in ["-", ":"] or x.isalnum(), str(text)))


def stripK(title):
    return title.lstrip('_').replace("__", ":").replace("_", "-")


class MetaT(type):
    def __getattr__(self, item):
        return T(stripK(item))


def _setupIndent(tabSize, level):
    tab = " " * tabSize
    return tab * level


class T(with_metaclass(MetaT)):
    def __init__(self, name, *children, **attributes):
        self._name = name
        self._children = list(children)
        self._attributes = {stripK(k): v for k, v in attributes.items()}

    def __setitem__(self, key, value):
        if isinstance(key, (int, slice)):
            self._children[key] = value
            return value
        return self.setAttribute(key, value)

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._children[item]
        return self.getAttribute(item)

    def __call__(self, *children, **attributes):
        if children:
            self._children.extend(children)
        if attributes:
            for attr in attributes:
                self._attributes[stripK(attr)] = attributes[attr]
        return self

    def __repr__(self):
        return "T<%s attributes: %d>" % (self._name, len(self._attributes)) + \
               "children: %d" % len(self._children) + \
               "</%s>" % self._name

    def setAttribute(self, attr, value):
        k = stripK(attr)
        if value is None:
            if k in self._attributes:
                self._attributes.pop(k)
        else:
            self._attributes[k] = value
        return value

    def getAttribute(self, attr):
        return self._attributes[stripK(attr)]

    def childrenCount(self):
        count = 0
        for child in self._children:
            if not isinstance(child, str):
                count += 1
        return count

    def buildChild(self, child, tabSize=0, level=0):
        s = ""
        if isinstance(child, str):
            esc = escape(child)
            if len(esc) == 0:
                esc = " "
            s += esc
        else:
            s += "\n" + child.build(tabSize, level + 1)
        return s

    def build(self, tabSize=2, level=0):
        name = identifier(self._name)
        s = _setupIndent(tabSize, level)
        s += '<' + name

        attrs = []
        for k, v in self._attributes.items():
            if not isinstance(v, str):
                v = str(v)
            attrs.append('%s="%s"' % (k, v.replace('"', '&quot;')))

        if len(attrs):
            s += " "
            s += " ".join(attrs)

        if self._children:
            s += '>'

        for child in self._children:
            s += self.buildChild(child, tabSize, level)

        if self.childrenCount():
            s += "\n" + _setupIndent(tabSize, level)

        if self._children:
            s += '</' + name + '>'
        else:
            s += '/>'
        return s


class Literal(T):
    def __init__(self, text, esc=True):
        self._name = ""
        self._children = [text]
        self._attributes = {}
        self._escape = esc

    def build(self, tabSize=2, level=0):
        s = _setupIndent(tabSize, level)
        if self._escape:
            s += escape(self._children[0])
        else:
            s += self._children[0]
        return s


class SVG(T):
    def __init__(self, useNS=True, *children, **attributes):
        super(SVG, self).__init__("svg", *children, **attributes)
        if useNS:
            self(
                **{
                    "version": "2.0",
                    "xmlns": "http://www.w3.org/2000/svg",
                    "xmlns:xlink": "http://www.w3.org/1999/xlink",
                }
            )


if __name__ == "__main__":
    svg = SVG(T.tcl(T.abc("hello", pos="xxx"),
              T.ccd(T.bcd("bcd"), v=3.14),
              T.script(Literal("xxdfas\nhello.n")),
              pos=3)
            )
    print(svg.build())
    pass
