import pyqtgraph as pg
import pyqtgraph.opengl as gl
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QGridLayout, QLabel,
                            QMainWindow, QWidget, QOpenGLWidget, QPushButton,QRadioButton)
from pyqtgraph.dockarea import *
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph import LayoutWidget
import pyqtgraph.console
import pyqtgraph.parametertree as ptree
import numpy as np
import os

from ntsim.viewer.viewer_base import viewerbase
from ntsim.viewer.geometry_viewer import geometry_viewer
from ntsim.viewer.photons_viewer import photons_viewer
from ntsim.viewer.hits_viewer import hits_viewer

from ntsim.io.h5Reader import h5Reader
import logging
log=logging.getLogger('h5viewer')
logformat='[%(name)20s ] %(levelname)8s: %(message)s'
logging.basicConfig(format=logformat)

import numpy as np
class h5Viewer(QMainWindow):
    sigKeyPress = QtCore.pyqtSignal(object)
    def __init__(self):
        super().__init__()
        self.initStateWidget()
        self.initReader()
        self.initDocks()
        self.initWidgets()
        self.createViewers()

    def init(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)
        self.dockPlacement()
        self.makeButtons()
        layout.addWidget(self.dockarea)
        self.openFile()
        self.readProductionHeader()
        self.readGeometry()
        self.initGeometryViewer()
        self.initTimer()
        self.readEvent()
        self.initPhotonsViewer()
        self.initHitsViewer()
        self.drawEvent()


    def initStateWidget(self):
        self.state_dict = {}
        self.state_tree = pg.DataTreeWidget()

    def initDocks(self):
        self.dockarea = DockArea()
        self.docks = {}
        self.docks["geometry"]  = Dock("geometry", size=(500,300))
        self.docks["events"]    = Dock("events", size=(10,10))
        self.docks["console"]   = Dock("console", size=(100,100))
        self.docks["Parameters"]= Dock("Parameters", size=(10,120))

    def dockPlacement(self):
        self.dockarea.addDock(self.docks["geometry"],'top')
        self.dockarea.addDock(self.docks["console"],'bottom')
        self.dockarea.addDock(self.docks["Parameters"],'right',self.docks["console"])
        self.dockarea.addDock(self.docks["events"],'right',self.docks["Parameters"])

    def initWidgets(self):
        self.widgets = {}
        self.widgets['geometry'] = gl.GLViewWidget()
        self.widgets['geometry'].show()
        self.initParametersWidget()

    def configure(self,opts):
        self.options       = opts
        self.h5_file       = opts.h5_file
        self.anim_status   = 'stop'
        self.event_number  = opts.event_number
        self.timerDelay    = opts.timerDelay
        self.n_frames_anim = int(opts.animation_frames[0])
        self.t_min_anim    = opts.animation_frames[1]
        self.t_max_anim    = opts.animation_frames[2]
        self.frames        = np.linspace(self.t_min_anim,self.t_max_anim,self.n_frames_anim)
        self.frame_number  = 0
        self.geometry_viewer.configure(opts)
        self.photons_viewer.configure(opts)

    def initReader(self):
        self.h5reader = h5Reader()

    def openFile(self):
        if not os.path.exists(self.h5_file):
            log.warning(f'file {self.h5_file} does not exist. Click open file')
            self.msg_file_status.setText("no file opened. click on open h5 to select a h5 file.")
            return
        self.h5reader.open(self.h5_file)
#        self.msg_file_status.setText(f"open {self.h5_file}")

    def readGeometry(self):
        self.geometry = self.h5reader.read_geometry()

    def readProductionHeader(self):
        self.productionHeader = self.h5reader.read_prod_header()
        self.add_state_info('ProductionHeader')


    def readEventHeader(self):
        log.debug(f'readEventHeader for event {self.event_number}')
        self.eventHeader = self.h5reader.read_event_header(self.event_number)
        self.add_state_info('EventHeader')


    def add_state_info(self,key):
        if key == 'ProductionHeader':
            self.state_dict['ProductionHeader'] = {'filename': self.h5_file,
                                                   'n_events': self.productionHeader.n_events,
                                                   'anisotropy': self.productionHeader.anisotropy,
                                                   'scattering_model':str(self.productionHeader.scattering_model_name)}
        elif key == 'EventHeader':
            self.state_dict['EventHeader'] = {'event number': self.event_number,
                                              'photons_sampling_weight': self.eventHeader.photons_sampling_weight,
                                              'om_area_weight':self.eventHeader.om_area_weight}
        elif key == 'Photons':
            self.state_dict['Photons'] = {'n_total': self.photons.n_tracks, 'n_steps': self.photons.n_steps}
        elif key == 'Hits':
            self.state_dict['Hits'] = 1  #FIXME!

    def readPhotons(self):
        self.photons = self.h5reader.read_photons(self.event_number)
        self.add_state_info('Photons')

    def readHits(self):
        self.hits = self.h5reader.read_hits(self.event_number)
        self.add_state_info('Hits')
