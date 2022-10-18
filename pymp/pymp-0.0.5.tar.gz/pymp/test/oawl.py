import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd
import param

from pymp.transforms import AffineRx, AffineRy, AffineRz, AffineScale, AffineOrthogProjectXY 
from pymp.oawl.geometry import CoordinateSystem, AbstractPoint, Point
from pymp.oawl.machine import MachineGeometry, MachineScale, generate_hdmlc_dataframe, generate_millennium_dataframe

import panel as pn

COORD_SYS = CoordinateSystem()

mlc_select = pn.widgets.Select(name='Select MLC Model', value='Varian Millennium MLC', options=['Varian Millennium MLC', 'Varian HDMLC'])
field_shape_select = pn.widgets.Select(name='Select Field Shape', value='Square', options=['Square', 'Circle'])
sizing_slider = pn.widgets.FloatSlider(name='Half Side Length', value=0.5, start=0, end=5.0, step=0.5)

##############################################################
#                  Make the MLC UI Section                   #
##############################################################

@pn.depends(mlc_select, field_shape_select, watch=True)
def update_sizing_slider(mlc_event, shape_event):
    tmp = sizing_slider.value
    
    mlc_gen = {'Varian Millennium MLC':generate_millennium_dataframe,
               'Varian HDMLC':generate_hdmlc_dataframe
               }
    mlc_func = mlc_gen[mlc_select.value]
    MLC_DF = mlc_func()
    
    mlc_min = MLC_DF['Thickness'].values.min()
    mlc_max = MLC_DF['Thickness'].values.max()
    
    if field_shape_select.value == 'Square':

        with param.edit_constant(sizing_slider):
            sizing_slider.name =  'Half Side Length'

            if tmp % mlc_min != 0:
                sizing_slider.value = np.round(tmp / mlc_min, 0) * mlc_min

            sizing_slider.step = mlc_min
            
    elif field_shape_select.value == 'Circle':
        with param.edit_constant(sizing_slider):
            sizing_slider.name =  'Radius'

            if tmp % mlc_min != 0:
                sizing_slider.value = np.round(tmp / mlc_min, 0) * mlc_min
                
            sizing_slider.step = mlc_min
    else:
        pass
            
@pn.depends(mlc_select, field_shape_select, sizing_slider)
def _make_field_layout(mlc_event, shape_event, size_event):
    return pn.Column(pn.Row(mlc_select, field_shape_select), sizing_slider)

##############################################################
#                 Make the Target UI Section                 #
##############################################################

# Will hold the off axis points where we want to find solutions for the W/L
TARGETS = {}

# Define Widgets
iso_select = pn.widgets.Select(options=[''] + list(TARGETS.keys()))
reset_iso_button = pn.widgets.Button(name='Reset Isocenter <0, 0, 0>', button_type='primary')

target_select = pn.widgets.Select(options=list(TARGETS.keys()))
add_target_button = pn.widgets.Button(name='Add New Target', button_type='primary')
load_targets_button = pn.widgets.FileInput()
    
def target_label_change(event):
    TARGETS[event.new] = TARGETS[event.old]
    
    iso_selected = iso_select.value
    
    del(TARGETS[event.old])
    lst = list(TARGETS.keys())
    
    lst.sort()
    target_select.options = lst
    target_select.value = event.new
    
    iso_list = [''] + lst
    iso_select.options = iso_list
    iso_select.value = event.new if iso_selected == event.old else iso_selected
    

def add_target(event):    
    target = Point(coordinate_system=COORD_SYS)
    target.param.watch(target_label_change, ['label'])
    
    iso_selected = iso_select.value
    
    TARGETS[target.label] = target
    lst = list(TARGETS.keys())
    lst.sort()
    target_select.options = lst
    target_select.value = target.label
    
    iso_list = [''] + lst
    iso_select.options = iso_list
    iso_select.value = iso_selected
    

# Connect add_target handler to add_target_button
add_target_button.on_click(add_target)

def rest_isocenter(event):
    iso_select.value = ''
    COORD_SYS.isocenter.param.set_param(**{'x':0, 'y':0, 'z':0})
    # COORD_SYS.isocenter.x = 0
    # COORD_SYS.isocenter.y = 0
    # COORD_SYS.isocenter.z = 0
    

