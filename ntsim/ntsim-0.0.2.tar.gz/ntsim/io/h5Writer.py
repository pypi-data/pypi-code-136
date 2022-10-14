import h5py
import numpy as np
import logging
logger = logging.getLogger('h5Writer')

import configargparse
p = configargparse.get_argument_parser()
p.add_argument("--h5_output_file",help="output file name")
p.add_argument("--h5_output_dir",help="output directory name")
p.add_argument("--h5_save_geometry",default=False,help="Boolean to save geometry")
p.add_argument("--h5_save_medium_model",default=False,help="Boolean to save water model: absorption & scattering")
p.add_argument("--h5_save_prod_header",default=False,help="Boolean to save production header")
p.add_argument("--h5_save_event_header",default=False,help="Boolean to save event header")
p.add_argument("--h5_save_primary_header",default=False,help="Boolean to save event header")
p.add_argument("--h5_save_tracks",type=bool,default=False,help="Boolean to save tracks")
p.add_argument("--h5_save_photons",type=bool,default=False,help="Boolean to save photons")
p.add_argument("--h5_save_hits",type=bool,default=False,help="Boolean to save hits")
p.add_argument("--h5_save_vertices",default=False,help="Boolean to save vertices")

class h5Writer:
    def __init__(self):
        self.event_folder = None

    def configure(self,options):
        self.save_event_header = options.h5_save_event_header
        self.save_tracks       = options.h5_save_tracks
        self.save_photons      = options.h5_save_photons
        self.save_hits         = options.h5_save_hits
        self.save_vertices     = options.h5_save_vertices
        self.h5_output_file    = options.h5_output_file
        self.h5_output_dir     = options.h5_output_dir
        self.save_geometry     = options.h5_save_geometry
        self.save_medium_model = options.h5_save_medium_model
        self.save_prod_header  = options.h5_save_prod_header
        self.save_primary_header  = options.h5_save_primary_header

        logger.info('configured')
        return

    def make_event_folder(self,n_events):
        self.event_folder = self.h5_file.create_group(f'event_{n_events}')

    '''
    # never called
    def write_event(self):
        event_folder = self.h5_file.create_group(f'event_{self.n_events}')
        if self.save_event_header:
            self.write_event_header(event_folder)
        if self.save_tracks:
            self.write_tracks(event_folder)
        if self.save_photons:
            self.write_photons(event_folder)
        if self.save_hits:
            self.write_hits(event_folder)
        self.n_events +=1
        return
    '''

    def init_h5(self):
        import os
        if not os.path.exists(self.h5_output_dir):
            os.makedirs(self.h5_output_dir)
        logger.info(f"open  {self.h5_output_dir}/{self.h5_output_file}.h5")
        self.h5_file =  h5py.File(f'{self.h5_output_dir}/{self.h5_output_file}.h5', 'w')

    def write_number_of_bunches(self,n_bunches,n_photons_total):
        self.event_folder.create_dataset("n_bunches", data=n_bunches)
        self.event_folder.create_dataset("n_photons_total", data=n_photons_total)


    def write_photons_bunch(self,photons,bunch_number):
        if not self.save_photons:
            return
        if photons:
            photons_folder = self.event_folder.create_group(f'photons_{bunch_number}')

            n_tracks   = photons.n_tracks
            n_steps    = photons.n_steps
            r          = photons.r
            t          = photons.t
            dir        = photons.dir
            wavelength = photons.wavelength
            ta         = photons.ta
            ts         = photons.ts

            dset_n_tracks   = photons_folder.create_dataset("n_tracks", data=n_tracks)
            dset_n_steps    = photons_folder.create_dataset("n_steps", data=n_steps)
            dset_r          = photons_folder.create_dataset("r",data=r)
            dset_t          = photons_folder.create_dataset("t",data=t)
            dset_dir        = photons_folder.create_dataset("dir",data=dir)
            dset_wavelength = photons_folder.create_dataset("wavelength",data=wavelength)
            dset_ta         = photons_folder.create_dataset("ta",data=ta)
            dset_ts         = photons_folder.create_dataset("ts",data=ts)

    def write_hits(self,hits):
        if not self.save_hits or hits is None:
            return
        #
        hits_folder = self.event_folder.create_group('hits')
        # name data fields
        data_type = [('uid', int), ('cluster', int), ('id', int),
                     ('time_ns', float),
                     ('w_noabs', float), ('w_pde', float), ('w_gel', float), ('w_angular', float),
                     ('x_m', float), ('y_m', float), ('z_m', float),
                     ('outside_mask', float), ('photon_id', int),
                     ('step_number', int)]
        named_hits = np.array([ tuple(row) for row in hits ], dtype=data_type)
        hits_folder.create_dataset('data', data=named_hits)

    def write_tracks(self,tracks):
        if not self.save_tracks or tracks == None or tracks == []:
            return
        #
        tracks_folder = self.event_folder.create_group('tracks')
        data_type = [('x_m', float), ('y_m', float), ('z_m', float), ('t_ns', float),
                     ('Px_GeV', float), ('Py_GeV', float), ('Pz_GeV', float), ('E_GeV', float)]
        for uid, track in tracks.items():
            track_folder = tracks_folder.create_group(f'track_{uid}')
            track_folder.create_dataset('pdg_id', data=track.pdg_id, dtype=int)
            # TODO It requires getting secondary particles during parent's tracking.
            # TODO This is not yet in geant4_pybind. 
