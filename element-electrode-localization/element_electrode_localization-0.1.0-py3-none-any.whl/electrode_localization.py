import importlib
import inspect
import pathlib
import json
import logging
import datajoint as dj
import numpy as np

from . import coordinate_framework

schema = dj.schema()

log = logging.getLogger(__name__)

_linking_module = None
ProbeInsertion, probe = None, None


def activate(
    electrode_localization_schema_name,
    coordinate_framework_schema_name=None,
    *,
    create_schema=True,
    create_tables=True,
    linking_module=None,
):
    """
    activate(electrode_localization_schema_name, coordinate_framework_schema_name=None,
             *, create_schema=True, create_tables=True, linking_module=None)
        :param electrode_localization_schema_name: schema name on the database server to
                                           activate the `electrode_localization` element
        :param coordinate_framework_schema_name: schema name on the database server to
                                            activate the `coordinate_framework` element.
                                            May be omitted if already activated
        :param create_schema: when True (default), create schema in the database if it
                              does not yet exist.
        :param create_tables: when True (default), create tables in the database if they
                              do not yet exist.
        :param linking_module: a module name or a module containing the
         required dependencies to activate the `electrode_localization` element:
            Upstream tables:
                + ProbeInsertion: table referenced by ElectrodePosition, typically
                                  identifying a Probe Insertion instance
                + probe: the probe schema - from element-array-ephys
    """

    if isinstance(linking_module, str):
        linking_module = importlib.import_module(linking_module)
    assert inspect.ismodule(
        linking_module
    ), "The argument 'dependency' must be a module's name or a module"

    global _linking_module, ProbeInsertion, probe
    _linking_module = linking_module
    ProbeInsertion = _linking_module.ProbeInsertion
    probe = _linking_module.probe

    # activate
    coordinate_framework.activate(
        coordinate_framework_schema_name,
        create_schema=create_schema,
        create_tables=create_tables,
    )
    schema.activate(
        electrode_localization_schema_name,
        create_schema=create_schema,
        create_tables=create_tables,
        add_objects=_linking_module.__dict__,
    )


# --------------- Functions required by element-electrode-localization  ----------------


def get_electrode_localization_dir(probe_insertion_key: dict) -> str:
    """
    Retrieve the electrode localization directory associated with a ProbeInsertion
        The directory should contain `channel_locations.json` files (one per shank)
        for the corresponding `probe_insertion_key`
    :param probe_insertion_key: key of a ProbeInsertion
    :return: full file-path of the electrode localization dir
    """
    return _linking_module.get_electrode_localization_dir(probe_insertion_key)


# ------------------------------------ Table declarations -----------------------------


