from ntsim.viewer.viewer_base import viewerbase
import pyqtgraph.opengl as gl
import numpy as np
from pyqtgraph.Qt import QtGui

class geometry_viewer(viewerbase):
    def configure(self,opts):
        self.options = opts
        self.widgets['geometry'].opts['distance'] = self.options.distance
        g = gl.GLGridItem()
        g.scale(*self.options.grid_scale)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        # check if this widget is not added already
        if not self.widgets['geometry'] in self.docks['geometry'].widgets:
            self.docks['geometry'].addWidget(self.widgets['geometry'])
        ax = gl.GLAxisItem()
#        self.widgets['geometry'].addItem(ax)
        self.widgets['geometry'].addItem(g)
        self.om_positions   = {}
        self.om_normals     = {}
        self.om_prod_radius = {}
        self.om_true_radius = {}
        self.om_list = []
        self.bb_list = []

    def display_static(self):
        self.display_om()
#        self.display_bounding_boxes()


    def display_bounding_boxes(self,vis=False):
        if len(self.bb_list):
            self.setVisible_bb(vis)
            return
        bb_clusters = self.data['bounding_box_cluster']
        n_clusters = bb_clusters.shape[0]
        for icluster in range(n_clusters):
            self.box(bb_clusters[icluster],vis)

    def clear_om(self):
        for item in self.om_list:
            self.widgets['geometry'].removeItem(item)
        self.om_list = []

    def clear_bounding_boxes(self):
        for item in self.bb_list:
            self.widgets['geometry'].removeItem(item)
        self.bb_list = []

    def setVisible_om(self,vis):
        for item in self.om_list:
            item.setVisible(vis)

    def setVisible_bb(self,vis):
        for item in self.bb_list:
            item.setVisible(vis)

    def display_om(self,vis=False):
        if len(self.om_list):
            self.setVisible_om(vis)
            return
        (n_clusters,n_strings,n_om,n_vars) = self.data['geom'].shape
        for icluster in range(n_clusters):
            for istring in range(n_strings):
                for iom in range(n_om):
                    vars = self.data['geom'][icluster,istring,iom]
                    uid = vars[0]
                    x   = vars[1]
                    y   = vars[2]
                    z   = vars[3]
                    dir_x = vars[4]
                    dir_y = vars[5]
                    dir_z = vars[6]
                    prod_radius = vars[7]
                    true_radius = vars[8]
                    self.om_positions[uid]   = np.array([x,y,z])
                    self.om_normals[uid]     = np.array([dir_x,dir_y,dir_z])
                    self.om_prod_radius[uid] = prod_radius
                    self.om_true_radius[uid] = true_radius
                    #
                    sphere = gl.MeshData.sphere(rows=4, cols=8, radius=prod_radius)
                    opticalModule = gl.GLMeshItem(meshdata=sphere,smooth=False,drawFaces=False, drawEdges=True,color=[0.7, 0.7, 0.9, 0.8])
                    self.widgets['geometry'].show() # This is necessary since otherwise a segfault 11
                    self.widgets['geometry'].addItem(opticalModule)
                    self.om_list.append(opticalModule)
                    opticalModule.translate(x,y,z)
                    opticalModule.setVisible(vis)

    def display_bounding_boxes_test(self):
        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        self.widgets['geometry'].addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)

        gy.translate(0, -10, 0)
        self.widgets['geometry'].addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, -10)
        self.widgets['geometry'].addItem(gz)

    def box(self,bb,vis):
        xmin = bb[0]
        xmax = bb[1]
        ymin = bb[2]
        ymax = bb[3]
        zmin = bb[4]
        zmax = bb[5]
        lx = xmax-xmin
        ly = ymax-ymin
        lz = zmax-zmin

        def add_plane(size,spacing,shift,rotation=None):
            # Rotation and translation do not commute! Their order is of great importance
            plane = gl.GLGridItem(size=size)
            plane.setSpacing(spacing=spacing)
            if rotation is not None:
                plane.rotate(90,rotation.x(),rotation.y(),rotation.z())
            plane.translate(shift.x(),shift.y(),shift.z())
            self.widgets['geometry'].addItem(plane)
            self.bb_list.append(plane)
            plane.setVisible(vis)


        size    = QtGui.QVector3D(lx,ly,0)
        spacing = QtGui.QVector3D(10,10,0)
        shift_min   = QtGui.QVector3D(xmin+lx/2,ymin+ly/2,zmin)
        shift_max   = QtGui.QVector3D(xmin+lx/2,ymin+ly/2,zmax)

        add_plane(size=size,spacing=spacing,shift=shift_min)
        add_plane(size=size,spacing=spacing,shift=shift_max)

        size    = QtGui.QVector3D(lz,ly,0)
        spacing = QtGui.QVector3D(10,10,0)
        shift_min   = QtGui.QVector3D(xmin,ymin+ly/2,zmin+lz/2)
        shift_max   = QtGui.QVector3D(xmax,ymin+ly/2,zmin+lz/2)
        rotation = QtGui.QVector3D(0, 1, 0)

        add_plane(size=size,spacing=spacing,shift=shift_min,rotation=rotation)
        add_plane(size=size,spacing=spacing,shift=shift_max,rotation=rotation)

        size    = QtGui.QVector3D(lx,lz,0)
        spacing = QtGui.QVector3D(10,10,0)
        shift_min   = QtGui.QVector3D(xmin+lx/2,ymin,zmin+lz/2)
        shift_max   = QtGui.QVector3D(xmin+lx/2,ymax,zmin+lz/2)
        rotation = QtGui.QVector3D(1, 0, 0)

        add_plane(size=size,spacing=spacing,shift=shift_min,rotation=rotation)
        add_plane(size=size,spacing=spacing,shift=shift_max,rotation=rotation)

    def display_frame(self,frame):
        return
