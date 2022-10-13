from collections import namedtuple

import ipympl
import matplotlib.pyplot as plt

from wridgets.app import Container

MPLEvent = namedtuple('MPLEvent', ['event_type', 'on_event', 'cid', 'active'])

class MPLFig(Container):
    _events = None
    event_types = [
        'resize_event',
        'draw_event',
        'key_press_event',
        'key_release_event',
        'button_press_event',
        'button_release_event',
        'scroll_event',
        'motion_notify_event',
        'pick_event',
        'figure_enter_event',
        'figure_leave_event',
        'axes_enter_event',
        'axes_leave_event',
        'close_event'
    ]
    
    def make(self, fig=None, makefig=None, updatefig=None, close_previous_figs=True, **kwargs):
        super().make(contents=fig, **kwargs)
        self._makefig = makefig
        self._updatefig = updatefig
        self.close_previous_figs = close_previous_figs
        self._events = {}
        if self.fig is not None:
            for event_type in self.event_types:
                if event_type in kwargs:
                    self.connect_event(event_type, kwargs.get(event_type))
        self.defaults.update(kwargs)

    @property
    def fig(self):
        return self.contents
    
    @fig.setter
    def fig(self, fig):
        if self.close_previous_figs:
            if self.contents is not None:
                plt.close(self.contents.number)
        
        self.contents = fig
        
        for event in self.events.values():
            if event.active:
                self.connect_event(event.event_type, event.on_event, overwrite=True)
        
    @property
    def events(self):
        return self._events
    
    @staticmethod
    def makefig(self, *args, **kwargs):
        self.fig = self._makefig(*args, **kwargs)
    
    @staticmethod
    def updatefig(self, *args, **kwargs):
        self._updatefig(*args, **kwargs)
        self.fig.show()
    
    def set_makefig(self, makefig):
        self._makefig = makefig

    def set_updatefig(self, updatefig):
        self._updatefig = updatefig

    def _display_contents(self):
        with self.container:
            self.container.clear_output()
            if self.fig is not None:
                self.fig.show()

    def _validate_event_type(self, event_type):
        assert event_type in self.event_types, \
            f'{event_type} not found. available types are {self.event_types}'
    
    def connect_event(self, event_type, on_event, overwrite=False):
        self._validate_event_type(event_type)

        old_event = self.events.get(event_type)
        if overwrite:
            if old_event is not None:
                self.fig.canvas.mpl_disconnect(old_event.cid)
        else:
            assert old_event is None, 'Cannot overwrite previous event while overwrite = False'
            
        cid = self.fig.canvas.mpl_connect(event_type, on_event)
        event = MPLEvent(event_type=event_type, on_event=on_event, cid=cid, active=True)
        self.events.update({event_type: event})
    
    def deactivate_event(self, event_type):
        event = self.events.get(event_type)
        assert event is not None, f'No event of type {event_type} to deactivate.'
        self.fig.canvas.mpl_disconnect(event.cid)
        event._replace(active=False)
    
    def reactivate_event(self, event_type):
        event = self.events.get(event_type)
        assert event is not None, f'No event of type {event_type} to reactive.'
        cid = self.fig.canvas.mpl_connect(event.event_type, event.on_event)
        event._replace(cid=cid)
        event._replace(active=True)
    
    def delete_event(self, event_type):
        self.deactivate_event(event_type)
        self.events.pop(event_type)


def contain_fig(figtype):
    def inner(func):
        def selection(*args, **kwargs):
            if figtype == 'mpl':
                return MPLFig(fig=func(), makefig=func)
        return selection
    return inner
