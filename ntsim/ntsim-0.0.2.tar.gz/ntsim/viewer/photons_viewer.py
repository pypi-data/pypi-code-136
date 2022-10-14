from ntsim.viewer.viewer_base import viewerbase
import pyqtgraph.opengl as gl
import numpy as np
from pyqtgraph.Qt import QtGui
import pyqtgraph as pg

class photons_viewer(viewerbase):
    def configure(self,opts):
        self.options = opts
        self.widgets['geometry'].opts['distance'] = self.options.distance
        g = gl.GLGridItem()
        g.scale(*self.options.grid_scale)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        # check if this widget is not added already
        if not self.widgets['geometry'] in self.docks['geometry'].widgets:
            self.docks['geometry'].addWidget(self.widgets['geometry'])
        # add photons object
        self.tracks_obj_static = []
        self.tracks_obj_animated = {}


    def display_static(self,vis=False):
        if len(self.tracks_obj_static):
            for item in self.tracks_obj_static:
                item.setVisible(vis)
            return
#            self.clean_static()
        x = self.data.r[:,:,0]
        y = self.data.r[:,:,1]
        z = self.data.r[:,:,2]
        t = self.data.t
        pos = np.array([x[:,:], y[:,:], z[:,:]]).T
#        self.widgets['geometry'].show() # This is necessary since otherwise a segfault 11
        for step in range(self.data.n_steps):
            travel_time = self.data.t[step,:]-self.data.t[0,:]
            colors = self.get_absorption_colors(travel_time,self.data.ta)
            points = gl.GLScatterPlotItem(pos=pos[:,step,:], color = colors, size=1, pxMode=False)
            points.setVisible(vis)
            self.tracks_obj_static.append(points)
            self.widgets['geometry'].addItem(self.tracks_obj_static[step])

    def clean_static(self):
        if len(self.tracks_obj_static):
            for step in range(self.data.n_steps):
                self.widgets['geometry'].removeItem(self.tracks_obj_static[step])
            self.tracks_obj_static = []

    def clean_animated(self):
        for frame in self.tracks_obj_animated:
            self.widgets['geometry'].removeItem(self.tracks_obj_animated[frame])
            self.tracks_obj_animated = {}

    def get_absorption_colors(self,t,ta):
        weight = np.exp(-t/ta)
        colors = pg.colormap.get('CET-R3').map(weight)/255
        colors[:,3] = 1.0
        return colors

    def clean_view(self):
        self.clean_static()
        self.clean_animated()

    def setVisible_photons_static(self,vis):
        for item in self.tracks_obj_static:
            item.setVisible(vis)

    def setVisible_photons_animated(self,vis):
        for frame in self.tracks_obj_animated:
            self.tracks_obj_animated[frame].setVisible(vis)

    def display_frame(self,frame,vis):
        # make all other frames invisible except the requisted frame
        for f in self.tracks_obj_animated:
            if f == frame:
                self.tracks_obj_animated[f].setVisible(vis)
            else:
                self.tracks_obj_animated[f].setVisible(False)
        # check if this frame is already computed
        if frame not in self.tracks_obj_animated:
            # this frame is not found. compute it, add to self.tracks_obj_animated

#            self.clean_view()
#            self.setVisible_photons_static(False)
            time_tick = np.array([self.frames[frame]])
            x_interp, y_interp, z_interp  = self.data.position(time_tick)
            pos = np.array([x_interp, y_interp, z_interp]).T
            travel_time = self.frames[frame]-self.data.t[0,:]
            colors = self.get_absorption_colors(travel_time,self.data.ta)
            mask   = np.isfinite(pos[:,:,0])
            pos    = pos[mask]
            colors = colors[None,:,:][mask]
            total  = len(pos)
            if total:
                self.tracks_obj_animated[frame] = gl.GLScatterPlotItem(pos=pos, color = colors, size=1)
                self.widgets['geometry'].addItem(self.tracks_obj_animated[frame])
                self.tracks_obj_animated[frame].setVisible(vis)
