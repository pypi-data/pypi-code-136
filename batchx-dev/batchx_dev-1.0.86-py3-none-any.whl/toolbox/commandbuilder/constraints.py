from functools import partial
from typing import Callable


class Constraints:
    @property
    def preconfigured_constraints(self):
        return dict(requires=self.requires)

    def requires(self, input, manifest, value, k=None, v=None):

        assert k in manifest.input_names, "Unknown Key {k}: not in manifest.".format(
            k=k
        )
        ip_val = getattr(input, k, None)
        mf_val = manifest.default_inputs.get(k, None)

        if v is None:
            r = k in input.keys()
            msg = """
            Checking library constraint "requires"
                Is key `{k}` explicitly given in input?
                (value unimportant)

            Result: {r}
            """.format(
                k=k, r=r
            )
            print(msg)
            return r
        elif k in input.keys():
            r = ip_val == v
            msg = """
            Checking library constraint "requires".
            Key {k} is explicitly set in input.
                input[{k}] == {v}?

            Result: {r}
            """.format(
                k=k, r=r, v=v
            )
            print(msg)
            return r
        else:
            r = mf_val == v
            msg = """
            Checking library constraint "requires".
            Key {k} is not explicitly set in input (check manifest-specified default)
                manifest[{k}]["default"] == {v}?

            Result: {r}                
            """.format(
                k=k, v=v, r=r
            )
            print(msg)
            return r


class ConstraintMixin(Constraints):
    def check_constraints(self, input, manifest):
        """Check all constraints."""

        all_keys = input.jsonpaths() if input.jsonpaths_enabled else input.keys()
        for key in all_keys:
            self.check_constraints_for_one_key(input, manifest, key)
        return input

    def check_constraints_for_one_key(self, input, manifest, key: str):
        relevant_constraints = self.constraints.get(key, [])
        for constraint in relevant_constraints:
            val = getattr(input, key)  # really needs to be *inside* the loop
            if self.verbose:
                msg = """
                CHECK CONSTRAINT
                ----------------
                Constraint: {c}
                for Key:    {k}
                with Value: {v}
                """.format(
                    k=key, v=val, c=constraint
                )
                print(msg)
            if constraint(input, manifest, val) is True:
                pass
            else:
                msg = """
                Constraint {c} 
                related to key {k} not satisfied in this input.
                """.format(
                    c=constraint, k=key
                )
                raise ValueError(msg)
        return True

    def add_constraint(
        self, constraint: Callable | str = None, key: str | None = None, **kwargs
    ):
        if key is None:
            key = self.active_key

        # obtain constraint-function
        if isinstance(constraint, str):
            if constraint in self.preconfigured_constraints:
                constraint = self.preconfigured_constraints.get(constraint)
            else:
                raise ValueError("Did not recognize action {c}".format(c=constraint))
        elif isinstance(constraint, Callable):
            constraint = constraint
        else:
            raise ValueError("Constraint needs to be string or callable.")

        # partially initialize function if desired
        if len(kwargs) > 0:
            constraint = partial(constraint, **kwargs)

        # record function in constraints dict
        if self.constraints.get(key, None) is not None:
            self.constraints[key].append(constraint)
        else:
            self.constraints[key] = [constraint]

        self.active_key = key
        return self
