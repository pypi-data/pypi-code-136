#!/usr/bin/env python

'''
face detection using haar cascades

USAGE:
    facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv
import re
import time

# local modules
#from video import create_capture
#from common import clock, draw_str

class VideoSynthBase(object):
    def __init__(self, size=None, noise=0.0, bg = None, **params):
        self.bg = None
        self.frame_size = (640, 480)
        if bg is not None:
            self.bg = cv.imread(cv.samples.findFile(bg))
            h, w = self.bg.shape[:2]
            self.frame_size = (w, h)

        if size is not None:
            w, h = map(int, size.split('x'))
            self.frame_size = (w, h)
            self.bg = cv.resize(self.bg, self.frame_size)

        self.noise = float(noise)

    def render(self, dst):
        pass

    def read(self, dst=None):
        w, h = self.frame_size

        if self.bg is None:
            buf = np.zeros((h, w, 3), np.uint8)
        else:
            buf = self.bg.copy()

        self.render(buf)

        if self.noise > 0.0:
            noise = np.zeros((h, w, 3), np.int8)
            cv.randn(noise, np.zeros(3), np.ones(3)*255*self.noise)
            buf = cv.add(buf, noise, dtype=cv.CV_8UC3)
        return True, buf

    def isOpened(self):
        return True

class Book(VideoSynthBase):
    def __init__(self, **kw):
        super(Book, self).__init__(**kw)
        backGr = cv.imread(cv.samples.findFile('graf1.png'))
        fgr = cv.imread(cv.samples.findFile('box.png'))
        self.render = TestSceneRender(backGr, fgr, speed = 1)

    def read(self, dst=None):
        noise = np.zeros(self.render.sceneBg.shape, np.int8)
        cv.randn(noise, np.zeros(3), np.ones(3)*255*self.noise)

        return True, cv.add(self.render.getNextFrame(), noise, dtype=cv.CV_8UC3)

class Cube(VideoSynthBase):
    def __init__(self, **kw):
        super(Cube, self).__init__(**kw)
        self.render = TestSceneRender(cv.imread(cv.samples.findFile('pca_test1.jpg')), deformation = True,  speed = 1)

    def read(self, dst=None):
        noise = np.zeros(self.render.sceneBg.shape, np.int8)
        cv.randn(noise, np.zeros(3), np.ones(3)*255*self.noise)

        return True, cv.add(self.render.getNextFrame(), noise, dtype=cv.CV_8UC3)

class Chess(VideoSynthBase):
    def __init__(self, **kw):
        super(Chess, self).__init__(**kw)

        w, h = self.frame_size

        self.grid_size = sx, sy = 10, 7
        white_quads = []
        black_quads = []
        for i, j in np.ndindex(sy, sx):
            q = [[j, i, 0], [j+1, i, 0], [j+1, i+1, 0], [j, i+1, 0]]
            [white_quads, black_quads][(i + j) % 2].append(q)
        self.white_quads = np.float32(white_quads)
        self.black_quads = np.float32(black_quads)

        fx = 0.9
        self.K = np.float64([[fx*w, 0, 0.5*(w-1)],
                        [0, fx*w, 0.5*(h-1)],
                        [0.0,0.0,      1.0]])

        self.dist_coef = np.float64([-0.2, 0.1, 0, 0])
        self.t = 0

    def draw_quads(self, img, quads, color = (0, 255, 0)):
        img_quads = cv.projectPoints(quads.reshape(-1, 3), self.rvec, self.tvec, self.K, self.dist_coef) [0]
        img_quads.shape = quads.shape[:2] + (2,)
        for q in img_quads:
            cv.fillConvexPoly(img, np.int32(q*4), color, cv.LINE_AA, shift=2)

    def render(self, dst):
        t = self.t
        self.t += 1.0/30.0

        sx, sy = self.grid_size
        center = np.array([0.5*sx, 0.5*sy, 0.0])
        phi = pi/3 + sin(t*3)*pi/8
        c, s = cos(phi), sin(phi)
        ofs = np.array([sin(1.2*t), cos(1.8*t), 0]) * sx * 0.2
        eye_pos = center + np.array([cos(t)*c, sin(t)*c, s]) * 15.0 + ofs
        target_pos = center + ofs

        R, self.tvec = common.lookat(eye_pos, target_pos)
        self.rvec = common.mtx2rvec(R)

        self.draw_quads(dst, self.white_quads, (245, 245, 245))
        self.draw_quads(dst, self.black_quads, (10, 10, 10))

classes = dict(chess=Chess, book=Book, cube=Cube)

presets = dict(
    empty = 'synth:',
    lena = 'synth:bg=lena.jpg:noise=0.1',
    chess = 'synth:class=chess:bg=lena.jpg:noise=0.1:size=640x480',
    book = 'synth:class=book:bg=graf1.png:noise=0.1:size=640x480',
    cube = 'synth:class=cube:bg=pca_test1.jpg:noise=0.0:size=640x480'
)

def create_capture(source = 0, fallback = presets['chess']):
    '''source: <int> or '<int>|<filename>|synth [:<param_name>=<value> [:...]]'
    '''
    source = str(source).strip()

    # Win32: handle drive letter ('c:', ...)
    source = re.sub(r'(^|=)([a-zA-Z]):([/\\a-zA-Z0-9])', r'\1?disk\2?\3', source)
    chunks = source.split(':')
    chunks = [re.sub(r'\?disk([a-zA-Z])\?', r'\1:', s) for s in chunks]

    source = chunks[0]
    try: source = int(source)
    except ValueError: pass
    params = dict( s.split('=') for s in chunks[1:] )

    cap = None
    if source == 'synth':
        Class = classes.get(params.get('class', None), VideoSynthBase)
        try: cap = Class(**params)
        except: pass
    else:
        cap = cv.VideoCapture(source)
        if 'size' in params:
            w, h = map(int, params['size'].split('x'))
            cap.set(cv.CAP_PROP_FRAME_WIDTH, w)
            cap.set(cv.CAP_PROP_FRAME_HEIGHT, h)
    if cap is None or not cap.isOpened():
        print('Warning: unable to open video source: ', source)
        if fallback is not None:
            return create_capture(fallback, None)
    return cap

def clock():
    return cv.getTickCount() / cv.getTickFrequency()

def draw_str(dst, target, s):
    x, y = target
    cv.putText(dst, s, (x+1, y+1), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv.LINE_AA)
    cv.putText(dst, s, (x, y), cv.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv.LINE_AA)

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

def main():
    import sys, getopt

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "haarcascades/haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "haarcascades/haarcascade_eye.xml")

    cascade = cv.CascadeClassifier(cv.samples.findFile(cascade_fn))
    nested = cv.CascadeClassifier(cv.samples.findFile(nested_fn))

#    cam = create_capture(video_src, fallback='synth:bg={}:noise=0.05'.format(cv.samples.findFile('lena.jpg')))

    ip_camera_url = 'http://admin:admin@192.168.120.74:8081/'
# 创建一个窗口
    cv.namedWindow('ip_camera', flags=cv.WINDOW_NORMAL | cv.WINDOW_FREERATIO)

    cam = cv.VideoCapture(ip_camera_url)

    if not cam.isOpened():
        print('请检查IP地址还有端口号，或者查看IP摄像头是否开启，另外记得使用sudo权限运行脚本')

    while cam.isOpened():
        while True:
            _ret, img = cam.read()
            cv.imshow('ip_camera', img)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            gray = cv.equalizeHist(gray)

            t = clock()
            rects = detect(gray, cascade)
            vis = img.copy()
            draw_rects(vis, rects, (0, 255, 0))
            if not nested.empty():
                for x1, y1, x2, y2 in rects:
                    roi = gray[y1:y2, x1:x2]
                    vis_roi = vis[y1:y2, x1:x2]
                    subrects = detect(roi.copy(), nested)
                    draw_rects(vis_roi, subrects, (255, 0, 0))
            dt = clock() - t

            draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
            cv.imshow('facedetect', vis)

            if cv.waitKey(5) == 27:
                break

        print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()