@schema
class ElectrodePosition(dj.Imported):
    definition = """
    -> ProbeInsertion
    -> coordinate_framework.CCF
    """

    class Electrode(dj.Part):
        definition = """
        -> master
        -> probe.ProbeType.Electrode
        ---
        -> coordinate_framework.CCF.Voxel
        """

    def make(self, key):
        skipped_electrode_count = 0
        voxel_resolution = (coordinate_framework.CCF & key).fetch1("ccf_resolution")
        electrode_location_dir = pathlib.Path(get_electrode_localization_dir(key))
        assert electrode_location_dir.exists()

        channel_locations_files = list(
            electrode_location_dir.glob("*channel_locations*.json")
        )

        electrodes_query = (
            probe.ProbeType.Electrode * probe.Probe * ProbeInsertion & key
        )
        probe_type = (probe.Probe * ProbeInsertion & key).fetch1("probe_type")

        shanks = np.unique(electrodes_query.fetch("shank"))

        if len(channel_locations_files) == 1:
            corresponding_shanks = [0]
            if len(shanks) != 1:
                raise ValueError(
                    "Only 1 file found ({}) for a {}-shank probe".format(
                        channel_locations_files[0].name, len(shanks)
                    )
                )
            if (
                "shank" in channel_locations_files[0].stem
                and channel_locations_files[0].stem[-1] != 1
            ):
                raise ValueError(
                    "The electrode-location file found ({}) is "
                    + "unexpected for this 1-shank probe"
                )
        else:
            if len(channel_locations_files) != len(shanks):  # ensure 1 file per shank
                raise ValueError(
                    f"{len(channel_locations_files)} files found for a "
                    + f"{len(shanks)}-shank probe"
                )
            corresponding_shanks = [int(f.stem[-1]) for f in channel_locations_files]

        # Insertion
        self.insert1(key)

        for channel_locations_file, shank_no in zip(
            channel_locations_files, corresponding_shanks
        ):

            log.debug(f"loading channel locations from {channel_locations_file}")
            with open(channel_locations_file, "r") as fh:
                chn_loc_raw = json.loads(fh.read())

            chn_loc_data = {"origin": chn_loc_raw["origin"]}

            if len(chn_loc_data["origin"]) > 1:
                log.error(
                    "More than one origin region found ({}). skipping.".format(
                        chn_loc_data["origin"]
                    )
                )
                raise ValueError(
                    "More than one origin region found " + f'({chn_loc_data["origin"]})'
                )

            # ensuring channel data is sorted;
            chn_loc_keymap = {
                int(k.split("_")[1]): k for k in chn_loc_raw if "channel_" in k
            }

            chn_loc_data["channels"] = np.array(
                [
                    tuple(chn_loc_raw[chn_loc_keymap[k]].values())
                    for k in sorted(chn_loc_keymap)
                ],
                dtype=[
                    ("x", float),
                    ("y", float),
                    ("z", float),
                    ("axial", float),
                    ("lateral", float),
                    ("brain_region_id", int),
                    ("brain_region", object),
                ],
            )

            # get/scale xyz positions
            pos_xyz_raw = np.array(
                [chn_loc_data["channels"][i] for i in ("x", "y", "z")]
            ).T

            pos_origin = next(iter(chn_loc_data["origin"].values()))

            pos_xyz = np.copy(pos_xyz_raw)

            # by adjusting xyz axes & offsetting from origin position
            # in "pos_xyz_raw", x-axis and y-axis are swapped, correcting for that below
            pos_xyz[:, 0] = pos_origin[1] - pos_xyz_raw[:, 1]
            pos_xyz[:, 1] = pos_origin[0] + pos_xyz_raw[:, 0]
            pos_xyz[:, 2] = pos_origin[2] - pos_xyz_raw[:, 2]

            # and quantizing to CCF voxel resolution;
            pos_xyz = (voxel_resolution * np.around(pos_xyz / voxel_resolution)).astype(
                int
            )

            # get recording geometry,
            probe_electrodes = (electrodes_query & {"shank": shank_no}).fetch(
                order_by="electrode asc"
            )

            rec_electrodes = np.array(
                [chn_loc_data["channels"]["lateral"], chn_loc_data["channels"]["axial"]]
            ).T

            # adjusting for the lateral offset
            # npx 1.0 probes has an alternating offset of 0um and 16um between the rows
            # npx 2.0 probes do not have this offset (i.e. offset = 0um for all rows)
            lateral_offset = np.abs(
                np.diff(
                    (
                        electrodes_query
                        & {"shank_col": 1, "shank": shank_no}
                        & "shank_row in (1, 2)"
                    ).fetch("x_coord")
                )[0]
            )
            if lateral_offset:
                rec_electrodes[:, 0] = lateral_offset * (
                    np.floor(rec_electrodes[:, 0] / lateral_offset)
                )

            # to find corresponding electrodes,
            elec_coord = np.array(
                [probe_electrodes["x_coord"], probe_electrodes["y_coord"]]
            ).T

            elec_coord_map = {tuple(c): i for i, c in enumerate(elec_coord)}

            rec_to_elec_idx = np.array(
                [elec_coord_map[tuple(i)] for i in rec_electrodes]
            )

            for electrode, x, y, z in zip(
                probe_electrodes[rec_to_elec_idx]["electrode"],
                pos_xyz[:, 0],
                pos_xyz[:, 1],
                pos_xyz[:, 2],
            ):
                entry = {
                    **key,
                    "electrode": electrode,
                    "x": x,
                    "y": y,
                    "z": z,
                    "probe_type": probe_type,
                }
                try:
                    self.Electrode.insert1(entry)
                except dj.IntegrityError as e:
                    skipped_electrode_count += 1
                    log.warning(
                        "...... ElectrodePositionError at X="
                        + f"{x}, Y={y}, Z={z}:\n {repr(e)}"
                    )
        if skipped_electrode_count > 0:
            log.info(f"Skipped {skipped_electrode_count} electrodes for \n\t{key}")
