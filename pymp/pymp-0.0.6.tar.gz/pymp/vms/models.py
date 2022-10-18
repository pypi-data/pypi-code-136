# -*- coding: utf-8 -*-
'''
Copyright (c) 2015 Michael J Tallhamer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

@author: Michael J Tallhamer M.Sc DABR (mike.tallhamer@gmail.com)
'''
# Standard python imports

# Third party imports
import numpy as np

# Local imports.
from pymp.models.machine.component import RectangularCollimator, CollimatorCollection
from pymp.models.machine.base import Units
from pymp.models.machine.transform import Affine2DTranslation

# -------------------------------------------------------------------------------
# Begin IEC 61217 Scale Layout
# -------------------------------------------------------------------------------


                    ###################################
                    #                |                #
                    #     -----------|-----------     #
                    #     :          |          :     #
                    #     :          |          :     #
                    #     :          |          :     #
                    #     :          |          :     #
                    #  X1 :          |          : X2  #
                    #  Y1 :          |          : Y2  #
                    #     :          |          :     #
                    #     :          |          :     #
                    #     :          |          :     #
                    #     -----------|-----------     #
                    #                |                #
                    ###################################

                    #     <--------------------->
                    #      -1        0        +1  X1,Y1
                    #      -1        0        +1  X2,Y2

# -------------------------------------------------------------------------------
# End IEC 61217 Scale Layout
# -------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Begin Varian BEV Layout
#-------------------------------------------------------------------------------

                    ##################################E
                    #               BEV               #
                    ###################################
                    #                Y2               #
                    #  60 -----------------------  60 #
                    #     :                     :     #
                    #     :                     :     #
                    #     :                     :     #
                    #     :                     :     #
                    #  X1 :                     : X2  #
                    # (B) :                     : (A) #
                    #     :                     :     #
                    #     :                     :     #
                    #     :                     :     #
                    #  1  -----------------------  1  #
                    #               Y1                #
                    ###################################

                    # A Bank under X2 A1 toward Y1
                    # B Bank under X1 B1 toward Y1

#-------------------------------------------------------------------------------
# End Varian BEV Layout
#-------------------------------------------------------------------------------

x1_coords = np.array([[-35.0,20.0],
                      [0.,20.0],
                      [0.,-20.0],
                      [-35.0,-20.0]
                      ],
                      dtype=np.float
                     )

x2_coords = np.array([[0.,20.0],
                      [35.0,20.0],
                      [35.0,-20.0],
                      [0.,-20.0]
                      ],
                      dtype=np.float
                     )

y1_coords = np.array([[-20.0,0.],
                      [20.0,0.],
                      [20.0,-35.0],
                      [-20.0,-35.0]
                      ],
                      dtype=np.float
                     )

y2_coords = np.array([[-20.0,35.0],
                      [20.0,35.0],
                      [20.0,0.],
                      [-20.0,0.]
                      ],
                      dtype=np.float
                      )

full_leaf_coords = np.array([[0.0, 0.0],
                             [20.0, 0.0],
                             [20.0, -1.0],
                             [0.0, -1.0]
                             ],
                             dtype=np.float
                            )

half_leaf_coords = np.array([[0.0, 0.0],
                             [20.0, 0.0],
                             [20.0, -0.5],
                             [0.0, -0.5]
                             ],
                             dtype=np.float
                            )

quarter_leaf_coords = np.array([[0.0, 0.0],
                                [20.0, 0.0],
                                [20.0, -0.25],
                                [0.0, -0.25]
                                ],
                                dtype=np.float
                               )
#-------------------------------------------------------------------------------
# Begin Generic Convenience Classes
#-------------------------------------------------------------------------------

class MLCLeafFull(RectangularCollimator):
    """
    """
    def __init__(self, axis=0, coords=full_leaf_coords, units=Units.CENTIMETER,
                 transform=Affine2DTranslation, name='FullLeaf', **kwargs):
        """
        """
        super(MLCLeafFull, self).__init__(axis=axis,
                                          coords=coords,
                                          units=units,
                                          transform=transform,
                                          name=name,
                                          **kwargs
                                          )

