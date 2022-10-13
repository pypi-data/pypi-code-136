#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

#  Inspired by the original work of Nilton Volpato.
#  https://github.com/NiltonVolpato/python-progressbar

import datetime
from .enums import *
from .utils import format_time, format_power


class Widget(object):
    """
    Provides a base class for all the progress widgets. Each derived class must
    implement the __call__ method, which is called by the progress bar to update
    the widget.
    """
    
    EXPAND = False
    
    
    def __call__(self, progress, width=None, *args, **kwargs):
        """Formats current progress."""
        
        raise NotImplementedError("The '%s' widget does not implement the call method!" % self.__name__)


class Variable(Widget):
    """
    The Variable widget provides a special type of widgets to displays custom
    variables within the progress bar. The variable is typically specified as
    a lambda function with no input parameters, returning the final formatted
    custom value.
    """
    
    
    def __init__(self, callback):
        """
        Initializes a new instance of the Variable widget.
        
        Args:
            callback: callable
                Custom function to be used to retrieve and format the value.
        """
        
        super().__init__()
        
        self._callback = callback
    
    
    def __call__(self, progress, *args, **kwargs):
        """Formats current progress."""
        
        return str(self._callback())


class Property(Widget):
    """
    The Property widget displays specified progress value using given formatting
    template. Optionally, if unit prefixes are provided, the value is scaled
    automatically and corresponding unit prefix is added (e.g. 1000 vs. 1k).
    There are predefined prefixes available like PREFIXES - typically used
    for data scaling. Note that the power multiplier can be specified as well
    (e.g. 1024 for data).
    """
    
    
    def __init__(self, name, template=None, prefixes=None, step=1000):
        """
        Initializes a new instance of the Property widget.
        
        Args:
            name: str
                Name of the progress bar property to show. (E.g. "current",
                "minimum", "maximum".)
            
            template: str
                Custom template to be used to format the property value (e.g.
                "{:.2f}").
            
            prefixes: (str,) or None
                Units prefix for each power.
            
            step: int
                Multiplier of the power.
            """
        
        super().__init__()
        
        self._name = name
        self._template = template
        self._prefixes = prefixes
        self._step = step
    
    
    def __call__(self, progress, *args, **kwargs):
        """Formats current progress."""
        
        # get value
        value = getattr(progress, self._name)
        
        # check value
        if value is None:
            return NA
        
        # format value
        return format_power(value, self._template, self._prefixes, self._step)


class Time(Widget):
    """
    The Time widget displays current time according to specified template, which
    should follow the standard datetime notation (e.g. "%Y-%m-%d %H:%M:%S").
    """
    
    
    def __init__(self, template=None):
        """
        Initializes a new instance of the Time widget.
        
        Args:
            template: str or None
                Custom template to be used to format the time. The template
                should use standard datetime notation
                (e.g. "%Y-%m-%d %H:%M:%S"). If set to None, full time is shown.
        """
        
        super().__init__()
        
        self._template = template
    
    
    def __call__(self, progress, *args, **kwargs):
        """Formats current progress."""
        
        # get current time
        now = datetime.datetime.now()
        
        # use custom template
        if self._template:
            return now.strftime(self._template)
        
        # use default
        return str(now)


class Timer(Widget):
    """
    The Timer widget displays current progress elapsed time, according to
    specified template or formatted automatically as needed. The template can
    use "dhms" characters to format individual parts (e.g. "{m:02}:{s:02}").
    Optionally, the time units can be displayed if automatic formatting is used.
    """
    
    
    def __init__(self, template=TIME_HMS, units=False):
        """
        Initializes a new instance of the Timer widget.
        
        Args:
            template: str or None
                Custom template to be used to format the time. The template can
                use "dhms" characters to format individual parts
                (e.g. "{m:02}:{s:02}"). If set to None, remaining time is
                formatted automatically.
            
            units: bool
                If se to True and no template is provided, remaining time is
                shown with units.
        """
        
        super().__init__()
        
        self._template = template
        self._units = units
    
    
    def __call__(self, progress, *args, **kwargs):
        """Formats current progress."""
        
        # calc elapsed
        elapsed = datetime.timedelta(seconds=int(progress.elapsed))
        
        # format delta
        return format_time(elapsed.seconds, self._template, self._units)


