from enum import Enum, IntEnum

import numpy as np
import pandas as pd
import param

class CoordinateSystem(IntEnum):
    IEC_61217 = 0
    VARIAN = 1
    IEC_60601_2_1 = 2

class Scale(Enum):
    NO_SCALE = 0
    GANTRY = 1
    COLL = 2
    JAW = 3
    IJAW = 4
    VRT = 5
    LAT = 6
    LNG = 7
    YAW = 8
    PITCH = 9
    ROLL = 10

class ValueType(Enum):
    STATE = 0
    TRANSLATION = 1
    ROTATION = 2

class Axis(IntEnum):
    NONE = 99
    X = 0
    Y = 1
    Z = 2

class CoordinateConverter(param.Parameterized):
    target = param.ObjectSelector(doc="""The coordinate system into which all others will be converted""",
                                  objects=dict([(i.name, i) for i in CoordinateSystem])
                                  )

    def __init__(self, **params):
        super(CoordinateConverter, self).__init__(**params)

        self._map = {Scale.NO_SCALE: lambda a, frame: a.copy('A'),
                     Scale.GANTRY: self._gan_coll_rtn,
                     Scale.COLL: self._gan_coll_rtn,
                     Scale.JAW: lambda a, frame: a.copy('A'),
                     Scale.IJAW: self._inv_jaw,
                     Scale.VRT: self._couch_vrt_lat,
                     Scale.LAT: self._couch_vrt_lat,
                     Scale.LNG: lambda a, frame: a.copy('A'),
                     Scale.YAW: self._couch_yaw,
                     Scale.PITCH: lambda a, frame: a.copy('A'),
                     Scale.ROLL: lambda a, frame: a.copy('A')
                     }

    def __call__(self, value, value_scale, value_frame):
        if type(value) in (int, float):
            tmp = np.array([value])
        elif type(value) is type(np.array([])):
            tmp = value.copy('A')
        elif type(value) is type(pd.Series()):
            tmp = value.values
        else:
            raise TypeError(f"A 'value' of type ({type(value)}) is not supported")

        func = self._map[value_scale]
        new_value = func(tmp, value_frame)

        if type(value) in (int, float):
            tmp, = new_value
            return tmp
        elif type(value) is type(np.array([])):
            return new_value
        elif type(value) is type(pd.Series()):
            tmp = value.copy(deep=True)
            tmp[::] = new_value
            return tmp
        else:
            raise TypeError(f"A 'value' of type ({type(value)}) is not supported")

    def _gan_coll_rtn(self, a, frame):
        if (self.target == CoordinateSystem.IEC_61217) or (self.target == CoordinateSystem.IEC_60601_2_1):
            if (frame == CoordinateSystem.IEC_60601_2_1) or (frame == CoordinateSystem.IEC_61217):
                return a.copy('A')
            else:
                x = np.zeros_like(a)

                idx_360 = np.where(a == 360)
                x[idx_360] = 180

                idx_0_180 = np.where(np.logical_and(a >= 0, a <= 180))
                x[idx_0_180] = -(a[idx_0_180] - 180)

                idx_180_360 = np.where(np.logical_and(a > 180, a < 360))
                x[idx_180_360] = 360 - (a[idx_180_360] - 180)

                x[np.where(np.abs(x) == 360)] = 0

                return np.abs(x)
        else:
            if (frame == CoordinateSystem.IEC_60601_2_1) or (frame == CoordinateSystem.IEC_61217):
                x = np.zeros_like(a)

                idx_360 = np.where(a == 360)
                x[idx_360] = 180

                idx_0_180 = np.where(np.logical_and(a >= 0, a <= 180))
                x[idx_0_180] = -(a[idx_0_180] - 180)

                idx_180_360 = np.where(np.logical_and(a > 180, a < 360))
                x[idx_180_360] = 360 - (a[idx_180_360] - 180)

                x[np.where(np.abs(x) == 360)] = 0

                return np.abs(x)
            else:
                return a.copy('A')

    def _inv_jaw(self, a, frame):
        if (self.target == CoordinateSystem.IEC_60601_2_1) or (self.target == CoordinateSystem.VARIAN):
            if (frame == CoordinateSystem.IEC_60601_2_1) or (frame == CoordinateSystem.VARIAN):
                return a.copy('A')
            else:
                x = a.copy('A')
                x[np.where(a != 0)] *= -1.0
                return x
        else:
            if (frame == CoordinateSystem.IEC_60601_2_1) or (frame == CoordinateSystem.VARIAN):
                # x = a.copy('A') * -1.0
                # return x
                x = a.copy('A')
                x[np.where(a != 0)] *= -1.0
                return x
            else:
                return a.copy('A')

    def _couch_vrt_lat(self, a, frame):
        if self.target == frame:
            return a.copy('A')

        if self.target == CoordinateSystem.IEC_61217:
            if frame == CoordinateSystem.IEC_60601_2_1:
                x = np.zeros_like(a)

                idx_0_N = np.where(np.logical_and(a > 0, a <= 500))
                x[idx_0_N] = -1.0 * a[idx_0_N]

                idx_1000_N = np.where(np.logical_and(a > 500, a < 1000))
                x[idx_1000_N] = 1000 - a[idx_1000_N]

                return x

            elif frame == CoordinateSystem.VARIAN:
                return 100.0 - a

            else:
                raise ValueError(f"Scale value of '{frame}' is not supported")
        elif self.target == CoordinateSystem.IEC_60601_2_1:
            if frame == CoordinateSystem.IEC_61217:
                x = np.zeros_like(a)

                idx_N_0 = np.where(a < 0)
                x[idx_N_0] = -1.0 * a[idx_N_0]

                idx_0_N = np.where(a > 0)
                x[idx_0_N] = 1000 - a[idx_0_N]

                return x

            elif frame == CoordinateSystem.VARIAN:
                x = np.zeros_like(a)

                idx_100_N = np.where(a >= 100)
                x[idx_100_N] = a[idx_100_N] - 100

                idx_N_100 = np.where(a < 100)
                x[idx_N_100] = 900 + a[idx_N_100]

                return x

            else:
                raise ValueError(f"Scale value of '{frame}' is not supported")

        elif self.target == CoordinateSystem.VARIAN:
            if frame == CoordinateSystem.IEC_61217:
                return 100.0 - a
            elif frame == CoordinateSystem.IEC_60601_2_1:
                x = np.zeros_like(a)

                idx_N_1000 = np.where(np.logical_and(a >= 900, a <= 1000))
                x[idx_N_1000] = a[idx_N_1000] - 900.0

                idx_0_N = np.where(np.logical_and(a >= 0, a < 500))
                x[idx_0_N] = 100 + a[idx_0_N]

                return x
            else:
                ValueError(f"Scale value of '{frame}' is not supported")
        else:
            raise ValueError(f"Scale value of '{frame}' is not supported")

    def _couch_yaw(self, a, frame):
        if self.target == frame:
            return a.copy('A')

        if self.target == CoordinateSystem.IEC_61217:
            if frame == CoordinateSystem.IEC_60601_2_1:
                x = 360 - a
                return x

            elif frame == CoordinateSystem.VARIAN:
                x = np.zeros_like(a)

                idx_0_180 = np.where(np.logical_and(a >= 0, a <= 180))
                x[idx_0_180] = 180 - a[idx_0_180]

                idx_180_360 = np.where(np.logical_and(a > 180, a <= 360))
                x[idx_180_360] = 360 - (a[idx_180_360] - 180)

                x[np.where(np.abs(x) == 360)] = 0

                return x

            else:
                raise ValueError(f"Scale value of '{frame}' is not supported")

        elif self.target == CoordinateSystem.IEC_60601_2_1:
            if frame == CoordinateSystem.IEC_61217:
                x = 360 - a
                x[np.where(np.abs(x) == 360)] = 0
                return x
            elif frame == CoordinateSystem.VARIAN:
                x = np.zeros_like(a)

                idx_0_180 = np.where(np.logical_and(a >= 0, a <= 180))
                x[idx_0_180] = a[idx_0_180] + 180

                idx_180_360 = np.where(np.logical_and(a > 180, a <= 360))
                x[idx_180_360] = a[idx_180_360] - 180

                x[np.where(np.abs(x) == 360)] = 0

                return x
            else:
                raise ValueError(f"Scale value of '{frame}' is not supported")

        elif self.target == CoordinateSystem.VARIAN:
            if frame == CoordinateSystem.IEC_61217:
                x = np.zeros_like(a)

                idx_0_180 = np.where(np.logical_and(a >= 0, a <= 180))
                x[idx_0_180] = 180 - a[idx_0_180]

                idx_180_360 = np.where(np.logical_and(a > 180, a <= 360))
                x[idx_180_360] = (360 - a[idx_180_360]) + 180

                x[np.where(np.abs(x) == 360)] = 0

                return x
            elif frame == CoordinateSystem.IEC_60601_2_1:
                x = np.zeros_like(a)

                idx_0_180 = np.where(np.logical_and(a > 0, a <= 180))
                x[idx_0_180] = 180 + a[idx_0_180]

                idx_180_360 = np.where(np.logical_and(a >= 180, a <= 360))
                x[idx_180_360] = a[idx_180_360] - 180

                x[np.where(np.abs(x) == 360)] = 0

                return x
            else:
                raise ValueError(f"Scale value of '{frame}' is not supported")
        else:
            raise ValueError(f"Scale value of '{frame}' is not supported")