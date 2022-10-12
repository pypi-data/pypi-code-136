from __future__ import annotations
import pandas

from . import SlicingOptions
from . import InterpOptions

class Variable:
    def __init__(self, variable) -> None:
        self.variable = variable

    @property
    def name(self) -> str:
        return self.variable.name
    
    @property
    def units(self) -> str:
        return self.variable.units
    
    @property
    def indeps(self) -> Sequence[Variable]:
        return [Variable(x) for (x) in self.variable.indeps]
    
    @indeps.setter
    def indeps(self, indeps):
        self.variable.indeps = [x.variable for (x) in indeps]

    @property
    def value(self):
        return self.variable.value

    @value.setter
    def value(self, val):
        self.variable.value = val

    @property
    def dataframe(self) -> pandas.DataFrame:
        df = self.variable.dataframe
        overall = {}
        indeps = []
        deps = []
        for var in df[0]:
            indeps.append(var.value)
            name = var.name + " (Indep)"
            overall[name] = var.value
        for var in df[1]:
            deps.append(var.value)
            name = var.name + " (Dep)"
            overall[name] = var.value
        return pandas.DataFrame(overall)

    @staticmethod
    def _build_options_map(options_list: list):
        """
        Convert a list of options (enum types) to a map with exactly one value for each type
        """
        opts = {}
        if options_list is None:
            return opts

        for option in options_list:
            if type(option) in opts and opts[type(option)] != option.value:
                raise RuntimeError("Cannot specify contradictory option values")

            opts[type(option)] = option.value 

        return opts

    @staticmethod
    def __get_slice_options(options_list):
        final_options = SlicingOptions._SliceDataOptionsDefaults.copy()
        final_options.update(Variable._build_options_map(options_list))
        return [final_options[feature] for feature in SlicingOptions._SliceDataOptionsOrder]

    @staticmethod
    def __get_interp_options(options_list):
        final_options = InterpOptions._InterpDataOptionsDefaults.copy()
        final_options.update(Variable._build_options_map(options_list))
        return [final_options[feature] for feature in InterpOptions._InterpDataOptionsOrder]    

    @staticmethod
    def __unpack_tuples(zipped_list):
        """
        Unpack a list of 2-tuples into two lists---one of the first tuple elements and one of the second.

        This function is the inverse of 'zip'. Given a list of 2-tuples, return 2 lists where the first
        contains all of the first tuple elements and the second list contains all of the second elements.
        Example:
        input of the form [(A, 1), (B, 2), ..., (Z,26)]
        output of the form ([A, B, ..., Z], [1, 2, ..., 26])
        """
        if zipped_list is None or len(zipped_list) == 0:
            return [(), ()]

        return list(zip(*zipped_list))

    def slice_data(self, query_items = None, slice_options: list = None) -> Variable:
        """
        Get a subset of data from a variable according to indep params, following certain slicing options.

        query_items has the following form:
        [ (indep_name1: indep_value1), (indep_name2: indep_value2), ... , (indep_nameN: indep_valueN) ]
        where name is the name of an indep and value is the associated search value for that indep
        
        slice_options is a list of the enumerated options
        [ option1, option2, ..., optionN ]
        if user specifies multiple contradictory values for an option we will throw an exception
        """
        indep_names, indep_values = Variable.__unpack_tuples(query_items)
        return Variable(self.variable.slice_data(indep_names, indep_values, Variable.__get_slice_options(slice_options)))

    def interp_data(self, query_items = None, interp_options: list = None) -> Variable:
        """
        Get a interpolated data from a variable according to indep params according to interpolation options.

        query_items has the following form:
        [ (indep_name1: indep_value1), (indep_name2: indep_value2), ... , (indep_nameN: indep_valueN) ]
        where name is the name of an indep and value is the associated search value for that indep
        
        interp_options is a list of the enumerated options
        [ option1, option2, ..., optionN ]
        if user specifies multiple contradictory values for an option we will throw an exception
        """
        indep_names, indep_values = Variable.__unpack_tuples(query_items)
        return Variable(self.variable.interp_data(indep_names, indep_values, Variable.__get_interp_options(interp_options)))