class ETA(Widget):
    """
    The ETA widget displays current progress estimated time of finish, according
    to specified template or formatted automatically as needed. If absolute time
    should be displayed, the template should use the standard datetime notation
    (e.g. "%Y-%m-%d %H:%M:%S"). For remaining time the template can use "dhms"
    characters to format individual parts (e.g. "{m:02}:{s:02}"). Optionally,
    the time units can be displayed if automatic formatting is used.
    
    The time is by default calculated using several latest progress updates,
    unless the adaptive parameter is set to False. In such case the whole
    elapsed time and progress is used.
    """
    
    
    def __init__(self, template=TIME_HMS, units=False, absolute=False, adaptive=True):
        """
        Initializes a new instance of the ETA widget.
        
        Args:
            template: str or None
                Custom template to be used to format the time. For absolute ETA
                the template should use the standard datetime notation
                (e.g. "%Y-%m-%d %H:%M:%S"). For relative ETA the template can
                use "dhms" characters to format individual parts
                (e.g. "{m:02}:{s:02}"). If set to None, remaining time is
                formatted automatically.
            
            units: bool
                If se to True and no template is provided, remaining time is
                shown with units.
            
            absolute: bool
                If set to True, remaining time is shown as the absolute time of
                expected finish, otherwise the remaining time is shown.
            
            adaptive: bool
                If set to True, the speed is calculated from last N updates
                only, otherwise the whole progress is used. Number of updates
                depends on the progress bar settings.
        """
        
        super().__init__()
        
        self._template = template
        self._units = units
        self._absolute = absolute
        self._adaptive = adaptive
    
    
    def __call__(self, progress, *args, **kwargs):
        """Formats current progress."""
        
        # unknown max value or zero current
        if not progress.maximum or not progress.current:
            return TIME_NA
        
        # already finished
        if progress.finished:
            return format_time(0, self._template, self._units)
        
        # get progress
        current = progress.current
        elapsed = progress.elapsed
        remains = progress.maximum - current
        
        # use adaptive measurement
        if self._adaptive and progress.samples:
            oldest = progress.samples[0]
            if current != oldest[0] and elapsed != oldest[1]:
                current -= oldest[0]
                elapsed -= oldest[1]
        
        # calc ETA
        eta = datetime.timedelta(seconds=int(remains * (elapsed / current)))
        
        # show absolute time
        if self._absolute:
            eta = datetime.datetime.now() + eta
            return eta.strftime(TIME_ABS)
        
        # format delta
        return format_time(eta.seconds, self._template, self._units)


class Speed(Widget):
    """
    The Speed widgets displays current progress speed, according to specified
    template. Optionally, if unit prefixes are provided, the value is scaled
    automatically and corresponding unit prefix is added (e.g. 1.5 MBps).
    There are predefined prefixes available like PREFIXES - typically used
    for data scaling. Note that the power multiplier can be specified as well
    (e.g. 1024 for data).
    
    The speed is by default calculated using several latest progress updates,
    unless the adaptive parameter is set to False. In such case the whole
    elapsed time and progress is used.
    """
    
    
    def __init__(self, template="{:.2f}", prefixes=None, step=1000, adaptive=True):
        """
        Initializes a new instance of the Speed widget.
        
        Args:
            template: str
                Custom template to be used to format the speed value.
            
            prefixes: (str,) or None
                Units prefix for each power.
            
            step: int
                Multiplier of the power.
            
            adaptive: bool
                If set to True, the speed is calculated from last N updates
                only, otherwise the whole progress is used. Number of updates
                depends on the progress bar settings.
        """
        
        super().__init__()
        
        self._template = template
        self._prefixes = prefixes
        self._step = step
        self._adaptive = adaptive
    
    
    def __call__(self, progress, *args, **kwargs):
        """Formats current progress."""
        
        # get progress
        current = progress.current
        elapsed = progress.elapsed
        
        # use adaptive measurement
        if self._adaptive and not progress.finished and progress.samples:
            oldest = progress.samples[0]
            if current != oldest[0] and elapsed != oldest[1]:
                current -= oldest[0]
                elapsed -= oldest[1]
        
        # calc speed
        speed = 0
        if elapsed >= 2e-6 and current >= 2e-6:
            speed = current / elapsed
        
        # format speed
        return format_power(speed, self._template, self._prefixes, self._step)


