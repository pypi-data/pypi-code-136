# external trigger
# self trigger
import numpy as np

def get_t0(packets):

    pckts_t0 = packets[packets['packet_type'] == 7]
    n_grps = len(np.unique(pckts_t0['io_group']))

    return pckts_t0['timestamp'].reshape(-1, n_grps)


def packet_to_eventid(assn, tracks):
    '''
    Assoiciate packet to eventID.
    
    Arguments
    ---------
    assn : array_like
        packet to track association (`mc_packets_assn`) from `larnd-sim` output
        
    tracks: array_like
        list of track segments
        
    Returns
    -------
    event_ids: ndarray (N,)
        array of eventID.
        `len(event_ids)` equals to `len(packets)`
    '''
    track_ids = assn['track_ids'].max(axis=-1)
    
    event_ids = np.full_like(track_ids, -1, dtype=int)
    mask = track_ids != -1
    event_ids[mask] = tracks['eventID'][track_ids[mask]]
    
    return event_ids