# Connect reset_isocenter handler to reset_iso_button
reset_iso_button.on_click(rest_isocenter)

@pn.depends(iso_select, watch=True)
def iso_change(event):
    if iso_select.value == '':
        pass
        # COORD_SYS.isocenter.param.set_param(**{'x':0, 'y':0, 'z':0})
    else:
        COORD_SYS.isocenter.param.set_param(**{'x':TARGETS[iso_select.value].x, 'y':TARGETS[iso_select.value].y, 'z':TARGETS[iso_select.value].z})
        
        
@pn.depends(load_targets_button, watch=True)
def load_targets(event):
    root = ET.fromstring(load_targets_button.value)
    for target in root:
        T = {}
        for p in target:
            if p.tag == 'label':
                T[p.tag] = p.text
            else:
                T[p.tag] = float(p.text)
        
        new_target = Point(coordinate_system=COORD_SYS, **T)
        new_target.param.watch(target_label_change, ['label'])
        
        TARGETS[new_target.label] = new_target  
        
    lst = list(TARGETS.keys())
    lst.sort()
    target_select.options = lst
    target_select.value = lst[0]
    
    iso_lst = [''] + lst
    iso_select.options = iso_lst
    iso_select.value = iso_lst[0]
    
    # Not ideal but will allow you to reload the file by simply reselecting it rather than requiring another widget or handler to clear the previous value.
    with param.discard_events(load_targets_button):
        load_targets_button.value = None
    

@pn.depends(target_select, iso_select)
def _make_target_layout(target_event, iso_event):
    wl_title = 'Define your Winston-Lutz Targets and the Field Geometry used to image them'
    if target_select.value is None:
        
        wl_layout = pn.Card(pn.Row(pn.Column(pn.pane.Markdown('''### Move Isocenter to Target'''),
                                             pn.Row(iso_select, 
                                                    reset_iso_button
                                                   ),
                                             pn.layout.HSpacer(),
                                             pn.layout.Divider(),
                                             pn.pane.Markdown('''### Add Winston-Lutz Target'''),
                                             pn.GridBox(target_select,
                                                        add_target_button,
                                                        pn.layout.HSpacer(),
                                                        load_targets_button,
                                                        ncols=2,
                                                        # sizing_mode='stretch_both'
                                                       ),
                                                       # sizing_mode='stretch_both'
                                             ),
                                   pn.layout.HSpacer(),
                                   pn.Column(pn.pane.Markdown('''### Winston-Lutz Field Settings'''),
                                             pn.Row(mlc_select, 
                                                    field_shape_select
                                                   ), 
                                             sizing_slider
                                            ),
                                   pn.layout.HSpacer(),
                                  ),
                            title=wl_title,
                            # collapsible=False,
                            # sizing_mode='stretch_both',
                            width=1500
                           )
        
        layout = pn.Row(
                        # iso_layout, 
                        wl_layout
                        )
    else:
        wl_layout = pn.Card(pn.Row(pn.Column(pn.pane.Markdown('''### Move Isocenter to Target'''),
                                             pn.Row(iso_select, 
                                                    reset_iso_button
                                                    ),
                                             pn.layout.HSpacer(),
                                             pn.layout.Divider(),
                                             pn.pane.Markdown('''### Select Current Winston-Lutz Target'''),
                                             pn.GridBox(target_select,
                                                        add_target_button,
                                                        pn.layout.HSpacer(),
                                                        load_targets_button,
                                                        ncols=2,
                                                        # sizing_mode='stretch_both'
                                                        ),
                                             pn.layout.Divider(),
                                             TARGETS[target_select.value].view,
                                             # sizing_mode='stretch_both'
                                             ),
                                   pn.layout.HSpacer(),
                                   pn.Column(pn.pane.Markdown('''### Winston-Lutz Field Settings'''),
                                             pn.Row(mlc_select, 
                                                    field_shape_select
                                                   ), 
                                             sizing_slider
                                            ),
                                   pn.layout.HSpacer(),
                                  ),
                            title=wl_title,
                            # collapsible=False,
                            # sizing_mode='stretch_both'
                            width=1500
                           )
        
        layout = pn.Row(
                        # iso_layout, 
                        wl_layout
                        )
        
    return layout

