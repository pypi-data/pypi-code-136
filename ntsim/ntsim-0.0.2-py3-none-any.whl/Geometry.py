from bgvd_model.GVDGeometry import GVDGeometry # FIXME must go outsude
import numpy as np
import configargparse
p = configargparse.get_argument_parser()
p.add_argument('--geometry_input',help='input file with geometry')
p.add_argument('--geometry_output',help='output file with geometry')
p.add_argument('--geometry_time_interval',nargs='+',help='time interval to read the geometry')
p.add_argument('--geometry_clusters',nargs='+',type=int,help='list of clusters')
p.add_argument('--geometry_true_radius',type=float,help='Optical Module true radius in m')
p.add_argument('--geometry_prod_radius',type=float,help='Optical Module production radius in m')


import logging
log = logging.getLogger('Geometry')

class Geometry():
    def __init__(self):
        self.module_type = 'auxiliary'
        self.df                   = 0
        self.geom                 = 0
        self.bounding_box_strings = 0
        self.bounding_box_cluster = 0
        self.bounding_box_gvd     = 0
        self.gvd_centre           = 0
        self.gvd_radius           = 0
        self.det_normals          = 0
        self.read_flag            = False

    def get(self):
        return self.geom

    def configure(self,opts):
        self.csv_input   = opts.geometry_input
        self.csv_output  = opts.geometry_output
        self.true_radius = opts.geometry_true_radius
        self.prod_radius = opts.geometry_prod_radius
        self.t1          = opts.geometry_time_interval[0]
        self.t2          = opts.geometry_time_interval[1]
        self.clusters    = opts.geometry_clusters
        self.build()
        log.info('configured')
        return

    def build(self):
        if self.read_flag:
            return
        geom = GVDGeometry()
        geom.read_csv(self.csv_input)
        geom.set_date_time_interval(self.t1,self.t2)
        df = geom.get_clusters(self.clusters)
        uid = df['cluster']*288+df['id']
        string = (df['id']/36).astype('int64')
        df.insert(5,"uid", uid, True)
        df.insert(6,"string", string, True)
#        df.replace({'dir_x'})
        df['dir_x'] = 0.
        df['dir_y'] = 0.
        df['dir_z'] = -1.
        df.insert(13,"true_radius", self.true_radius, True)
        df.insert(14,"prod_radius", self.prod_radius, True)
        self.df = df
        self.read_flag = True
        self.bounding_boxes()
#        print(self.df['id'])


    def bounding_boxes(self):
        clusters = self.df['cluster'].unique()
        strings  = self.df['string'].unique()
        uids     = self.df['uid'].unique()
#        print(clusters,strings)
        n_clusters = len(clusters)
        n_strings  = len(strings)
        self.bounding_box_strings = np.zeros(n_clusters*n_strings*6).reshape(n_clusters,n_strings,6)
        self.bounding_box_cluster = np.zeros(n_clusters*6).reshape(n_clusters,6)
        self.bounding_box_gvd     = np.zeros(6)
        n_om = 36
        n_vars = 9
        n_det = len(uids)
        self.geom = np.zeros(n_det*n_vars).reshape(n_clusters,n_strings,n_om,n_vars)
        self.det_normals = self.df[['dir_x','dir_y','dir_z']].to_numpy()

        for cluster in clusters:
            for string in strings:
                mask = (self.df['cluster'] == cluster) & (self.df['string'] == string)
                df = self.df[mask]
                x = df['x']
                y = df['y']
                z = df['z']
                r = df['prod_radius']
                xmin = np.amin(x-r)
                xmax = np.amax(x+r)
                ymin = np.amin(y-r)
                ymax = np.amax(y+r)
                zmin = np.amin(z-r)
                zmax = np.amax(z+r)
                self.bounding_box_strings[cluster,string][2*0]   = xmin
                self.bounding_box_strings[cluster,string][2*0+1] = xmax
                self.bounding_box_strings[cluster,string][2*1]   = ymin
                self.bounding_box_strings[cluster,string][2*1+1] = ymax
                self.bounding_box_strings[cluster,string][2*2]   = zmin
                self.bounding_box_strings[cluster,string][2*2+1] = zmax
                # make self.geom.geom array
                for i in range(n_om):
                    row = df.iloc[[i]]
                    v = row[['uid','x','y','z','dir_x','dir_y','dir_z','prod_radius','true_radius']].to_numpy()
                    self.geom[cluster,string,i] = v
            for i in range(3):
                xi_min = np.amin(self.bounding_box_strings[cluster,:,2*i])
                xi_max = np.amax(self.bounding_box_strings[cluster,:,2*i+1])
                self.bounding_box_cluster[cluster][2*i]   = xi_min
                self.bounding_box_cluster[cluster][2*i+1] = xi_max


        for i in range(3):

            gvd_xi_min = np.amin(self.bounding_box_cluster[:,2*i])
            gvd_xi_max = np.amax(self.bounding_box_cluster[:,2*i+1])

            self.bounding_box_gvd[2*i]   = gvd_xi_min
            self.bounding_box_gvd[2*i+1] = gvd_xi_max


        self.gvd_centre = np.array([0.5*(self.bounding_box_gvd[0]+self.bounding_box_gvd[1]),0.5*(self.bounding_box_gvd[2]+self.bounding_box_gvd[3]),0.5*(self.bounding_box_gvd[4]+self.bounding_box_gvd[5])])

        self.gvd_radius = 0.5*np.sqrt((self.bounding_box_gvd[0]-self.bounding_box_gvd[1])**2+(self.bounding_box_gvd[2]-self.bounding_box_gvd[3])**2)
