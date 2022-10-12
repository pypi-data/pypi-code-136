from functools import partial


class FunctionDictMixin:
    def do_functions(
        self, input_object: object | None, key: str | None = None, kind: str = "fixes"
    ) -> str:
        """Do all fixes. This may or may not involve transforming the manifest."""

        assigned_functions = getattr(self, kind, dict())

        relevant_functions = assigned_functions.get(key, []) + assigned_functions.get(
            None, []
        )

        if len(relevant_functions) == 0:
            return input_object  # edge-case if nothing happens.
        elif input_object is None:
            assert (
                len(relevant_functions) == 1
            ), "Not passing an input object to be progressively modified implies that you will only ever see the results of a single function. Providing more than one relevant function is useless in this case."
            func = relevant_functions[0]
            output_object = func()
            return output_object
        else:
            intermediate_object = input_object
            for func in relevant_functions:
                intermediate_object = func(intermediate_object)
            output_object = intermediate_object
            return output_object

    def add_function(
        self,
        function: str,
        key: str | None = None,
        kind="fixes",
        **kwargs,
    ):

        available_functions = getattr(self, "available_{}".format(kind), dict())
        assigned_functions = getattr(self, kind, dict())

        # process parameters
        if isinstance(function, str):
            if function in available_functions:
                function = available_functions.get(function)
            else:
                raise ValueError("Did not recognize function {f}".format(f=function))
        else:
            raise TypeError(
                "Provided function needs to be string and match one of the implemented {}!".format(
                    kind
                )
            )

        if len(kwargs) > 0:
            function = partial(function, **kwargs)

        # actual job
        if assigned_functions.get(key, None) is None:
            assigned_functions[key] = [function]
        else:
            assert isinstance(
                assigned_functions[key], list
            ), "Functions should be stored in collections associated with keys."
            assigned_functions[key].append(function)

        return