##############################################################
#            Make the Machine Geometry UI Section            #
##############################################################

# Will hold the machine geometries for the W/L
GEOS = {}

# Define Widgets
geometry_select = pn.widgets.Select(options=list(GEOS.keys()))
add_geometry_button = pn.widgets.Button(name='Add New Machine Geometry', button_type='primary')
load_geometries_button = pn.widgets.FileInput(margin=[30,30,30,30])

def geometry_label_change(event):    
    GEOS[event.new] = GEOS[event.old]
    del(GEOS[event.old])
    
    lst = list(GEOS.keys())
    lst.sort()
    geometry_select.options = lst
    geometry_select.value = event.new
    

def add_geometry(event):    
    geo = MachineGeometry(actual_scale=MachineScale.IEC_61217, target_scale=MachineScale.IEC_61217)
    geo.param.target_scale.constant = True
    
    geo.param.watch(geometry_label_change, ['label'])
    
    GEOS [geo.label] = geo
    
    lst = list(GEOS .keys())
    lst.sort()
    geometry_select.options = lst
    geometry_select.value = geo.label
    
    
# Connect the add_geometry handler to the add_geometry_button
add_geometry_button.on_click(add_geometry)


@pn.depends(load_geometries_button, watch=True)
def load_geometries(event):
    GEOS.clear()
    
    root = ET.fromstring(load_geometries_button.value)
    for geo in root:
        G = {}
        for p in geo:
            if p.tag == 'label':
                G[p.tag] = p.text
            elif p.tag in ('actual_scale', 'target_scale'):
                G[p.tag] = getattr(MachineScale, p.text)
            else:
                G[p.tag] = float(p.text)
        
        new_geo = MachineGeometry(**G)
        new_geo.target_scale = MachineScale.IEC_61217
        new_geo.param.target_scale.constant = True
        
        new_geo.param.watch(geometry_label_change, ['label'])
        
        GEOS[new_geo.label] = new_geo 
        
    lst = list(GEOS.keys())
    lst.sort()
    geometry_select.options = lst
    geometry_select.value = lst[0]
    
    # Not ideal but will allow you to reload the file by simply reselecting it rather than requiring another widget or handler to clear the previous value.
    with param.discard_events(load_geometries_button):
        load_geometries_button.value = None
    
@pn.depends(geometry_select)
def _make_geometry_layout(geometry_event):
    geometry_title = 'Define the Machine Geometries for the Winston Lutz Images'
    
    if geometry_select.value is None:
        
        geo_layout = pn.Card(pn.Column(pn.pane.Markdown('''### Add Machine Geometry'''),
                                       pn.GridBox(geometry_select,
                                                  add_geometry_button,
                                                  None,
                                                  load_geometries_button,
                                                  ncols=2,
                                                  # sizing_mode='stretch_both'
                                                ),
                                       pn.layout.HSpacer(),
                                       # sizing_mode='stretch_both'
                                      ),
                             title=geometry_title,
                             # collapsible=False,
                             # sizing_mode='stretch_both'
                             width=1500
                            )
        
        layout = pn.Row(
                        geo_layout
                        )
    else:
        geo_layout = pn.Card(pn.Column(pn.pane.Markdown(f'''### Select Current Winston-Lutz Machine Geometry'''),
                                       pn.GridBox(geometry_select,
                                                  add_geometry_button,
                                                  None,
                                                  load_geometries_button,
                                                  ncols=2,
                                                  # sizing_mode='stretch_both'
                                                 ),
                                       pn.layout.Divider(),
                                       GEOS[geometry_select.value].view,
                                       # sizing_mode='stretch_both'
                                      ),
                             title=geometry_title,
                             # collapsible=False,
                             # sizing_mode='stretch_both'
                             width=1500
                            )
         
        layout = pn.Row(
                        # iso_layout, 
                        geo_layout
                        )
        
    return layout

##############################################################
#               Make the Processing UI Section               #
##############################################################

processing_layout = pn.Column(pn.Card(COORD_SYS.view, title='Define Your TPS  Coordinate System', sizing_mode='stretch_both'),
                              _make_target_layout,
                              _make_geometry_layout,
                              None
                              )

