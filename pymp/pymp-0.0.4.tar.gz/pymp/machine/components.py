from functools import reduce

import numpy as np
import pandas as pd
import param

# import holoviews as hv

from .base import *

class ColumnDescriptor(param.Parameterized):
    controller = param.Parameter(doc="""
        The Controller object that contains the column vector of values that represent the values for the Element over
        time.""",
                                 allow_None=False,
                                 constant=True
                                 )

    column = param.String(doc="""The column vector that holds the values beig described""",
                          allow_None=False,
                          constant=True
                          )

    describes = param.ObjectSelector(doc="""The type of motion described""",
                                     objects=dict([(d.name, d) for d in ValueType])
                                     )

    target = param.ObjectSelector(doc="""
    The internal machine coordinate system used to represent the values within the Controler column vectors.""",
                                  default=CoordinateSystem.IEC_61217,
                                  objects=dict([(i.name, i) for i in CoordinateSystem])
                                  )

    scale = param.ObjectSelector(doc="""The scale on which the values for the column fall""",
                                 objects=dict([(i.name, i) for i in Scale]))

    axis = param.ObjectSelector(doc="""The axis (along or around) on which the column values fall""",
                                objects=dict([(a.name, a.value) for a in Axis])
                                )

    value = param.Parameter(doc="""The current column value at the current Controller.index.""")

    transform = param.Array()

    @param.depends('controller.index', 'controller.coordinate_system', 'column', 'scale', 'target', watch=True,
                   on_init=True)
    def _set_value(self):
        # print(f"_set_value from ColumnDescriptor {self.name}")
        cc = CoordinateConverter(target=self.target)
        current_value, = self.controller.control_point[self.column]
        self.value = cc(current_value, self.scale, self.controller.coordinate_system)
        self._set_transform()

    def _set_transform(self):
        # print(f"_set_transform from ColumnDescriptor {self.name}")
        rotations = (Scale.NO_SCALE, Scale.GANTRY, Scale.COLL, Scale.YAW, Scale.PITCH, Scale.ROLL)
        linear = [l for l in Scale if (l is Scale.NO_SCALE) or (l not in rotations)]

        if self.describes == ValueType.STATE:
            self.transform = None
        elif self.describes == ValueType.ROTATION:
            if (self.scale in rotations):
                # TODO: Expand for rotation about any axis. Right now only in 2D around Z axis no mater what axis is
                #       selected
                R = np.identity(3)
                R[0:2, 0:2] = np.array([[np.cos(np.deg2rad(self.value)), -np.sin(np.deg2rad(self.value))],
                                        [np.sin(np.deg2rad(self.value)), np.cos(np.deg2rad(self.value))]
                                        ]
                                       )
                self.transform = R
            else:
                raise ValueError(f"'{self.scale}' is not a rotational scale")

        elif self.describes == ValueType.TRANSLATION:
            if (self.scale in linear):
                T = np.identity(3)
                # TODO: This for example assume the value is a number and not a str so I may not support Element.value as a str
                #       in the future.
                if self.axis in (Axis.X, Axis.Y):
                    T[self.axis, 2] = self.value
                    self.transform = T
                else:
                    raise ValueError("Currently Axis.X and Axis.Y are the only supported axes for translations")
            else:
                raise ValueError(f"'{self.scale}' is not a linear scale")

        else:
            raise ValueError(f"'{self.describes}' is not a suported value description.")