#        log.debug(self.hits)

    def updateStateTree(self):
        self.state_tree.setData(self.state_dict)

    def readEvent(self):
        self.readEventHeader()
        self.readPhotons()
        self.readHits()
        self.updateStateTree()


    def makeButtons(self):
        self.buttons = {}
        self.buttons['open']      = QPushButton("open h5")
        self.buttons['next']      = QPushButton("next")
        self.buttons['previous']  = QPushButton("previous")
        self.buttons['animation'] = QPushButton("start animation")
        self.buttons['pause']     = QPushButton("pause")
        self.buttons['pause'].setVisible(False)

        # connect push to class methods calls
        self.buttons['open'].clicked.connect(self.FileDialog)
        self.buttons['next'].clicked.connect(self.next)
        self.buttons['previous'].clicked.connect(self.previous)
#        self.msg_file_status.setText("no file opened. click on open h5 to select a h5 file.")
        self.buttons['animation'].clicked.connect(self.animate)
        self.buttons['pause'].clicked.connect(self.pause)

        # add buttons to docks
        self.docks["events"].addWidget(self.buttons['open'])
        self.docks["events"].addWidget(self.buttons['next'])
        self.docks["events"].addWidget(self.buttons['previous'])
        self.docks["events"].addWidget(self.buttons['animation'])
        self.docks["events"].addWidget(self.buttons['pause'])

        self.docks["console"].addWidget(self.state_tree)

    def FileDialog(self):
        self.anim_status = 'stop'
        self.timer.stop()
        self.frame_number  = 0
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilter("*.h5") # FIXME does not filter
        self.h5_file = dialog.getOpenFileName()[0]
        self.openFile()
#        self.next()

    def next(self):
        if self.event_number <self.productionHeader.n_events-1:
            self.event_number += 1
        self.clean_view()
        self.readEvent()
        self.initPhotonsViewer()
        self.drawEvent()

    def previous(self):
        if self.event_number != 0:
            self.event_number -= 1
        self.clean_view()
        self.readEvent()
        self.initPhotonsViewer()
        self.drawEvent()

    def animate(self):
        self.change_timer_status()
        self.drawEvent()

    def pause(self):
        if self.timer.isActive():
            self.timer.stop()
            self.buttons['pause'].setText("continue")
        else:
            self.timer.start(self.timerDelay)
            self.buttons['pause'].setText("pause")


    def setVisible_pause_button(self,vis):
        self.buttons['pause'].setVisible(vis)
        if vis == True:
            self.buttons['pause'].setText("pause")


    def change_timer_status(self):
        if self.anim_status == 'stop':
            self.anim_status = 'start'
            self.buttons['animation'].setText("stop animation")
            self.setVisible_pause_button(True)
            self.timer.start(self.timerDelay)
        elif self.anim_status == 'start':
            self.anim_status = 'stop'
            self.buttons['animation'].setText("start animation")
            self.setVisible_pause_button(False)
            self.timer.stop()

    def initTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.drawEventAnimated)


    def createViewers(self):
        # geometry viewer
        self.geometry_viewer = geometry_viewer()
        self.geometry_viewer.set_docks(self.docks)
        self.geometry_viewer.set_widgets(self.widgets)
        # photons viewer
        self.photons_viewer  = photons_viewer()
        self.photons_viewer.set_docks(self.docks)
        self.photons_viewer.set_widgets(self.widgets)
        # hits viewer
        self.hits_viewer = hits_viewer()
        self.hits_viewer.set_docks(self.docks)
        self.hits_viewer.set_widgets(self.widgets)

    def initGeometryViewer(self):
        self.geometry_viewer.set_data(self.geometry)

    def initPhotonsViewer(self):
        self.photons_viewer.set_data(self.photons)
        self.photons_viewer.set_frames(self.frames)

    def initHitsViewer(self):
        data = {}
        data['hits'] = self.hits
        data['event_header'] = self.state_dict['EventHeader']
        self.hits_viewer.set_data(data)
        self.hits_viewer.set_frames(self.frames)
        self.hits_viewer.hits_analysis()

    def initParametersWidget(self):
        children = []
        children.append(dict(name='show_modules',  title='show_modules', type='bool', value=False))
        children.append(dict(name='show_boxes',    title='show_boxes',   type='bool', value=False))
        children.append(dict(name='show_hits',     title='show_hits',    type='bool', value=False))
        children.append(dict(name='show_photons',  title='show_photons', type='bool', value=False))
        children.append(dict(name='show_tracks',   title='show_tracks',  type='bool', value=False))
