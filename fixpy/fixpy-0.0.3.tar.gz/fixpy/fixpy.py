import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import threading


def eps(abs_error=1e-8, rel_error=1e-8):
    def _margin(x, y):
        return (abs(np.log(abs(x))-np.log(abs(y))) < rel_error and x*y >= 0) and abs(x-y) < abs_error
    return _margin


def array_eps(abs_error=1e-8, rel_error=1e-8):
    def _margin(x, y):
        return (np.max(abs(np.log(abs(x))-np.log(abs(y)))) < rel_error and np.all(x*y >= 0)) and np.max(abs(x-y)) < abs_error
    return _margin


def no_change():
    def _no_change(x, y):
        return x == y
    return _no_change


updates_list = []


class Variable:

    def __init__(self, value=None, still_ok=None, max_recursions=None, name=None, alpha=None):
        """
        class that allows for event-based programming
        :param value: value of binding class
        :param still_ok: function that takes original value and new value and returns whether difference is "still ok"
        :param max_recursions: maximum recursion depth (default None: no recursion depth limit)
        :param name: name of node (to draw computation net for debugging)
        such that value does not have to be updated
        """
        if still_ok is None:
            if type(value) == str:
                still_ok = no_change()
            elif type(value) == np.ndarray:
                still_ok = array_eps()
            else:
                still_ok = eps()
        self._value = value.get_value() if isinstance(value, Variable) else value
        self._still_ok = still_ok
        self._max_recursions = max_recursions
        self.name = name
        self.alpha = alpha
        self._lock = threading.Lock()

        self._observers = []  # set of observers that are instances of Variable
        self._callbacks = []  # set of "callback function" - observers
        self._observing = []  # set of observing Variable instances
        self._disable_update = False  # needed when "force setting" the value
        if isinstance(value, Variable):
            self.observe(value)

    def enable_update(self):
        self._disable_update = False

    def disable_update(self):
        """
        by disabling updates, this Variable will not be updated by other observing Variables anymore
        """
        self._disable_update = True

    def get_nodes_and_edges(self, nodes=[], edges=[]):
        if self not in nodes:
            nodes.append(self)
        for o in self._observing:
            if [o, self] not in edges:
                edges.append([o, self])
                nodes, edges = o.get_nodes_and_edges(nodes, edges)
        for o in self._observers:
            if [self, o] not in edges:
                edges.append([self, o])
                nodes, edges = o.get_nodes_and_edges(nodes, edges)
        return nodes, edges

    def __str__(self):
        return "" if self.name is None else self.name

    def plot(self, blocking=True, mark_self=True, show_values=False):
        plt.figure(1, figsize=(5, 5))
        plt.clf()
        g = nx.DiGraph()
        nodes, edges = self.get_nodes_and_edges([], [])
        nodes.sort(key=lambda e: hash(e))
        for node in nodes:
            g.add_node(node)
        for edge in edges:
            g.add_edge(*edge)
        node_color = [(0.5, 0.5, 1) for _ in nodes]
        edge_colors = [(0.2, 0.2, 1) for _ in nodes]
        if mark_self:
            index = nodes.index(self)
            node_color[index] = (1, 0.5, 0.5)
            edge_colors[index] = (1, 0.2, 0.2)
        label_dict = {}
        for n in nodes:
            if show_values:
                label_dict[n] = str(n)+":\n"+str(round(n._value,3))
            else:
                label_dict[n] = str(n)

        nx.draw_kamada_kawai(g, with_labels=True, labels=label_dict, node_size=3000, edge_color=(0, 0, 0),
                             edgecolors=edge_colors, node_color=node_color, font_size=8)
        if blocking:
            plt.show()
        else:
            plt.draw()
            plt.pause(0.0001)

    def get_value(self):
        return self._value

    def set_value(self, new_value, animate_graph=False):
        new_value = new_value.get_value() if isinstance(new_value, Variable) else new_value

        if self._still_ok(self._value, new_value):
            return

        self._lock.acquire()
        self._value = new_value
        tmp_disable_update = self._disable_update
        self._disable_update = True
        self._send_updates(self._max_recursions, animate_graph)
        self._disable_update = tmp_disable_update
        self._lock.release()

    def _send_updates(self, max_recursions=None, animate_graph=False):
        global updates_list
        if max_recursions is None or max_recursions > 0:
            for cb in np.random.permutation(list(self._callbacks)):
                cb(self._value)
            for o in self._observers:
                updates_list = [[o, self, max_recursions], *updates_list]

        while len(updates_list) > 0:
            u = updates_list[0]
            updates_list = updates_list[1:]
            u[0]._update_value(u[1], u[2], animate_graph)

    def _update_value(self, new_value, max_recursions=0, animate_graph=False):
        tmp_new_value = new_value
        new_value = new_value.get_value() if isinstance(new_value, Variable) else new_value

        if self._disable_update or self._still_ok(self._value, new_value):
            return

        if animate_graph:
            self.plot(blocking=False, show_values=True)

        self._value = new_value if self.alpha is None else (1-self.alpha)*self._value + self.alpha * new_value
        self._send_updates(None if max_recursions is None else max_recursions-1, animate_graph)
        if self.alpha is not None:
            self._update_value(tmp_new_value, None if max_recursions is None else max_recursions-1, animate_graph)

    @staticmethod
    def set_values(variables, new_values):
        """
        set values of multiple variables at the same time (might be useful, if there are interdependencies between these
        variables that should not affect each other)
        :param variables: list of variables to set
        :param new_values: list of new values
        """
        tmp_disable_updates = [var._disable_update for var in variables]
        for var in variables:
            var._lock.acquire()
            var._disable_update = True
        for var, val in zip(variables, new_values):
            if not var._still_ok(var._value, val):
                var._value = val
        for var, val in zip(variables, new_values):
            var.set_value(val)
        for var, tmp_disable_update in zip(variables, tmp_disable_updates):
            var._disable_update = tmp_disable_update
            var._lock.release()

    def observe(self, other: 'Variable'):
        other._observers.append(self)
        self._observing.append(other)
        self._update_value(other, self._max_recursions)

    def remove_observers(self, observers=None):
        """
        :param observers: either single observer to remove or list of observers. If None: all observers. Default: None
        """
        if observers is None:
            self.remove_observers(self._observers)
        elif type(observers) is list or type(observers) is set:
            for o in list(observers):
                self.remove_observers(o)
        elif isinstance(observers, Variable):
            self._observers.remove(observers)
            observers._observing.remove(self)
        else:
            raise ValueError(f"observer must be None or (list / set of) Binding-Class Instance but is {observers}")

    def remove_observing(self, observing=None):
        """
        :param observing: either single observing Variable to remove or list. If None: all observing Variables. Default: None
        """
        if observing is None:
            self.remove_observing(self._observing)
        elif type(observing) is list or type(observing) is set:
            for o in list(observing):
                self.remove_observing(o)
        elif isinstance(observing, Variable):
            observing._observers.remove(self)
            self._observing.remove(observing)
        else:
            raise ValueError(f"observing must be None or (list / set of) Binding-Class Instance but is {observing}")

    def on_change(self, callback):
        """
        :param callback: function that takes new changed value as parameter
        """
        self._callbacks.append(callback)

    def remove_callback(self, callback=None):
        if callback is None:
            self._callbacks = []
        else:
            self._callbacks.remove(callback)

    # shortcuts
    @property
    def x(self):
        return self.get_value()

    @x.setter
    def x(self, new_value):
        self.set_value(new_value)

    def __lshift__(self, other: 'Variable'):
        self.observe(other)

    def __rlshift__(self, other):
        if isinstance(other, Variable):
            other.observe(self)
        else:
            self.on_change(other)

    def __rshift__(self, other):
        if isinstance(other, Variable):
            other.observe(self)
        else:
            self.on_change(other)

    def __add__(self, other):
        return Function(lambda a, b: a + b, [self, other], name="add")

    def __sub__(self, other):
        return Function(lambda a, b: a - b, [self, other], name="sub")

    def __mul__(self, other):
        return Function(lambda a, b: a * b, [self, other], name="mul")

    def __truediv__(self, other):
        return Function(lambda a, b: a / b, [self, other], name="div")

    def __pow__(self, other, modulo=None):
        return Function(lambda a, b: a ** b, [self, other], name="pow")

    def __radd__(self, other):
        return Function(lambda a, b: a + b, [other, self], name="radd")

    def __rsub__(self, other):
        return Function(lambda a, b: a - b, [other, self], name="rsub")

    def __rmul__(self, other):
        return Function(lambda a, b: a * b, [other, self], name="rmul")

    def __rtruediv__(self, other):
        return Function(lambda a, b: a / b, [other, self], name="rdiv")

    def __rpow__(self, other, modulo=None):
        return Function(lambda a, b: a ** b, [other, self], name="rpow")

    def __neg__(self):
        return Function(lambda a: -a, [self], name="neg")

    def sqrt(self):
        return Function(lambda a: np.sqrt(a), [self], name="sqrt")