def check_field(y, mlc_df, RADIUS):
    if y < 0:
        return not (y - RADIUS) in mlc_df['Y'].tolist()
    else:
        return not (y + RADIUS) in mlc_df['Y'].tolist()
    
def id_selectable_rows(df):
    # print(df.index[df['Field Exlusion'] == False].tolist())
    return df.index[df['Field Size Exclusion'] == False].tolist()

def project_point(point, mach_geom):

    POINT_HEADERS = ['Original', 'IEC-61217', 'Couch', 'Gantry', 'Collimator', 'BEV']
    POINT_VECTORS = ['X', 'Y', 'Z', 'h']

    point_couch = AffineRz(mach_geom.t_couch_yaw) @ point.iec_hcoord
    point_gantry = AffineRy(-mach_geom.t_gantry) @ point_couch
    point_coll = AffineRz(-mach_geom.t_collimator) @ point_gantry
    bev = AffineScale(100 / (100.0 - point_coll[2,0])) @ AffineOrthogProjectXY() @ point_coll

    # Display as column vectors
    A = np.hstack((point.hcoord, point.iec_hcoord, point_couch, point_gantry, point_coll, bev))
    POINT_DF = pd.DataFrame(A.tolist(), index=POINT_VECTORS, columns=POINT_HEADERS).round(decimals=2)

    R = np.sqrt(np.sum(np.square(bev[0:2,0])))
    
    return (AbstractPoint(x=bev[0,0], y=bev[1,0], z=bev[2,0]), R, POINT_DF)

def gap_solve(bev, r, mlc, mach_geom):
    # Used later to easily covert back the corrected collimator vectors
    rev_mach_geom = MachineGeometry(actual_scale=mach_geom.target_scale, target_scale=mach_geom.actual_scale)
    
    mlc_gen = {'Varian Millennium MLC':generate_millennium_dataframe,
               'Varian HDMLC':generate_hdmlc_dataframe
               }
    mlc_func = mlc_gen[mlc]
    MLC_DF = mlc_func()
    
    RESULTS = []
    RESULT_HEADERS = ['Leaf', 'Thickness', 'Center (X)', 'Center (Y)', 'Arc Length', 'Theta', 'Correction', f'Target ({mach_geom.target_scale.name})', f'Actual ({mach_geom.actual_scale.name})', 'Field Size Exclusion']

    for row in MLC_DF.itertuples():
        if np.abs(row.Y) <= r:
            x = np.sqrt(np.square(r) -np.square(row.Y))

            if x == 0:
                dist = np.sqrt(np.sum(np.square(np.array([bev.x, bev.y]) - np.array([x, row.Y]))))
                theta = np.arccos(1 - (dist * dist) / (2 * r * r))
                arc_len = r * theta

                correction = np.rad2deg(np.arctan2(row.Y, x) - np.arctan2(bev.y, bev.x))
                tmp = mach_geom.t_collimator - correction

                if tmp < 0:
                    tmp += 360

                if tmp >= 360:
                    tmp -= 360

                rev_mach_geom.collimator = tmp

                RESULTS.append([row.Leaf, row.Thickness, x, row.Y, arc_len, np.rad2deg(theta), correction, rev_mach_geom.collimator, rev_mach_geom.t_collimator, check_field(row.Y, MLC_DF, sizing_slider.value)])

            else:
                dist_1 = np.sqrt(np.sum(np.square(np.array([bev.x, bev.y]) - np.array([x, row.Y]))))
                theta_1 = np.arccos(1 - (dist_1 * dist_1) / (2 * r * r))
                arc_len_1 = r * theta_1

                correction_1 = np.rad2deg(np.arctan2(row.Y, x) - np.arctan2(bev.y, bev.x))
                tmp = mach_geom.t_collimator - correction_1

                if tmp < 0:
                    tmp += 360

                if tmp >= 360:
                    tmp -= 360

                rev_mach_geom.collimator = tmp

                RESULTS.append([row.Leaf, row.Thickness, x, row.Y, arc_len_1, np.rad2deg(theta_1), correction_1, rev_mach_geom.collimator, rev_mach_geom.t_collimator, check_field(row.Y, MLC_DF, sizing_slider.value)])

                dist_2 = np.sqrt(np.sum(np.square(np.array([bev.x, bev.y]) - np.array([-x, row.Y]))))
                theta_2 = np.arccos(1 - (dist_2 * dist_2) / (2 * r * r))
                arc_len_2 = r * theta_2

                correction_2 = np.rad2deg(np.arctan2(row.Y, -x) - np.arctan2(bev.y, bev.x))
                tmp = mach_geom.t_collimator - correction_2

                if tmp < 0:
                    tmp += 360

                if tmp >= 360:
                    tmp -= 360

                rev_mach_geom.collimator = tmp

                RESULTS.append([row.Leaf, row.Thickness, -x, row.Y, arc_len_2, np.rad2deg(theta_2), correction_2, rev_mach_geom.collimator, rev_mach_geom.t_collimator, check_field(row.Y, MLC_DF, sizing_slider.value)])



    RESULTS_DF = pd.DataFrame(RESULTS, columns=RESULT_HEADERS) \
                             .sort_values(by=['Arc Length']) \
                             .round({'Center (X)':2, 'Center(Y)':2, 'Arc Length':3, 'Theta':3, 'Correction':3, mach_geom.target_scale.name:1, mach_geom.actual_scale.name:1})
    
    return RESULTS_DF


