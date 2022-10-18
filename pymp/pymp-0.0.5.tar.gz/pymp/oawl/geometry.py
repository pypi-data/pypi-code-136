import numpy as np
import pandas as pd

import param
import panel as pn

from .assets import AXES_IMAGE

class AbstractPoint(param.Parameterized):
    '''
    A Parameterized object that allows the user to define a abstract point in 3D space. A Point object has coordinates
    defined within a coordinate system reference frame represented by a CoordinateSystemDef object. However, to have a
    proper CoordinateSystemDef a single abstract point locating the origin of the CoordinateSystemDef is needed.
    Therefore, and AbstractPoint is simply used as a way to avoid a circular reference allowing the origin of the
    CoordinateSystemDef to be defined by a Point object without the point needing a CoordinateSystemDef reference of
    its own.
    '''
    # Add Parameters
    label = param.String(default=None,
                         precedence=1,
                         doc='''A simple label used to identify the point.'''
                         )

    x = param.Number(default=0.0,
                     bounds=(None, None),
                     precedence=2,
                     doc='The "X" coordinate of the Point.'
                     )

    y = param.Number(default=0.0,
                     bounds=(None, None),
                     precedence=3,
                     doc='The "Y" coordinate of the Point.'
                     )

    z = param.Number(default=0.0,
                     bounds=(None, None),
                     precedence=4,
                     doc='The "Z" coordinate of the Point.'
                     )

    coord = param.Dynamic(constant=True,
                          doc='The column vector that represents the coordinate of the Point'
                          )

    hcoord = param.Dynamic(constant=True,
                           doc='The column vector that represents the homogeneous coordinate of the Point'
                           )

    def __init__(self, **params):
        super(AbstractPoint, self).__init__(**params)
        with param.edit_constant(self):
            self.coord = lambda : self._get_coord()
            self.hcoord = lambda : self._get_hcoord()

        if self.label is None:
            self.label = self.name

    def _get_coord(self):
        return self.hcoord[0:3, 0][:, None]

    def _get_hcoord(self):
        return np.array([self.x, self.y, self.z, 1.], dtype='f8')[:, None]

    @param.depends('label', 'x', 'y', 'z')
    def view(self):
        layout = pn.Row(pn.Param(self.param,
                                 parameters=['label', 'x', 'y', 'z'],
                                 default_layout=pn.Column,
                                 name=self.name
                                 )
                        )
        return layout

    @param.depends('x', 'y', 'z')
    def coordinate_view(self):
        '''
        A dependency interface method which allows the user to see updates to the CoordinateSystemDef objects transform matrices

        '''
        return pn.Column('### 3x1 Column Vector',
                         pd.DataFrame(self.coord, index=['X', 'Y', 'Z']),
                         '### 4x1 Homogeneous Column Vector',
                         pd.DataFrame(self.hcoord, index=['X', 'Y', 'Z', 'h'])
                         )