class Function(Variable):
    def __init__(self, fun, parameters, still_ok=None, max_recursions=None, name=None, alpha=None):
        super().__init__(fun(*[p.get_value() if isinstance(p, Variable) else p for p in parameters]), still_ok,
                         max_recursions, name, alpha)
        self._fun = fun
        self._parameters = parameters

        for parameter in parameters:
            if isinstance(parameter, Variable):
                self.observe(parameter)

    def set_value(self, new_value, animate_graph=False):
        new_value = self._fun(*[p.get_value() if isinstance(p, Variable) else p for p in self._parameters]) if isinstance(new_value, Variable) else new_value

        if self._still_ok(self._value, new_value):
            return

        self._lock.acquire()
        self._value = new_value
        self._disable_update = True
        self._send_updates(self._max_recursions, animate_graph)
        self._disable_update = False
        self._lock.release()

    def _update_value(self, new_value, max_recursions=0, animate_graph=False):
        tmp_new_value = new_value
        new_value = self._fun(*[p.get_value() if isinstance(p, Variable) else p for p in self._parameters]) if isinstance(new_value, Variable) else new_value

        if self._disable_update or self._still_ok(self._value, new_value):
            return

        if animate_graph:
            self.plot(blocking=False, show_values=True)

        self._value = new_value if self.alpha is None else (1-self.alpha)*self._value + self.alpha * new_value
        self._send_updates(None if max_recursions is None else max_recursions-1, animate_graph)
        if self.alpha is not None:
            self._update_value(tmp_new_value, None if max_recursions is None else max_recursions-1, animate_graph)
