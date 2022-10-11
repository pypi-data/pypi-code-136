# -*- coding: utf-8 -*-
# -*- Python Version: 3.7 -*-

"""DEV SANDBOX: export a specified HBJSON file to a PHPP XL file."""

from rich import print
import pathlib

from PHX.from_HBJSON import read_HBJSON_file, create_project
from PHX.to_PHPP import phpp_app, xl_app
from PHX.to_PHPP.phpp_localization.shape_model import PhppShape

# --- Input file Path
# -------------------------------------------------------------------------
# SOURCE_FILE = pathlib.Path(
#     "/Users/em/Dropbox/bldgtyp-00/00_PH_Tools/PHX/tests/_source_hbjson/Default_Model_Single_Zone.hbjson"
# )
SOURCE_FILE = pathlib.Path(
    "/Users/em/Dropbox/bldgtyp-00/00_PH_Tools/PHX/sample/hbjson/221007_Penziner.hbjson"
)

if __name__ == '__main__':
    # --- Read in an existing HB_JSON and re-build the HB Objects
    # -------------------------------------------------------------------------
    print("[bold green]- " * 50)
    print(
        f"[bold green]> Reading in the HBJSON file: ./{SOURCE_FILE}[/bold green]")
    hb_json_dict = read_HBJSON_file.read_hb_json_from_file(SOURCE_FILE)
    hb_model = read_HBJSON_file.convert_hbjson_dict_to_hb_model(hb_json_dict)

    # --- Generate the PhxProject file.
    # -------------------------------------------------------------------------
    phx_project = create_project.convert_hb_model_to_PhxProject(
        hb_model, group_components=True)

    # --- Connect to open instance of XL, Load the correct PHPP Shape file
    # -------------------------------------------------------------------------
    xl = xl_app.XLConnection = xl_app.XLConnection(_output=print)
    shape_file_dir = pathlib.Path("PHX", "to_PHPP", "phpp_localization")
    phpp_shape_file = phpp_app.get_shape_file(xl, shape_file_dir)
    phpp_shape = PhppShape.parse_file(phpp_shape_file)
    phpp_conn = phpp_app.PHPPConnection(xl, phpp_shape)

    if phpp_conn.xl.connection_is_open():
        file = phpp_conn.xl.wb.name
        print(f'[bold green]> connected to excel doc: {file}[/bold green]')

    with phpp_conn.xl.in_silent_mode():
        phpp_conn.xl.unprotect_all_sheets()
        phpp_conn.write_certification_config(phx_project)
        phpp_conn.write_climate_data(phx_project)
        phpp_conn.write_project_constructions(phx_project)
        phpp_conn.write_project_tfa(phx_project)
        phpp_conn.write_project_opaque_surfaces(phx_project)
        phpp_conn.write_project_thermal_bridges(phx_project)
        phpp_conn.write_project_window_components(phx_project)
        phpp_conn.write_project_window_surfaces(phx_project)
        phpp_conn.write_project_window_shading(phx_project)
        phpp_conn.write_project_ventilation_components(phx_project)
        phpp_conn.write_project_ventilators(phx_project)
        phpp_conn.write_project_spaces(phx_project)
        phpp_conn.write_project_ventilation_type(phx_project)
        phpp_conn.write_project_airtightness(phx_project)
        phpp_conn.write_project_volume(phx_project)
        phpp_conn.write_project_hot_water(phx_project)
        phpp_conn.write_project_res_elec_appliances(phx_project)

        # TODO: add custom any-range writer (User-Determined)
        
        # phpp_conn.activate_variant_assemblies()
        # phpp_conn.activate_variant_windows()
        # phpp_conn.activate_variant_ventilation()
        # phpp_conn.activate_variant_additional_vent()