class CoordinateSystem(param.Parameterized):
    '''
    A Parameterized object that ensures consistent definition of rotations and translations in the IEC-61217 corrdinate
    system while allowing the user to define the coordinate system axes based on their specific convention. The
    CoordinateSystem object will provide the affine transform matrix required to conver the user's coordinate
    convention into standard IEC-61217 coordinates.
    '''
    # Add Parameters
    isocenter = param.ClassSelector(class_=AbstractPoint,
                                    # default=AbstractPoint(label='Isocenter'),
                                    doc='''
                                    The AbstractPoint object that represents the location of the isocenter within the 
                                    coordinate system'''
                                    )

    a_axis = param.Selector(default='+Z',
                            objects=['+X', '-X', '+Y', '-Y', '+Z', '-Z'],
                            doc='''
                            The axis label and directionality for the axis tha defines the couch vertical motion 
                            (i.e. Labeled A in the diagrahm parameter)'''
                            )

    b_axis = param.Selector(default='+Y',
                            objects=['+X', '-X', '+Y', '-Y', '+Z', '-Z'],
                            doc='''
                            The axis label and directionality for the axis tha defines the couch longitudinal motion 
                            (i.e. Labeled B in the diagrahm parameter)'''
                            )

    c_axis = param.Selector(default='+X',
                            objects=['+X', '-X', '+Y', '-Y', '+Z', '-Z'],
                            doc='''
                            The axis label and directionality for the axis tha defines the couch lateral motion 
                            (i.e. Labeled C in the diagrahm parameter)'''
                            )
    diagram = param.Parameter(default=AXES_IMAGE,
                              readonly=True,
                              doc='''The schematic representation of the coordinate system being defined.'''
                              )

    T_axis = param.Dynamic(
                           # default=np.eye(4),
                           constant=True,
                           doc='''
                           The affine transform matrix used to convert the user defined coordinate system axes to the 
                           IEC-61217 convention.'''
                           )

    T_iso = param.Dynamic(constant=True,
                          doc='The affine transform matrix used to move the isocenter to <0, 0, 0>'
                          )

    T_coord = param.Dynamic(constant=True,
                            doc='''
                            The affine transform matrix used to convert the user defined coordinate system to IEC-61217 
                            convention with the isocenter defined at <0, 0, 0>.'''
                            )

    _axes = param.Dict(default={'+X': np.array([1., 0., 0.]),
                                '-X': np.array([-1., 0., 0.]),
                                '+Y': np.array([0., 1., 0.]),
                                '-Y': np.array([0., -1., 0.]),
                                '+Z': np.array([0., 0., 1.]),
                                '-Z': np.array([0., 0., -1.])
                                },
                       readonly=True,
                       precedence=-1,
                       doc='''Axis conventions for converting to IEC-61217 coordinates'''
                       )

    def __init__(self, **params):
        super(CoordinateSystem, self).__init__(**params)
        self.isocenter = AbstractPoint(label='Isocenter')
        with param.edit_constant(self):
            self.T_axis = lambda : self._get_axis_transform()
            self.T_iso = lambda : self._get_isocenter_transform()
            self.T_coord = lambda : self._get_coord_transform()

    def _get_axis_transform(self):
        axis_transform = np.eye(4)
        axis_transform[0, 0:3] = self._axes[self.c_axis]
        axis_transform[1, 0:3] = self._axes[self.b_axis]
        axis_transform[2, 0:3] = self._axes[self.a_axis]
        return axis_transform

    def _get_isocenter_transform(self):
        isocenter_transform = np.eye(4)
        isocenter_transform[0:3, 3] = self.isocenter.coord.ravel() * -1
        return isocenter_transform

    def _get_coord_transform(self):
        return self.T_axis @ self.T_iso

    @param.depends('a_axis', watch=True)
    def _update_a_axis(self):
        '''
        The dependency interface which allows update events to be triggered when the 'a_axis' parameter is set

        '''
        all_axes = {'X', 'Y', 'Z'}

        ab = {self.a_axis[1], self.b_axis[1]}
        ac = {self.a_axis[1], self.c_axis[1]}

        if self.a_axis[1] == self.b_axis[1]:
            sign = self.b_axis[0]
            self.b_axis = ''.join([sign] + [i for i in all_axes.difference(ac)])
        else:
            if self.a_axis[1] == self.c_axis[1]:
                sign = self.c_axis[0]
                self.c_axis = ''.join([sign] + [i for i in all_axes.difference(ab)])
            else:
                pass

    @param.depends('b_axis', watch=True)
    def _update_b_axis(self):
        '''
        The dependency interface method which allows update events to be triggered when the 'b_axis' parameter is set

        '''
        all_axes = {'X', 'Y', 'Z'}

        ab = {self.a_axis[1], self.b_axis[1]}
        bc = {self.b_axis[1], self.c_axis[1]}

        if self.b_axis[1] == self.a_axis[1]:
            sign = self.a_axis[0]
            self.a_axis = ''.join([sign] + [i for i in all_axes.difference(bc)])
        else:
            if self.b_axis[1] == self.c_axis[1]:
                sign = self.c_axis[0]
                self.c_axis = ''.join([sign] + [i for i in all_axes.difference(ab)])
            else:
                pass

    @param.depends('c_axis', watch=True)
    def _update_c_axis(self):
        '''
        The dependency interface method which allows update events to be triggered when the 'c_axis' parameter is set

        '''
        all_axes = {'X', 'Y', 'Z'}

        ac = {self.a_axis[1], self.c_axis[1]}
        bc = {self.b_axis[1], self.c_axis[1]}

        if self.c_axis[1] == self.a_axis[1]:
            sign = self.a_axis[0]
            self.a_axis = ''.join([sign] + [i for i in all_axes.difference(bc)])
        else:
            if self.c_axis[1] == self.b_axis[1]:
                sign = self.b_axis[0]
                self.b_axis = ''.join([sign] + [i for i in all_axes.difference(ac)])
            else:
                pass

    @param.depends('isocenter.label', 'isocenter.x', 'isocenter.y', 'isocenter.z', 'a_axis', 'b_axis', 'c_axis')
    def view(self):
        '''
        A dependency interface method which allows updates via a simplified UI for the CoordinateSystem object

        '''
        title = """
        ##Coordinate System Definition
        Assign the **< X, Y, Z \>** designation and direction (**+/-**) in which the arrow points for the illustrated **A**, **B**, **C** axes so that they match your coordinate system.
        """

        axes_graphic = pn.pane.PNG(object=AXES_IMAGE, width=250)

        axes_layout = pn.Param(self.param,
                               parameters=['a_axis', 'b_axis', 'c_axis'],
                               widgets={'a_axis': {'widget_type': pn.widgets.Select, 'width': 100},
                                        'b_axis': {'widget_type': pn.widgets.Select, 'width': 100},
                                        'c_axis': {'widget_type': pn.widgets.Select, 'width': 100}
                                        },
                               default_layout=pn.Column,
                               show_name=False
                               )

        axes_title = '''
        **Select Axis Label and Direction Combination**
        (Direction defined by arrow)
        '''

        layout = pn.Column(title,
                           pn.Row(pn.Param(self.isocenter.param,
                                           parameters=['label', 'x', 'y', 'z'],
                                           default_layout=pn.layout.WidgetBox,
                                           name='Isocenter'
                                           ),
                                  axes_graphic,
                                  pn.Column(axes_layout,
                                            axes_title
                                            )
                                  )
                           )

        return layout

    @param.depends('isocenter.x', 'isocenter.y', 'isocenter.z', 'a_axis', 'b_axis', 'c_axis')
    def transform_view(self):
        '''
        A dependency interface method which allows the user to see updates to the CoordinateSystem objects transform matrices

        '''
        return pn.Column('### Affine Axis Transform (A)',
                         pd.DataFrame(self.T_axis, index=['X', 'Y', 'Z', 'h'],
                                      columns=['1', '2', '3', 'h']
                                      ),
                         '### Affine Isocenter Transform (I)',
                         pd.DataFrame(self.T_iso, index=['X', 'Y', 'Z', 'h'],
                                      columns=['1', '2', '3', 'h']
                                      ),
                         '### Affine Coordinate Transform (AI)',
                         pd.DataFrame(self.T_coord, index=['X', 'Y', 'Z', 'h'],
                                      columns=['1', '2', '3', 'h']
                                      )
                         )