class MLCLeafHalf(RectangularCollimator):
    """
    """
    def __init__(self, axis=0, coords=half_leaf_coords, units=Units.CENTIMETER,
                 transform=Affine2DTranslation, name='HalfLeaf', **kwargs):
        """
        """
        super(MLCLeafHalf, self).__init__(axis=axis,
                                          coords=coords,
                                          units=units,
                                          transform=transform,
                                          name=name,
                                          **kwargs
                                          )

class MLCLeafQuarter(RectangularCollimator):
    """
    """
    def __init__(self, axis=0, coords=quarter_leaf_coords, units=Units.CENTIMETER,
                 transform=Affine2DTranslation, name='QuarterLeaf', **kwargs):
        """
        """
        super(MLCLeafQuarter, self).__init__(axis=axis,
                                             coords=coords,
                                             units=units,
                                             transform=transform,
                                             name=name,
                                             **kwargs
                                             )

class VarianX1Jaw(RectangularCollimator):
    """
    """
    def __init__(self, axis=0, coords=x1_coords, units=Units.CENTIMETER,
                 transform=Affine2DTranslation, name='X1', flip=False, **kwargs):
        """
        """
        super(VarianX1Jaw, self).__init__(axis=axis,
                                          coords=coords,
                                          units=units,
                                          transform=transform,
                                          name=name,
                                          flip=flip,
                                          **kwargs
                                          )

class VarianX2Jaw(RectangularCollimator):
    """
    """
    def __init__(self, axis=0, coords=x2_coords, units=Units.CENTIMETER,
                 transform=Affine2DTranslation, name='X2', flip=True, **kwargs):
        """
        """
        super(VarianX2Jaw, self).__init__(axis=axis,
                                          coords=coords,
                                          units=units,
                                          transform=transform,
                                          name=name,
                                          flip=flip,
                                          **kwargs
                                          )

class VarianY1Jaw(RectangularCollimator):
    """
    """
    def __init__(self, axis=1, coords=y1_coords, units=Units.CENTIMETER,
                 transform=Affine2DTranslation, name='Y1', flip=True, **kwargs):
        """
        """
        super(VarianY1Jaw, self).__init__(axis=axis,
                                          coords=coords,
                                          units=units,
                                          transform=transform,
                                          name=name,
                                          flip=flip,
                                          **kwargs
                                          )

class VarianY2Jaw(RectangularCollimator):
    """
    """
    def __init__(self, axis=1, coords=y2_coords, units=Units.CENTIMETER,
                 transform=Affine2DTranslation, name='Y2', flip=False, **kwargs):
        """
        """
        super(VarianY2Jaw, self).__init__(axis=axis,
                                          coords=coords,
                                          units=units,
                                          transform=transform,
                                          name=name,
                                          flip=flip,
                                          **kwargs
                                          )