class Gauge(Widget):
    """
    The Gauge widget displays current progress as a proportionally filled bar.
    The characters used can be fully customized to achieve desired look. If the
    size is not specified, it fills all available space automatically.
    
    In case the parent progress does not specify the maximum value, the marker
    character just bounces back a forth instead of filling the bar.
    """
    
    EXPAND = True
    
    
    def __init__(self, marker="|", left="|", right="|", fill="-", tip="", size=None):
        """
        Initializes a new instance of the Gauge widget.
        
        Args:
            marker: str
                Character used to show current progress.
            
            left: str
                Character used for the left edge.
            
            right: str
                Character used for the right edge.
            
            fill: str
                Character used to fill remaining space.
            
            tip: str
                Character used for the progress tip.
            
            size: int or None
                Desired length of the gauge. If set to None, whole available
                space will be used.
        """
        
        super().__init__()
        
        self._marker = marker
        self._left = left
        self._right = right
        self._fill = fill
        self._tip = tip
        self._size = size
    
    
    def __call__(self, progress, width=0, *args, **kwargs):
        """Formats current progress."""
        
        # get available width
        width = width if self._size is None else self._size
        width -= len(self._left) + len(self._right)
        
        # fill if finished
        if progress.finished:
            return '%s%s%s' % (self._left, width * self._fill, self._right)
        
        # show current progress
        if progress.maximum:
            
            # fill current progress
            bar = self._marker * int(progress.percent / 100 * width)
            if bar and self._tip and not progress.finished:
                bar = bar[:-1] + self._tip
            
            # fill remaining
            bar = bar.ljust(width, self._fill)
        
        # show bouncing bar
        else:
            
            # get position
            position = int(progress.current % (width * 2 - 1))
            if position > width:
                position = width * 2 - position
            
            # get pads
            pad_left = self._fill * (position - 1)
            pad_right = self._fill * (width - len(self._marker) - len(pad_left))
            
            # fill bar
            bar = "%s%s%s" % (pad_left, self._marker, pad_right)
        
        # make full bar
        return "%s%s%s" % (self._left, bar, self._right)


class Spin(Widget):
    """
    The Spin widget displays current progress as animated character. It is
    defined by a sequence of characters to use, each update displays the next
    available character. By setting the widget as relative, available characters
    are mapped to cover the whole progress range, otherwise the widget circles
    through them.
    """
    
    
    def __init__(self, markers=STAR, fin=None, relative=False):
        """
        Initializes a new instance of the Spin widget.
        
        Args:
            markers: str
                Individual characters to animate.
            
            fin: str
                Final character after process finished. If not specified, the
                last character of given markers is used.
            
            relative: bool
                If set to True, characters are distributed equally across full
                progress. If set to False, next character is used for every
                update.
        """
        
        super().__init__()
        
        self._markers = markers
        self._fin = fin
        self._relative = relative
        self._current = -1
    
    
    def __call__(self, progress, width=0, *args, **kwargs):
        """Formats current progress."""
        
        # check for finish
        if progress.finished:
            return self._fin or self._markers[-1]
        
        # use relative
        if self._relative and progress.maximum:
            self._current = int(len(self._markers) * progress.percent / 100)
            return self._markers[self._current]
        
        # get next marker
        self._current = (self._current + 1) % len(self._markers)
        return self._markers[self._current]
