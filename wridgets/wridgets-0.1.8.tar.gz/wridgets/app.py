import functools
import traceback
from hashlib import md5

from . import wridgets
from IPython.display import display
from ipywidgets import VBox, HBox, Output
from .utils import unwrap, wrap


class App:
    is_wrapp = False
    _disable_build = False
    trait_names = (
        'prefix', 
        'name',
        'output',
        'display_output',
        'propagate',
        'hide',
        'minimize',
        'clear_previous_output'
    )

    @classmethod
    def _init_trait(cls, trait):
        def getter_lda(self): return self._config.get(trait)
        setattr(cls, trait, property(getter_lda))
        def setter_lda(self, value): self._config.update({trait: value}); self.build()
        setattr(cls, trait, getattr(cls, trait).setter(setter_lda))

    @classmethod
    def _init_store(cls, store):
        def getter_lda(self): return self._store.get(store)
        setattr(cls, store, property(getter_lda))
        def setter_lda(self, value): self._store.update({store: value})
        setattr(cls, store, getattr(cls, store).setter(setter_lda))

    def display(self):
        display(
            self.app
        )
    
    def with_output(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            with self.output:
                if self.clear_previous_output:
                    self.output.clear_output()
                try:
                    return func(self, *args, **kwargs)
                except Exception as e:
                    (
                        Button(
                            on_interact=self.output.clear_output,
                            button_style='warning',
                            description='Clear'
                        ) + \
                        Button(
                            on_interact=self.print_traceback,
                            on_interact_kws=dict(tb=traceback.format_exc()),
                            button_style='info',
                            description='Traceback'
                        )
                    ).display()
                    print(e)
        return wrapper
    
    def print_traceback(self, tb):
        with self.output:
            self.output.clear_output()
            self.clear_button.display()
            print(tb)
    
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.app = VBox()
        
        for trait in cls.trait_names:
            cls._disable_build = True
            cls._init_trait(trait)
            cls._disable_build = False

        # set store
        if hasattr(cls, 'store_config'):
            for row in cls.store_config:
                row = wrap(row)
                cls._init_store(store=row[0])
        
        cls.make = cls._build(cls.make)
        cls.set = cls._build(cls.set)
        return obj
    
    def __init_subclass__(cls):
        # automatically assign output to methods
        base_method_list = [func for func in dir(App) if callable(getattr(App, func))]
        method_list = [func for func in dir(cls) if callable(getattr(cls, func)) and func not in base_method_list]
        for method in method_list:
            setattr(cls, method, cls.with_output(getattr(cls, method)))
    
    def __init__(self, core=None, prefix=None, name=None, output=None, display_output=None, propagate=None, hide=None, minimize=None, clear_previous_output=None, **kwargs):
        self._config = {}
        self._store = {}
        self._core = None
        self._defaults = {}
        prefix = self.setdefault('prefix', prefix if prefix is not None else '')
        self.setdefault('name', prefix + (name if name is not None else self.__class__.__name__))
        self.setdefault('output', output if output is not None else Output())
        self.setdefault('display_output', display_output if display_output is not None else True)
        self.setdefault('propagate', propagate if propagate is not None else False)
        self.setdefault('hide', hide if hide is not None else False)
        self.setdefault('minimize', minimize if minimize is not None else False)
        self.setdefault('clear_previous_output', clear_previous_output if clear_previous_output is not None else True)
        self.defaults.update(kwargs)
        # UPDATE STORE
        if hasattr(self, 'store_config'):
            for row in self.store_config:
                row = wrap(row)
                if len(row)==2:
                    setattr(self, row[0], row[1])
                else:
                    setattr(self, row[0], None)
        # SET CORE
        if core is not None:
            self.core = core
        else:
            self._app_layout = []
            self.children = AppGroup()
        
        # UPDATE CONFIG
        self.set_trait_defaults(build=False)

        # RUN MAKE
        self.make(**kwargs)
    
    def set_trait_defaults(self, build=True):
        self._disable_build = True
        self.prefix = self.getdefault('prefix')
        self.name = self.getdefault('name')
        self.output = self.getdefault('output') 
        self.display_output = self.getdefault('display_output')
        self.propagate = self.getdefault('propagate')
        self.hide = self.getdefault('hide')
        self.minimize = self.getdefault('minimize')
        self.clear_previous_output = self.getdefault('clear_previous_output')
        self._disable_build = False
        if build:
            self.build()

    @property
    def core(self):
        return self._core

    @core.setter
    def core(self, core):
        self.app = core.app
        self._app_layout = core._app_layout
        self.children = core.children
        self._core = core

    def make(self, **kwargs):
        pass
    
    @property
    def app_layout(self):
        return self._app_layout
    
    @property
    def config(self):
        return self._config

    @property
    def store(self):
        return self._store

    @property
    def defaults(self):
        return self._defaults

    @defaults.setter
    def defaults(self, default_dict:dict):
        assert isinstance(default_dict, dict), 'defaults must be a dict'
        self._defaults = default_dict

    def clear_output(self):
        self.output.clear_output()

    @property
    def clear_button(self):
        return Button(description='Clear', button_style='warning', on_interact=self.clear_output)

    def msg(self, msg:str, with_clear_button=True):
        clear_button = self.clear_button if with_clear_button else None
        with self.output:
            self.clear_output()
            if isinstance(msg, str):
                (
                    Label(text=msg, fontsize=0.5) + \
                    clear_button
                ).display()
            else:
                (
                    msg + \
                    clear_button
                ).display()
    
    def _build(func):
        @functools.wraps(func)
        def wrapper(self, **kwargs):
            func(self, **kwargs)
            self.build()
        return wrapper
    
    def build(self):
        if not self._disable_build:
            if self.display_output:
                self.app.children = [HBox(row) for row in self.app_layout] + [self.output]
            else:
                self.app.children = [HBox(row) for row in self.app_layout]
            
            self.app.layout.visibility = 'hidden' if self.hide else None
            self.app.layout.display = 'none' if self.minimize else None

    @property
    def model_id(self):
        if not isinstance(self, WrApp):
            ids = []
            for _, value in self.children:
                model_id = getattr(value, 'model_id', None)
                model_id = value.wridget.widget.model_id if model_id is None else model_id
                ids.append(model_id)
            encoded = ''.join(ids).encode()
            dhash = md5()
            dhash.update(encoded)
            return dhash.hexdigest()
        else:
            return self.wridget.widget.model_id

    def _union(self, other):
        if isinstance(other, App):
            obj = App()
            obj.children = self.children + other.children
            for source in [self, other]:
                if source.propagate:
                    setattr(obj.children, source.name, source)
            return obj
        else:
            raise TypeError(f'Cannot add type {type(self)} to type {type(other)}.')
    
    def _horizontal_app_layout(self, other):
        return [
            [
                self.app, other.app
            ]
        ]
    
    def _vertical_app_layout(self, other):
        return [
            [
                self.app
            ],
            [
                other.app
            ]
        ]
    
    def __radd__(self, other):
        if other is None:
            return self

    def __add__(self, other):
        if other is not None:
            obj = self._union(other)
            obj._app_layout = self._horizontal_app_layout(other)
            obj.build()
            return obj
        else:
            return self

    def __rsub__(self, other):
        if other is None:
            return self
    
    def __sub__(self, other):
        if other is not None:
            obj = self._union(other)
            obj._app_layout = self._vertical_app_layout(other)
            obj.build()
            return obj
        else:
            return self
    
    def wridgets(self, include=None, exclude=None):
        wridgets = {}
        for name, value in self.children:
            if isinstance(value, WrApp):
                wridgets[name] = value
        
        subset = set(wridgets.keys())
        if include is not None:
            subset = set(wridgets.keys()).intersection(wrap(include))
        if exclude is not None:
            subset = set(wridgets.keys()).difference(wrap(exclude))
        return {k: v.wridget for k, v in wridgets.items() if k in subset}

    def get(self, name, include=None, exclude=None, skip_children=False, children_only=False):
        if not children_only:
            if name in self.trait_names:
                return getattr(self, name)
        if not skip_children:
            wridgets = self.wridgets(include=include, exclude=exclude)
            return {wridget_name: wridget.get(name) for wridget_name, wridget in wridgets.items()}

    def get1(self, name, include=None, exclude=None, skip_children=False, children_only=False):
        if name in self.trait_names:
            return getattr(self, name)
        d = list(self.get(name=name, include=include, exclude=exclude, skip_children=skip_children, children_only=children_only).values())
        assert len(d) == 1, f'get1 must return one value'
        return unwrap(d)

    def set(self, include=None, exclude=None, **kwargs):
        for name, value in kwargs.items():
            if name in self.trait_names:
                setattr(self, name, value)
            else:
                wridgets = self.wridgets(include=include, exclude=exclude)
                for wridget in wridgets.values():
                    wridget.set({name: value})
    
    @property
    def ch(self):
        """
        alias for children
        """
        return self.children

    def updatedefault(self, name, value):
        self.defaults.update({name: value})

    def setdefault(self, name, value):
        return self.defaults.setdefault(name, value)

    def getdefault(self, name, value=None):
        return value if name not in self.defaults else self.defaults.get(name)
    
    def popdefault(self, name):
        return self.defaults.pop(name)

    def reset(self):
        child_to_reset = []
        for _, child in self.children:
            if child.is_wrapp:
                child_to_reset.append(child)
        for child in child_to_reset:
            child.set_trait_defaults(build=False)
            child.make(**{k: v for k, v in child.defaults.items() if k not in self.trait_names})
        self.set_trait_defaults()


class AppGroup:
    def __init__(self, *args, **kwargs):
        for value in args:
            self.__setattr__(value.name, value)
            
        for name, value in kwargs.items():
            self.__setattr__(name, value)
            
    def __setattr__(self, name, value):
        cont = False
        new_model_id = getattr(value, 'model_id', None)
        if new_model_id is not None:
            original = getattr(self, name, None)
            if original is not None:
                original_model_id = getattr(original, 'model_id', None)
                if original_model_id is not None and original_model_id == new_model_id:
                    self.__dict__[name] = value
                else:
                    cont = True
            else:
                cont = True
        else:
            cont = True

        if cont:
            i = 1
            base = name
            while hasattr(self, name):
                i += 1
                name = base
                name += str(i)
            # if getattr(value, 'name', name) != name:
            #     value.set_config(name=name, update=True)
            self.__dict__[name] = value
    
    def __iter__(self):
        yield from self.__dict__.items()
        
    def __add__(self, other):
        if isinstance(other, AppGroup):
            obj = AppGroup()
            for source in [self, other]:
                for name, value in source:
                    setattr(obj, name, value)
            return obj
        else:
            raise TypeError(f'Cannot add type {type(self)} to type {type(other)}.')

    def __repr__(self):
        return str(tuple([a for a, _ in self if not a.startswith('_')]))
        

class WrApp:
    is_wrapp = True
    def _set_wridget(self, wridget_type, **kwargs):
        if hasattr(self, 'allowed_wridget_types'):
            assert wridget_type in self.allowed_wridget_types, f'Allowed types are {self.allowed_wridget_types}'
        try:
            delattr(self.children, self.name)
        except:
            pass
        setattr(self.children, self.name, self)
        self.wridget = getattr(wridgets, wridget_type)(output=self.output, **kwargs)
        self._app_layout = [
                [
                    self.wridget.widget
                ]
        ]

# DEFAULT APPS

def _make(self, **kwargs):
    kwargs.setdefault('layout', {'width': 'auto'})
    self._set_wridget(wridget_type=self.wridget_type, **kwargs)
    


def _initialize_default_apps():
    for wridget in wridgets.wridget_list:

        globals()[wridget] = type(wridget, (WrApp, App), {
            "wridget_type": wridget,
            "make": _make,
        })


_initialize_default_apps()

# CUSTOM APPS

class Button(WrApp, App):
    allowed_wridget_types = 'Button', 'ToggleButton'
    def make(self, **kwargs):
        kwargs.setdefault('wridget_type', 'Button')
        kwargs.setdefault('value', None)
        kwargs.setdefault('layout', {'width': 'auto'})
        self._set_wridget(wridget_type=kwargs.pop('wridget_type'), **kwargs)


class Checkbox(WrApp, App):
    def make(self, **kwargs):
        kwargs.setdefault('indent', False)
        kwargs.setdefault('layout', {'width': 'auto'})
        self._set_wridget(wridget_type='Checkbox', **kwargs)


class Field(WrApp, App):
    allowed_wridget_types = ('Text', 'Textarea', 'IntText', 'FloatText', 'BoundedIntText', 'BoundedFloatText', 'Password')
    def make(self, **kwargs):
        kwargs.setdefault('wridget_type', 'Text')
        kwargs.setdefault('continuous_update', False)
        kwargs.setdefault('layout', {'width': 'auto'})
        self._set_wridget(wridget_type=kwargs.pop('wridget_type'), **kwargs)


class Buttons(WrApp, App):
    allowed_wridget_types = 'ToggleButtons', 'RadioButtons'
    def make(self, **kwargs):
        kwargs.setdefault('wridget_type', 'ToggleButtons')
        kwargs.setdefault('options', ())
        kwargs.setdefault('layout', {'width': 'auto'})
        kwargs.setdefault('style', {'button_width': 'auto'})
        self._set_wridget(wridget_type=kwargs.pop('wridget_type'), **kwargs)


class Select(WrApp, App):
    allowed_wridget_types = 'Select', 'SelectMultiple'
    def make(self, **kwargs):
        kwargs.setdefault('wridget_type', 'Select')
        kwargs.setdefault('layout', {'width': 'auto'})
        self._set_wridget(wridget_type=kwargs.pop('wridget_type'), **kwargs)


class Label(WrApp, App):
    def make(self, **kwargs):
        if 'value' not in kwargs:
            kwargs.setdefault('text', '')
            kwargs.setdefault('fontsize', 1)
            kwargs.setdefault('bold', False)
            kwargs['value'] = f"<font size='+{kwargs.get('fontsize')}'>{kwargs.get('text')}</font>"
            if kwargs.get('bold'):
                kwargs['value'] = "<b>" + kwargs['value'] + "</b>"
        self._set_wridget(wridget_type='HTML', **kwargs)


class HTMLink(WrApp, App):
    def make(self, link_kws=None, **kwargs):
        link_kws = {} if link_kws is None else link_kws
        link_kws.setdefault('src', '')
        link_kws.setdefault('text', link_kws.get('src'))
        link_kws.setdefault('fontsize', 1)
        link_kws.setdefault('link_color', 'blue')
        link_kws.setdefault('link_background_color', 'transparent')
        link_kws.setdefault('link_text_decoration', 'underline')
        link_kws.setdefault('visited_color', 'purple')
        link_kws.setdefault('visited_background_color', 'transparent')
        link_kws.setdefault('visited_text_decoration', 'underline')
        kwargs['value'] = f"""
            <style>
            a:link {{
            color: {link_kws.get('link_color')};
            background-color: {link_kws.get('link_background_color')};
            text-decoration: {link_kws.get('link_text_decoration')};
            }}

            a:visited {{
            color: {link_kws.get('visited_color')};
            background-color: {link_kws.get('visited_background_color')};
            text-decoration: {link_kws.get('visited_text_decoration')};
            }}
            </style>
            <font size='+{link_kws.get('fontsize')}'>
            <a href={link_kws.get('src')} target='_blank'>{link_kws.get('text')}</a>
            </font>
            """
        self._set_wridget(wridget_type='HTML', **kwargs)


class Tags(WrApp, App):
    allowed_wridget_types = 'TagsInput', 'ColorsInput', 'FloatsInput', 'IntsInput'
    def make(self, **kwargs):
        kwargs.setdefault('wridget_type', 'TagsInput')
        kwargs.setdefault('allow_duplicates', False)
        self._set_wridget(wridget_type=kwargs.pop('wridget_type'), **kwargs)


class Container(WrApp, App):
    _container = None
    _contents = None
    
    def make(self, contents=None, **kwargs):
        kwargs.setdefault('container', Output())
        self.container = kwargs.pop('container')
        kwargs.setdefault('children', [self.container])
        self._set_wridget(wridget_type='Box', **kwargs)
        self.contents = contents
    
    @property
    def container(self):
        return self._container
    
    @property
    def contents(self):
        return self._contents
    
    @container.setter
    def container(self, container):
        self._container = container
    
    @contents.setter
    def contents(self, contents):
        self._contents = contents
        self._display_contents()
    
    def _display_contents(self):
        with self.container:
            self.container.clear_output()
            if self.contents is not None:
                display(self.contents)