class VarianHD120(CollimatorCollection):
    """
    """
    def __init__(self, name='HD120', **kwargs):
        """
        """
        super(VarianHD120, self).__init__(name=name, **kwargs)
        # Based on BEV geometry leaves go 60 down to 1 reading top to bottom of
        # the BEV. We want the leaves in order (i.e. A or B 1-60) so we have to
        # work up from the bottom.

        # We need the starting position for the top edge of the leaves so we
        # will start at the bottom of the BEV coordinates in IEC-61217 and add
        # a leaf width before each leaf is created.
        top = -11.0
        left = 0.0

        # Bottom 14 Half width (0.5cm) leaves
        for i in range(14):
            top += 0.5  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafA{i + 1}'
            self.append(MLCLeafHalf(coords=half_leaf_coords + np.array([left, top]),
                                    flip=True,
                                    name=name
                                    )
                        )

        # Central 32 Quarter width (0.25cm) leaves
        for i in range(14,46):
            top += 0.25  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafA{i + 1}'
            self.append(MLCLeafQuarter(coords=quarter_leaf_coords + np.array([left, top]),
                                       flip=True,
                                       name=name
                                       )
                        )

        # Top 14 Half width (0.5cm) leaves
        for i in range(46, 60):
            top += 0.5  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafA{i + 1}'
            self.append(MLCLeafHalf(coords=half_leaf_coords + np.array([left, top]),
                                    flip=True,
                                    name=name
                                    )
                        )

        ##################################
        # Repeat to create B side leaves #
        ##################################

        # Start at the bottom for leaf 1
        top = -11.0
        left = -20.0

        # Bottom 14 Half width (0.5cm) leaves
        for i in range(14):
            top += 0.5  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafB{i + 1}'
            self.append(MLCLeafHalf(coords=half_leaf_coords + np.array([left, top]),
                                    flip=False,
                                    name=name
                                    )
                        )

        # Central 32 Quarter width (0.25cm) leaves
        for i in range(14, 46):
            top += 0.25  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafB{i + 1}'
            self.append(MLCLeafQuarter(coords=quarter_leaf_coords + np.array([left, top]),
                                       flip=False,
                                       name=name
                                       )
                        )

        # Top 14 Half width (0.5cm) leaves
        for i in range(46, 60):
            top += 0.5  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafB{i + 1}'
            self.append(MLCLeafHalf(coords=half_leaf_coords + np.array([left, top]),
                                    flip=False,
                                    name=name
                                    )
                        )

class VarianMillennium120(CollimatorCollection):
    """
    """

    def __init__(self, name='Millennium120', **kwargs):
        """
        """
        super(VarianMillennium120, self).__init__(name=name, **kwargs)
        # Based on BEV geometry leaves go 60 down to 1 reading top to bottom of
        # the BEV. We want the leaves in order (i.e. A or B 1-60) so we have to
        # work up from the bottom.

        # We need the starting position for the top edge of the leaves so we
        # will start at the bottom of the BEV coordinates in IEC-61217 and add
        # a leaf width before each leaf is created.
        top = -20.0
        left = 0.0

        # Bottom 10 Full width (1.0cm) leaves
        for i in range(10):
            top += 1  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafA{i + 1}'
            self.append(MLCLeafFull(coords=full_leaf_coords + np.array([left, top]),
                                    flip=True,
                                    name=name
                                    )
                        )

        # Central 40 Half width (0.5cm or 5mm) leaves
        for i in range(10, 50):
            top += 0.5  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafA{i + 1}'
            self.append(MLCLeafHalf(coords=full_leaf_coords + np.array([left, top]),
                                    flip=True,
                                    name=name
                                    )
                        )

        # Top 10 Full width (1.0cm or 10mm) leaves
        for i in range(50, 60):
            top += 1  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafA{i + 1}'
            self.append(MLCLeafFull(coords=full_leaf_coords + np.array([left, top]),
                                    flip=True,
                                    name=name
                                    )
                        )

        ##################################
        # Repeat to create B side leaves #
        ##################################

        # Start at the bottom for leaf 1
        top = -20.0
        left = -20.0

        # Bottom 10 Full width (1.0cm) leaves
        for i in range(10):
            top += 1  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafB{i + 1}'
            self.append(MLCLeafFull(coords=full_leaf_coords + np.array([left, top]),
                                    flip=False,
                                    name=name
                                    )
                        )

        # Central 40 Half width (0.5cm or 5mm) leaves
        for i in range(10, 50):
            top += 0.5  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafB{i + 1}'
            self.append(MLCLeafHalf(coords=full_leaf_coords + np.array([left, top]),
                                    flip=False,
                                    name=name
                                    )
                        )

        # Top 10 Full width (1.0cm or 10mm) leaves
        for i in range(50, 60):
            top += 1  # Add leaf width (cm)
            # Format the leaf name to match that common to the VMS Trajectory Log Specification
            name = f'LeafB{i + 1}'
            self.append(MLCLeafFull(coords=full_leaf_coords + np.array([left, top]),
                                    flip=False,
                                    name=name
                                    )
                        )
