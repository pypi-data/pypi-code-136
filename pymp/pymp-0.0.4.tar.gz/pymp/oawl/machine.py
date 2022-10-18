from enum import IntEnum

import param
import panel as pn
import numpy as np
import pandas as pd

from .assets import SCALES_IMAGE

class MachineScale(IntEnum):
    IEC_61217 = 0
    VARIAN = 1
    IEC_60601_2_1 = 2

class MachineGeometry(param.Parameterized):
    label = param.String(default=None,
                         doc='''A simple label used to identify the machine geometry defined.'''
                         )

    actual_scale = param.ObjectSelector(doc='''The scale in which all axes will be converted''',
                                        objects=dict([(i.name, i) for i in MachineScale])
                                        )

    target_scale = param.ObjectSelector(doc='''The scale into which all axes will be converted''',
                                        objects=dict([(i.name, i) for i in MachineScale])
                                        )

    gantry = param.Number(default=0.0, bounds=(0.0, 360), label='Gantry')
    collimator = param.Number(default=0.0, bounds=(0.0, 360), label='Collimator')
    couch_vrt = param.Number(default=0.0, label='Couch Vrt')
    couch_lat = param.Number(default=0.0, label='Couch Lat')
    couch_lng = param.Number(default=0.0, label='Couch Lng')
    couch_yaw = param.Number(default=0.0, bounds=(0.0, 360), label='Couch Yaw')
    couch_pitch = param.Number(default=0.0, bounds=(0.0, 360), label='Couch Pitch')
    couch_roll = param.Number(default=0.0, bounds=(0.0, 360), label='Couch Roll')
    x1 = param.Number(default=0.0, label='X1')
    x2 = param.Number(default=0.0, label='X2')
    y1 = param.Number(default=0.0, label='Y1')
    y2 = param.Number(default=0.0, label='Y2')

    t_gantry = param.Number(constant=True, label='Gantry')
    t_collimator = param.Number(constant=True, label='Collimator')
    t_couch_vrt = param.Number(constant=True, label='Couch Vrt')
    t_couch_lat = param.Number(constant=True, label='Couch Lat')
    t_couch_lng = param.Number(constant=True, label='Couch Lng')
    t_couch_yaw = param.Number(constant=True, label='Couch Yaw')
    t_couch_pitch = param.Number(constant=True, label='Couch Pitch')
    t_couch_roll = param.Number(constant=True, label='Couch Roll')
    t_x1 = param.Number(constant=True, label='X1')
    t_x2 = param.Number(constant=True, label='X2')
    t_y1 = param.Number(constant=True, label='Y1')
    t_y2 = param.Number(constant=True, label='Y2')


    def __init__(self, **params):
        super(MachineGeometry, self).__init__(**params)
        with param.edit_constant(self):
            self.t_gantry = lambda : self._convert_gantry()
            self.t_collimator = lambda : self._convert_collimator()

            self.t_couch_vrt = lambda : self._convert_couch_vrt()
            self.t_couch_lat = lambda : self._convert_couch_lat()
            self.t_couch_lng = lambda : self.couch_lng

            self.t_couch_yaw = lambda : self._convert_couch_yaw()
            self.t_couch_pitch = lambda : self.couch_pitch
            self.t_couch_roll = lambda : self.couch_roll

            self.t_x1 = lambda : self._convert_x1()
            self.t_x2 = lambda: self.x2
            self.t_y1 = lambda: self._convert_y1()
            self.t_y2 = lambda: self.y2

        if self.label is None:
            self.label = self.name

    def _convert_gantry(self):
        if (self.target_scale == MachineScale.IEC_61217) or (self.target_scale == MachineScale.IEC_60601_2_1):
            if (self.actual_scale == MachineScale.IEC_60601_2_1) or (self.actual_scale == MachineScale.IEC_61217):
                if self.gantry == 360:
                    return 0
                else:
                    return self.gantry
            else:
                if (self.gantry >= 0) and (self.gantry <= 180):
                    x = 180 - self.gantry
                    return x
                elif (self.gantry > 180) and (self.gantry <= 360):
                    x = 360 - (self.gantry - 180)
                    if x == 360:
                        x = 0
                    return x
                else:
                    raise ValueError('Actual value outside of range for gantry')
        else:
            if (self.actual_scale == MachineScale.IEC_60601_2_1) or (self.actual_scale == MachineScale.IEC_61217):
                if (self.gantry >= 0) and (self.gantry <= 180):
                    x = -(self.gantry - 180)
                    return np.abs(x)
                elif (self.gantry > 180) and (self.gantry <= 360):
                    x = 360 - (self.gantry - 180)
                    if x == 360:
                        x = 0
                    return x
                else:
                    raise ValueError('Actual value outside of range for gantry')
            else:
                return self.gantry

    def _convert_collimator(self):
        if (self.target_scale == MachineScale.IEC_61217) or (self.target_scale == MachineScale.IEC_60601_2_1):
            if (self.actual_scale == MachineScale.IEC_60601_2_1) or (self.actual_scale == MachineScale.IEC_61217):
                if self.collimator == 360:
                    return 0
                else:
                    return self.collimator
            else:
                if (self.collimator >= 0) and (self.collimator <= 180):
                    x = 180 - self.collimator
                    return x
                elif (self.collimator > 180) and (self.collimator <= 360):
                    x = 360 - (self.collimator - 180)
                    if x == 360:
                        x = 0
                    return x
                else:
                    raise ValueError('Actual value outside of range for collimator')
        else:
            if (self.actual_scale == MachineScale.IEC_60601_2_1) or (self.actual_scale == MachineScale.IEC_61217):
                if (self.collimator >= 0) and (self.collimator<= 180):
                    x = -(self.collimator - 180)
                    return x
                elif (self.collimator > 180) and (self.collimator <= 360):
                    x = 360 - (self.collimator - 180)
                    if x == 360:
                        x = 0
                    return x
                else:
                    raise ValueError('Actual value outside of range for collimator')
            else:
                return self.collimator

    def _convert_couch_vrt(self):
        if self.target_scale == self.actual_scale:
            return self.couch_vrt

        if self.target_scale == MachineScale.IEC_61217:
            if self.actual_scale == MachineScale.IEC_60601_2_1:
                if (self.couch_vrt >= 0) and (self.couch_vrt <= 500):
                    x = -1.0 * self.couch_vrt
                    return x
                elif (self.couch_vrt > 500) and (self.couch_vrt < 1000):
                    x = 1000 - self.couch_vrt
                    return x
                else:
                    raise ValueError('Actual value outside of range for couch vrt')

            elif self.actual_scale == MachineScale.VARIAN:
                x = 100.0 - self.couch_vrt
                return x
            else:
                raise ValueError(f"Scale value of '{self.actual_scale}' for couch vrt is not supported")

        elif self.target_scale == MachineScale.IEC_60601_2_1:
            if self.actual_scale == MachineScale.IEC_61217:
                if self.couch_vrt < 0:
                    x = -1.0 * self.couch_vrt
                    return x
                elif self.couch_vrt > 0:
                    x = 1000 - self.couch_vrt
                    return x
                else:
                    return self.couch_vrt

            elif self.actual_scale == MachineScale.VARIAN:
                if self.couch_vrt >= 100:
                    x = self.couch_vrt - 100
                    return x
                elif self.couch_vrt < 100:
                    x = 900 + self.couch_vrt
                    return x
                else:
                    raise ValueError('Actual value outside of range for couch vrt')

            else:
                raise ValueError(f"Scale value of '{self.actual_scale}' is not supportedfor couch vrt")

        elif self.target_scale == MachineScale.VARIAN:
            if self.actual_scale == MachineScale.IEC_61217:
                x = 100 - self.couch_vrt
                return x
            elif self.actual_scale == MachineScale.IEC_60601_2_1:
                if (self.couch_vrt >= 900) and (self.couch_vrt <= 1000):
                    x = self.couch_vrt - 900.0
                    return x
                elif (self.couch_vrt >= 0) and (self.couch_vrt < 500):
                    x = 100 + self.couch_vrt
                    return x
            else:
                raise ValueError(f"Scale value of '{self.actual_scale}' is not supported for couch vrt")
        else:
            raise ValueError(f"Scale value of '{self.actual_scale}' is not supported for couch vrt")

    def _convert_couch_lat(self):
        if self.target_scale == self.actual_scale:
            return self.couch_lat

        if self.target_scale == MachineScale.IEC_61217:
            if self.actual_scale == MachineScale.IEC_60601_2_1:
                if (self.couch_lat >= 0) and (self.couch_lat <= 500):
                    return self.couch_lat
                elif (self.couch_lat > 500) and (self.couch_lat < 1000):
                    x = self.couch_lat - 1000
                    return x
                else:
                    raise ValueError('Actual value outside of range for couch lat')

            elif self.actual_scale == MachineScale.VARIAN:
                x = self.couch_lat - 100
                return x
            else:
                raise ValueError(f"Scale value of '{self.actual_scale}' for couch lat is not supported")

        elif self.target_scale == MachineScale.IEC_60601_2_1:
            if self.actual_scale == MachineScale.IEC_61217:
                if self.couch_lat < 0:
                    x = 1000 + self.couch_lat
                    return x
                else:
                    return self.couch_lat

            elif self.actual_scale == MachineScale.VARIAN:
                if self.couch_lat >= 100:
                    x = self.couch_lat - 100
                    return x
                elif self.couch_lat < 100:
                    x = 900 + self.couch_lat
                    return x
                else:
                    raise ValueError('Actual value outside of range for couch lat')

            else:
                raise ValueError(f"Scale value of '{self.actual_scale}' is not supportedfor couch lat")

        elif self.target_scale == MachineScale.VARIAN:
            if self.actual_scale == MachineScale.IEC_61217:
                x = 100 + self.couch_lat
                return x
            elif self.actual_scale == MachineScale.IEC_60601_2_1:
                if (self.couch_lat >= 900) and (self.couch_lat <= 1000):
                    x = self.couch_lat - 900.0
                    return x
                elif (self.couch_lat >= 0) and (self.couch_lat < 500):
                    x = 100 + self.couch_lat
                    return x
            else:
                raise ValueError(f"Scale value of '{self.actual_scale}' is not supported for couch lat")
        else:
            raise ValueError(f"Scale value of '{self.actual_scale}' is not supported for couch lat")

    def _convert_couch_yaw(self):
        if self.target_scale == self.actual_scale:
            if self.couch_yaw == 360:
                return 0
            else:
                return self.couch_yaw

        if self.target_scale == MachineScale.IEC_61217:
            if self.actual_scale == MachineScale.IEC_60601_2_1:
                x = 360 - self.couch_yaw
                if x == 360:
                    x = 0
                return x

            elif self.actual_scale == MachineScale.VARIAN:
                if (self.couch_yaw >= 0) and (self.couch_yaw <= 180):
                    x = 180 - self.couch_yaw
                    return x
                elif (self.couch_yaw > 180) and (self.couch_yaw <= 360):
                    x = 360 - (self.couch_yaw - 180)
                    if x == 360:
                        x = 0
                    return x
            else:
                raise ValueError(f"Scale value of '{self.actual_scale}' is not supported for couch yaw")

        elif self.target_scale == MachineScale.IEC_60601_2_1:
            if self.actual_scale == MachineScale.IEC_61217:
                x = 360 - self.couch_yaw
                if x == 360:
                    x = 0
                return x
            elif self.actual_scale == MachineScale.VARIAN:
                if (self.couch_yaw >= 0) and (self.couch_yaw <= 180):
                    x = self.couch_yaw + 180
                    if x == 360:
                        x = 0
                    return x
                elif (self.couch_yaw > 180) and (self.couch_yaw <= 360):
                    x = self.couch_yaw - 180
                    return x
                else:
                    raise ValueError('Actual value outside of range for couch yaw')
            else:
                raise ValueError(f"Scale value of '{self.actual_scale}' is not supported for couch yaw")

        elif self.target_scale == MachineScale.VARIAN:
            if self.actual_scale == MachineScale.IEC_61217:
                if (self.couch_yaw >= 0) and (self.couch_yaw <= 180):
                    x = 180 - self.couch_yaw
                    return x
                elif (self.couch_yaw > 180) and (self.couch_yaw <= 360):
                    x = (360 - self.couch_yaw) + 180
                    if x == 360:
                        x = 0
                    return x
                else:
                    raise ValueError('Actual value outside of range for couch yaw')

            elif self.actual_scale == MachineScale.IEC_60601_2_1:
                if (self.couch_yaw >= 0) and (self.couch_yaw <= 180):
                    x = 180 + self.couch_yaw
                    if x == 360:
                        x = 0
                    return x
                elif (self.couch_yaw > 180) and (self.couch_yaw <= 360):
                    x = self.couch_yaw - 180
                    return x
                else:
                    raise ValueError('Actual value outside of range for couch yaw')
            else:
                raise ValueError(f"Scale value of '{self.actual_scale}' is not supported for couch yaw")
        else:
            raise ValueError(f"Scale value of '{self.actual_scale}' is not supported for couch yaw")

    def _convert_x1(self):
        if (self.target_scale == MachineScale.IEC_60601_2_1) or (self.target_scale == MachineScale.VARIAN):
            if (self.actual_scale == MachineScale.IEC_60601_2_1) or (self.actual_scale == MachineScale.VARIAN):
                return self.x1
            else:
                if self.x1 == 0:
                    return 0.0
                else:
                    x = self.x1 * -1.0
                    return x
        else:
            if (self.actual_scale == MachineScale.IEC_60601_2_1) or (self.actual_scale == MachineScale.VARIAN):
                if self.x1 == 0:
                    return 0.0
                else:
                    x = self.x1 * -1.0
                    return x
            else:
                return self.x1

    def _convert_y1(self):
        if (self.target_scale == MachineScale.IEC_60601_2_1) or (self.target_scale == MachineScale.VARIAN):
            if (self.actual_scale == MachineScale.IEC_60601_2_1) or (self.actual_scale == MachineScale.VARIAN):
                return self.y1
            else:
                if self.y1 == 0:
                    return 0.0
                else:
                    x = self.y1 * -1.0
                    return x
        else:
            if (self.actual_scale == MachineScale.IEC_60601_2_1) or (self.actual_scale == MachineScale.VARIAN):
                if self.y1 == 0:
                    return 0.0
                else:
                    x = self.y1 * -1.0
                    return x
            else:
                return self.y1

    @param.depends('gantry', 'collimator', 'couch_vrt', 'couch_lat', 'couch_lng', 'couch_yaw', 'couch_pitch',
                   'couch_roll', 'x1', 'x2', 'y1', 'y2', 'actual_scale', 'target_scale')
    def view(self):

        label = pn.Param(self.param,
                         parameters=['label'],
                         widgets={'label': {'widget_type': pn.widgets.TextInput,
                                                   'width': 300,
                                                   'name': 'Geometry Label',
                                                   }
                                  },
                         show_name=False
                         )

        actual = pn.Param(self.param,
                          parameters=['actual_scale'],
                          widgets={'actual_scale': {'widget_type': pn.widgets.Select,
                                                    'width': 150,
                                                    'name': 'Actual Machine Scale',
                                                    # 'options':dict([(i.name, i) for i in MachineScale])
                                                    }
                                   },
                          show_name=False
                          )

        target = pn.Param(self.param,
                          parameters=['target_scale'],
                          widgets={'target_scale': {'widget_type':pn.widgets.Select,
                                                    'width':150,
                                                    'name':'Target Machine Scale',
                                                    # 'options':dict([(i.name, i) for i in MachineScale])
                                                    }
                                   },
                          show_name=False
                          )

        actual_values = pn.Param(self.param,
                                 parameters=['gantry',
                                             'collimator',
                                             'couch_vrt',
                                             'couch_lat',
                                             'couch_lng',
                                             'couch_yaw',
                                             'couch_pitch',
                                             'couch_roll',
                                             'x1',
                                             'x2',
                                             'y1',
                                             'y2'
                                             ],
                                 widgets={'gantry':pn.widgets.FloatInput,
                                          'collimator':pn.widgets.FloatInput,
                                          'couch_vrt':pn.widgets.FloatInput,
                                          'couch_lat':pn.widgets.FloatInput,
                                          'couch_lng':pn.widgets.FloatInput,
                                          'couch_yaw':pn.widgets.FloatInput,
                                          'couch_pitch':pn.widgets.FloatInput,
                                          'couch_roll':pn.widgets.FloatInput,
                                          'x1':pn.widgets.FloatInput,
                                          'x2':pn.widgets.FloatInput,
                                          'y1':pn.widgets.FloatInput,
                                          'y2':pn.widgets.FloatInput
                                          },
                                 name=self.actual_scale.name,
                                 show_name = False
                                 )

        target_values = pn.Param(self.param,
                                 parameters=['t_gantry',
                                             't_collimator',
                                             't_couch_vrt',
                                             't_couch_lat',
                                             't_couch_lng',
                                             't_couch_yaw',
                                             't_couch_pitch',
                                             't_couch_roll',
                                             't_x1',
                                             't_x2',
                                             't_y1',
                                             't_y2'],
                                 name=self.target_scale.name,
                                 show_name = False
                                 )

        return pn.GridBox(actual,
                          target,
                          label,
                          actual_values,
                          target_values,
                          pn.pane.PNG(object=SCALES_IMAGE, width=675),
                          ncols=3
                          )

