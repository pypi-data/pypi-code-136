from .optimize import ModelManager

### WHEN RESAMPLE ###
# 1. Underlying DiGraph is copied to the new global statement constructor
# 2. This carries over all elements from the original statement
# 3. All elements containing a DiGraph MUST have their DiGraphs updated
# 4. The original instantiated ModelManager, however, is carried across in the copied DiGraph
# 5. After instantiation, the ModelManager must be overwritten, this time with the new grouped statement and a clone of the origina AbstractModel
# 5. So, ALL elements have a new DiGraph, which is the same among all the elements
# 6. And ALL elements have a new ModelManager and new underlying AbstractModel, which is a clone of the original
# 7. this should allow parameters to be updated via `instance_data` and new instances to be created without issue

"""
BUG FIX NEEDED!!!!!!
GROUPBY has a bug where the graph instances inside each of the lineitems is NOT the same
as the post-groupby instance of the Stat.
So data may be inaccurate when retrieving from lineitem graph nodes
Use the main stat graph instead for now!!!
"""
class Grouper:
    def __init__(self, stat, *args, **kwargs):
        self.original = stat
        self.grouped = stat._constructor(name=stat.name, short_name=stat.short_name, graph=stat.G._graph.copy(), *args, **kwargs)
        for substat in stat.statements:
            self.grouped.add_statement(name=substat.name, short_name=substat.short_name) # have to create new substatement nodes

        self.grouped.G.graph['model_mngr'] = ModelManager(self.grouped, self.grouped.G.graph['model_mngr'].abstract.clone())
        self.grouped.elements.update_graphs(self.grouped.graph._graph)
        self.grouped.M.update_stat(self.grouped)
        
    def _call(self):
        return NotImplementedError

    def sum(self, *args, **kwargs):
        self.funcstr = 'sum'
        return self._call(*args, **kwargs)

    def last(self, *args, **kwargs):
        self.funcstr = 'sum'
        return self._call(*args, **kwargs)

    def mean(self, *args, **kwargs):
        self.funcstr = 'mean'
        return self._call(*args, **kwargs)

class FinStatResampler(Grouper):
    def __init__(self, stat, freq='A-DEC'):
        super().__init__(stat)
        self.freqstr = freq

        _new_periods = stat.periods.asfreq(self.freqstr).unique()
        self.grouped.update_periods(_new_periods)

    def resamp_accounts(self, *args, **kwargs):
        last = kwargs.pop('last', [])
        mean = kwargs.pop('mean', [])
        summ = kwargs.pop('summ', []) 
        
        for name, obj in self.grouped.G.filter_nodes_by_attribute('nodetype', 'account', data='obj', return_tuple=True):
            resampled = obj.resample(self.freqstr)
            if name in last:
                funcstr = 'last'
            elif name in mean:
                funcstr = 'mean'
            elif name in summ:
                funcstr = 'sum'
            else:
                funcstr = self.funcstr
            self.grouped.G.nodes[name]['obj'] = getattr(resampled, funcstr)(*args, **kwargs)

    def _call(self, *args, **kwargs):
        self.resamp_accounts(*args, **kwargs)
        
        if hasattr(self.grouped.M.abstract, 'obj'):
            self.grouped.M.create_instance()
            self.grouped.solve_out_of_context()
        
        return self.grouped

class FinStatGroupBy(Grouper):
    def __init__(self, stat, by, convert_to_account:str=None, convert_all_metrics:bool=False):
        super().__init__(stat)
        self.grouped.G.graph['by'] = by
        self.grouped.G.graph['auto_align'] = True
        self.convert_to_account = [convert_to_account] if isinstance(convert_to_account, str) else convert_to_account
        self.convert_all_metrics = convert_all_metrics

    def metric_to_account(self, name):
        import pyomo.environ as pyo
        convert_node = self.original.G.nodes[name]
        self.grouped.G.remove_node(name)
        to_del = [comp for comp in (self.original.M.abstract.component_objects([pyo.Var, pyo.Set, pyo.Constraint])) if name in comp.name]
        for comp in to_del:
            self.grouped.M.abstract.del_component(comp.name)

        assert not [var.name for var in (self.grouped.M.abstract.component_objects([pyo.Var, pyo.Set, pyo.Constraint])) if name in var.name], 'None of the variables or sets containing this name should exist'
        obj = getattr(self.original, name)

        self.grouped.add_account(
            obj.to_frame(), 
            name=obj.name, 
            short_name=obj.short_name, 
            insert_after=convert_node['insert_after'],
            hide=convert_node['hide']
        )

    def _call(self, *args, **kwargs):
        """
        Params
        -------
        convert_to_account: str; 
            + some metrics do not group easily. for instance, a MethodExpression may reference an index value that is
            eliminated by the Grouper.
            + these metrics can be converted to accounts to avoid the issue
        """
        if self.convert_all_metrics or self.convert_to_account is not None:
            to_convert = self.grouped.metrics.short_names if self.convert_all_metrics else self.convert_to_account
            for name in to_convert:
                self.metric_to_account(name)

        if self.grouped.metrics.size: # only need to solve if metrics exist
            self.grouped.M.create_instance()
            self.grouped.solve_out_of_context()
        else:
            self.grouped.M.abstract.del_component('obj') # if there are no metrics, then the objective_function should be deleted

        return self.grouped