class SetupGeometry(param.Parameterized):
    '''
    '''
    vrt = param.Number(default=0.0,
                       bounds=(None, None),
                       doc='The vertical displacement of the plan geometry'
                       )

    lat = param.Number(default=0.0,
                       bounds=(None, None),
                       doc='The lateral displacement of the plan geometry'
                       )

    lng = param.Number(default=0.0,
                       bounds=(None, None),
                       doc='The longitudinal displacement of the plan geometry'
                       )

    yaw = param.Number(default=0.0,
                       bounds=(None, None),
                       doc='The delta value for the yaw rotation of the plan geometry around the axis defined by the vertical couch motion'
                       )

    roll = param.Number(default=0.0,
                        bounds=(None, None),
                        doc='The rotation angle (in Degrees) of the plan geometry around the axis defined by the logitudinal couch motion'
                        )

    pitch = param.Number(default=0.0,
                         bounds=(None, None),
                         doc='The delta value for the pitch rotation of the plan geometry around the axis defined by the lateral couch motion'
                         )

    T_vrt = param.Dynamic()
    T_lat = param.Dynamic()
    T_lng = param.Dynamic()
    T = param.Dynamic()

    R_yaw = param.Dynamic()
    R_roll = param.Dynamic()
    R_pitch = param.Dynamic()
    R = param.Dynamic()

    def __init__(self, **params):
        super(SetupGeometry, self).__init__(**params)

        with param.edit_constant(self):
            self.T_vrt = lambda : self._get_vrt_transform()
            self.T_lat = lambda: self._get_lat_transform()
            self.T_lng = lambda: self._get_lng_transform()
            self.T = lambda: self._get_translation_transform()

            self.R_yaw = lambda : self._get_yaw_transform()
            self.R_roll = lambda : self._get_roll_transform()
            self.R_pitch = lambda : self._get_pitch_transform()
            self.R = lambda : self._get_rotation_transform()

    def _get_vrt_transform(self):
        T = np.eye(4)
        T[2,3] = self.vrt
        return T

    def _get_lat_transform(self):
        T = np.eye(4)
        T[0,3] = self.lat
        return T

    def _get_lng_transform(self):
        T = np.eye(4)
        T[1,3] = self.lng
        return T

    def _get_translation_transform(self):
        T = np.eye(4)
        T[0:3, 3] = np.array([self.lat, self.lng, self.vrt])
        return self.T_lng @ self.T_lat @ self.T_vrt

    def _get_yaw_transform(self):
        theta_z = np.deg2rad(self.yaw)
        Rz = np.array([[np.cos(theta_z), -np.sin(theta_z), 0, 0],
                       [np.sin(theta_z), np.cos(theta_z), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]
                       ],
                      dtype='f8'
                      )
        return Rz

    def _get_roll_transform(self):
        theta_y = np.deg2rad(self.roll)
        Ry = np.array([[np.cos(theta_y), 0, np.sin(theta_y), 0],
                       [0, 1, 0, 0],
                       [-np.sin(theta_y), 0, np.cos(theta_y), 0],
                       [0, 0, 0, 1]
                       ],
                      dtype='f8'
                      )
        return Ry

    def _get_pitch_transform(self):
        theta_x = np.deg2rad(self.pitch)
        Rx = np.array([[1, 0, 0, 0],
                       [0, np.cos(theta_x), -np.sin(theta_x), 0],
                       [0, np.sin(theta_x), np.cos(theta_x), 0],
                       [0, 0, 0, 1]
                       ],
                      dtype='f8'
                      )

        return Rx

    def _get_rotation_transform(self):
        return self.R_roll @ self.R_pitch @ self.R_yaw

    @param.depends('vrt', 'lat', 'lng', 'yaw', 'roll', 'pitch')
    def view(self):
        layout = pn.Param(self.param,
                          parameters=['vrt', 'lat', 'lng', 'yaw', 'roll', 'pitch']
                          )
        return layout

    @param.depends('vrt', 'lat', 'lng', 'yaw', 'roll', 'pitch')
    def trans_transform_view(self):
        '''
        A dependency interface method which allows the user to see updates to the CoordinateSystem objects transform matrices

        '''
        return pn.Column('### Affine VRT Transform',
                         pd.DataFrame(self.T_vrt, index=['X', 'Y', 'Z', 'h'],
                                      columns=['1', '2', '3', 'h']
                                      ),
                         '### Affine LAT Transform',
                         pd.DataFrame(self.T_lat, index=['X', 'Y', 'Z', 'h'],
                                      columns=['1', '2', '3', 'h']
                                      ),
                         '### Affine LNG Transform',
                         pd.DataFrame(self.T_lng, index=['X', 'Y', 'Z', 'h'],
                                      columns=['1', '2', '3', 'h']
                                      ),
                         '### Affine Total Translation Transform',
                         pd.DataFrame(self.T, index=['X', 'Y', 'Z', 'h'],
                                      columns=['1', '2', '3', 'h']
                                      )
                         )

    @param.depends('vrt', 'lat', 'lng', 'yaw', 'roll', 'pitch')
    def rot_transform_view(self):
        '''
        A dependency interface method which allows the user to see updates to the CoordinateSystem objects transform matrices

        '''
        return pn.Column('### Affine Yaw Transform',
                         pd.DataFrame(self.R_yaw, index=['X', 'Y', 'Z', 'h'],
                                      columns=['1', '2', '3', 'h']
                                      ),
                         '### Affine Roll Transform',
                         pd.DataFrame(self.R_roll, index=['X', 'Y', 'Z', 'h'],
                                      columns=['1', '2', '3', 'h']
                                      ),
                         '### Affine Pitch Transform',
                         pd.DataFrame(self.R_pitch, index=['X', 'Y', 'Z', 'h'],
                                      columns=['1', '2', '3', 'h']
                                      ),
                         '### Affine Total Rotation Transform',
                         pd.DataFrame(self.R, index=['X', 'Y', 'Z', 'h'],
                                      columns=['1', '2', '3', 'h']
                                      )
                         )