def generate_millennium_dataframe():
    MLC_HEADERS = ['Leaf', 'Thickness', 'Y']
    MLC = []

    leaf_edge = -20.0
    # Bottom 10 Full width (1.0cm or 10mm) leaves
    for i in range(1,11):
        leaf_edge += 1.0 # Add leaf width
        MLC.append([i, 1.0, leaf_edge])

    # Central 40 Half width (0.5cm or 5mm) leaves
    for i in range(11,51):
        leaf_edge += 0.5 # Add leaf width
        MLC.append([i, 0.5, leaf_edge])

    # Top 10 Full width (1.0cm or 10mm) leaves
    for i in range(51,60):
        leaf_edge += 1.0 # Add leaf width
        MLC.append([i, 1.0, leaf_edge])

    return pd.DataFrame(MLC, columns=MLC_HEADERS)

def generate_hdmlc_dataframe():
    MLC_HEADERS = ['Leaf', 'Thickness', 'Y']
    HDMLC = []

    leaf_edge = -11.0
    # Bottom 14 Half width (0.5cm or 5mm) leaves
    for i in range(1,15):
        leaf_edge += 0.5 # Add leaf width
        HDMLC.append([i, 0.5, leaf_edge])

    # Central 32 Quarter width (0.25cm or 2.5mm) leaves
    for i in range(15,47):
        leaf_edge += 0.25 # Add leaf width
        HDMLC.append([i, 0.25, leaf_edge])

    # Top 14 Half width (0.5cm or 5mm) leaves
    for i in range(47,60):
        leaf_edge += 0.5 # Add leaf width
        HDMLC.append([i, 0.5, leaf_edge])

    return pd.DataFrame(HDMLC, columns=MLC_HEADERS)