#            parent_vertex = -1 # FIXME
#            named_parent = np.array([ tuple([track.parent[0], track.parent[1]]) ], dtype=[('particle_id', int), ('vertex_id', int)])
#            track_folder.create_dataset('parent', data=named_parent)
            track_folder.create_dataset('parent_id', data=track.parent_id, dtype=int)
            track_folder.create_dataset('status', data=0)
            named_points = np.array([ tuple(row) for row in track.points ], dtype=data_type)
            track_folder.create_dataset('points', data=named_points)

    def write_prod_header(self,productionHeader):
        if self.save_prod_header:
            g_header = self.h5_file.create_group('ProductionHeader')
            g_header.create_dataset("n_events",data=productionHeader.n_events)
            g_header.create_dataset("scattering_model",data=str(productionHeader.scattering_model_name))
            g_header.create_dataset("anisotropy",data=productionHeader.anisotropy)

    def write_primary_header(self,primHeader):
        if self.save_primary_header:
            g_header = self.h5_file.create_group('PrimaryHeader')
            g_header.create_dataset("name",data=primHeader.name)
            g_header.create_dataset("track",data=primHeader.track)


    def write_geometry(self,geometry):
        if self.save_geometry:
            geometry_folder = self.h5_file.create_group('geometry')
            geometry_folder.create_dataset('geom',data=geometry.geom)
            geometry_folder.create_dataset('bounding_box_strings',data=geometry.bounding_box_strings)
            geometry_folder.create_dataset('bounding_box_cluster',data=geometry.bounding_box_cluster)
            geometry_folder.create_dataset('det_normals',data=geometry.det_normals)

    def write_event_header(self,evtHeader):
        g_header = self.event_folder.create_group('event_header')
        g_header.create_dataset("photons_sampling_weight",data=evtHeader.get_photons_sampling_weight())
        g_header.create_dataset("om_area_weight",data=evtHeader.get_om_area_weight())
        if evtHeader.vertices == []:
            return g_header
        vertices = evtHeader.get_vertices()
        if len(vertices)==0:
            return
        g_vertices = g_header.create_group("vertices")
        ### "human readable structure"
        for iv, v in enumerate(vertices):
            pos           = v[0]
            in_particles  = v[1]
            out_particles = v[2]
            # create group for every vertex
            g_vertex = g_vertices.create_group(f"vertex{iv}")
            # convert data to tables with named columns
            pos_dtype = [("x_m", float), ("y_m", float), ("z_m", float), ("t_ns", float)]
            particle_dtype = [("PDGID", int), ("dir_x", float), ("dir_y", float), ("dir_z", float), ("E_GeV", float)]
            named_pos = np.array([ tuple(pos) ], dtype=pos_dtype)
            named_in_particles  = np.array([ tuple(row) for row in in_particles],  dtype=particle_dtype)
            named_out_particles = np.array([ tuple(row) for row in out_particles], dtype=particle_dtype)
            g_vertex.create_dataset("pos",data=named_pos)
            g_vertex.create_dataset("in_particles", data=named_in_particles)
            g_vertex.create_dataset("out_particles", data=named_out_particles)
        return g_header
        ### keep gEvent structure
        for iv, v in enumerate(vertices):
            pos           = v[0]
            in_particles  = v[1]
            out_particles = v[2]
            # create group for every vertex
            g_vertex = g_vertices.create_group(f"vertex{iv}")
            g_vertex.create_dataset("pos",data=pos)
            # create group for incoming particles to the vertex
            g_in_particles = g_vertex.create_group("in_particles")
            for ip, p in enumerate(in_particles):
                g_in_particles.create_dataset(f"particle{ip}",data=p) # format pdg, px,py,pz, E
            # create group for outgoing particles from the vertex
            g_out_particles = g_vertex.create_group("out_particles")
            for ip, p in enumerate(out_particles):
                g_out_particles.create_dataset(f"particle{ip}",data=p) # format pdg, px,py,pz, E


    def close(self):
        logger.info(f"close {self.h5_output_dir}/{self.h5_output_file}.h5")
        self.h5_file.close()