class Point(AbstractPoint):
    '''
    A Parameterized object that allows the user to define a Point within 3D coordinate frame defined by a
    CoordinateSystem object convention.
    '''
    # Add Parameters
    coordinate_system = param.ClassSelector(class_=CoordinateSystem, default=CoordinateSystem())

    iec_coord = param.Dynamic(constant=True,
                              doc='The column vector that represents the IEC-61217 coordinate of the Point'
                              )

    iec_hcoord = param.Dynamic(constant=True,
                               doc='The column vector that represents the homogeneous IEC-61217 coordinate of the Point'
                               )

    def __init__(self, **params):
        super(Point, self).__init__(**params)
        with param.edit_constant(self):
            self.iec_coord = lambda: self._get_iec_coord()
            self.iec_hcoord = lambda: self._get_iec_hcoord()

    def _get_hcoord(self):
        return self.coordinate_system.T_iso @ np.array([self.x, self.y, self.z, 1.], dtype='f8')[:, None]

    def _get_iec_coord(self):
        return self.iec_hcoord[0:3, 0][:, None]

    def _get_iec_hcoord(self):
        return self.coordinate_system.T_coord @ np.array([self.x, self.y, self.z, 1.], dtype='f8')[:, None]

    @param.depends('label', 'x', 'y', 'z',
                   'coordinate_system.a_axis', 'coordinate_system.b_axis', 'coordinate_system.c_axis',
                   'coordinate_system.isocenter.x', 'coordinate_system.isocenter.y', 'coordinate_system.isocenter.z')
    def view(self):
        layout = pn.Row(pn.Param(self.param,
                                 parameters=['label', 'x', 'y', 'z'],
                                 default_layout=pn.Column,
                                 name=self.name
                                 )
                        )
        return layout

    @param.depends('x', 'y', 'z',
                   'coordinate_system.a_axis', 'coordinate_system.b_axis', 'coordinate_system.c_axis',
                   'coordinate_system.isocenter.x', 'coordinate_system.isocenter.y', 'coordinate_system.isocenter.z')
    def coordinate_view(self):
        '''
        A dependency interface method which allows the user to see updates to the CoordinateSystemDef objects transform matrices

        '''
        return pn.Column('### 3x1 Column Vector',
                         pd.DataFrame(self.coord, index=['X', 'Y', 'Z']),
                         '### 4x1 Homogeneous Column Vector',
                         pd.DataFrame(self.hcoord, index=['X', 'Y', 'Z', 'h'])
                         )

