#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

#  Inspired by the original work of Nilton Volpato.
#  https://github.com/NiltonVolpato/python-progressbar

import re
import time
import math

from .enums import *
from .widgets import Widget
from .prebuilds import WIDGETS

# init widgets repository
WIDGETS_PATTERN = re.compile("(\{[a-zA-Z0-9_]+\})")


class Bar(object):
    """
    Bar is the main progress monitor class. The easiest way to monitor
    progress is to initialize the **Bar** object with a custom template,
    using predefined widgets and continuously increase its value. Although
    this should cover most of the use cases, there are many ways to go deeper
    to customize the main progress bar or individual widgets.
    
    Attrs:
        minimum: int or float
            Returns current minimum value.
        
        maximum: int or float
            Returns current maximum value.
        
        current: int or float
            Returns current progress value.
        
        percent: float
            Returns current progress as percentage.
        
        elapsed: float
            Returns current elapsed time in seconds.
        
        finished: bool
            Returns True if current progress finished already, False otherwise.
        
        samples:
            Returns last progress samples as ((value, elapsed),).
        
        updates: int
            Returns number of widgets updates.
    """
    
    def __init__(self, *widgets, minimum=0, maximum=None, size=80, refresh=0.5, keep=0.05, output=None):
        """
        Initializes a new instance of the Progress monitor class.
        
        Args:
            widgets: (Widget,) or str
                Collection of widgets to display on each update. The widget can
                be one of the many predefined widgets, simple string to show or
                any class derived from the Widget base. The widgets can also be
                provided using a template, where the widgets are specified by a
                name in curly brackets (e.g. 'Processed: {count} ETA: {eta}').
            
            minimum: int or float
                Minimum progress value or count.
            
            maximum: int, float or None
                Maximum progress value or count.
            
            size: int
                Number of characters available to display the progress.
            
            refresh: float
                Minimum number of seconds between individual updates to be
                displayed.
            
            keep: int or float
                Absolute or relative number of last updates to keep for adaptive
                widgets like ETA or speed. If value is grater than 1 it is
                considered as absolute, otherwise it is relative to maximum
                value. The widgets are calculating progress from last
                measurements instead of overall progress.
            
            output: any
                Custom output to which all the progress and messages are writen.
                This must support 'write' and 'flush' method calls.
        """
        
        self._variables = {}
        self._widgets = widgets
        
        self._min_value = minimum
        self._max_value = maximum
        self._curr_value = None
        
        self._start_time = None
        self._end_time = None
        self._finished = False
        
        self._keep = keep
        self._samples = []
        
        self._size = int(size)
        self._refresh = float(refresh)
        self._updates = 0
        self._update_time = None
        self._next_update = None
        
        self._output = output
    
    
    def __enter__(self):
        """Enters the with block."""
        
        self.start()
        return self
    
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exits the with block."""
        
        self.finish()
    
    
    def __iadd__(self, value):
        """Increases current progress by given value."""
        
        self.increase(value)
        return self
    
    
    @property
    def minimum(self):
        """Returns current minimum value."""
        
        return self._min_value
    
    
    @property
    def maximum(self):
        """Returns current maximum value."""
        
        return self._max_value
    
    
    @property
    def current(self):
        """Returns current progress value."""
        
        return self._curr_value
    
    
    @property
    def percent(self):
        """Returns current progress as percentage."""
        
        if not self._max_value:
            return None
        
        return 100. * (self._curr_value / self._max_value)
    
    
    @property
    def elapsed(self):
        """Returns current elapsed time in seconds."""
        
        if self._start_time is None:
            return 0
        
        if self._end_time is not None:
            return self._end_time - self._start_time
        
        return time.time() - self._start_time
    
    
    @property
    def finished(self):
        """Returns True if current progress finished already, False otherwise."""
        
        return self._finished
    
    
    @property
    def samples(self):
        """Returns last progress samples as ((value, elapsed),)."""
        
        return tuple(self._samples)
    
    
    @property
    def updates(self):
        """Returns number of widgets updates."""
        
        return self._updates
    
    
    def start(self, value=0, minimum=None, maximum=None):
        """
        Starts progress time. Additionally, it allows to set the progress range,
        if the information was not available upon init.
        
        Args:
            value: int or float
                Initial value at which the progress starts.
            
            minimum: int, float or None
                Minimum progress value or count. If set to None, the original
                value is retained.
            
            maximum: int, float or None
                Maximum progress value or count. If set to None, the original
                value is retained.
        """
        
        # reset
        self._start_time = time.time()
        self._end_time = None
        self._update_time = None
        self._finished = False
        self._next_update = None
        
        # reset range
        if minimum is not None:
            self._min_value = minimum
        if maximum is not None:
            self._max_value = maximum
        
        # init widgets
        if not self._widgets:
            self._widgets = [DEFAULT_BAR] if maximum else [DEFAULT_BAR_NOMAX]
        self._widgets = self._init_widgets(self._widgets)
        
        # init measurements to keep
        if self._keep < 1 and maximum:
            self._keep = max(int(maximum * self._keep), 5)
        elif self._keep >= 1:
            self._keep = int(self._keep)
        
        # update progress
        self.update(value)
        
        return self
    
    
    def update(self, value=None):
        """
        Updates current progress time and value and automatically update
        displayed bar if needed.
        
        Args:
            value: int or float
                Specifies the new value to set for current progress.
        """
        
        # start if needed
        if self._start_time is None:
            self.start(value)
            return
        
        # update current value
        if value is not None:
            self._curr_value = value
        
        # store sample
        self._samples.append((value, self.elapsed))
        
        # remove old samples
        while len(self._samples) > self._keep:
            self._samples.pop(0)
        
        # update widgets if needed
        if self._should_update():
            
            # show widgets
            line = self._format_widgets(self._widgets)
            self._write_line("\r", line, "")
            
            # set update time
            self._update_time = time.time()
            self._updates += 1
    
    
    def increase(self, value=1):
        """
        Increases current progress by given value and automatically update
        displayed bar if needed.
        
        Args:
            value: int or float
                Specifies the value by which current progress should be
                increased.
        """
        
        # increase value
        value = value + self._curr_value if self._curr_value else value
        
        # update progress
        self.update(value)
    
    
    def finish(self, *widgets, permanent=True):
        """
        Finalizes current progress and optionally prints final report by
        provided widgets template.
        
        Args:
            widgets: (Widget,) or str
                Collection of widgets to display on each update. The widget can
                be one of the many predefined widgets, simple string to show or
                any class derived from the Widget base. The widgets can also be
                provided using a template, where the widgets are specified by a
                name in curly brackets (e.g. 'Processed: {count} ETA: {eta}').
            
            permanent: bool
                If set to True, line is ended by new-line character and stays
                visible even after next progress update.
        """
        
        # set state
        self._end_time = time.time()
        self._finished = True
        
        # update with max value
        self.update(self._max_value)
        
        # write final widgets
        widgets = self._init_widgets(widgets)
        if widgets:
            self.write(*widgets, permanent=permanent)
        
        # keep last
        elif permanent:
            self._write_line("\r", "", "\n")
        
        # clear last
        else:
            self._write_line("\r", " ", "")
            self._write_line("\r", "", "")
    
    
    def write(self, *widgets, permanent=True):
        """
        Writes given widgets to current output.
        
        Args:
            widgets: (Widget,) or str
                Collection of widgets to display on each update. The widget can
                be one of the many predefined widgets, simple string to show or
                any class derived from the Widget base. The widgets can also be
                provided using a template, where the widgets are specified by a
                name in curly brackets (e.g. 'Processed: {count} ETA: {eta}').
            
            permanent: bool
                If set to True, line is ended by new-line character and stays
                visible even after next progress update.
        """
        
        # format widgets
        widgets = self._init_widgets(widgets)
        line = self._format_widgets(widgets)
        
        # get end
        end = "\n" if permanent else ""
        
        # write line
        self._write_line("\r", line, end)
        
        # show progress back
        if permanent and self._updates and not self._finished:
            line = self._format_widgets(self._widgets)
            self._write_line("\r", line, "")
    
    
    def register(self, tag, widget):
        """
        Registers a new widget instance to be recognized in the widgets
        templates.
        
        Args:
            tag: str
                Unique tag of the widget to be recognized in the widgets
                templates.
            
            widget: Widget
                The widget instance to be registered.
        """
        
        # format tag
        tag = "{%s}" % tag.lower()
        
        # check if used
        if tag in WIDGETS or tag in self._variables:
            raise KeyError("Widget with the same tag already exists!")
        
        # check if widget
        if not isinstance(widget, Widget):
            raise TypeError("Widget must be of type gress.Widget!")
        
        # add to variables
        self._variables[tag] = widget
        
        # try to init previously unrecognized widgets
        self._widgets = self._init_widgets(self._widgets)
    
    
    def _should_update(self):
        """Checks whether widgets should be updated."""
        
        # check finished
        if self._finished:
            return True
        
        # first update
        if self._update_time is None:
            return True
        
        # check last update time
        if time.time() - self._update_time >= self._refresh:
            return True
        
        return False
    
    
    def _init_widgets(self, widgets):
        """Initializes all widgets given by template string."""
        
        # make editable
        buff = []
        
        # process template
        for widget in widgets:
            
            # no widget
            if widget is None:
                continue
            
            # ready widgets
            if isinstance(widget, Widget):
                buff.append(widget)
                continue
            
            # split template
            items = WIDGETS_PATTERN.split(widget)
            
            # init template widgets
            for item in items:
                
                # make tag
                tag = item.lower()
                
                # get custom variable
                if tag in self._variables:
                    item = self._variables[tag]
                
                # get known widget
                elif tag in WIDGETS:
                    cls, kwargs = WIDGETS[tag]
                    item = cls(**kwargs)
                
                # add to progress
                buff.append(item)
        
        return tuple(buff)
    
    
    def _format_widgets(self, widgets):
        """Formats widgets line."""
        
        # init buffs
        space = self._size
        results = []
        expanding = []
        
        # prepare widgets
        for idx, widget in enumerate(widgets):
            
            # add simple string
            if isinstance(widget, str):
                results.append(widget)
                space -= len(widget)
            
            # block non-widgets
            elif not isinstance(widget, Widget):
                raise TypeError("Unrecognized widget type.")
            
            # add expandable widget
            elif widget.EXPAND:
                results.append(widget)
                expanding.insert(0, idx)
            
            # add regular widget
            else:
                text = widget(self)
                results.append(text)
                space -= len(text)
        
        # finalize expandable
        count = len(expanding)
        while count:
            width = max(int(math.ceil(space * 1. / count)), 0)
            idx = expanding.pop()
            text = results[idx](self, width)
            results[idx] = text
            space -= len(text)
            count -= 1
        
        # join widgets
        line = ''.join(results)
        
        return line
    
    
    def _write_line(self, pref, line, end):
        """Writes line to current output."""
        
        # print line
        if self._output is None:
            print(end=LINE_CLEAR)
            print(pref + line, end=end)
            return
        
        # write line
        self._output.write(LINE_CLEAR)
        self._output.write(pref + line + end)
        self._output.flush()
