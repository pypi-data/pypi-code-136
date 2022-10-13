# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pakcer
   Description :
   Author :       liaozhaoyan
   date：          2022/10/3
-------------------------------------------------
   Change Activity:
                   2022/10/3:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

svgHead = '''<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20001102//EN"
"http://www.w3.org/TR/2000/CR-SVG-20001102/DTD/svg-20001102.dtd">\n'''


class Packer(object):
    def __init__(self, filePath):
        super(Packer, self).__init__()
        self._path = filePath

    def render(self, svg):
        s = svgHead + svg.build()
        with open(self._path, "w") as f:
            f.write(s)


if __name__ == "__main__":
    pass