class Sphere(Point):
    '''
    A Parameterized object that allows the user to represent a sphere of any radius in 3D space. A Sphere can be viewed as a special Point that has both a radius and a volume.

    '''
    # Add new Parameters
    radius = param.Number(default=0.0,
                          bounds=(0, None),
                          step=0.05,
                          precedence=5,
                          doc='The radius of the sphere'
                          )

    volume = param.Number(constant=True,
                          precedence=6,
                          doc='The volume of the sphere'
                          )

    # Override Point parameter metadata for the Sphere
    label = param.String(precedence=1,
                         doc='''A simple label used to identify the sphere.'''
                         )
    x = param.Number(precedence=2,
                     doc='The "X" coordinate of the Point representing the sphere center.'
                     )

    y = param.Number(precedence=3,
                     doc='The "Y" coordinate of the Point representing the sphere center.'
                     )

    z = param.Number(precedence=4,
                     doc='The "Z" coordinate of the Point representing the  sphere center.'
                     )

    coord = param.Dynamic(doc='The column vector that represents the coordinate of the center of the sphere')

    hcoord = param.Dynamic(doc='''
    The column vector that represents the homogeneous coordinate of the center of the sphere'''
                           )

    def __init__(self, **params):
        super(Sphere, self).__init__(**params)
        with param.edit_constant(self):
            self.volume = lambda : self._get_volume()

    def _get_volume(self):
        if self.radius > 0.0:
            return (4.0 / 3.0) * np.pi * np.power(self.radius, 3)
        else:
            return 0.0

    @param.depends('label', 'x', 'y', 'z', 'radius')
    def view(self):
        layout = pn.Row(pn.Param(self.param,
                                 parameters=['label', 'x', 'y', 'z', 'radius', 'volume'],
                                 default_layout=pn.Column,
                                 name=self.name
                                 )
                        )

        return layout
