# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.

import base64
import dill
import inspect
from typing import Callable, overload, Union, List, Dict
from typing_extensions import get_args

from shapelets.dsl.widgets.util import unique_id_str
from shapelets.dsl.widgets.attribute_names import AttributeNames
from shapelets.dsl.node import (
    Node,
    NodeType
)
from shapelets.dsl.argument_types import (
    ArgumentType,
    ArgumentValue,
    SupportedTypes,
)


class Widget:
    """
    Units defined in Layout
    """

    def __init__(self,
                 widget_type: str,
                 widget_id: str = None,
                 draggable: bool = False,
                 resizable: bool = False,
                 # these are the optional properties:
                 placeholder: str = None,
                 disabled: bool = None,
                 parent_data_app: object = None) -> object:
        # parent_data_app is a reference to the DataApp used as a factory
        # for this widget
        self.parent_data_app = parent_data_app
        self.widget_id = widget_id if widget_id else unique_id_str()
        self.widget_type = widget_type
        self.placeholder = placeholder
        self.disabled = disabled
        self.draggable = draggable
        self.resizable = resizable
        self._bind = []

    def to_dict_widget(self):
        properties = {}
        if self.placeholder is not None:
            properties[AttributeNames.PLACEHOLDER.value] = self.placeholder
        widget_dict = {
            AttributeNames.ID.value: self.widget_id,
            AttributeNames.TYPE.value: self.widget_type,
            AttributeNames.DRAGGABLE.value: self.draggable,
            AttributeNames.RESIZABLE.value: self.resizable,
            AttributeNames.DISABLED.value: False if self.disabled is None else self.disabled,
            AttributeNames.BIND.value: self._bind if self._bind else None,
            AttributeNames.PROPERTIES.value: properties
        }
        return widget_dict

    @staticmethod
    def add_widget_providers(current_dict: dict, providers: dict):
        """
        When any attribute from a widget receives another widget inside, this widget is called a provider. This means
        that the widget attribute with the provider inside must update its value everytime the provider changes.
        In order to do this, a list of providers is given to the UI. This list contains the id of the provider widget
        and the target attribute of the current widget. This list looks like:
        providers: [{
                      id: 85535b68-2dce-11ed-bd74-00155d7482db,
                      target: title
                     }]
        The list of providers is added to the bind section of the current widget.
        """
        if current_dict[AttributeNames.BIND.value]:
            current_dict[AttributeNames.BIND.value].append({
                "providers": providers
            })
        else:
            current_dict[AttributeNames.BIND.value] = [
                {"providers": providers}
            ]

    @overload
    def bind(self, string: str):
        ...

    @overload
    def bind(self, fn: Callable, *args, **kwargs):
        ...

    def bind(self, fn: Union[Callable, str], *args, **kwargs):
        if isinstance(fn, Callable):
            self._bind_function(fn, *args, **kwargs)
        if isinstance(fn, str):
            self._add_bind_to_widget(props=fn)

    def _bind_function(self, fn: Callable, *args, **kwargs):
        """
        Bind for functions
        """
        try:
            return_type = fn.__annotations__['return'].__name__
        except AttributeError:
            return_type = fn.__annotations__['return']._name

        if return_type == "List" and get_args(fn.__annotations__['return']):
            # If return type is a list, it might contain another type inside
            inside_type = get_args(fn.__annotations__['return'])[0].__name__
            if inside_type == "Sequence" or inside_type == "View":
                # For now, let's care only if the inside type is a Sequence or View
                return_type = f"{return_type}[{inside_type}]"

        fn_original_name = fn.__name__
        if return_type in self._compatibility:
            entry_arguments = self._find_parameters(fn)
            # Find other widgets references' inside the function
            references = []

            if (len(args) > len(entry_arguments)):
                raise TypeError(
                    "Function %s called with incorrectly specified arguments. Expected %i but received %i" % (
                        fn_original_name, len(entry_arguments), len(args)))

            on_changes_widgets = []
            for i, arguments in enumerate(args):
                if isinstance(arguments, Widget):
                    on_change = False if kwargs.get("mute") and arguments in kwargs.get("mute") else True
                    if on_change:
                        on_changes_widgets.append(arguments.widget_id)
                    references.append(
                        {
                            "ref": arguments.widget_id,
                            "name": entry_arguments[i]["name"],
                            "type": entry_arguments[i]["type"],
                        }
                    )
                else:
                    references.append(
                        {
                            "value": arguments,
                            "name": entry_arguments[i]["name"],
                            "type": entry_arguments[i]["type"],
                        }
                    )
            fn = self._adjust_arguments(fn, entry_arguments)
            body = fn
            if return_type != self._parent_class:
                body = self._adjust_return(fn, return_type)
            # Add to widget structure
            result = {
                "body": str(base64.b64encode(dill.dumps(body)), encoding='utf-8'),
                "parameters": entry_arguments,
                "result": self._parent_class
            }
            # Get widgets from Triggers
            on_changes_widgets.extend(self._find_triggers(kwargs))
            # We need to check if there is another function already in the bind attribute in order to avoid looping with triggers
            if on_changes_widgets and len(self._bind) > 0:
                self._check_triggers(on_changes_widgets)
            # Add to DataApp Structure
            self.parent_data_app.functions[fn_original_name] = result
            self._add_bind_to_widget(fn_name=fn_original_name, parameters=references, triggers=on_changes_widgets)
        else:
            raise ValueError("Return type does not match")

    @staticmethod
    def _find_parameters(fn: Callable) -> List:
        """
        Find the parameters use in a function.
        param fn: Function to extract parameters from.
        return List with all the parameters.
        """
        parameters = []
        for param in inspect.signature(fn).parameters.values():
            parameters.append({
                "name": param.name,
                "type": param.annotation.__name__,
                "default": None if param.default is param.empty else param.default
            })
        return parameters

    @staticmethod
    def _find_triggers(kwargs: Dict) -> List:
        """
        Find if there are triggers in the kwargs. In bind function, triggers are defined in the on_change parameter.
        param kwargs.
        return List of all the triggers.
        """
        on_change = "on_change"
        triggers = []
        if kwargs.get(on_change):
            triggers = [y.widget_id for y in kwargs.get(on_change) if kwargs.get(on_change)]
        return triggers

    def _add_bind_to_widget(self, fn_name: str = None,
                            props: str = None,
                            parameters: List = None,
                            triggers: List = None):
        """
        Find if there are triggers to bind in the kwargs. In bind function, triggers are defined in the on_change parameter.
        param fn_name: Name of the function to add.
        param props: Properties to change.
        param parameters: Parameters use in the function.
        param triggers: Widgets that trigger the bind.
        """
        self._bind.append({
            "fn": fn_name,
            "props": props,
            "parameters": parameters,
            "triggers": triggers
        })

    def _adjust_return(self, fn: Callable, return_type) -> Callable:
        """
        Add wrapper to function in order to return a Widget.
        If the return value type of the function (fn) is different from the widget type that will receive this result,
        but compatible with the value of the widget, we will wrap the function result to return the same widget type
        with the result inside. Therefore, the front-end will send the function to the back-end to be executed,
        without worrying about the return type since it will always be a compatible widget. When registering the DataApp,
        if the widget does not support the return type, an exception is raised.
        param fn: function to wrap.
        param return_type: return type from the function.
        return new function with return type wrapped
        """
        if return_type == "str":
            if "from_string" not in dir(self):
                raise Exception("String return type not supported for this widget")

            def result_from_string(*args, **kwargs) -> Widget:
                return self.from_string(fn(*args, **kwargs))

            return result_from_string
        elif return_type == "int":
            if "from_int" not in dir(self):
                raise Exception("Int return type not supported for this widget")

            def result_from_int(*args, **kwargs) -> Widget:
                return self.from_int(fn(*args, **kwargs))

            return result_from_int
        elif return_type == "float":
            if "from_float" not in dir(self):
                raise Exception("Float return type not supported for this widget")

            def result_from_float(*args, **kwargs) -> Widget:
                return self.from_float(fn(*args, **kwargs))

            return result_from_float
        elif return_type == "DataFrame":
            if "from_dataframe" not in dir(self):
                raise Exception("DataFrame return type not supported for this widget")

            def result_from_dataframe(*args, **kwargs) -> Widget:
                return self.from_dataframe(fn(*args, **kwargs))

            return result_from_dataframe
        elif return_type == "ndarray":
            if "from_ndarray" not in dir(self):
                raise Exception("ndarray return type not supported for this widget")

            def result_from_ndarray(*args, **kwargs) -> Widget:
                return self.from_ndarray(fn(*args, **kwargs))

            return result_from_ndarray
        elif return_type == "list":
            if "from_list" not in dir(self):
                raise Exception("list return type not supported for this widget")

            def result_from_list(*args, **kwargs) -> Widget:
                return self.from_list(fn(*args, **kwargs))

            return result_from_list
        elif return_type == "List":
            if "from_List" not in dir(self):
                raise Exception("List return type not supported for this widget")

            def result_from_List(*args, **kwargs) -> Widget:
                return self.from_list(fn(*args, **kwargs))

            return result_from_List
        elif return_type == "Colors":
            if "from_color" not in dir(self):
                raise Exception("Color return type not supported for this widget")

            def result_from_color(*args, **kwargs) -> Widget:
                return self.from_color(fn(*args, **kwargs))

            return result_from_color
        elif return_type == "Sequence":
            if "from_sequence" not in dir(self):
                raise Exception("Sequence return type not supported for this widget")

            def result_from_sequence(*args, **kwargs) -> Widget:
                return self.from_sequence(fn(*args, **kwargs))

            return result_from_sequence
        elif return_type == "View":
            if "from_view" not in dir(self):
                raise Exception("View return type not supported for this widget")

            def result_from_view(*args, **kwargs) -> Widget:
                return self.from_view(fn(*args, **kwargs))

            return result_from_view
        elif return_type == "List[View]":
            if "from_views" not in dir(self):
                raise Exception("List of Views return type not supported for this widget")

            def result_from_views(*args, **kwargs) -> Widget:
                return self.from_views(fn(*args, **kwargs))

            return result_from_views
        elif return_type == "List[Sequence]":
            if "from_sequences" not in dir(self):
                raise Exception("List of Views return type not supported for this widget")

            def result_from_sequences(*args, **kwargs) -> Widget:
                return self.from_sequences(fn(*args, **kwargs))

            return result_from_sequences
        elif return_type == "datetime":
            if "from_datetime" not in dir(self):
                raise Exception("datetime return type not supported for this widget")

            def result_from_datetime(*args, **kwargs) -> Widget:
                return self.from_datetime(fn(*args, **kwargs))

            return result_from_datetime
        elif return_type == "date":
            if "from_date" not in dir(self):
                raise Exception("date return type not supported for this widget")

            def result_from_date(*args, **kwargs) -> Widget:
                return self.from_date(fn(*args, **kwargs))

            return result_from_date
        elif return_type == "time":
            if "from_time" not in dir(self):
                raise Exception("time return type not supported for this widget")

            def result_from_time(*args, **kwargs) -> Widget:
                return self.from_time(fn(*args, **kwargs))

            return result_from_time
        else:
            raise Exception(f"Return type {return_type} not supported for this widget")

    @staticmethod
    def _adjust_arguments(fn: Callable, references: List) -> Callable:
        """
        Add Wrapper to arguments to use the requested type.
        When a function requests any Python native type, but a widget is given, we wrap the function arguments
        to extract the value of the given widget and convert it to the requested type. This allows for the execution
        to be carried out quickly and easily, as all the work is done before actually executing the function.
        param fn: function to wrap.
        param references: List of arguments use in the function. Contains the widget reference, type, etc.
        return new function with entry arguments wrapped to use the proper types.
        """
        type_list = []
        for argument in references:
            type_list.append(argument["type"])

        def fun_new_arguments(*args, **kwargs):
            new_args = []
            for i, item in enumerate(args):
                if isinstance(item, Widget):
                    argument_type = type_list[i]
                    if argument_type == "str":
                        new_args.append(item.to_string())
                    elif argument_type == "int":
                        new_args.append(item.to_int())
                    elif argument_type == "float":
                        new_args.append(item.to_float())
                    else:
                        new_args.append(item.value)
                else:
                    new_args.append(item)
            return fn(*new_args)

        return fun_new_arguments

    def _check_triggers(self, triggers):
        for fn in self._bind:
            for param in fn["triggers"]:
                if param in triggers:
                    raise Exception(f"Trigger Loop Found")

    # def _find_widget(self, widget_id: str) -> Widget:
    #     """
    #     Find widget inside a DataApp using the widget ID
    #     param widget_id: ID from wanted widget
    #     return Widget
    #     """
    #     return next(widget for widget in self.parent_data_app.main_panel.widgets if widget.widget_id == widget_id)


class WidgetNode(Widget, Node):
    OPERATION = AttributeNames.OPERATION.value

    def __init__(self,
                 widget_type: str,
                 value_type: ArgumentType,
                 value: SupportedTypes,
                 **additional):
        Widget.__init__(self, widget_type, **additional)
        Node.__init__(self, WidgetNode.OPERATION, node_type=NodeType.WidgetNode)
        self.value_type = value_type
        self.value = ArgumentValue(value_type, value)

    def __hash__(self):
        return hash((Node.__hash__(self), Widget.__hash__(self)))

    def __eq__(self, other):
        return (isinstance(other, WidgetNode) and
                Node.__eq__(self, other) and
                Widget.__eq__(self, other))

    def __repr__(self):
        s_repr = Node.__repr__(self).replace('Node{id:', 'WidgetNode{id:')
        s_repr += f".{AttributeNames.VALUE.value}: {self.value.to_dict()}"
        return s_repr


class StateControl:
    disabled: bool
    draggable: bool
    resizable: bool
