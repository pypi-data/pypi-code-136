import h5py
from ntsim.io.gEvent import gEvent
from ntsim.io.gProductionHeader import gProductionHeader
from ntsim.io.gPrimaryHeader import gPrimaryHeader
from ntsim.io.gEventHeader import gEventHeader
from ntsim.photonTransporters.mcPhotonTransport.Photon import Photon
import pandas as pd
import numpy as np
class h5Reader:
    def __init__(self,n_tracks_max=500000):
        self.n_tracks_max = n_tracks_max
        self.gEvent = gEvent()
        self.read_event_header_flag         = True
        self.read_event_photons_flag        = True
        self.read_event_hits_flag           = True
        self.read_event_photoelectrons_flag = True

    def set_read_event_header(self,flag=True):
        self.read_event_header_flag = flag

    def set_read_event_photons(self,flag=True):
        self.read_event_photons_flag = flag

    def set_read_event_photoelectrons(self,flag=True):
        self.read_event_photoelectrons_flag = flag

    def set_read_event_hits(self,flag=True):
        self.read_event_hits_flag = flag

    def open(self,filename):
        self.filename = filename
        self.h5_file =  h5py.File(filename, 'r')
#        self.read_run_header()

    def read_geometry(self):
        if 'geometry' in self.h5_file.keys():
            geometry = {}
            geometry_folder = self.h5_file['geometry']
            geometry['geom']                 = geometry_folder['geom'][:]
            geometry['bounding_box_strings'] = geometry_folder['bounding_box_strings'][:]
            geometry['bounding_box_cluster'] = geometry_folder['bounding_box_cluster'][:]
            geometry['det_normals']          = geometry_folder['det_normals'][:]
            return geometry
        else:
            return None

    def print_event(self,event):
        self.gEvent.print_event(event)

    def read_prod_header(self):
        if 'ProductionHeader' in self.h5_file.keys():
            prod_header = gProductionHeader()
            prod_header.set_scattering_model_name(self.h5_file['ProductionHeader/scattering_model'][()].decode())
            prod_header.set_anisotropy(self.h5_file['ProductionHeader/anisotropy'][()])
            prod_header.set_n_events(self.h5_file['ProductionHeader/n_events'][()])
            return prod_header
        else:
            return None

    def read_event_header(self,event_number):
        event_folder    = self.get_event_folder(event_number)
        if 'event_header' in event_folder.keys():
            event_header = gEventHeader()
            event_header.photons_sampling_weight = event_folder['event_header/photons_sampling_weight'][()]
            event_header.om_area_weight          = event_folder['event_header/om_area_weight'][()]
            vertex_list = []
            return event_header # FIXME no vertices yet
            node = 'event_header/vertices'
            if node in event.keys():
                vertices = self.h5_file['event_header/vertices']
                for iv, vname in enumerate(vertices.keys()):
                    g_vertex = vertices[vname]
                    g_in_particles  = g_vertex['in_particles']
                    g_out_particles = g_vertex['out_particles']
                    g_pos           = g_vertex['pos']

                    in_particles  = []
                    out_particles = []
                    pos           = g_pos[:]

                    for ip, pname in enumerate(g_in_particles.keys()):
                        particle = g_in_particles[pname][:]
                        in_particles.append(particle)
                    for ip, pname in enumerate(g_out_particles.keys()):
                        particle = g_out_particles[pname][:]
                        out_particles.append(particle)
                    v = (pos,in_particles,out_particles)
                    vertex_list.append(v)
            event_header.add_vertices(vertex_list)
            return event_header

    def get_event_folder(self,event_number):
        e = False
        node = f'event_{event_number}'
        if node in self.h5_file.keys():
            event_folder = self.h5_file[node]
            e = True
            return event_folder
        if not e:
            logger.warning(f'read_event. node {node} does not exist. skip it')
            return None

    def read_event(self,event):
        e = False
        node = f'event_{event}'
        if node in self.h5_file.keys():
            event = self.h5_file[node]
            e = True
        if not e:
            print(f'read_event. node {node} does not exist. skip it')
            return
        if self.read_event_header_flag:
            self.read_event_header(event)
        if self.read_event_photons_flag:
            self.read_photons(event)
        if self.read_event_hits_flag:
            self.read_hits(event)
        if self.read_event_photoelectrons_flag:
            self.read_photoelectrons(event)

    def read_hits(self,event_number):
        event_folder    = self.get_event_folder(event_number)
        hits = {}
        if 'hits' in event_folder.keys():
            data = event_folder['hits/data'][:]
            df = pd.DataFrame(data=data)
            h = df.to_records(index=False)
            for uid in df.uid.unique():
                hits[uid] = h[h['uid'] == uid]#.to_numpy()
            return hits


    def read_photons(self,event_number):
        #  check existence
        event_folder    = self.get_event_folder(event_number)
        n_bunches       = event_folder['n_bunches'][()]
        n_photons_total = event_folder['n_photons_total'][()]
        photons = Photon()
        if n_photons_total>self.n_tracks_max:
            # read a portion of photons
            fraction = np.float64(self.n_tracks_max/n_photons_total)
            print(fraction)
            for bunch in range(n_bunches):
                n_tracks       = event_folder[f'photons_{bunch}/n_tracks'][()]
                tracks_to_read = np.int(n_tracks*fraction)
                print(tracks_to_read,n_tracks)
                indices    = np.random.default_rng().integers(0,n_tracks,size=tracks_to_read)
                indices = np.sort(indices)
                print(indices)
                print(np.all(indices[1:] >= indices[:-1], axis=0))
                n_steps    = event_folder[f'photons_{bunch}/n_steps'][()]
#                r          = event_folder[f'photons_{bunch}/r'][:,indices,:]
                r          = event_folder[f'photons_{bunch}/r'][:]
                t          = event_folder[f'photons_{bunch}/t'][:]
                dir        = event_folder[f'photons_{bunch}/dir'][:]
                wavelength = event_folder[f'photons_{bunch}/wavelength'][:]
                ta         = event_folder[f'photons_{bunch}/ta'][:]
                ts         = event_folder[f'photons_{bunch}/ts'][:]
                r = r[:,indices,:]
                t = t[:,indices]
                dir = dir[:,indices,:]
                wavelength = wavelength[indices]
                ta = ta[indices]
                ts = ts[indices]
                new_photons = Photon()
                new_photons.init(n_tracks,n_steps,r,t,dir,wavelength,ta,ts)
                photons = photons.add_photons(new_photons)
            return photons
        else:
            for bunch in range(n_bunches):
                n_tracks   = event_folder[f'photons_{bunch}/n_tracks'][()]
                n_steps    = event_folder[f'photons_{bunch}/n_steps'][()]
                r          = event_folder[f'photons_{bunch}/r'][:]
                t          = event_folder[f'photons_{bunch}/t'][:]
                dir        = event_folder[f'photons_{bunch}/dir'][:]
                wavelength = event_folder[f'photons_{bunch}/wavelength'][:]
                ta         = event_folder[f'photons_{bunch}/ta'][:]
                ts         = event_folder[f'photons_{bunch}/ts'][:]
                new_photons = Photon()
                new_photons.init(n_tracks,n_steps,r,t,dir,wavelength,ta,ts)
                photons = photons.add_photons(new_photons)
            return photons