class Controller(param.Parameterized):
    """
        Base class for defining a series of element values for a machine configuration. A Controller is a single source
        of truth for 1-N axes who's values are stored in a pandas.Dataframe. The pandas.Dataframe should have a single
        monotonically increasing integer index and 1-N columns of vales reresenting the current value for the axis it
        represents within the controller frame of reference.

        The rows of the Controller represent values for multiple elements (axes) changing over time similar to control
        points for an MLC file. The pandas.DataFrame structure matches well with other radiation oncology log file
        structures like those provided in a Varian Trajectory Log file on the TrueBeam platforms.

        It supports IEC-61217, IEC-60601-2-1, and Varian Standard scales for input.
    """

    control_points = param.DataFrame(doc="""
    A pandas.DataFrame with a single monotonically increasing integer index and 1-N columns of vales reresenting the 
    values for multiple elements (axes) changing over time similar to control points for an MLC file.""",
                                     allow_None=False,
                                     constant=True
                                     )

    coordinate_system = param.ObjectSelector(doc="""
    The machine coordinate system used to represent the positional values within the Controler column vectors""",
                                         objects=dict([(i.name, i) for i in CoordinateSystem])
                                         )

    index = param.Integer(doc="""The current position of the monotonically increasing integer index""",
                          default=0
                          )

    control_point = param.DataFrame(doc="""
    A pandas.DataFrame with a single row representing the values for each supported axis at the current index 
    position.""",
                                    default=None
                                    )

    column_desc = param.Dict(doc="""A map between Controller columns and their ColumnDescriptors""",
                             default={}
                             )

    @param.depends("control_points", watch=True, on_init=True)
    def _update_index_range(self):
        # print("control_points changed")
        self.param["index"].bounds = (0, len(self.control_points) - 1)
        self.index = 0
        self.control_point = self.control_points.iloc[[self.index]]

    @param.depends("index", watch=True)
    def _update_cp(self):
        self.control_point = self.control_points.iloc[[self.index]]

    def describe_column(self, column, desc=ValueType.STATE, target=CoordinateSystem.IEC_61217, scale=Scale.NO_SCALE,
                        axis=Axis.NONE, **kwargs):
        name = kwargs.get('name', column)
        self.column_desc[name] = ColumnDescriptor(name=name, controller=self, column=column, describes=desc,
                                                  target=target, scale=scale, axis=axis)

        self.param.trigger('column_desc')


class Element(param.Parameterized):
    controller = param.Parameter(doc="""
    The Controller object that contains the column vector of values that represent the values for the Element over
    time.""",
                                 allow_None=False,
                                 constant=True
                                 )
    columns = param.ListSelector([], objects=[])

    value = param.Parameter(doc="""The current value at the current Controller.index.""")

    vertices = param.Array(doc="""
        A Nx2 array of (x, y) coordinates that make up the vertices for the element's geometry or None (default=None)""",
                           default=None
                           )

    coordinates = param.Array()

    @param.depends("controller.column_desc", watch=True, on_init=True)
    def _update_columns(self):
        tmp = [k for k in self.controller.column_desc.keys()]
        self.param["columns"].objects = tmp

        for col in self.columns:
            if not col in list(self.controller.column_desc.keys()):
                raise ValueError(f"Column {col} not found in column descriptors")

    @param.depends('controller.index', 'columns', watch=True, on_init=True)
    def current_value(self):
        values = []
        for col in self.columns:
            v, = self.controller.control_point[col]
            values.append(v)

        if len(values) == 1:
            self.value, = values
        else:
            self.value = values

    @param.depends("value", "vertices", watch=True, on_init=True)
    def _update_coords(self):
        if self.vertices is not None:
            Ts = [self.controller.column_desc[col].transform for col in self.columns[::-1]
                  if not self.controller.column_desc[col].scale == Scale.NO_SCALE]

            T = reduce(np.dot, Ts)

            h_coords = np.vstack((self.vertices.T, np.ones_like(self.vertices[::, 0].ravel())))
            self.coordinates = np.dot(T, h_coords)[0:2].T

    # @param.depends("value")
    # def plot(self):
    #     # print(f'Update: {self.coordinates}')
    #     if self.vertices is not None:
    #         return hv.Polygons(self.coordinates, extents=(-25, -25, 25, 25)).opts(width=600, height=600, color='lightblue')
    #     else:
    #         s = f"Shapeless Element\n{self.value}"
    #         return hv.Text(0, 0, s, extents=(-25, -25, 25, 25)).opts(width=600, height=600)