def process(*args):
    processing_layout[-1] = None
    
    if (target_select.value is not None) and (geometry_select.value is not None):
    
        BEV, R, POINT_DF = project_point(TARGETS[target_select.value], GEOS[geometry_select.value])

        if R == 0:
            processing_layout[-1] = pn.Card(pn.Column(pn.pane.Markdown('###Target is at isocenter.'),
                                                      pn.widgets.Tabulator(POINT_DF, 
                                                                           configuration={'headerSort': False},
                                                                           widths=200,
                                                                           selectable=False,
                                                                           header_align='center',
                                                                           disabled=True,
                                                                           text_align='center'
                                                                           ),
                                                      sizing_mode='stretch_width'
                                                     ),
                                            title='Processing Results', 
                                            # sizing_mode='stretch_both'
                                            width=1500
                                            )
        else:                               
            RESULTS_DF = gap_solve(BEV, R, mlc_select.value, GEOS[geometry_select.value])
            id_selectable_rows(RESULTS_DF)

            best = RESULTS_DF.iloc[0]
            message = f'''##MLC Leaf Gap Alignment Solutions 

            Closest leaf gap solution 
            Top edge of Leaf Pair: {best['Leaf']} 
            Centered on BEV coordinate: ({best['Center (X)']}, {best['Center (Y)']})

            '''

            processing_layout[-1] = pn.Card(pn.Column(pn.pane.Markdown(f'''##Point Transforms
            Radial distance (R) from isocenter in the BEV plane {R:.4f}'''),
                                                      pn.widgets.Tabulator(POINT_DF,
                                                                           configuration={'headerSort': False},
                                                                           widths=200,
                                                                           selectable=False,
                                                                           header_align='center',
                                                                           disabled=True,
                                                                           text_align='center'
                                                                          ),
                                                      pn.pane.Markdown(message),
                                                      pn.widgets.Tabulator(RESULTS_DF, 
                                                                           height=400, 
                                                                           width=1500, 
                                                                           show_index=False,
                                                                           selectable=1,
                                                                           selectable_rows=id_selectable_rows,
                                                                           header_align='center',
                                                                           text_align='center',
                                                                           hidden_columns=['Field Size Exclusion'],
                                                                           disabled=True,
                                                                           widths=150,
                                                                           groupby=['Field Size Exclusion']
                                                                          )
                                                     ),
                                            title='Processing Results', 
                                            # sizing_mode='stretch_both'
                                            width=1500
                                           )
    else:
        pass
        

iso_select.param.watch(process, ['value'], onlychanged=True)
target_select.param.watch(process, ['value'], onlychanged=True)
geometry_select.param.watch(process, ['value'], onlychanged=True)
mlc_select.param.watch(process, ['value'], onlychanged=True)
field_shape_select.param.watch(process, ['value'], onlychanged=True)
sizing_slider.param.watch(process, ['value'], onlychanged=True)
COORD_SYS.param.watch(process, ['a_axis', 'b_axis', 'c_axis'], onlychanged=True)
COORD_SYS.isocenter.param.watch(process, ['x', 'y', 'z'], onlychanged=True)

pn.Column(processing_layout).servable()