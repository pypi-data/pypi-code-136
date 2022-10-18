# -*- coding: utf-8 -*-
"""
Copyright (c) 2015 Michael J Tallhamer

Varian Trajectory Log Definitions
Field definitions for Varian trajectory logs as layed out in the "TrueBeam 2.7MR2 Trajectory Log File Specification"
found on the myvarian site (https://varian.force.com/)

@author: Michael J Tallhamer M.Sc DABR (mike.tallhamer@pm.me)
"""
# Standard python imports

# Third party imports
import param

# Local imports.
from .header import VMSTrajectoryLogSubbeamHeader


class VMSTrajectoryLogSubbeam(param.Parameterized):
    """
        Simple storage object that parses out, stores, and provides 'get' access to the subbeam information for a
        VMSTrajectoryLog. The simplistic 'readonly' access provided by the properties is used to discourage setting
        these values by mistake using the simple assignment operator '=' during use. These values are used in a number
        of calculation fuctions to determine the accuracy of delivery so changing them is not recomended.

        Currently there is no reason to write a trajectory log within the Varian framework as they are very simple
        diagnostic tools. With that in mind assignment to these attributes with the intent to write out later is not
        supported at this time.
    """
    log_file = param.Parameter(doc="The VMSTrajectoryLog object this subbeam belogs to.",
                               constant=True
                               )
    header = param.ClassSelector(doc="""
        The VMSTrajectoryLogSubbeamHeader object representing the header for the subbeam.""",
                                 class_=VMSTrajectoryLogSubbeamHeader,
                                 constant=True
                                 )
    snapshots = param.Array(doc="""
    The (NumberOfSnapshots X 2*samples) numpy array representing the snapshots for all axes in the Varian Trajectory Log
    .bin file for the associated subbeam. The 2 * samples comes from the header.samples_per_axis representing both the 
    expected and actual values per sample.""",
                            constant=True
                            )
    index_map = param.Dict(doc="""
    Dictionary of key (Axis Name) value (Axis Index) pairs where users can access the column index values associated 
    with the given axis name. The index represents the first sample column for the named axis.""",
                           constant=True
                           )
    recarray = param.Array(doc="""
    The numpy.recarray view giving you dot '.' access as well as dict type access '[]' to the axis and sample data (i.e.
    object.recarray.MU.actual or object.recarray['MU']['actual']). The numpy dtype object reresenting the view is
    constructed using the definitions.AXIS Enum, definitions.COMPOSITE_TYPE dict, and the definitions.SAMPLE_TYPE
    numpy.dtype.""",
                           constant=True
                           )
    dataframe = param.DataFrame(doc="""
    The pandas.DataFrame view giving you dot '.' access as well as "fancy indexing" into the trajectory log data
    columns. The columns are not organized according to the composite column specification in the "TrueBeam 2.7MR2 
    Trajectory Log File Specification" document as the pandas.DataFrame objects (and param and panel objecs) do not
    support composite and non-composite columns in the same frame. Therefore composite axes like MLC are represented as
    individual columns and samples (i.e. object.dataframe.LeafA1_expected not object.dataframe.MLC.LeafA1.expected) as
    in the recarray view and the individual axis objects. If you need this type 0f axis use those views instead""",
                                constant=True
                                )
    start_index = param.Integer(doc="The starting row index for the snapshots in the subbeam object.",
                                constant=True
                                )
    stop_index = param.Integer(doc="""
    The last row index (+1) for the snapshots in the subbeam object to be used in slicing if needed.""",
                               constant=True
                               )

    # --------------------------------------------------------------------------
    # 'VMSTrajectoryLogSubbeam' Private Methods
    # --------------------------------------------------------------------------
    @param.depends('log_file', watch=True)
    def _parse(self):
        """
            Method used to parse the Varian Trajectory Log Subbeams into their various components.
        """
        # print("Parsing Subbeam")

        with param.edit_constant(self):
            # Build the VMSTrajectoryLogSubbeamHeader passing 'self' as the subbeam object.
            self.header = VMSTrajectoryLogSubbeamHeader()
            with param.edit_constant(self.header):
                self.header.subbeam = self
