import logging
import pathlib
from tqdm import tqdm
import datajoint as dj
import pandas as pd
import numpy as np
from tqdm import tqdm
import nrrd
import re


log = logging.getLogger(__name__)
schema = dj.schema()


def activate(schema_name, *, create_schema=True, create_tables=True):
    """
    activate(schema_name, create_schema=True, create_tables=True)
        :param schema_name: schema name on the database server to activate the
                            `coordinate_framework` element
        :param create_schema: when True (default), create schema in the database if it
                              does not yet exist.
        :param create_tables: when True (default), create tables in the database if
                              they do not yet exist.
    """
    schema.activate(
        schema_name, create_schema=create_schema, create_tables=create_tables
    )

    # ----------------------------- Table declarations ----------------------


@schema
class CCF(dj.Lookup):
    definition = """  # Common Coordinate Framework
    ccf_id            : int             # CCF ID, a.k.a atlas ID
    ---
    ccf_version       : varchar(64)     # Allen CCF Version - e.g. CCFv3
    ccf_resolution    : float           # voxel resolution in micron
    ccf_description='': varchar(255)    # CCFLabel Description
    """

    class Voxel(dj.Part):
        definition = """  # CCF voxel coordinates
        -> master
        x   :  int   # (um)  Anterior-to-Posterior (AP axis)
        y   :  int   # (um)  Superior-to-Inferior (DV axis)
        z   :  int   # (um)  Left-to-Right (ML axis)
        index(y, z)
        """


@schema
class BrainRegionAnnotation(dj.Lookup):
    definition = """
    -> CCF
    """

    class BrainRegion(dj.Part):
        definition = """
        -> master
        acronym: varchar(32)  # CHARACTER SET utf8 COLLATE utf8_bin
        ---
        region_name: varchar(128)
        region_id=null: int
        color_code=null: varchar(6)  # hexcode of the color code of this region
        """

    class Voxel(dj.Part):
        definition = """
        -> master.BrainRegion
        -> CCF.Voxel
        """

    @classmethod
    def retrieve_acronym(self, acronym):
        """Retrieve the DataJoint translation of the CCF acronym"""
        return re.sub(r"(?<!^)(?=[A-Z])", "_", acronym).lower()

    @classmethod
    def voxel_query(self, x=None, y=None, z=None):
        """Given one or more coordinates, return unique brain regions
        :param x: x coordinate
        :param y: y coordinate
        :param z: z coordinate
        """
        if not any(x, y, z):
            raise ValueError("Must specify at least one dimension")
        # query = self.Voxel  #  TODO: add utility function name lookup
        raise NotImplementedError("Coming soon")


@schema
class ParentBrainRegion(dj.Lookup):
    definition = """ # Hierarchical structure between the brain regionss
    -> BrainRegionAnnotation.BrainRegion
    ---
    -> BrainRegionAnnotation.BrainRegion.proj(parent='acronym')
    """


# ---- HELPERS ----


def load_ccf_annotation(
    ccf_id, version_name, voxel_resolution, nrrd_filepath, ontology_csv_filepath
):
    """
    :param ccf_id: unique id to identify a new CCF dataset to be inserted
    :param version_name: CCF version
    :param voxel_resolution: voxel resolution in micron
    :param nrrd_filepath: path to the .nrrd file for the volume data
    :param ontology_csv_filepath: path to the .csv file for the brain region ontology

    load_ccf_annotation(
        ccf_id=0, version_name='ccf_2017', voxel_resolution=10,
        nrrd_filepath='./data/annotation_10.nrrd',
        ontology_csv_filepath='./data/query.csv')

    For an example Allen brain atlas for mouse, see:
    http://download.alleninstitute.org/informatics-archive/current-release/mouse_ccf/annotation/ccf_2017

    For the structure/ontology tree, see:
    https://community.brain-map.org/t/allen-mouse-ccf-accessing-and-using-related-data-and-tools/359
    (particularly the ontology file downloadable as CSV)
    """
    ccf_key = {"ccf_id": ccf_id}
    if CCF & ccf_key:
        print(f"CCF ID {ccf_id} already exists!")
        return

    nrrd_filepath = pathlib.Path(nrrd_filepath)
    ontology_csv_filepath = pathlib.Path(ontology_csv_filepath)

    def to_snake_case(s):
        return re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()

    ontology = pd.read_csv(ontology_csv_filepath)

    stack, hdr = nrrd.read(nrrd_filepath.as_posix())  # AP (x), DV (y), ML (z)

    log.info(
        ".. loaded atlas brain volume of shape " + f"{stack.shape} from {nrrd_filepath}"
    )

    ccf_key = {"ccf_id": ccf_id}
    ccf_entry = {
        **ccf_key,
        "ccf_version": version_name,
        "ccf_resolution": voxel_resolution,
        "ccf_description": (
            f"Version: {version_name}"
            + f" - Voxel resolution (uM): {voxel_resolution}"
            + f" - Volume file: {nrrd_filepath.name}"
            + " - Region ontology file: "
            + ontology_csv_filepath.name
        ),
    }

    with dj.conn().transaction:
        CCF.insert1(ccf_entry)
        BrainRegionAnnotation.insert1(ccf_key)
        BrainRegionAnnotation.BrainRegion.insert(
            [
                dict(
                    ccf_id=ccf_id,
                    acronym=to_snake_case(r.acronym),
                    region_id=r.id,
                    region_name=r.safe_name,
                    color_code=r.color_hex_triplet,
                )
                for _, r in ontology.iterrows()
            ]
        )

        # Process voxels per brain region
        for idx, (region_id, r) in enumerate(tqdm(ontology.iterrows())):
            dj.conn().ping()
            region_id = int(region_id)

            log.info(
                ".. loading region {} ({}/{}) ({})".format(
                    region_id, idx, len(ontology), r.safe_name
                )
            )

            # extracting filled volumes from stack in scaled [[x,y,z]] shape,
            vol = np.array(np.where(stack == region_id)).T * voxel_resolution
            vol = pd.DataFrame(vol, columns=["x", "y", "z"])

            if not vol.shape[0]:
                log.info(
                    ".. region {} volume: shape {} - skipping".format(
                        region_id, vol.shape
                    )
                )
                continue
            else:
                log.info(".. region {} volume: shape {}".format(region_id, vol.shape))

            vol["ccf_id"] = [ccf_key["ccf_id"]] * len(vol)
            CCF.Voxel.insert(vol)

            vol["acronym"] = [to_snake_case(r.acronym)] * len(vol)
            BrainRegionAnnotation.Voxel.insert(vol)

    log.info(".. done.")


def load_parent_regions(ccf_id):
    raise NotImplementedError("Coming soon")
