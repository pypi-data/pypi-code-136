# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     flame
   Description :
   Author :       liaozhaoyan
   date：          2022/10/5
-------------------------------------------------
   Change Activity:
                   2022/10/5:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

import os
from treelib import Tree
from random import randrange
from .tag import T, SVG, Literal

flameHead = '''<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'''


def getCwd(pathStr):
    return os.path.split(os.path.realpath(pathStr))[0]


def joinCwd(path):
    return os.path.join(getCwd(__file__), path)


def flameColor():
    r = randrange(200, 255)
    g = randrange(0, r)
    b = randrange(0, 45)
    return "rgb(%d,%d,%d)" % (r, g, b)


class Flame(object):
    def __init__(self, filePath):
        super(Flame, self).__init__()
        self._file = filePath

        self._barBeg = 10
        self._barWidth = 1180
        self._barHeigh = 16.0
        self._rectHeigh = 15.0
        self._yBeg = 55

    def _loadCSS(self):
        fileName = joinCwd("flame.css")
        with open(fileName, "r") as f:
            s = f.read()
        return s

    def _loadScript(self):
        fileName = joinCwd("flameScript.js")
        with open(fileName, "r") as f:
            s = f.read()
        return s

    def _calY(self, beg, level):
        return beg - level * self._barHeigh

    def _calWidth(self, node, parent, pWidth, cbValue):
        if parent is None:
            return pWidth
        v1 = cbValue(node.data)
        v2 = cbValue(parent.data)
        return pWidth * v1 / v2

    def _setupFrame(self, tree, cbValue, cbNote):
        yBeg = self._yBeg + tree.depth() * self._barHeigh
        res = []
        stack = []   # contains x start, width, x + width
        for nid in tree.expand_tree(mode=Tree.DEPTH, sorting=False):
            node = tree.get_node(nid)
            parent = tree.parent(nid)
            level = tree.level(nid)

            if level == 0:
                x = self._barBeg
                y = yBeg
                width = self._barWidth
            else:
                x = stack[level - 1][0]
                if len(stack) > level:
                    x = stack[level][2]
                y = self._calY(yBeg, level)
                width = self._calWidth(node, parent, stack[level - 1][1], cbValue)
            if (len(node.tag) + 1) * 6 > width:
                text = " "
            else:
                text = node.tag
            g = T.g()(
                T.title("%s" % node.tag),
                T.desc("%s (%s)" % (node.tag, cbNote(tree, node))),
                T.rect(x=x, y=y,
                       width=width, height=self._barHeigh,
                       fill=flameColor(),
                       rx=2, ry=2),
                T.text(text, x=x+3, y=y+10.5)
            )
            if len(stack) > level:
                stack[level] = (x, width, x + width)
            else:
                stack.append((x, width, x + width))
            stack = stack[:level+1]
            res.append(g)
        return tuple(res)

    def _setupCells(self, tree, cbValue, cbNote, title):
        height = self._yBeg + (tree.depth() + 3) * self._barHeigh
        defs = T.defs()(
            T.linearGradient(id="background", y1=0, y2=1, x1=0, x2=0)(
                T.stop(stop_color="#eeeeee", offset="5%"),
                T.stop(stop_color="#eeeeb0", offset="95%"),
            ),
        )
        css = T.style(Literal(self._loadCSS(), esc=False), type="text/css")
        script = T.script(Literal(self._loadScript(), esc=False), type="text/ecmascript")
        rect = T.rect(x=0.0, y=0, width=1200.0, height=height, fill="url(#background)")
        title = T.text(title, id="title", x=600.00, y=24)
        details = T.text(" ", id="details", x=10.00, y=height - 1.0 * self._barHeigh)
        unzoom = T.text("Reset Zoom", id="unzoom", _class="hide", x=10.00, y=24)
        search = T.text("Search", id="search", x=1090, y=24)
        matched = T.text(id="matched", x=1090, y=height - 1.0 * self._barHeigh)
        frames = T.g(id="frames")(
            *self._setupFrame(tree, cbValue, cbNote)
        )
        return tuple([defs, css, script, rect, title, details, unzoom, search, matched, frames])

    def _setupRoot(self, tree, cbValue, cbNote, title):
        root = SVG(version="1.1",
                   width="1200",
                   height="870",
                   onload="init(evt)",
                   viewBox="0 0 1200 870",
                   useNS=True)(
            *self._setupCells(tree, cbValue, cbNote, title)
        )
        return root.build()

    def render(self, tree, cbValue, cbNote, title="Flame Graph"):
        s = flameHead
        s += self._setupRoot(tree, cbValue, cbNote, title)
        with open(self._file, 'w') as f:
            f.write(s)


if __name__ == "__main__":
    pass