#        children.append(dict(name='animate',       title='animate', type='bool', value=False))

        self.params = ptree.Parameter.create(name='Display options', type='group', children=children)
        self.params.sigTreeStateChanged.connect(self.parametersChanged)

        for c in self.params.children():
            c.setDefault(c.value())
        t = ptree.ParameterTree(showHeader=False)
        t.setParameters(self.params)
        self.docks['Parameters'].addWidget(t)

    def parametersChanged(self,param, changes):

        for param, change, data in changes:
            path = self.params.childPath(param)
            if path is not None:
                childName = '.'.join(path)
            else:
                childName = param.name()
            log.debug('parameter: %s'% childName)
            log.debug('change:    %s'% change)
            log.debug('data:      %s'% str(data))
        self.update_visibility(childName,data)

    def update_visibility(self,name,value):
        if name == 'show_modules':
            self.geometry_viewer.setVisible_om(value)
        elif name == 'show_boxes':
            self.geometry_viewer.setVisible_bb(value)
        elif name == 'show_photons':
            if self.anim_status == 'start': # animation ongoing
                self.photons_viewer.setVisible_photons_animated(value)
            else:
                self.photons_viewer.setVisible_photons_static(value)


    def setStaticVis(self,vis):
        self.photons_viewer.setVisible_photons_static(vis)

    def setAnimatedVis(self,vis):
        self.photons_viewer.setVisible_photons_animated(vis)

    def drawEvent(self):
        if self.anim_status == 'start':
            self.setStaticVis(False)
            self.drawEventAnimated()
        elif self.anim_status == 'stop':
            self.setStaticVis(True)
            self.setAnimatedVis(False)
            self.drawEventStatic()

    def clean_view(self):
        self.photons_viewer.clean_view()

    def drawEventStatic(self):
        for par in self.params.children():
            if par.name() == 'show_modules':
                self.geometry_viewer.display_om(par.value())
            elif par.name() == 'show_boxes':
                self.geometry_viewer.display_bounding_boxes(par.value())
            elif par.name() == 'show_photons':
                self.photons_viewer.display_static(par.value())

    def drawEventAnimated(self):
        if self.frame_number >= len(self.frames):
            self.frame_number = 0
        for par in self.params.children():
            if par.name() == 'show_photons':
                self.photons_viewer.display_frame(self.frame_number,par.value())
        self.frame_number += 1

def run(opts) -> None:
    app = QApplication(sys.argv)
    viewer = h5Viewer()
    viewer.configure(opts)
    viewer.init()
    viewer.setWindowTitle('gvdViewer: a lightweight 3D visualization of the generators events')
    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()
    width, height = width*opts.screen_fraction[0], height*opts.screen_fraction[1]
    viewer.resize(int(width), int(height))
    viewer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    import configargparse
    p = configargparse.get_argument_parser()
    p.add_argument("--h5viewer-config", is_config_file=True,default='configs/h5viewer.cfg',help="Config for h5viewer and its brothers")
    p.add_argument('-prefix', '--generators_path', help='path to GENERATORS [ENV]', env_var='GENERATORS')  # this option can be set in a config file because it starts with '--'
    p.add_argument("--viewers",nargs='+',type=str,default=[],help="list of viewers to test")
    p.add_argument("--distance",type=float,default=1200,help="OpenGL view distance")
    p.add_argument("--grid_scale",nargs='+',type=int,help="grid scale")
    p.add_argument("--h5_file",type=str,default='h5_output/events.h5',help="path to h5 file")
    p.add_argument("--event_number",type=int,default=0,help="event number to view")
    p.add_argument("--screen_fraction",nargs='+',type=float,default=(0.9,0.9),help="(x,y) fraction of the screen for the viewer")
    p.add_argument('-l', '--log-level', choices=('deepdebug', 'debug', 'info', 'warning', 'error', 'critical'), default='INFO', help='logging level')
    p.add_argument("--timerDelay",type=float,default=150,help="timer delay in ms")
    p.add_argument("--animation_frames",nargs='+',type=float,default=(100,0,3000),help="(n,t1,t2), where n = number of frames, (t1,t2) = time interval")

    opts = p.parse_args()
    log.setLevel(logging.getLevelName(opts.log_level.upper()))
    logging.root.setLevel(logging.getLevelName(opts.log_level.upper()))  # set global logging level
    run(opts)
else:
    from types import SimpleNamespace
    opts = SimpleNamespace()
    opts.h5viewer_config='configs/h5viewer.cfg'
    opts.distance = 1200
    opts.h5_file = 'h5_output/events.h5'
    opts.event_number = 0
    opts.timerDelay = 150
    opts.animation_frames = (100,0,3000)
    opts.screen_fraction = (0.9,0.9)
    opts.grid_scale = [ 20, 20, 1 ]
    run(opts)
