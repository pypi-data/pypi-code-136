from ntsim.viewer.viewer_base import viewerbase
import pyqtgraph.opengl as gl
import numpy as np
from pyqtgraph.Qt import QtGui
import pyqtgraph as pg

class hits_viewer(viewerbase):
    def configure(self,opts):
        self.options = opts
        self.widgets['geometry'].opts['distance'] = self.options.distance
        g = gl.GLGridItem()
        g.scale(*self.options.grid_scale)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        # check if this widget is not added already
        if not self.widgets['geometry'] in self.docks['geometry'].widgets:
            self.docks['geometry'].addWidget(self.widgets['geometry'])

    def hits_analysis(self):
        self.hits_time_histos = {}
        evtHeader = self.data['event_header']
        photons_sampling_weight = evtHeader['photons_sampling_weight']
        om_area_weight = evtHeader['om_area_weight']
        for uid in self.data['hits']:
            hits = self.data['hits'][uid]
            weights = hits.w_noabs*hits.w_pde*hits.w_gel*hits.w_angular*photons_sampling_weight*om_area_weight
            self.hits_time_histos[uid] = np.histogram(hits.time_ns,bins=self.frames,weights=weights)
            v = np.cumsum(self.hits_time_histos[uid][0])[-1]
            if v>=1:
                print(v,hits.time_ns)
            print(hits.w_noabs,hits.w_pde,hits.w_gel,hits.w_angular)
#            print(hits.time_ns,self.frames)
    def display_static(self):
        pass

    def display_frame(self,frame):
        pass
